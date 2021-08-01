window.BENCHMARK_DATA = {
  "lastUpdate": 1627776755694,
  "repoUrl": "https://github.com/tchar/ulauncher-albert-calculate-anything",
  "entries": {
    "Benchmark": [
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "Tilemachos Charalampous",
            "username": "tchar"
          },
          "committer": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "Tilemachos Charalampous",
            "username": "tchar"
          },
          "distinct": true,
          "id": "e9f296560951df3e8e96b5e0656e981fc3369b1a",
          "message": "Update benchmark action",
          "timestamp": "2021-07-31T22:59:19+03:00",
          "tree_id": "ac8e8a9fb57ea84b6d2d9b6f403cfa843d139a39",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/e9f296560951df3e8e96b5e0656e981fc3369b1a"
        },
        "date": 1627761621144,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 107.39551521831713,
            "unit": "iter/sec",
            "range": "stddev: 0.00011929618610935794",
            "extra": "mean: 9.311375786662666 msec\nrounds: 75"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 3279.805411908215,
            "unit": "iter/sec",
            "range": "stddev: 0.000008819378156693594",
            "extra": "mean: 304.89613693825595 usec\nrounds: 1979"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 5031.246164127906,
            "unit": "iter/sec",
            "range": "stddev: 0.000004817084118397484",
            "extra": "mean: 198.7579155100505 usec\nrounds: 1728"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 4074.7666977518998,
            "unit": "iter/sec",
            "range": "stddev: 0.0000061087627020862714",
            "extra": "mean: 245.4128234020644 usec\nrounds: 2316"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 5103.541322938894,
            "unit": "iter/sec",
            "range": "stddev: 0.000006015848531702725",
            "extra": "mean: 195.94237348589667 usec\nrounds: 3221"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 5079.7405383478,
            "unit": "iter/sec",
            "range": "stddev: 0.000005032766978119176",
            "extra": "mean: 196.86044837346216 usec\nrounds: 3167"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 7967.271952976556,
            "unit": "iter/sec",
            "range": "stddev: 0.000005371505694374183",
            "extra": "mean: 125.51347636958747 usec\nrounds: 4507"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 17.172767243067973,
            "unit": "iter/sec",
            "range": "stddev: 0.00013599155227358826",
            "extra": "mean: 58.23173317647241 msec\nrounds: 17"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 13.298102581510083,
            "unit": "iter/sec",
            "range": "stddev: 0.0002165237020759389",
            "extra": "mean: 75.19869800000022 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 13.160997553340193,
            "unit": "iter/sec",
            "range": "stddev: 0.0007538917071750222",
            "extra": "mean: 75.98208235713903 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 53.80718237787221,
            "unit": "iter/sec",
            "range": "stddev: 0.00017598740241780633",
            "extra": "mean: 18.584879486483615 msec\nrounds: 37"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 3379.7058527502445,
            "unit": "iter/sec",
            "range": "stddev: 0.000005673822845682418",
            "extra": "mean: 295.88373768866524 usec\nrounds: 1990"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 5746.670058300266,
            "unit": "iter/sec",
            "range": "stddev: 0.000006549875132069703",
            "extra": "mean: 174.01381841221928 usec\nrounds: 3150"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 3917.523350894667,
            "unit": "iter/sec",
            "range": "stddev: 0.000004497978216211707",
            "extra": "mean: 255.26331573023666 usec\nrounds: 2670"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 6445.958884435051,
            "unit": "iter/sec",
            "range": "stddev: 0.000002944371690159956",
            "extra": "mean: 155.1359569504365 usec\nrounds: 3554"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 5202.606476023707,
            "unit": "iter/sec",
            "range": "stddev: 0.0000037784550803479844",
            "extra": "mean: 192.2113472561332 usec\nrounds: 3280"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 6479.726150932004,
            "unit": "iter/sec",
            "range": "stddev: 0.0000032989810154620014",
            "extra": "mean: 154.32750963652472 usec\nrounds: 4099"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 6534.275909267063,
            "unit": "iter/sec",
            "range": "stddev: 0.000004800308460177631",
            "extra": "mean: 153.03914525277034 usec\nrounds: 4234"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 12783.375882469827,
            "unit": "iter/sec",
            "range": "stddev: 0.0000023614343065786905",
            "extra": "mean: 78.22659751179856 usec\nrounds: 7153"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 17.30843994908348,
            "unit": "iter/sec",
            "range": "stddev: 0.00013218145696011635",
            "extra": "mean: 57.77528205555882 msec\nrounds: 18"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 13.393538180357051,
            "unit": "iter/sec",
            "range": "stddev: 0.00014399763320727452",
            "extra": "mean: 74.66286999999738 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 13.292739762092063,
            "unit": "iter/sec",
            "range": "stddev: 0.0006811675896044276",
            "extra": "mean: 75.22903614285578 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 54.65040276042371,
            "unit": "iter/sec",
            "range": "stddev: 0.00018019563935934294",
            "extra": "mean: 18.298126811320998 msec\nrounds: 53"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 4431.629955019721,
            "unit": "iter/sec",
            "range": "stddev: 0.000007432259781578363",
            "extra": "mean: 225.65060940327317 usec\nrounds: 2765"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "Tilemachos Charalampous",
            "username": "tchar"
          },
          "committer": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "Tilemachos Charalampous",
            "username": "tchar"
          },
          "distinct": true,
          "id": "c61972ea4338d294c8851207ff1f6b4104a8523f",
          "message": "Update README",
          "timestamp": "2021-07-31T23:15:08+03:00",
          "tree_id": "e49e7906274e7d65f4c3e9a7a0751514292c10fe",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/c61972ea4338d294c8851207ff1f6b4104a8523f"
        },
        "date": 1627762577754,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 86.22807338483679,
            "unit": "iter/sec",
            "range": "stddev: 0.0012906566889262687",
            "extra": "mean: 11.597151145161154 msec\nrounds: 62"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 2049.518737118336,
            "unit": "iter/sec",
            "range": "stddev: 0.00013822111534456162",
            "extra": "mean: 487.91942317444716 usec\nrounds: 1562"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 3588.808581741859,
            "unit": "iter/sec",
            "range": "stddev: 0.0002059436553723353",
            "extra": "mean: 278.6440060045335 usec\nrounds: 1832"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 2847.8186092205024,
            "unit": "iter/sec",
            "range": "stddev: 0.00012472548413999072",
            "extra": "mean: 351.1459601964317 usec\nrounds: 2437"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 3709.2425840669835,
            "unit": "iter/sec",
            "range": "stddev: 0.00016013323553900813",
            "extra": "mean: 269.5968185784048 usec\nrounds: 3208"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 3705.9905749251398,
            "unit": "iter/sec",
            "range": "stddev: 0.0001202607603388326",
            "extra": "mean: 269.83338996219646 usec\nrounds: 3726"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 6130.790648253567,
            "unit": "iter/sec",
            "range": "stddev: 0.00005876562831405986",
            "extra": "mean: 163.1110989387417 usec\nrounds: 4619"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 13.380423913008803,
            "unit": "iter/sec",
            "range": "stddev: 0.0026638084553504662",
            "extra": "mean: 74.73604771428606 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 10.811082336323393,
            "unit": "iter/sec",
            "range": "stddev: 0.0024670377150850928",
            "extra": "mean: 92.49767681818226 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 10.426187800152261,
            "unit": "iter/sec",
            "range": "stddev: 0.0042246705530254456",
            "extra": "mean: 95.91233336362848 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 49.435983245051396,
            "unit": "iter/sec",
            "range": "stddev: 0.0013397883799023335",
            "extra": "mean: 20.228180656244987 msec\nrounds: 32"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 2448.928359812293,
            "unit": "iter/sec",
            "range": "stddev: 0.00017602197027915474",
            "extra": "mean: 408.34187574055807 usec\nrounds: 1352"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 3618.0914196897384,
            "unit": "iter/sec",
            "range": "stddev: 0.00009632373391281428",
            "extra": "mean: 276.3888149862595 usec\nrounds: 2162"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 2476.0670180937154,
            "unit": "iter/sec",
            "range": "stddev: 0.0001321556226286105",
            "extra": "mean: 403.8662898429478 usec\nrounds: 1349"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 4991.226480435506,
            "unit": "iter/sec",
            "range": "stddev: 0.0000662201914589999",
            "extra": "mean: 200.35155766218517 usec\nrounds: 1951"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 3871.364884125482,
            "unit": "iter/sec",
            "range": "stddev: 0.00006786753655879211",
            "extra": "mean: 258.30683232688716 usec\nrounds: 662"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 4816.266640779842,
            "unit": "iter/sec",
            "range": "stddev: 0.00013208083848775183",
            "extra": "mean: 207.62970046817875 usec\nrounds: 4704"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 4862.697732833212,
            "unit": "iter/sec",
            "range": "stddev: 0.00006810996366590967",
            "extra": "mean: 205.64716438119171 usec\nrounds: 4958"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 10042.385377589539,
            "unit": "iter/sec",
            "range": "stddev: 0.00004684197146532303",
            "extra": "mean: 99.57793516185781 usec\nrounds: 6817"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 14.168418904549604,
            "unit": "iter/sec",
            "range": "stddev: 0.0038299248710514417",
            "extra": "mean: 70.57950550000263 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 10.187156173523611,
            "unit": "iter/sec",
            "range": "stddev: 0.004901681868167047",
            "extra": "mean: 98.16282218181723 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 10.546511450590165,
            "unit": "iter/sec",
            "range": "stddev: 0.005589393283080082",
            "extra": "mean: 94.81808318181285 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 49.01858943343533,
            "unit": "iter/sec",
            "range": "stddev: 0.001769367561087965",
            "extra": "mean: 20.40042383018686 msec\nrounds: 53"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 3263.3556179592756,
            "unit": "iter/sec",
            "range": "stddev: 0.00015147729106101759",
            "extra": "mean: 306.43304532815375 usec\nrounds: 3243"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "Tilemachos Charalampous",
            "username": "tchar"
          },
          "committer": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "Tilemachos Charalampous",
            "username": "tchar"
          },
          "distinct": true,
          "id": "45427ad037cad764d2873de00ff9a9c32a20b749",
          "message": "Update .coveragerc",
          "timestamp": "2021-07-31T23:42:10+03:00",
          "tree_id": "f46d9a564da269af521ee396453b0d392d5bfadf",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/45427ad037cad764d2873de00ff9a9c32a20b749"
        },
        "date": 1627764203948,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 102.75171168278497,
            "unit": "iter/sec",
            "range": "stddev: 0.000579366351282539",
            "extra": "mean: 9.732197971428443 msec\nrounds: 70"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 2239.1157986868047,
            "unit": "iter/sec",
            "range": "stddev: 0.0000766199820938963",
            "extra": "mean: 446.60486098417925 usec\nrounds: 1971"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 4225.383214689759,
            "unit": "iter/sec",
            "range": "stddev: 0.00006152704000536921",
            "extra": "mean: 236.66492462114425 usec\nrounds: 2043"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 3559.9289637020647,
            "unit": "iter/sec",
            "range": "stddev: 0.00005807713109385948",
            "extra": "mean: 280.9044815770912 usec\nrounds: 3094"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 4240.751296146179,
            "unit": "iter/sec",
            "range": "stddev: 0.0000731203561845956",
            "extra": "mean: 235.80727332648794 usec\nrounds: 3794"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 4184.496657015537,
            "unit": "iter/sec",
            "range": "stddev: 0.000060225227772465426",
            "extra": "mean: 238.9773685978326 usec\nrounds: 3280"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 6733.984974979523,
            "unit": "iter/sec",
            "range": "stddev: 0.00005379805649849893",
            "extra": "mean: 148.50047983705824 usec\nrounds: 3174"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 15.913973403359142,
            "unit": "iter/sec",
            "range": "stddev: 0.0030134350521425516",
            "extra": "mean: 62.83785794118009 msec\nrounds: 17"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 12.376303629985662,
            "unit": "iter/sec",
            "range": "stddev: 0.007425328937643593",
            "extra": "mean: 80.79956907142868 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 11.617566106333884,
            "unit": "iter/sec",
            "range": "stddev: 0.004305083038876678",
            "extra": "mean: 86.07654915385427 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 58.840965233929055,
            "unit": "iter/sec",
            "range": "stddev: 0.0007534203639410868",
            "extra": "mean: 16.994962540542705 msec\nrounds: 37"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 2824.830153514219,
            "unit": "iter/sec",
            "range": "stddev: 0.00010999147087467792",
            "extra": "mean: 354.00358451850775 usec\nrounds: 2532"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 3949.5027095094238,
            "unit": "iter/sec",
            "range": "stddev: 0.00007555228370822848",
            "extra": "mean: 253.19643346293896 usec\nrounds: 2833"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 2675.131272396034,
            "unit": "iter/sec",
            "range": "stddev: 0.00008233840914278657",
            "extra": "mean: 373.8134312580221 usec\nrounds: 2553"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 5527.058902025485,
            "unit": "iter/sec",
            "range": "stddev: 0.000053289938408400266",
            "extra": "mean: 180.92805192170704 usec\nrounds: 3409"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 4438.887700275872,
            "unit": "iter/sec",
            "range": "stddev: 0.000050942149505784334",
            "extra": "mean: 225.28166232676966 usec\nrounds: 3533"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 5565.472635489285,
            "unit": "iter/sec",
            "range": "stddev: 0.0000528713424157067",
            "extra": "mean: 179.6792591564123 usec\nrounds: 4341"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 5564.38002219242,
            "unit": "iter/sec",
            "range": "stddev: 0.00005340883135740332",
            "extra": "mean: 179.71454070564906 usec\nrounds: 3599"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 11294.175024611923,
            "unit": "iter/sec",
            "range": "stddev: 0.00003725358480163104",
            "extra": "mean: 88.54121685035254 usec\nrounds: 8439"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 16.190261461352772,
            "unit": "iter/sec",
            "range": "stddev: 0.004429960642071613",
            "extra": "mean: 61.76552505881799 msec\nrounds: 17"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 12.489027564117354,
            "unit": "iter/sec",
            "range": "stddev: 0.003679629165588521",
            "extra": "mean: 80.07028528571222 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 12.649998525203562,
            "unit": "iter/sec",
            "range": "stddev: 0.004250382299053875",
            "extra": "mean: 79.05139261539226 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 59.84678867805945,
            "unit": "iter/sec",
            "range": "stddev: 0.0007213738667378989",
            "extra": "mean: 16.70933431999856 msec\nrounds: 50"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 3866.630528745758,
            "unit": "iter/sec",
            "range": "stddev: 0.00007540561751588607",
            "extra": "mean: 258.6231067503561 usec\nrounds: 2726"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "Tilemachos Charalampous",
            "username": "tchar"
          },
          "committer": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "Tilemachos Charalampous",
            "username": "tchar"
          },
          "distinct": true,
          "id": "3220643ad66289d8ae13a6d6ed5cbd8f5bc8fb84",
          "message": "Move demo to misc\n\nUpdate README\n\nAdd python badge",
          "timestamp": "2021-08-01T00:26:19+03:00",
          "tree_id": "d369ad76e981bae1160565256a7c86b1da06a3d2",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/3220643ad66289d8ae13a6d6ed5cbd8f5bc8fb84"
        },
        "date": 1627766876623,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 85.26751257389563,
            "unit": "iter/sec",
            "range": "stddev: 0.0011781822239502482",
            "extra": "mean: 11.727796083336745 msec\nrounds: 60"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 2285.089879396982,
            "unit": "iter/sec",
            "range": "stddev: 0.00008085761141887668",
            "extra": "mean: 437.6195479295075 usec\nrounds: 1763"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 3650.7142125397468,
            "unit": "iter/sec",
            "range": "stddev: 0.00003764086618239331",
            "extra": "mean: 273.9190037294963 usec\nrounds: 1609"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 2801.338959450391,
            "unit": "iter/sec",
            "range": "stddev: 0.0001541544584279911",
            "extra": "mean: 356.97215312930035 usec\nrounds: 2253"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 3395.3129494562836,
            "unit": "iter/sec",
            "range": "stddev: 0.00024439058793462073",
            "extra": "mean: 294.5236609662556 usec\nrounds: 2982"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 3547.3977858844073,
            "unit": "iter/sec",
            "range": "stddev: 0.00004912197483850908",
            "extra": "mean: 281.89677627334044 usec\nrounds: 2141"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 5932.969179678916,
            "unit": "iter/sec",
            "range": "stddev: 0.00007362473521377014",
            "extra": "mean: 168.54967044580513 usec\nrounds: 3969"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 12.95588827098293,
            "unit": "iter/sec",
            "range": "stddev: 0.0031392478560059696",
            "extra": "mean: 77.18498176923013 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 10.394775630120222,
            "unit": "iter/sec",
            "range": "stddev: 0.002372527366082467",
            "extra": "mean: 96.20217266665856 msec\nrounds: 9"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 10.241926720492417,
            "unit": "iter/sec",
            "range": "stddev: 0.0021831014269591007",
            "extra": "mean: 97.63787881816845 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 46.72927637417741,
            "unit": "iter/sec",
            "range": "stddev: 0.000908235602203399",
            "extra": "mean: 21.39986059258987 msec\nrounds: 27"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 2213.7497550390412,
            "unit": "iter/sec",
            "range": "stddev: 0.00015134431829540054",
            "extra": "mean: 451.72224083763444 usec\nrounds: 1337"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 3931.6872432547193,
            "unit": "iter/sec",
            "range": "stddev: 0.00009149355835033127",
            "extra": "mean: 254.34373034518953 usec\nrounds: 2633"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 2678.3437023339397,
            "unit": "iter/sec",
            "range": "stddev: 0.00010708819375838892",
            "extra": "mean: 373.3650760089485 usec\nrounds: 2355"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 4813.748543212672,
            "unit": "iter/sec",
            "range": "stddev: 0.0000671126126912795",
            "extra": "mean: 207.7383126731844 usec\nrounds: 2517"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 3342.1669210116916,
            "unit": "iter/sec",
            "range": "stddev: 0.00016707905127892164",
            "extra": "mean: 299.20707841165955 usec\nrounds: 3048"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 4362.183432850839,
            "unit": "iter/sec",
            "range": "stddev: 0.00018181599686710142",
            "extra": "mean: 229.24299617232396 usec\nrounds: 3919"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 4469.243307422127,
            "unit": "iter/sec",
            "range": "stddev: 0.00016902059264862877",
            "extra": "mean: 223.7515237398885 usec\nrounds: 4128"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 8614.231130064441,
            "unit": "iter/sec",
            "range": "stddev: 0.00020022290666848864",
            "extra": "mean: 116.08697107161542 usec\nrounds: 6326"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 12.372068022470462,
            "unit": "iter/sec",
            "range": "stddev: 0.005242569986055805",
            "extra": "mean: 80.8272310000054 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 8.131512202354784,
            "unit": "iter/sec",
            "range": "stddev: 0.019087131491949",
            "extra": "mean: 122.97835569999052 msec\nrounds: 10"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 9.089510008738838,
            "unit": "iter/sec",
            "range": "stddev: 0.011750837402247522",
            "extra": "mean: 110.01693150000165 msec\nrounds: 10"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 43.57069827095908,
            "unit": "iter/sec",
            "range": "stddev: 0.0028824930494325053",
            "extra": "mean: 22.951204357138437 msec\nrounds: 42"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 2941.3174317007347,
            "unit": "iter/sec",
            "range": "stddev: 0.0002456679122141749",
            "extra": "mean: 339.9837056763295 usec\nrounds: 2854"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "Tilemachos Charalampous",
            "username": "tchar"
          },
          "committer": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "Tilemachos Charalampous",
            "username": "tchar"
          },
          "distinct": true,
          "id": "fcb244afd2f157b5bd385a496916a3d386248dab",
          "message": "Update README",
          "timestamp": "2021-08-01T00:43:24+03:00",
          "tree_id": "f146f5e40c624127ac3941cb7c5c013b53b41fa1",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/fcb244afd2f157b5bd385a496916a3d386248dab"
        },
        "date": 1627767945502,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 95.20292144629389,
            "unit": "iter/sec",
            "range": "stddev: 0.00010294272887629156",
            "extra": "mean: 10.503879343283836 msec\nrounds: 67"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 2802.3907010837834,
            "unit": "iter/sec",
            "range": "stddev: 0.000013417550552327625",
            "extra": "mean: 356.83818091933597 usec\nrounds: 2023"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 4373.692465590133,
            "unit": "iter/sec",
            "range": "stddev: 0.000008420890675165936",
            "extra": "mean: 228.6397609954206 usec\nrounds: 1728"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 3538.3296784061868,
            "unit": "iter/sec",
            "range": "stddev: 0.0000072957730829074485",
            "extra": "mean: 282.61922740066507 usec\nrounds: 2489"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 4342.6470202229875,
            "unit": "iter/sec",
            "range": "stddev: 0.000024746457598707942",
            "extra": "mean: 230.27429937159653 usec\nrounds: 3023"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 4420.809506904746,
            "unit": "iter/sec",
            "range": "stddev: 0.000006515372257906062",
            "extra": "mean: 226.20291565111012 usec\nrounds: 3118"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 6973.893198938684,
            "unit": "iter/sec",
            "range": "stddev: 0.0000063429771247094355",
            "extra": "mean: 143.39192922429388 usec\nrounds: 4267"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 14.9322749655397,
            "unit": "iter/sec",
            "range": "stddev: 0.0003370945071267387",
            "extra": "mean: 66.9690319999982 msec\nrounds: 15"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 11.524558787236723,
            "unit": "iter/sec",
            "range": "stddev: 0.0003174998408132932",
            "extra": "mean: 86.77121775000056 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 11.492667898156942,
            "unit": "iter/sec",
            "range": "stddev: 0.0004075979966508022",
            "extra": "mean: 87.01199833333462 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 46.41815516864489,
            "unit": "iter/sec",
            "range": "stddev: 0.00018151247083110682",
            "extra": "mean: 21.54329478125172 msec\nrounds: 32"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 2903.1984195329474,
            "unit": "iter/sec",
            "range": "stddev: 0.000008677168256040333",
            "extra": "mean: 344.4476937132238 usec\nrounds: 1861"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 4867.7245609180545,
            "unit": "iter/sec",
            "range": "stddev: 0.000007509473116393146",
            "extra": "mean: 205.43479555700245 usec\nrounds: 2881"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 3339.615049307981,
            "unit": "iter/sec",
            "range": "stddev: 0.00000795244524504478",
            "extra": "mean: 299.43570897706167 usec\nrounds: 2395"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 5647.643010710674,
            "unit": "iter/sec",
            "range": "stddev: 0.000005359622724026105",
            "extra": "mean: 177.06501599047857 usec\nrounds: 3377"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 4506.989327160548,
            "unit": "iter/sec",
            "range": "stddev: 0.00000625869043859639",
            "extra": "mean: 221.87760551676539 usec\nrounds: 3009"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 5603.782539789109,
            "unit": "iter/sec",
            "range": "stddev: 0.000004541142510834243",
            "extra": "mean: 178.45089328495493 usec\nrounds: 3842"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 5675.788647874687,
            "unit": "iter/sec",
            "range": "stddev: 0.000006161705917505868",
            "extra": "mean: 176.18696925482814 usec\nrounds: 3838"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 11275.629162851972,
            "unit": "iter/sec",
            "range": "stddev: 0.00000275635996305706",
            "extra": "mean: 88.68684714237868 usec\nrounds: 6614"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 15.254705447612164,
            "unit": "iter/sec",
            "range": "stddev: 0.0007018681292387423",
            "extra": "mean: 65.55354368750076 msec\nrounds: 16"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 11.766017943312555,
            "unit": "iter/sec",
            "range": "stddev: 0.00040672159249344555",
            "extra": "mean: 84.99052141666752 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 11.693812100634737,
            "unit": "iter/sec",
            "range": "stddev: 0.0009955137481731822",
            "extra": "mean: 85.51531283333347 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 47.03801184698886,
            "unit": "iter/sec",
            "range": "stddev: 0.0002877780225996045",
            "extra": "mean: 21.259401933332672 msec\nrounds: 45"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 3811.5986230906456,
            "unit": "iter/sec",
            "range": "stddev: 0.000005785571616276014",
            "extra": "mean: 262.35711020095476 usec\nrounds: 2686"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "Tilemachos Charalampous",
            "username": "tchar"
          },
          "committer": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "Tilemachos Charalampous",
            "username": "tchar"
          },
          "distinct": true,
          "id": "13616e8f5d1f0ed574568dad04577e3b4b38056c",
          "message": "Use paths-ignore in github actions",
          "timestamp": "2021-08-01T00:56:24+03:00",
          "tree_id": "85c914b33ef134ff0a0ef8c972e926465ecc5360",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/13616e8f5d1f0ed574568dad04577e3b4b38056c"
        },
        "date": 1627768661110,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 82.08305942261465,
            "unit": "iter/sec",
            "range": "stddev: 0.0014227707206716869",
            "extra": "mean: 12.182781770491495 msec\nrounds: 61"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 2178.008266301051,
            "unit": "iter/sec",
            "range": "stddev: 0.00016340852129119416",
            "extra": "mean: 459.13508018879884 usec\nrounds: 1484"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 3504.0994533565686,
            "unit": "iter/sec",
            "range": "stddev: 0.00009514392257329137",
            "extra": "mean: 285.3800279675574 usec\nrounds: 1609"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 2849.6152919833326,
            "unit": "iter/sec",
            "range": "stddev: 0.00019122241996958895",
            "extra": "mean: 350.9245626289435 usec\nrounds: 2419"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 3513.8597481954125,
            "unit": "iter/sec",
            "range": "stddev: 0.00010502468434558154",
            "extra": "mean: 284.58734032101387 usec\nrounds: 3053"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 3508.9523501286935,
            "unit": "iter/sec",
            "range": "stddev: 0.00009721562192668563",
            "extra": "mean: 284.98534611429653 usec\nrounds: 2921"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 5738.291783669579,
            "unit": "iter/sec",
            "range": "stddev: 0.0001445917583264367",
            "extra": "mean: 174.26788976570836 usec\nrounds: 3928"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 13.328652627879393,
            "unit": "iter/sec",
            "range": "stddev: 0.0028881398136934616",
            "extra": "mean: 75.02633821428516 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 10.475075798434307,
            "unit": "iter/sec",
            "range": "stddev: 0.0018923542275384728",
            "extra": "mean: 95.4647029999982 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 10.283535913350272,
            "unit": "iter/sec",
            "range": "stddev: 0.004059798236621407",
            "extra": "mean: 97.2428169090927 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 45.66068496235633,
            "unit": "iter/sec",
            "range": "stddev: 0.0014749183694914045",
            "extra": "mean: 21.900678906249915 msec\nrounds: 32"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 2380.32051960364,
            "unit": "iter/sec",
            "range": "stddev: 0.00020814914070474685",
            "extra": "mean: 420.1114899293123 usec\nrounds: 1837"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 4060.6723141011234,
            "unit": "iter/sec",
            "range": "stddev: 0.00018493011439707008",
            "extra": "mean: 246.26463862336095 usec\nrounds: 2615"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 2744.62897317048,
            "unit": "iter/sec",
            "range": "stddev: 0.00011489819466216544",
            "extra": "mean: 364.3479719026802 usec\nrounds: 2349"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 4586.111589974176,
            "unit": "iter/sec",
            "range": "stddev: 0.00014588061932898058",
            "extra": "mean: 218.04964410070775 usec\nrounds: 3102"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 3636.4992974012434,
            "unit": "iter/sec",
            "range": "stddev: 0.00014083657075293068",
            "extra": "mean: 274.98974101676066 usec\nrounds: 2950"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 4570.733496538225,
            "unit": "iter/sec",
            "range": "stddev: 0.00011170729583982362",
            "extra": "mean: 218.78326547749464 usec\nrounds: 2859"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 4299.629476006893,
            "unit": "iter/sec",
            "range": "stddev: 0.00014611269906882767",
            "extra": "mean: 232.57818041770182 usec\nrounds: 3830"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 9639.259317143325,
            "unit": "iter/sec",
            "range": "stddev: 0.00012534025402569074",
            "extra": "mean: 103.74241081174256 usec\nrounds: 6419"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 13.584709256971438,
            "unit": "iter/sec",
            "range": "stddev: 0.0028474100528422495",
            "extra": "mean: 73.61217535714408 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 10.585415694865237,
            "unit": "iter/sec",
            "range": "stddev: 0.001895167473888895",
            "extra": "mean: 94.4696012727284 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 10.203416489158732,
            "unit": "iter/sec",
            "range": "stddev: 0.006972579074026422",
            "extra": "mean: 98.00638845454496 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 45.476686839480266,
            "unit": "iter/sec",
            "range": "stddev: 0.002188780507737296",
            "extra": "mean: 21.98928878723542 msec\nrounds: 47"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 3171.533132430523,
            "unit": "iter/sec",
            "range": "stddev: 0.00023562574433217038",
            "extra": "mean: 315.3049198113356 usec\nrounds: 2544"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "Tilemachos Charalampous",
            "username": "tchar"
          },
          "committer": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "Tilemachos Charalampous",
            "username": "tchar"
          },
          "distinct": true,
          "id": "f70c348891afe2de3802be1fcf5d65f778b853eb",
          "message": "Update requirements",
          "timestamp": "2021-08-01T02:16:17+03:00",
          "tree_id": "cb8cf0a9e9cd037a6f12c34d0a21c6b26fb69364",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/f70c348891afe2de3802be1fcf5d65f778b853eb"
        },
        "date": 1627773438453,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 87.16165337441609,
            "unit": "iter/sec",
            "range": "stddev: 0.0003819098932898991",
            "extra": "mean: 11.472935187499811 msec\nrounds: 64"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 2565.1341310495204,
            "unit": "iter/sec",
            "range": "stddev: 0.00005766585052761165",
            "extra": "mean: 389.8431617651322 usec\nrounds: 1972"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 3850.5715475221364,
            "unit": "iter/sec",
            "range": "stddev: 0.00012674630665843482",
            "extra": "mean: 259.7017060086847 usec\nrounds: 1398"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 3297.598427941479,
            "unit": "iter/sec",
            "range": "stddev: 0.00004323147895681581",
            "extra": "mean: 303.2509936706419 usec\nrounds: 2528"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 4057.2741719371807,
            "unit": "iter/sec",
            "range": "stddev: 0.00002869187994170913",
            "extra": "mean: 246.47089588292263 usec\nrounds: 2939"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 4040.5880521083095,
            "unit": "iter/sec",
            "range": "stddev: 0.00003441414409564028",
            "extra": "mean: 247.48872864637048 usec\nrounds: 3044"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 6462.122922953682,
            "unit": "iter/sec",
            "range": "stddev: 0.00002804640228361763",
            "extra": "mean: 154.74790744818017 usec\nrounds: 4095"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 13.674994467284176,
            "unit": "iter/sec",
            "range": "stddev: 0.001843157853598032",
            "extra": "mean: 73.12617218181572 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 10.469955009727977,
            "unit": "iter/sec",
            "range": "stddev: 0.002832195376386952",
            "extra": "mean: 95.51139418181523 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 10.467563080791995,
            "unit": "iter/sec",
            "range": "stddev: 0.0030041879207245267",
            "extra": "mean: 95.53321936363606 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 44.12915918833361,
            "unit": "iter/sec",
            "range": "stddev: 0.0005964026915524727",
            "extra": "mean: 22.660753533331974 msec\nrounds: 30"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 2683.463989888084,
            "unit": "iter/sec",
            "range": "stddev: 0.000051935814378723694",
            "extra": "mean: 372.65266229330166 usec\nrounds: 2058"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 4466.064341528843,
            "unit": "iter/sec",
            "range": "stddev: 0.00005387008230090158",
            "extra": "mean: 223.91079114137335 usec\nrounds: 2935"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 3073.356284209697,
            "unit": "iter/sec",
            "range": "stddev: 0.00008158393909219144",
            "extra": "mean: 325.3771797099491 usec\nrounds: 2415"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 5064.683702576127,
            "unit": "iter/sec",
            "range": "stddev: 0.0001106140942026881",
            "extra": "mean: 197.44569626161547 usec\nrounds: 3424"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 4125.054497767085,
            "unit": "iter/sec",
            "range": "stddev: 0.00003620533394691931",
            "extra": "mean: 242.42103965930764 usec\nrounds: 3051"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 5134.991540704974,
            "unit": "iter/sec",
            "range": "stddev: 0.00004169357885705816",
            "extra": "mean: 194.74228770836726 usec\nrounds: 3726"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 5184.0042019218245,
            "unit": "iter/sec",
            "range": "stddev: 0.00004703023755172841",
            "extra": "mean: 192.90107821079272 usec\nrounds: 3823"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 10523.511841592059,
            "unit": "iter/sec",
            "range": "stddev: 0.000020122052166992095",
            "extra": "mean: 95.02531237221606 usec\nrounds: 6854"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 13.772148913390303,
            "unit": "iter/sec",
            "range": "stddev: 0.001565743913780568",
            "extra": "mean: 72.61030985714407 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 10.677918412531985,
            "unit": "iter/sec",
            "range": "stddev: 0.0021938121662234936",
            "extra": "mean: 93.65121190908935 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 10.705381728530355,
            "unit": "iter/sec",
            "range": "stddev: 0.0008795571686462226",
            "extra": "mean: 93.41096145455067 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 43.70178591777358,
            "unit": "iter/sec",
            "range": "stddev: 0.0012096878976319853",
            "extra": "mean: 22.882360045457517 msec\nrounds: 44"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 3433.8379171870747,
            "unit": "iter/sec",
            "range": "stddev: 0.00014234009354440534",
            "extra": "mean: 291.2193365315211 usec\nrounds: 2710"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "Tilemachos Charalampous",
            "username": "tchar"
          },
          "committer": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "Tilemachos Charalampous",
            "username": "tchar"
          },
          "distinct": true,
          "id": "9d20d61f102af50ae5816b608857e0406a367124",
          "message": "Update benchmark-linux.yml",
          "timestamp": "2021-08-01T02:45:27+03:00",
          "tree_id": "175d0af2e9dc93975a44eba4419078a36ccc88c7",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/9d20d61f102af50ae5816b608857e0406a367124"
        },
        "date": 1627775271217,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 89.29527839381132,
            "unit": "iter/sec",
            "range": "stddev: 0.000584111134043255",
            "extra": "mean: 11.198800406778346 msec\nrounds: 59"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 2106.1905635350554,
            "unit": "iter/sec",
            "range": "stddev: 0.00008423207656884042",
            "extra": "mean: 474.79084623833285 usec\nrounds: 1821"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 3651.8909875957647,
            "unit": "iter/sec",
            "range": "stddev: 0.00005778953663942211",
            "extra": "mean: 273.830736841998 usec\nrounds: 1862"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 3096.6219129889296,
            "unit": "iter/sec",
            "range": "stddev: 0.00007082463809272347",
            "extra": "mean: 322.932546529317 usec\nrounds: 2622"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 3671.820740939196,
            "unit": "iter/sec",
            "range": "stddev: 0.00012812953896988017",
            "extra": "mean: 272.3444499483423 usec\nrounds: 3876"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 3699.948301892633,
            "unit": "iter/sec",
            "range": "stddev: 0.00005891362530642229",
            "extra": "mean: 270.27404666396836 usec\nrounds: 2593"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 6128.843512598342,
            "unit": "iter/sec",
            "range": "stddev: 0.00004418687751008448",
            "extra": "mean: 163.1629193899987 usec\nrounds: 4131"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 15.408394389256035,
            "unit": "iter/sec",
            "range": "stddev: 0.0032295658880038677",
            "extra": "mean: 64.89968875000241 msec\nrounds: 16"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 10.646129503230291,
            "unit": "iter/sec",
            "range": "stddev: 0.014955892196557618",
            "extra": "mean: 93.93085061538805 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 11.207168750665724,
            "unit": "iter/sec",
            "range": "stddev: 0.0024620980474643023",
            "extra": "mean: 89.22860200000098 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 49.653329257312045,
            "unit": "iter/sec",
            "range": "stddev: 0.0016352570457403223",
            "extra": "mean: 20.13963645454324 msec\nrounds: 33"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 2648.745235163835,
            "unit": "iter/sec",
            "range": "stddev: 0.00007995218196163094",
            "extra": "mean: 377.5372530073268 usec\nrounds: 2494"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 3789.5552121179735,
            "unit": "iter/sec",
            "range": "stddev: 0.000060293983786928644",
            "extra": "mean: 263.8832116239579 usec\nrounds: 2925"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 2571.4767085319336,
            "unit": "iter/sec",
            "range": "stddev: 0.00006305458848780328",
            "extra": "mean: 388.8816090311407 usec\nrounds: 2591"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 4139.231301485181,
            "unit": "iter/sec",
            "range": "stddev: 0.00031246430957281344",
            "extra": "mean: 241.59075131684332 usec\nrounds: 2658"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 3866.1065733977252,
            "unit": "iter/sec",
            "range": "stddev: 0.00005311419457220812",
            "extra": "mean: 258.6581567308298 usec\nrounds: 3573"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 4689.48414710259,
            "unit": "iter/sec",
            "range": "stddev: 0.00007481620139954133",
            "extra": "mean: 213.24307080083693 usec\nrounds: 3983"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 4997.163704986261,
            "unit": "iter/sec",
            "range": "stddev: 0.00004951614036996894",
            "extra": "mean: 200.11351619363236 usec\nrounds: 2995"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 10428.29836633273,
            "unit": "iter/sec",
            "range": "stddev: 0.000034332777796964425",
            "extra": "mean: 95.89292182399124 usec\nrounds: 7675"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 13.587582385905993,
            "unit": "iter/sec",
            "range": "stddev: 0.009957691967614033",
            "extra": "mean: 73.59660987500405 msec\nrounds: 16"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 10.583714381849564,
            "unit": "iter/sec",
            "range": "stddev: 0.0035488288120079843",
            "extra": "mean: 94.4847870909045 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 11.142822977514326,
            "unit": "iter/sec",
            "range": "stddev: 0.0057429174437163555",
            "extra": "mean: 89.74386490909451 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 53.77701481483395,
            "unit": "iter/sec",
            "range": "stddev: 0.0010627341209141585",
            "extra": "mean: 18.595305139997436 msec\nrounds: 50"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 3408.9147529779216,
            "unit": "iter/sec",
            "range": "stddev: 0.00017180119757997074",
            "extra": "mean: 293.3484913714639 usec\nrounds: 3303"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "Tilemachos Charalampous",
            "username": "tchar"
          },
          "committer": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "Tilemachos Charalampous",
            "username": "tchar"
          },
          "distinct": true,
          "id": "e8dbebe284e0d27638ff30cd878891cb6b59b743",
          "message": "Update actions",
          "timestamp": "2021-08-01T03:11:21+03:00",
          "tree_id": "96b3e0889d4a01cddd810eb622a22c936d133368",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/e8dbebe284e0d27638ff30cd878891cb6b59b743"
        },
        "date": 1627776754854,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 91.51309967801191,
            "unit": "iter/sec",
            "range": "stddev: 0.0007042087315905576",
            "extra": "mean: 10.92739731818168 msec\nrounds: 66"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 2809.3757796581713,
            "unit": "iter/sec",
            "range": "stddev: 0.00013738932719748392",
            "extra": "mean: 355.95095794613644 usec\nrounds: 2045"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 4314.061449047088,
            "unit": "iter/sec",
            "range": "stddev: 0.00007075713093521441",
            "extra": "mean: 231.80012890657483 usec\nrounds: 1536"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 3362.8724060252903,
            "unit": "iter/sec",
            "range": "stddev: 0.00010928886440340773",
            "extra": "mean: 297.36483555197947 usec\nrounds: 2554"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 4262.14267406111,
            "unit": "iter/sec",
            "range": "stddev: 0.00006030901322886165",
            "extra": "mean: 234.6237741138701 usec\nrounds: 3245"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 4300.190306059222,
            "unit": "iter/sec",
            "range": "stddev: 0.0000732267102319497",
            "extra": "mean: 232.54784761291629 usec\nrounds: 3058"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 6432.483392898235,
            "unit": "iter/sec",
            "range": "stddev: 0.00006214734680587492",
            "extra": "mean: 155.46095324615172 usec\nrounds: 4128"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 14.175713503069282,
            "unit": "iter/sec",
            "range": "stddev: 0.0019966975230053838",
            "extra": "mean: 70.54318639999906 msec\nrounds: 15"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 10.919623046154673,
            "unit": "iter/sec",
            "range": "stddev: 0.0023774306791480037",
            "extra": "mean: 91.57825281818207 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 11.109788754476984,
            "unit": "iter/sec",
            "range": "stddev: 0.006125141782586931",
            "extra": "mean: 90.0107123636373 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 46.22686015406992,
            "unit": "iter/sec",
            "range": "stddev: 0.0013556727590679934",
            "extra": "mean: 21.6324447878807 msec\nrounds: 33"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 2956.8317962309784,
            "unit": "iter/sec",
            "range": "stddev: 0.00012300434601775608",
            "extra": "mean: 338.199826339355 usec\nrounds: 2240"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 4720.472217726968,
            "unit": "iter/sec",
            "range": "stddev: 0.00015390979577967353",
            "extra": "mean: 211.84321268636265 usec\nrounds: 2680"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 3420.395838940183,
            "unit": "iter/sec",
            "range": "stddev: 0.0000946793060635731",
            "extra": "mean: 292.36382193408707 usec\nrounds: 2544"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 5779.832692855902,
            "unit": "iter/sec",
            "range": "stddev: 0.00008666021235989116",
            "extra": "mean: 173.0153887042507 usec\nrounds: 3612"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 4585.73513653255,
            "unit": "iter/sec",
            "range": "stddev: 0.0000567562454900948",
            "extra": "mean: 218.06754429261218 usec\nrounds: 3364"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 5585.846970296227,
            "unit": "iter/sec",
            "range": "stddev: 0.00005537919942770354",
            "extra": "mean: 179.02388041020185 usec\nrounds: 3997"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 5656.688387347652,
            "unit": "iter/sec",
            "range": "stddev: 0.00005113039467482491",
            "extra": "mean: 176.7818786406382 usec\nrounds: 3914"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 11018.230343011875,
            "unit": "iter/sec",
            "range": "stddev: 0.00005989364061274026",
            "extra": "mean: 90.75867620014253 usec\nrounds: 7937"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 15.234053545998794,
            "unit": "iter/sec",
            "range": "stddev: 0.0022405032067401827",
            "extra": "mean: 65.64241073333031 msec\nrounds: 15"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 11.628531142660133,
            "unit": "iter/sec",
            "range": "stddev: 0.004302621131358839",
            "extra": "mean: 85.99538391666901 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 11.541091275983685,
            "unit": "iter/sec",
            "range": "stddev: 0.002751832732210499",
            "extra": "mean: 86.64691891666602 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 48.24042313325202,
            "unit": "iter/sec",
            "range": "stddev: 0.0011707138747056752",
            "extra": "mean: 20.729503081632426 msec\nrounds: 49"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 3882.3077027191025,
            "unit": "iter/sec",
            "range": "stddev: 0.00009983081846002393",
            "extra": "mean: 257.57875896843956 usec\nrounds: 2676"
          }
        ]
      }
    ]
  }
}