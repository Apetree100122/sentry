import {Fragment, useCallback, useMemo, useState} from 'react';
import styled from '@emotion/styled';

import {ModalRenderProps, openModal} from 'sentry/actionCreators/modal';
import {Button} from 'sentry/components/button';
import Input from 'sentry/components/input';
import LoadingIndicator from 'sentry/components/loadingIndicator';
import PanelTable from 'sentry/components/panels/panelTable';
import Tag from 'sentry/components/tag';
import {Tooltip} from 'sentry/components/tooltip';
import {t} from 'sentry/locale';
import {space} from 'sentry/styles/space';
import {parseDashboard, ParseResult} from 'sentry/utils/metrics/import';
import useOrganization from 'sentry/utils/useOrganization';
import {DDMContextProvider, useDDMContext} from 'sentry/views/ddm/context';
import {OrganizationContext} from 'sentry/views/organizationContext';

export function useImportDashboard() {
  const organization = useOrganization();

  return useMemo(() => {
    return function () {
      return openModal(deps => (
        <OrganizationContext.Provider value={organization}>
          <DDMContextProvider>
            <ImportDashboardModal {...deps} />
          </DDMContextProvider>
        </OrganizationContext.Provider>
      ));
    };
  }, [organization]);
}

type FormState = {
  dashboard: string;
  importResult: ParseResult | null;
  isValid: boolean;
  step: 'initial' | 'importing' | 'add-widgets';
};

function ImportDashboardModal({Header, Body, Footer}: ModalRenderProps) {
  const {metricsMeta, addWidgets} = useDDMContext();
  const [formState, setFormState] = useState<FormState>({
    step: 'initial',
    dashboard: '',
    importResult: null,
    isValid: false,
  });

  const handleImportDashboard = useCallback(async () => {
    if (formState.isValid) {
      setFormState(curr => ({...curr, step: 'importing'}));

      const dashboardJson = JSON.parse(formState.dashboard);
      const importResult = await parseDashboard(dashboardJson, metricsMeta);

      setFormState(curr => ({
        ...curr,
        importResult,
        step: 'add-widgets',
      }));
    }
  }, [formState.isValid, formState.dashboard, metricsMeta]);

  const handleSetWidgets = useCallback(() => {
    if (formState.importResult) {
      addWidgets(formState.importResult.widgets);
    }
  }, [addWidgets, formState.importResult]);

  return (
    <Fragment>
      <Header>
        <h4>{t('Import dashboard')}</h4>
      </Header>
      <Body>
        <ContentWrapper>
          {formState.step === 'initial' && (
            <Input
              name="dashboard"
              placeholder={t('Paste dashboard JSON')}
              value={formState.dashboard}
              onChange={e => {
                const isValid = isValidJson(e.target.value);
                setFormState(curr => ({...curr, dashboard: e.target.value, isValid}));
              }}
            />
          )}
          {formState.step === 'importing' && <LoadingIndicator />}
          {formState.step === 'add-widgets' && (
            <Fragment>
              <div>
                {t(
                  'Processed %s widgets from the dashboard',
                  formState.importResult?.report.length
                )}
              </div>
              <PanelTable headers={['Title', 'Outcome', 'Errors', 'Notes']}>
                {formState.importResult?.report.map(widget => {
                  return (
                    <Fragment key={widget.id}>
                      <div>{widget.title}</div>
                      <div>
                        <Tag type={widget.outcome}>{widget.outcome}</Tag>
                      </div>
                      <div>{widget.errors.join(', ')}</div>
                      <div>{widget.notes.join(', ')}</div>
                    </Fragment>
                  );
                })}
              </PanelTable>
              <div>
                {t(
                  'Found %s widgets that can be imported',
                  formState.importResult?.widgets.length
                )}
              </div>
            </Fragment>
          )}
        </ContentWrapper>
      </Body>
      <Footer>
        <Tooltip
          disabled={formState.isValid}
          title={t('Please input valid dashboard JSON')}
        >
          <Button
            priority="primary"
            disabled={!formState.isValid}
            onClick={
              formState.step === 'initial' ? handleImportDashboard : handleSetWidgets
            }
          >
            {formState.step === 'initial' ? t('Import') : t('Add Widgets')}
          </Button>
        </Tooltip>
      </Footer>
    </Fragment>
  );
}

const ContentWrapper = styled('div')`
  display: grid;
  grid-template-columns: 1fr;
  gap: ${space(2)};
`;

const isValidJson = (str: string) => {
  try {
    JSON.parse(str);
  } catch (e) {
    return false;
  }
  return true;
};
