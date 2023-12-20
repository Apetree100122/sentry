from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from sentry import features
from sentry.api.api_owners import ApiOwner
from sentry.api.api_publish_status import ApiPublishStatus
from sentry.api.base import region_silo_endpoint
from sentry.api.bases.project import ProjectEndpoint, ProjectSettingPermission
from sentry.api.permissions import SuperuserPermission
from sentry.models.options.project_option import ProjectOption
from sentry.projectoptions.defaults import DEFAULT_PROJECT_PERFORMANCE_GENERAL_SETTINGS

SETTINGS_PROJECT_OPTION_KEY = "sentry:performance_general_settings"


class ProjectOwnerOrSuperUserPermissions(ProjectSettingPermission):
    def has_object_permission(self, request: Request, view, project):
        return super().has_object_permission(
            request, view, project
        ) or SuperuserPermission().has_permission(request, view)


@region_silo_endpoint
class ProjectPerformanceGeneralSettingsEndpoint(ProjectEndpoint):
    owner = ApiOwner.PERFORMANCE
    publish_status = {
        "DELETE": ApiPublishStatus.UNKNOWN,
        "GET": ApiPublishStatus.UNKNOWN,
        "POST": ApiPublishStatus.UNKNOWN,
    }
    permission_classes = (ProjectOwnerOrSuperUserPermissions,)

    def has_feature(self, project, request) -> bool:
        return features.has(
            "organizations:performance-view", project.organization, actor=request.user
        )

    def get(self, request: Request, project) -> Response:
        if not self.has_feature(project, request):
            return self.respond(status=status.HTTP_404_NOT_FOUND)

        project_option_settings = (
            ProjectOption.objects.get_value(
                project,
                "sentry:performance_general_settings",
                DEFAULT_PROJECT_PERFORMANCE_GENERAL_SETTINGS,
            )
            if project
            else DEFAULT_PROJECT_PERFORMANCE_GENERAL_SETTINGS
        )
        return Response(project_option_settings)

    def post(self, request: Request, project) -> Response:
        if not self.has_feature(project, request):
            return self.respond(status=status.HTTP_404_NOT_FOUND)

        ProjectOption.objects.set_value(
            project,
            "sentry:performance_general_settings",
            request.data,
        )
        data = {}
        return Response(data)

    def delete(self, request: Request, project) -> Response:
        if not self.has_feature(project, request):
            return self.respond(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT)
