import {projectStatsToPredictedSeries} from 'sentry/views/settings/project/server-side-sampling/utils/projectStatsToPredictedSeries';

import {outcomesWithoutClientDiscarded} from '../utils';

describe('projectStatsToPredictedSeries', function () {
  it('returns correct series', function () {
    expect(projectStatsToPredictedSeries(TestStubs.Outcomes(), 0.3, 0.1)).toEqual([
      {
        seriesName: 'Indexed and Processed',
        color: '#2BA185',
        barMinHeight: 1,
        type: 'bar',
        stack: 'predictedUsage',
        data: [
          {name: 1656788400000, value: 29437},
          {name: 1656792000000, value: 28213},
          {name: 1656795600000, value: 26325},
          {name: 1656799200000, value: 25983},
          {name: 1656802800000, value: 24739},
          {name: 1656806400000, value: 27874},
          {name: 1656810000000, value: 29096},
          {name: 1656813600000, value: 24303},
          {name: 1656817200000, value: 24376},
          {name: 1656820800000, value: 24941},
          {name: 1656824400000, value: 25125},
          {name: 1656828000000, value: 26933},
          {name: 1656831600000, value: 29639},
          {name: 1656835200000, value: 30842},
          {name: 1656838800000, value: 30323},
          {name: 1656842400000, value: 30219},
          {name: 1656846000000, value: 31770},
          {name: 1656849600000, value: 33488},
          {name: 1656853200000, value: 33660},
          {name: 1656856800000, value: 33003},
          {name: 1656860400000, value: 32401},
          {name: 1656864000000, value: 32080},
          {name: 1656867600000, value: 31281},
          {name: 1656871200000, value: 30730},
          {name: 1656874800000, value: 30192},
          {name: 1656878400000, value: 29997},
          {name: 1656882000000, value: 27718},
          {name: 1656885600000, value: 27479},
          {name: 1656889200000, value: 29929},
          {name: 1656892800000, value: 36845},
          {name: 1656896400000, value: 44476},
          {name: 1656900000000, value: 42343},
          {name: 1656903600000, value: 41643},
          {name: 1656907200000, value: 46482},
          {name: 1656910800000, value: 52822},
          {name: 1656914400000, value: 76354},
          {name: 1656918000000, value: 101122},
          {name: 1656921600000, value: 110820},
          {name: 1656925200000, value: 107708},
          {name: 1656928800000, value: 94690},
          {name: 1656932400000, value: 91411},
          {name: 1656936000000, value: 100290},
          {name: 1656939600000, value: 103284},
          {name: 1656943200000, value: 100178},
          {name: 1656946800000, value: 83511},
          {name: 1656950400000, value: 66709},
          {name: 1656954000000, value: 54611},
          {name: 1656957600000, value: 31394},
        ],
      },
      {
        seriesName: 'Processed',
        color: '#F5B000',
        data: [
          {name: 1656788400000, value: 58873},
          {name: 1656792000000, value: 56426},
          {name: 1656795600000, value: 52651},
          {name: 1656799200000, value: 51967},
          {name: 1656802800000, value: 49478},
          {name: 1656806400000, value: 55747},
          {name: 1656810000000, value: 58193},
          {name: 1656813600000, value: 48605},
          {name: 1656817200000, value: 48752},
          {name: 1656820800000, value: 49882},
          {name: 1656824400000, value: 50249},
          {name: 1656828000000, value: 53866},
          {name: 1656831600000, value: 59278},
          {name: 1656835200000, value: 61684},
          {name: 1656838800000, value: 60647},
          {name: 1656842400000, value: 60438},
          {name: 1656846000000, value: 63540},
          {name: 1656849600000, value: 66975},
          {name: 1656853200000, value: 67320},
          {name: 1656856800000, value: 66006},
          {name: 1656860400000, value: 64802},
          {name: 1656864000000, value: 64159},
          {name: 1656867600000, value: 62562},
          {name: 1656871200000, value: 61460},
          {name: 1656874800000, value: 60385},
          {name: 1656878400000, value: 59994},
          {name: 1656882000000, value: 55435},
          {name: 1656885600000, value: 54958},
          {name: 1656889200000, value: 59857},
          {name: 1656892800000, value: 73690},
          {name: 1656896400000, value: 88951},
          {name: 1656900000000, value: 84686},
          {name: 1656903600000, value: 83286},
          {name: 1656907200000, value: 92963},
          {name: 1656910800000, value: 105643},
          {name: 1656914400000, value: 152709},
          {name: 1656918000000, value: 202244},
          {name: 1656921600000, value: 221641},
          {name: 1656925200000, value: 215416},
          {name: 1656928800000, value: 189380},
          {name: 1656932400000, value: 182821},
          {name: 1656936000000, value: 200579},
          {name: 1656939600000, value: 206568},
          {name: 1656943200000, value: 200357},
          {name: 1656946800000, value: 167023},
          {name: 1656950400000, value: 133418},
          {name: 1656954000000, value: 109223},
          {name: 1656957600000, value: 62788},
        ],
        barMinHeight: 1,
        type: 'bar',
        stack: 'predictedUsage',
      },
      {
        seriesName: 'Discarded',
        color: '#F55459',
        data: [
          {name: 1656788400000, value: 206057},
          {name: 1656792000000, value: 197491},
          {name: 1656795600000, value: 184277},
          {name: 1656799200000, value: 181883},
          {name: 1656802800000, value: 173172},
          {name: 1656806400000, value: 195115},
          {name: 1656810000000, value: 203674},
          {name: 1656813600000, value: 170118},
          {name: 1656817200000, value: 170631},
          {name: 1656820800000, value: 174586},
          {name: 1656824400000, value: 175873},
          {name: 1656828000000, value: 188531},
          {name: 1656831600000, value: 207472},
          {name: 1656835200000, value: 215894},
          {name: 1656838800000, value: 212264},
          {name: 1656842400000, value: 211533},
          {name: 1656846000000, value: 222391},
          {name: 1656849600000, value: 234413},
          {name: 1656853200000, value: 235619},
          {name: 1656856800000, value: 231020},
          {name: 1656860400000, value: 226808},
          {name: 1656864000000, value: 224558},
          {name: 1656867600000, value: 218968},
          {name: 1656871200000, value: 215110},
          {name: 1656874800000, value: 211346},
          {name: 1656878400000, value: 209980},
          {name: 1656882000000, value: 194023},
          {name: 1656885600000, value: 192352},
          {name: 1656889200000, value: 209500},
          {name: 1656892800000, value: 257915},
          {name: 1656896400000, value: 311329},
          {name: 1656900000000, value: 296402},
          {name: 1656903600000, value: 291501},
          {name: 1656907200000, value: 325372},
          {name: 1656910800000, value: 369751},
          {name: 1656914400000, value: 534481},
          {name: 1656918000000, value: 707853},
          {name: 1656921600000, value: 775742},
          {name: 1656925200000, value: 753955},
          {name: 1656928800000, value: 662829},
          {name: 1656932400000, value: 639875},
          {name: 1656936000000, value: 702028},
          {name: 1656939600000, value: 722989},
          {name: 1656943200000, value: 701248},
          {name: 1656946800000, value: 584579},
          {name: 1656950400000, value: 466962},
          {name: 1656954000000, value: 382279},
          {name: 1656957600000, value: 219759},
        ],
        barMinHeight: 1,
        type: 'bar',
        stack: 'predictedUsage',
      },
    ]);

    expect(
      projectStatsToPredictedSeries(outcomesWithoutClientDiscarded, 0.3, 0.1, 0.2)
    ).toEqual([
      {
        seriesName: 'Indexed and Processed',
        color: '#2BA185',
        barMinHeight: 1,
        type: 'bar',
        stack: 'predictedUsage',
        data: [
          {name: 1656788400000, value: 147184},
          {name: 1656792000000, value: 141065},
          {name: 1656795600000, value: 131626},
          {name: 1656799200000, value: 129916},
          {name: 1656802800000, value: 123647},
          {name: 1656806400000, value: 139367},
          {name: 1656810000000, value: 145481},
          {name: 1656813600000, value: 121513},
          {name: 1656817200000, value: 121596},
          {name: 1656820800000, value: 124615},
          {name: 1656824400000, value: 125623},
          {name: 1656828000000, value: 134665},
          {name: 1656831600000, value: 148194},
          {name: 1656835200000, value: 154210},
          {name: 1656838800000, value: 151506},
          {name: 1656842400000, value: 151092},
          {name: 1656846000000, value: 158708},
          {name: 1656849600000, value: 167206},
          {name: 1656853200000, value: 168258},
          {name: 1656856800000, value: 165011},
          {name: 1656860400000, value: 162006},
          {name: 1656864000000, value: 159481},
          {name: 1656867600000, value: 156334},
          {name: 1656871200000, value: 153650},
          {name: 1656874800000, value: 150962},
          {name: 1656878400000, value: 149985},
          {name: 1656882000000, value: 138588},
          {name: 1656885600000, value: 137394},
          {name: 1656889200000, value: 149643},
          {name: 1656892800000, value: 184225},
          {name: 1656896400000, value: 222378},
          {name: 1656900000000, value: 211715},
          {name: 1656903600000, value: 208215},
          {name: 1656907200000, value: 232408},
          {name: 1656910800000, value: 263684},
          {name: 1656914400000, value: 369107},
          {name: 1656918000000, value: 432009},
          {name: 1656921600000, value: 444095},
          {name: 1656925200000, value: 444039},
          {name: 1656928800000, value: 423655},
          {name: 1656932400000, value: 416410},
          {name: 1656936000000, value: 434188},
          {name: 1656939600000, value: 440677},
          {name: 1656943200000, value: 436599},
          {name: 1656946800000, value: 396735},
          {name: 1656950400000, value: 330343},
          {name: 1656954000000, value: 272984},
          {name: 1656957600000, value: 156280},
        ],
      },
      {
        seriesName: 'Processed',
        color: '#F5B000',
        data: [
          {name: 1656788400000, value: 294367},
          {name: 1656792000000, value: 282129},
          {name: 1656795600000, value: 263252},
          {name: 1656799200000, value: 259832},
          {name: 1656802800000, value: 247294},
          {name: 1656806400000, value: 278734},
          {name: 1656810000000, value: 290962},
          {name: 1656813600000, value: 243026},
          {name: 1656817200000, value: 243192},
          {name: 1656820800000, value: 249230},
          {name: 1656824400000, value: 251246},
          {name: 1656828000000, value: 269329},
          {name: 1656831600000, value: 296387},
          {name: 1656835200000, value: 308420},
          {name: 1656838800000, value: 303012},
          {name: 1656842400000, value: 302184},
          {name: 1656846000000, value: 317415},
          {name: 1656849600000, value: 334411},
          {name: 1656853200000, value: 336515},
          {name: 1656856800000, value: 330022},
          {name: 1656860400000, value: 324011},
          {name: 1656864000000, value: 318962},
          {name: 1656867600000, value: 312667},
          {name: 1656871200000, value: 307300},
          {name: 1656874800000, value: 301923},
          {name: 1656878400000, value: 299970},
          {name: 1656882000000, value: 277175},
          {name: 1656885600000, value: 274788},
          {name: 1656889200000, value: 299285},
          {name: 1656892800000, value: 368449},
          {name: 1656896400000, value: 444755},
          {name: 1656900000000, value: 423429},
          {name: 1656903600000, value: 416430},
          {name: 1656907200000, value: 464816},
          {name: 1656910800000, value: 527367},
          {name: 1656914400000, value: 738213},
          {name: 1656918000000, value: 864018},
          {name: 1656921600000, value: 888189},
          {name: 1656925200000, value: 888078},
          {name: 1656928800000, value: 847309},
          {name: 1656932400000, value: 832819},
          {name: 1656936000000, value: 868375},
          {name: 1656939600000, value: 881353},
          {name: 1656943200000, value: 873198},
          {name: 1656946800000, value: 793470},
          {name: 1656950400000, value: 660685},
          {name: 1656954000000, value: 545968},
          {name: 1656957600000, value: 312560},
        ],
        barMinHeight: 1,
        type: 'bar',
        stack: 'predictedUsage',
      },
      {
        seriesName: 'Discarded',
        color: '#F55459',
        data: [
          {name: 1656788400000, value: 1030285},
          {name: 1656792000000, value: 987452},
          {name: 1656795600000, value: 921382},
          {name: 1656799200000, value: 909412},
          {name: 1656802800000, value: 865529},
          {name: 1656806400000, value: 975569},
          {name: 1656810000000, value: 1018367},
          {name: 1656813600000, value: 850591},
          {name: 1656817200000, value: 851172},
          {name: 1656820800000, value: 872305},
          {name: 1656824400000, value: 879361},
          {name: 1656828000000, value: 942652},
          {name: 1656831600000, value: 1037355},
          {name: 1656835200000, value: 1079470},
          {name: 1656838800000, value: 1060542},
          {name: 1656842400000, value: 1057644},
          {name: 1656846000000, value: 1110953},
          {name: 1656849600000, value: 1170439},
          {name: 1656853200000, value: 1177803},
          {name: 1656856800000, value: 1155077},
          {name: 1656860400000, value: 1134039},
          {name: 1656864000000, value: 1116367},
          {name: 1656867600000, value: 1094335},
          {name: 1656871200000, value: 1075550},
          {name: 1656874800000, value: 1056731},
          {name: 1656878400000, value: 1049895},
          {name: 1656882000000, value: 970113},
          {name: 1656885600000, value: 961758},
          {name: 1656889200000, value: 1047498},
          {name: 1656892800000, value: 1289572},
          {name: 1656896400000, value: 1556643},
          {name: 1656900000000, value: 1482002},
          {name: 1656903600000, value: 1457505},
          {name: 1656907200000, value: 1626856},
          {name: 1656910800000, value: 1845785},
          {name: 1656914400000, value: 2583746},
          {name: 1656918000000, value: 3024063},
          {name: 1656921600000, value: 3108662},
          {name: 1656925200000, value: 3108273},
          {name: 1656928800000, value: 2965582},
          {name: 1656932400000, value: 2914867},
          {name: 1656936000000, value: 3039313},
          {name: 1656939600000, value: 3084736},
          {name: 1656943200000, value: 3056193},
          {name: 1656946800000, value: 2777145},
          {name: 1656950400000, value: 2312398},
          {name: 1656954000000, value: 1910888},
          {name: 1656957600000, value: 1093960},
        ],
        barMinHeight: 1,
        type: 'bar',
        stack: 'predictedUsage',
      },
    ]);
  });
});
