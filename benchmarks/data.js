window.BENCHMARK_DATA = {
  "lastUpdate": 1717019894345,
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
          "id": "a12c786d5c3e1b39a2bbcbb160156d0acaa71b91",
          "message": "Update actions",
          "timestamp": "2021-08-01T03:22:05+03:00",
          "tree_id": "cd20c3d85ea13164767f7c28d8a8d78f9b6f5f14",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/a12c786d5c3e1b39a2bbcbb160156d0acaa71b91"
        },
        "date": 1627777406342,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 91.84291513423146,
            "unit": "iter/sec",
            "range": "stddev: 0.00007332202208490399",
            "extra": "mean: 10.888156136360294 msec\nrounds: 66"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 2739.151577172449,
            "unit": "iter/sec",
            "range": "stddev: 0.0001692178890140289",
            "extra": "mean: 365.0765471811796 usec\nrounds: 1738"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 4382.844157158134,
            "unit": "iter/sec",
            "range": "stddev: 0.0000053551449004350255",
            "extra": "mean: 228.16234484787313 usec\nrounds: 1679"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 3523.053256428815,
            "unit": "iter/sec",
            "range": "stddev: 0.000006062341370575473",
            "extra": "mean: 283.8447015171329 usec\nrounds: 2372"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 4358.43034259558,
            "unit": "iter/sec",
            "range": "stddev: 0.000004432826061904657",
            "extra": "mean: 229.4403997298874 usec\nrounds: 2967"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 4369.286815571412,
            "unit": "iter/sec",
            "range": "stddev: 0.0000050682755058473165",
            "extra": "mean: 228.87030360107423 usec\nrounds: 3027"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 6863.484664639663,
            "unit": "iter/sec",
            "range": "stddev: 0.000005872587867478241",
            "extra": "mean: 145.69858444529658 usec\nrounds: 3896"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 14.509960361324865,
            "unit": "iter/sec",
            "range": "stddev: 0.0002365750416000464",
            "extra": "mean: 68.91817586665638 msec\nrounds: 15"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 11.169970744478793,
            "unit": "iter/sec",
            "range": "stddev: 0.000404018428183916",
            "extra": "mean: 89.52574924999605 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 11.169932274401003,
            "unit": "iter/sec",
            "range": "stddev: 0.00020109441324949414",
            "extra": "mean: 89.52605758333713 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 45.185315938090994,
            "unit": "iter/sec",
            "range": "stddev: 0.00007881659231371255",
            "extra": "mean: 22.131083500005033 msec\nrounds: 32"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 2896.5143488904127,
            "unit": "iter/sec",
            "range": "stddev: 0.000007915566956518918",
            "extra": "mean: 345.24255002675085 usec\nrounds: 1849"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 4839.688988579644,
            "unit": "iter/sec",
            "range": "stddev: 0.000007034038006642718",
            "extra": "mean: 206.62484766267613 usec\nrounds: 2803"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 3323.967268401375,
            "unit": "iter/sec",
            "range": "stddev: 0.000005519305318184449",
            "extra": "mean: 300.84532104341054 usec\nrounds: 2414"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 5588.595408434627,
            "unit": "iter/sec",
            "range": "stddev: 0.000004807655959653768",
            "extra": "mean: 178.9358375256049 usec\nrounds: 3379"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 4471.360433551828,
            "unit": "iter/sec",
            "range": "stddev: 0.0000044323799981525004",
            "extra": "mean: 223.64558054776393 usec\nrounds: 2992"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 5604.6634946176055,
            "unit": "iter/sec",
            "range": "stddev: 0.000005040463540947776",
            "extra": "mean: 178.4228439335104 usec\nrounds: 3569"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 5633.964618237045,
            "unit": "iter/sec",
            "range": "stddev: 0.000004022043431422729",
            "extra": "mean: 177.49490239307102 usec\nrounds: 3719"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 11151.749284785621,
            "unit": "iter/sec",
            "range": "stddev: 0.0000023171550558860788",
            "extra": "mean: 89.67203032122542 usec\nrounds: 6761"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 14.850655967287494,
            "unit": "iter/sec",
            "range": "stddev: 0.00012685335101771266",
            "extra": "mean: 67.33709286665619 msec\nrounds: 15"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 11.45221965136671,
            "unit": "iter/sec",
            "range": "stddev: 0.00019920104793354605",
            "extra": "mean: 87.3193171666647 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 11.38735630229889,
            "unit": "iter/sec",
            "range": "stddev: 0.00020772526729675688",
            "extra": "mean: 87.81669541666304 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 45.75700377900733,
            "unit": "iter/sec",
            "range": "stddev: 0.0001653728610659961",
            "extra": "mean: 21.854577822221522 msec\nrounds: 45"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 3770.6842172222946,
            "unit": "iter/sec",
            "range": "stddev: 0.000005283497049077763",
            "extra": "mean: 265.2038575472804 usec\nrounds: 2471"
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
          "id": "328c496e164f646a5d0be06925cee56388803e26",
          "message": "Update logging module\n\nMove loggers from objects to modules",
          "timestamp": "2021-08-04T06:11:02+03:00",
          "tree_id": "d5fff82d2cb697c06fde37f0434d6bdf97328db9",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/328c496e164f646a5d0be06925cee56388803e26"
        },
        "date": 1628046759688,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 100.35025122750181,
            "unit": "iter/sec",
            "range": "stddev: 0.00040976442945228245",
            "extra": "mean: 9.965097124997946 msec\nrounds: 72"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 3457.8327500575147,
            "unit": "iter/sec",
            "range": "stddev: 0.000015027650500998018",
            "extra": "mean: 289.19848711114406 usec\nrounds: 2250"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 6469.999566832768,
            "unit": "iter/sec",
            "range": "stddev: 0.000010008785156400814",
            "extra": "mean: 154.55951575735975 usec\nrounds: 1999"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 5093.654682307731,
            "unit": "iter/sec",
            "range": "stddev: 0.000010196440376818055",
            "extra": "mean: 196.3226921277946 usec\nrounds: 3849"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 6267.773767364221,
            "unit": "iter/sec",
            "range": "stddev: 0.000007662809573101418",
            "extra": "mean: 159.54628184043864 usec\nrounds: 3761"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 6273.588878912129,
            "unit": "iter/sec",
            "range": "stddev: 0.000006945029369071282",
            "extra": "mean: 159.39839528875933 usec\nrounds: 3863"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 12635.064414114919,
            "unit": "iter/sec",
            "range": "stddev: 0.000005479386826328567",
            "extra": "mean: 79.14482801392585 usec\nrounds: 5640"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 15.078681313025807,
            "unit": "iter/sec",
            "range": "stddev: 0.00045793629897561595",
            "extra": "mean: 66.31879666666501 msec\nrounds: 15"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 11.691344404070573,
            "unit": "iter/sec",
            "range": "stddev: 0.0004898571279974718",
            "extra": "mean: 85.53336258333388 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 11.670551976582182,
            "unit": "iter/sec",
            "range": "stddev: 0.0021329049022986",
            "extra": "mean: 85.68575008333568 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 47.661571887609746,
            "unit": "iter/sec",
            "range": "stddev: 0.00040839044304970083",
            "extra": "mean: 20.981263529412953 msec\nrounds: 34"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 3454.481011257725,
            "unit": "iter/sec",
            "range": "stddev: 0.000015174093772703792",
            "extra": "mean: 289.4790843374516 usec\nrounds: 2241"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 5481.63410904855,
            "unit": "iter/sec",
            "range": "stddev: 0.000013830124268354738",
            "extra": "mean: 182.42735288539177 usec\nrounds: 3171"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 4118.821589731042,
            "unit": "iter/sec",
            "range": "stddev: 0.000018907560738308573",
            "extra": "mean: 242.78788925773785 usec\nrounds: 2709"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 8453.356807465023,
            "unit": "iter/sec",
            "range": "stddev: 0.000007504742273767198",
            "extra": "mean: 118.29620147074783 usec\nrounds: 4760"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 6577.7896959468035,
            "unit": "iter/sec",
            "range": "stddev: 0.000009975514703978183",
            "extra": "mean: 152.026751572218 usec\nrounds: 4134"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 8436.578852205583,
            "unit": "iter/sec",
            "range": "stddev: 0.000008110465370218449",
            "extra": "mean: 118.53145896201386 usec\nrounds: 5105"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 8450.993710762083,
            "unit": "iter/sec",
            "range": "stddev: 0.00000791861563530668",
            "extra": "mean: 118.32927987232206 usec\nrounds: 5013"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 30183.595383688422,
            "unit": "iter/sec",
            "range": "stddev: 0.000003295140018018956",
            "extra": "mean: 33.13057928613806 usec\nrounds: 13054"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 15.80727137704075,
            "unit": "iter/sec",
            "range": "stddev: 0.0012818264477745024",
            "extra": "mean: 63.262025187500015 msec\nrounds: 16"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 12.102974466843117,
            "unit": "iter/sec",
            "range": "stddev: 0.0014271750990173218",
            "extra": "mean: 82.62431708333888 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 12.033154105335617,
            "unit": "iter/sec",
            "range": "stddev: 0.0016418694160112012",
            "extra": "mean: 83.10373084614534 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 50.05926652141349,
            "unit": "iter/sec",
            "range": "stddev: 0.0007288706665798847",
            "extra": "mean: 19.976321458330542 msec\nrounds: 48"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 4489.633422966491,
            "unit": "iter/sec",
            "range": "stddev: 0.000012576465603506736",
            "extra": "mean: 222.7353339995535 usec\nrounds: 3003"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "9965e0fe019cf7a20c84c4e5d775ea912cad9811",
          "message": "Merge pull request #13 from tchar/development\n\nCreate UpdateThread for currency updates",
          "timestamp": "2021-08-04T09:16:13+03:00",
          "tree_id": "7f8faf17f28757737dd20dd4dc9e5cfec56d33f5",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/9965e0fe019cf7a20c84c4e5d775ea912cad9811"
        },
        "date": 1628057834858,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 82.76852923927244,
            "unit": "iter/sec",
            "range": "stddev: 0.0012745474569164186",
            "extra": "mean: 12.081886789472088 msec\nrounds: 57"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 2436.425528069745,
            "unit": "iter/sec",
            "range": "stddev: 0.0001835115098660056",
            "extra": "mean: 410.4373347262737 usec\nrounds: 1915"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 5200.708038935462,
            "unit": "iter/sec",
            "range": "stddev: 0.00006922423413602024",
            "extra": "mean: 192.28151100070036 usec\nrounds: 1818"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 4120.262725425658,
            "unit": "iter/sec",
            "range": "stddev: 0.00013565684079057733",
            "extra": "mean: 242.70296984440276 usec\nrounds: 4112"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 5042.674539515908,
            "unit": "iter/sec",
            "range": "stddev: 0.00011169398457354718",
            "extra": "mean: 198.3074640577536 usec\nrounds: 4702"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 4902.56835378635,
            "unit": "iter/sec",
            "range": "stddev: 0.00012526675155171573",
            "extra": "mean: 203.9747185223191 usec\nrounds: 4249"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 10270.63563228278,
            "unit": "iter/sec",
            "range": "stddev: 0.00006108701480018714",
            "extra": "mean: 97.36495732131597 usec\nrounds: 5600"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 13.402992527691174,
            "unit": "iter/sec",
            "range": "stddev: 0.003955275672985203",
            "extra": "mean: 74.61020349999866 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 9.867458264308368,
            "unit": "iter/sec",
            "range": "stddev: 0.0035800067246979546",
            "extra": "mean: 101.34322063637248 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 10.33134281636702,
            "unit": "iter/sec",
            "range": "stddev: 0.004281643666033405",
            "extra": "mean: 96.79283881818245 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 46.99627595955349,
            "unit": "iter/sec",
            "range": "stddev: 0.001256711764540168",
            "extra": "mean: 21.278281727272013 msec\nrounds: 33"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 2774.734560787834,
            "unit": "iter/sec",
            "range": "stddev: 0.00015774395496724537",
            "extra": "mean: 360.39483348492575 usec\nrounds: 2192"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 4097.543882072,
            "unit": "iter/sec",
            "range": "stddev: 0.00015611631660492837",
            "extra": "mean: 244.04863712998997 usec\nrounds: 2968"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 2912.1591790950615,
            "unit": "iter/sec",
            "range": "stddev: 0.00008626300145363823",
            "extra": "mean: 343.38782274626374 usec\nrounds: 2629"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 6667.698733430757,
            "unit": "iter/sec",
            "range": "stddev: 0.00010918342105064367",
            "extra": "mean: 149.9767820921726 usec\nrounds: 4713"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 5297.948488144192,
            "unit": "iter/sec",
            "range": "stddev: 0.00007912607608123664",
            "extra": "mean: 188.75230709354972 usec\nrounds: 4497"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 6671.132646599305,
            "unit": "iter/sec",
            "range": "stddev: 0.0000857231693142805",
            "extra": "mean: 149.89958272074873 usec\nrounds: 6528"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 6587.213759418214,
            "unit": "iter/sec",
            "range": "stddev: 0.00012186064023474928",
            "extra": "mean: 151.80925297440484 usec\nrounds: 3194"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 25312.397904205933,
            "unit": "iter/sec",
            "range": "stddev: 0.0000309812989350154",
            "extra": "mean: 39.50633218490292 usec\nrounds: 13643"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 13.367051695773627,
            "unit": "iter/sec",
            "range": "stddev: 0.005780659242374342",
            "extra": "mean: 74.81081264286412 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 10.570302185202452,
            "unit": "iter/sec",
            "range": "stddev: 0.0018838969702495477",
            "extra": "mean: 94.60467472726722 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 10.591304479711091,
            "unit": "iter/sec",
            "range": "stddev: 0.0037537089801129033",
            "extra": "mean: 94.41707599999786 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 45.98518023054631,
            "unit": "iter/sec",
            "range": "stddev: 0.0020799593193523125",
            "extra": "mean: 21.746136363639515 msec\nrounds: 44"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 3701.2173337924496,
            "unit": "iter/sec",
            "range": "stddev: 0.00010845390224931999",
            "extra": "mean: 270.1813781292737 usec\nrounds: 3036"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "a93b0163a4f6c3293acff4c979017321d56463e4",
          "message": "Merge pull request #15 from tchar/development\n\nImprove threading",
          "timestamp": "2021-08-04T19:29:09+03:00",
          "tree_id": "76610025182af03226387d2a5313686f5f2c021b",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/a93b0163a4f6c3293acff4c979017321d56463e4"
        },
        "date": 1628094603876,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 102.58245426798497,
            "unit": "iter/sec",
            "range": "stddev: 0.0008632476191958125",
            "extra": "mean: 9.748255753246204 msec\nrounds: 77"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 2666.4775957369943,
            "unit": "iter/sec",
            "range": "stddev: 0.00006664718670970863",
            "extra": "mean: 375.02658998475766 usec\nrounds: 2017"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 5382.124487716487,
            "unit": "iter/sec",
            "range": "stddev: 0.0000699130144669114",
            "extra": "mean: 185.80023600016676 usec\nrounds: 1500"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 4756.9355023284215,
            "unit": "iter/sec",
            "range": "stddev: 0.00017798203738029114",
            "extra": "mean: 210.2193732730916 usec\nrounds: 3764"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 6207.276634173144,
            "unit": "iter/sec",
            "range": "stddev: 0.0000427385544640164",
            "extra": "mean: 161.10124599484803 usec\nrounds: 4931"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 6210.515221268028,
            "unit": "iter/sec",
            "range": "stddev: 0.00003980162020095197",
            "extra": "mean: 161.01723679469958 usec\nrounds: 3919"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 13041.464875670239,
            "unit": "iter/sec",
            "range": "stddev: 0.00002230526602493426",
            "extra": "mean: 76.67850272445772 usec\nrounds: 6974"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 15.985622435268407,
            "unit": "iter/sec",
            "range": "stddev: 0.003271417200389137",
            "extra": "mean: 62.55621287499835 msec\nrounds: 16"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 12.63369184588994,
            "unit": "iter/sec",
            "range": "stddev: 0.0037920650797452662",
            "extra": "mean: 79.15342658332492 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 12.517534998906713,
            "unit": "iter/sec",
            "range": "stddev: 0.004253947631921107",
            "extra": "mean: 79.88793321427424 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 55.50866337865124,
            "unit": "iter/sec",
            "range": "stddev: 0.0010269671722577271",
            "extra": "mean: 18.015205899996545 msec\nrounds: 40"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 3321.543764181133,
            "unit": "iter/sec",
            "range": "stddev: 0.00006584128069995935",
            "extra": "mean: 301.06482738050937 usec\nrounds: 2352"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 4213.671663207044,
            "unit": "iter/sec",
            "range": "stddev: 0.0000762043163577484",
            "extra": "mean: 237.32271518253407 usec\nrounds: 1594"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 3116.90389376504,
            "unit": "iter/sec",
            "range": "stddev: 0.00004179317678090138",
            "extra": "mean: 320.8311946994483 usec\nrounds: 2830"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 7559.344524552983,
            "unit": "iter/sec",
            "range": "stddev: 0.000046782266336212565",
            "extra": "mean: 132.2866019338012 usec\nrounds: 3826"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 6345.0541284074925,
            "unit": "iter/sec",
            "range": "stddev: 0.00003269669743010877",
            "extra": "mean: 157.60306843134592 usec\nrounds: 4647"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 7953.915847474161,
            "unit": "iter/sec",
            "range": "stddev: 0.00003098893834431052",
            "extra": "mean: 125.72423686347639 usec\nrounds: 4910"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 7795.827487847401,
            "unit": "iter/sec",
            "range": "stddev: 0.00002830630197282554",
            "extra": "mean: 128.27374663675658 usec\nrounds: 4981"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 29617.296864766606,
            "unit": "iter/sec",
            "range": "stddev: 0.000011790586395148141",
            "extra": "mean: 33.76405363953461 usec\nrounds: 13889"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 16.206774964931764,
            "unit": "iter/sec",
            "range": "stddev: 0.003727897611198161",
            "extra": "mean: 61.702590562514814 msec\nrounds: 16"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 12.899443492912795,
            "unit": "iter/sec",
            "range": "stddev: 0.003194742897946631",
            "extra": "mean: 77.52272418181602 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 12.020989621578329,
            "unit": "iter/sec",
            "range": "stddev: 0.006686996887729136",
            "extra": "mean: 83.187826583341 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 55.51064023237289,
            "unit": "iter/sec",
            "range": "stddev: 0.0021108959538227784",
            "extra": "mean: 18.014564339627565 msec\nrounds: 53"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 4589.117764557925,
            "unit": "iter/sec",
            "range": "stddev: 0.000048363791229810143",
            "extra": "mean: 217.9068072131575 usec\nrounds: 2967"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "10adfb4c5030e87dc683a320f16f1b7f42d6a9f7",
          "message": "Merge pull request #16 from tchar/development\n\nFix UpdateThread exiting without stop event being set",
          "timestamp": "2021-08-04T20:22:56+03:00",
          "tree_id": "61fa4396acb23acd3acb41d7afbf7de06eecf3c5",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/10adfb4c5030e87dc683a320f16f1b7f42d6a9f7"
        },
        "date": 1628097837921,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 78.80929989543895,
            "unit": "iter/sec",
            "range": "stddev: 0.0007473202681676475",
            "extra": "mean: 12.688857803923652 msec\nrounds: 51"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 2513.6132055093635,
            "unit": "iter/sec",
            "range": "stddev: 0.00007995362952061391",
            "extra": "mean: 397.83368332414454 usec\nrounds: 1661"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 4658.020630501842,
            "unit": "iter/sec",
            "range": "stddev: 0.00009992559618645981",
            "extra": "mean: 214.68346306835977 usec\nrounds: 1408"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 3907.4224487564757,
            "unit": "iter/sec",
            "range": "stddev: 0.0001447655940424237",
            "extra": "mean: 255.92318545394204 usec\nrounds: 3176"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 4908.358287250236,
            "unit": "iter/sec",
            "range": "stddev: 0.00007820243370816122",
            "extra": "mean: 203.73410853025172 usec\nrounds: 2497"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 5039.2804968708,
            "unit": "iter/sec",
            "range": "stddev: 0.00005056682186691223",
            "extra": "mean: 198.44102756751914 usec\nrounds: 4099"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 10265.519634530378,
            "unit": "iter/sec",
            "range": "stddev: 0.00006653670716450305",
            "extra": "mean: 97.41348081750053 usec\nrounds: 6021"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 12.718405958038066,
            "unit": "iter/sec",
            "range": "stddev: 0.001102185536146268",
            "extra": "mean: 78.62620546154193 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 9.872543657399357,
            "unit": "iter/sec",
            "range": "stddev: 0.0023339507320741222",
            "extra": "mean: 101.29101827273375 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 9.756957753409285,
            "unit": "iter/sec",
            "range": "stddev: 0.002915676520643722",
            "extra": "mean: 102.49096339999824 msec\nrounds: 10"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 43.73075211222792,
            "unit": "iter/sec",
            "range": "stddev: 0.0015607418818853684",
            "extra": "mean: 22.867203322587763 msec\nrounds: 31"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 2783.418073377919,
            "unit": "iter/sec",
            "range": "stddev: 0.000056717168884246166",
            "extra": "mean: 359.2704989467907 usec\nrounds: 1900"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 4010.9031320124145,
            "unit": "iter/sec",
            "range": "stddev: 0.00012045086240320979",
            "extra": "mean: 249.32040667316338 usec\nrounds: 2877"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 2933.6808213005675,
            "unit": "iter/sec",
            "range": "stddev: 0.00006329483607786466",
            "extra": "mean: 340.8687109856338 usec\nrounds: 2121"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 6561.236175899643,
            "unit": "iter/sec",
            "range": "stddev: 0.00003489559139677012",
            "extra": "mean: 152.4103039718556 usec\nrounds: 4280"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 5259.237876593361,
            "unit": "iter/sec",
            "range": "stddev: 0.000029721244166654864",
            "extra": "mean: 190.1416181326531 usec\nrounds: 4114"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 6565.606443985154,
            "unit": "iter/sec",
            "range": "stddev: 0.000029282124703033448",
            "extra": "mean: 152.30885502071393 usec\nrounds: 5049"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 6504.003179197867,
            "unit": "iter/sec",
            "range": "stddev: 0.000035310642597529156",
            "extra": "mean: 153.75146236065174 usec\nrounds: 4862"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 22414.76638886725,
            "unit": "iter/sec",
            "range": "stddev: 0.0000362546392229122",
            "extra": "mean: 44.613447343206325 usec\nrounds: 10616"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 12.269092346381324,
            "unit": "iter/sec",
            "range": "stddev: 0.00354497297172371",
            "extra": "mean: 81.50562175000194 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 9.626865494838164,
            "unit": "iter/sec",
            "range": "stddev: 0.004724567254165044",
            "extra": "mean: 103.87597089999758 msec\nrounds: 10"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 9.81437990656405,
            "unit": "iter/sec",
            "range": "stddev: 0.002585130177930631",
            "extra": "mean: 101.89130739998973 msec\nrounds: 10"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 44.24641873122919,
            "unit": "iter/sec",
            "range": "stddev: 0.0006470352828869931",
            "extra": "mean: 22.600699190468003 msec\nrounds: 42"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 3558.532236846741,
            "unit": "iter/sec",
            "range": "stddev: 0.0000393873425434013",
            "extra": "mean: 281.0147368191646 usec\nrounds: 2276"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "2163cfe5486b54ed1adb947c6c6d3235d9b84965",
          "message": "Merge pull request #17 from tchar/development\n\nDisable outbound connections for tests",
          "timestamp": "2021-08-04T20:58:38+03:00",
          "tree_id": "fb15596a241a8edc25fba5caffaf572f76db032c",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/2163cfe5486b54ed1adb947c6c6d3235d9b84965"
        },
        "date": 1628099982244,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 98.61972428513614,
            "unit": "iter/sec",
            "range": "stddev: 0.0005737197269451977",
            "extra": "mean: 10.139959397054602 msec\nrounds: 68"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 3329.230582413331,
            "unit": "iter/sec",
            "range": "stddev: 0.00007324561889051577",
            "extra": "mean: 300.36970262213214 usec\nrounds: 1335"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 6367.528728100039,
            "unit": "iter/sec",
            "range": "stddev: 0.000032589503206859546",
            "extra": "mean: 157.04679832648085 usec\nrounds: 2390"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 5152.601580970338,
            "unit": "iter/sec",
            "range": "stddev: 0.00004352282764147361",
            "extra": "mean: 194.07671722440455 usec\nrounds: 3791"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 6370.531189049711,
            "unit": "iter/sec",
            "range": "stddev: 0.000038286830309419546",
            "extra": "mean: 156.9727814407215 usec\nrounds: 3761"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 6149.720845408844,
            "unit": "iter/sec",
            "range": "stddev: 0.00006423039283477136",
            "extra": "mean: 162.60900700014102 usec\nrounds: 4857"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 13063.921692017424,
            "unit": "iter/sec",
            "range": "stddev: 0.000023437348334965865",
            "extra": "mean: 76.5466927600339 usec\nrounds: 5953"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 15.666266447172285,
            "unit": "iter/sec",
            "range": "stddev: 0.0017989218698540503",
            "extra": "mean: 63.831417866667074 msec\nrounds: 15"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 11.986462010347719,
            "unit": "iter/sec",
            "range": "stddev: 0.002809966766276771",
            "extra": "mean: 83.42745333332857 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 11.656441437106505,
            "unit": "iter/sec",
            "range": "stddev: 0.002619005941195467",
            "extra": "mean: 85.78947575000484 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 49.63213037210837,
            "unit": "iter/sec",
            "range": "stddev: 0.0010080321485856803",
            "extra": "mean: 20.148238499993287 msec\nrounds: 34"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 3454.774053149178,
            "unit": "iter/sec",
            "range": "stddev: 0.00006842162831575885",
            "extra": "mean: 289.45453005485444 usec\nrounds: 2379"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 5461.22576058799,
            "unit": "iter/sec",
            "range": "stddev: 0.00005734049745013866",
            "extra": "mean: 183.10907547838372 usec\nrounds: 3299"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 4060.1784583596877,
            "unit": "iter/sec",
            "range": "stddev: 0.000048594062373953674",
            "extra": "mean: 246.29459277610178 usec\nrounds: 3433"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 8415.57120569652,
            "unit": "iter/sec",
            "range": "stddev: 0.000038286360885572205",
            "extra": "mean: 118.82734701633771 usec\nrounds: 4726"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 6927.56035014714,
            "unit": "iter/sec",
            "range": "stddev: 0.000015285491500537857",
            "extra": "mean: 144.3509618763206 usec\nrounds: 4669"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 8687.3787475675,
            "unit": "iter/sec",
            "range": "stddev: 0.000011801700118085667",
            "extra": "mean: 115.10952026582287 usec\nrounds: 5872"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 8769.923717660315,
            "unit": "iter/sec",
            "range": "stddev: 0.000011813440580547204",
            "extra": "mean: 114.02607732907228 usec\nrounds: 4927"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 31918.51246635169,
            "unit": "iter/sec",
            "range": "stddev: 0.000004544377086239438",
            "extra": "mean: 31.329780830300102 usec\nrounds: 12739"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 15.864033918266344,
            "unit": "iter/sec",
            "range": "stddev: 0.0010805796978341307",
            "extra": "mean: 63.03566956249185 msec\nrounds: 16"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 12.726379232215505,
            "unit": "iter/sec",
            "range": "stddev: 0.0014108519476315863",
            "extra": "mean: 78.57694492307789 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 12.197691624955544,
            "unit": "iter/sec",
            "range": "stddev: 0.0030236356343240262",
            "extra": "mean: 81.98272515383783 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 51.05655962283421,
            "unit": "iter/sec",
            "range": "stddev: 0.0007674222366067618",
            "extra": "mean: 19.58612188888588 msec\nrounds: 54"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 4677.219370770576,
            "unit": "iter/sec",
            "range": "stddev: 0.000021200273496792715",
            "extra": "mean: 213.80224460911896 usec\nrounds: 2968"
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
          "id": "7fb7d52771f7c29c6a9ef7608ef2a40654ae0ff0",
          "message": "Merge branch 'development'",
          "timestamp": "2021-08-05T17:38:39+03:00",
          "tree_id": "581ae1b214070befc64c4ca04d66b55dfdf1ada7",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/7fb7d52771f7c29c6a9ef7608ef2a40654ae0ff0"
        },
        "date": 1628174372086,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 6180.2485380883845,
            "unit": "iter/sec",
            "range": "stddev: 0.000003434410152472095",
            "extra": "mean: 161.80579046895585 usec\nrounds: 2644"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 4548.718145492852,
            "unit": "iter/sec",
            "range": "stddev: 0.000004153924817973416",
            "extra": "mean: 219.8421550895302 usec\nrounds: 2908"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 9305.24895452329,
            "unit": "iter/sec",
            "range": "stddev: 0.0000023783788875056432",
            "extra": "mean: 107.46622738276113 usec\nrounds: 2476"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 7369.471912621789,
            "unit": "iter/sec",
            "range": "stddev: 0.000002959421600006397",
            "extra": "mean: 135.69493334892658 usec\nrounds: 4276"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 9299.149641836317,
            "unit": "iter/sec",
            "range": "stddev: 0.0000024833290662543612",
            "extra": "mean: 107.53671448635043 usec\nrounds: 5695"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 9356.89793120803,
            "unit": "iter/sec",
            "range": "stddev: 0.0000022737330524901885",
            "extra": "mean: 106.87302644017343 usec\nrounds: 5711"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 32984.93779313706,
            "unit": "iter/sec",
            "range": "stddev: 0.000003791420510896511",
            "extra": "mean: 30.316867846513347 usec\nrounds: 12092"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 17.19013819325973,
            "unit": "iter/sec",
            "range": "stddev: 0.00035042994092566364",
            "extra": "mean: 58.172888941177966 msec\nrounds: 17"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 13.281058845393902,
            "unit": "iter/sec",
            "range": "stddev: 0.0002368840634259648",
            "extra": "mean: 75.29520135714307 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 13.156447208059241,
            "unit": "iter/sec",
            "range": "stddev: 0.000700855107438677",
            "extra": "mean: 76.00836184615481 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 31.190653854815718,
            "unit": "iter/sec",
            "range": "stddev: 0.00008394452450793759",
            "extra": "mean: 32.060886080001296 msec\nrounds: 25"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 5031.672267370773,
            "unit": "iter/sec",
            "range": "stddev: 0.000004423322384845758",
            "extra": "mean: 198.74108385094314 usec\nrounds: 2898"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 107.57397732765817,
            "unit": "iter/sec",
            "range": "stddev: 0.00004366014114428039",
            "extra": "mean: 9.295928484210572 msec\nrounds: 95"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 3937.5215323221705,
            "unit": "iter/sec",
            "range": "stddev: 0.0000046940078845697725",
            "extra": "mean: 253.96686514378138 usec\nrounds: 2714"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 7203.497058891297,
            "unit": "iter/sec",
            "range": "stddev: 0.0000032766579918964536",
            "extra": "mean: 138.82146294010033 usec\nrounds: 4061"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 5807.537691986393,
            "unit": "iter/sec",
            "range": "stddev: 0.000003989819355563861",
            "extra": "mean: 172.19001460461686 usec\nrounds: 3629"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 7189.59411049177,
            "unit": "iter/sec",
            "range": "stddev: 0.0000030390963484555734",
            "extra": "mean: 139.08991031088956 usec\nrounds: 4471"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 7275.227881215486,
            "unit": "iter/sec",
            "range": "stddev: 0.000003386720146041727",
            "extra": "mean: 137.45273912065116 usec\nrounds: 4481"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 14685.826915190359,
            "unit": "iter/sec",
            "range": "stddev: 0.000001695145528444224",
            "extra": "mean: 68.09286298789515 usec\nrounds: 7430"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 16.96888835770304,
            "unit": "iter/sec",
            "range": "stddev: 0.00013859427333266485",
            "extra": "mean: 58.93137952941091 msec\nrounds: 17"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 12.932437524817017,
            "unit": "iter/sec",
            "range": "stddev: 0.0016958347755793607",
            "extra": "mean: 77.32494342857065 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 13.015691431244441,
            "unit": "iter/sec",
            "range": "stddev: 0.000752666790176063",
            "extra": "mean: 76.8303401538453 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 30.91105640266178,
            "unit": "iter/sec",
            "range": "stddev: 0.00011646672263201933",
            "extra": "mean: 32.35088400000102 msec\nrounds: 31"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 4027.50266358474,
            "unit": "iter/sec",
            "range": "stddev: 0.000004619256977191054",
            "extra": "mean: 248.29282151484287 usec\nrounds: 2482"
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
          "id": "7e66295804ad1c7e948a1af99a04b329f9057cfa",
          "message": "Merge branch 'development'",
          "timestamp": "2021-08-05T18:07:17+03:00",
          "tree_id": "dc9ce78b778848a1faf2a37cd0a328ffb315fc69",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/7e66295804ad1c7e948a1af99a04b329f9057cfa"
        },
        "date": 1628176096109,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 4899.012030529478,
            "unit": "iter/sec",
            "range": "stddev: 0.00005534111266987543",
            "extra": "mean: 204.12278920080985 usec\nrounds: 2315"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 3480.744957288669,
            "unit": "iter/sec",
            "range": "stddev: 0.00007710793690472979",
            "extra": "mean: 287.29482115775335 usec\nrounds: 2902"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 7669.560386471323,
            "unit": "iter/sec",
            "range": "stddev: 0.00004952575362679701",
            "extra": "mean: 130.3855696558494 usec\nrounds: 2498"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 5951.662008809985,
            "unit": "iter/sec",
            "range": "stddev: 0.00005409602364838408",
            "extra": "mean: 168.0202939144971 usec\nrounds: 4634"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 7515.527437037025,
            "unit": "iter/sec",
            "range": "stddev: 0.0000879723743615118",
            "extra": "mean: 133.05786032686578 usec\nrounds: 6057"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 7519.163096381648,
            "unit": "iter/sec",
            "range": "stddev: 0.000047272023849380035",
            "extra": "mean: 132.99352430341847 usec\nrounds: 3086"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 28236.251934346194,
            "unit": "iter/sec",
            "range": "stddev: 0.000021122875317704866",
            "extra": "mean: 35.41546527935648 usec\nrounds: 8842"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 15.493668478968038,
            "unit": "iter/sec",
            "range": "stddev: 0.0018334207021365296",
            "extra": "mean: 64.5424936874992 msec\nrounds: 16"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 11.830485002760385,
            "unit": "iter/sec",
            "range": "stddev: 0.002987540779806084",
            "extra": "mean: 84.52738833333306 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 11.681652641870574,
            "unit": "iter/sec",
            "range": "stddev: 0.0055206022148842505",
            "extra": "mean: 85.60432591666849 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 30.42781203242877,
            "unit": "iter/sec",
            "range": "stddev: 0.0006471894486369119",
            "extra": "mean: 32.86466995833415 msec\nrounds: 24"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 4032.925371967287,
            "unit": "iter/sec",
            "range": "stddev: 0.00018679383624078944",
            "extra": "mean: 247.95896471354575 usec\nrounds: 3089"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 97.13680198871988,
            "unit": "iter/sec",
            "range": "stddev: 0.0006107577686460291",
            "extra": "mean: 10.294759344827165 msec\nrounds: 87"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 3032.106725341353,
            "unit": "iter/sec",
            "range": "stddev: 0.00010149845059086086",
            "extra": "mean: 329.80369445518795 usec\nrounds: 2615"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 5571.5166171565315,
            "unit": "iter/sec",
            "range": "stddev: 0.00013858388216131216",
            "extra": "mean: 179.48434308185875 usec\nrounds: 4069"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 4703.951824518607,
            "unit": "iter/sec",
            "range": "stddev: 0.00007277474169828495",
            "extra": "mean: 212.58721120136852 usec\nrounds: 3821"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 5781.871450132625,
            "unit": "iter/sec",
            "range": "stddev: 0.00006442233670997822",
            "extra": "mean: 172.95438140138205 usec\nrounds: 4667"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 5768.014232125893,
            "unit": "iter/sec",
            "range": "stddev: 0.00007826017570696697",
            "extra": "mean: 173.36989122362726 usec\nrounds: 4569"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 12234.834608160303,
            "unit": "iter/sec",
            "range": "stddev: 0.000052214846535317036",
            "extra": "mean: 81.73383883203678 usec\nrounds: 7123"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 15.267167064860784,
            "unit": "iter/sec",
            "range": "stddev: 0.003137452771513545",
            "extra": "mean: 65.50003650000136 msec\nrounds: 16"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 11.8323515288465,
            "unit": "iter/sec",
            "range": "stddev: 0.0015479852759969757",
            "extra": "mean: 84.51405433333055 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 11.73959192579734,
            "unit": "iter/sec",
            "range": "stddev: 0.0023261230173239633",
            "extra": "mean: 85.18183650000093 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 29.857700379603962,
            "unit": "iter/sec",
            "range": "stddev: 0.0024649127059762103",
            "extra": "mean: 33.492197566665524 msec\nrounds: 30"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 3240.8959194360637,
            "unit": "iter/sec",
            "range": "stddev: 0.00009790442944541528",
            "extra": "mean: 308.55665373357823 usec\nrounds: 2732"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "e4a1bb968f351f43ffeaa4f0bc8e600edf42fee1",
          "message": "Merge pull request #18 from tchar/development\n\nAdd codecov.yml",
          "timestamp": "2021-08-05T18:24:12+03:00",
          "tree_id": "eb022797d3c3dcbcf4370d860263f5823c8cd973",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/e4a1bb968f351f43ffeaa4f0bc8e600edf42fee1"
        },
        "date": 1628177205201,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 6195.022498216667,
            "unit": "iter/sec",
            "range": "stddev: 0.000003626434518168673",
            "extra": "mean: 161.4199141791439 usec\nrounds: 2412"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 4581.843994374759,
            "unit": "iter/sec",
            "range": "stddev: 0.000005049071523461363",
            "extra": "mean: 218.25273868506312 usec\nrounds: 2342"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 9401.382995545593,
            "unit": "iter/sec",
            "range": "stddev: 0.000002573425982070897",
            "extra": "mean: 106.36732919760885 usec\nrounds: 2418"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 7413.635892012528,
            "unit": "iter/sec",
            "range": "stddev: 0.0000029060016882690397",
            "extra": "mean: 134.88658123572037 usec\nrounds: 3933"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 9376.682729785973,
            "unit": "iter/sec",
            "range": "stddev: 0.0000024564383471956064",
            "extra": "mean: 106.64752437697393 usec\nrounds: 5538"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 9519.547931161314,
            "unit": "iter/sec",
            "range": "stddev: 0.0000026913163093163212",
            "extra": "mean: 105.0470050921848 usec\nrounds: 5695"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 32771.008337760104,
            "unit": "iter/sec",
            "range": "stddev: 0.0000038856461719398114",
            "extra": "mean: 30.514776649327537 usec\nrounds: 10929"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 17.19023186754088,
            "unit": "iter/sec",
            "range": "stddev: 0.00099447681224874",
            "extra": "mean: 58.17257194117494 msec\nrounds: 17"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 13.32571984194136,
            "unit": "iter/sec",
            "range": "stddev: 0.00011592631850727157",
            "extra": "mean: 75.04285035714175 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 13.259312438713696,
            "unit": "iter/sec",
            "range": "stddev: 0.00009785564892102487",
            "extra": "mean: 75.41869192856966 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 31.877255147988123,
            "unit": "iter/sec",
            "range": "stddev: 0.00026585758964868127",
            "extra": "mean: 31.370329576921346 msec\nrounds: 26"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 5026.583395660746,
            "unit": "iter/sec",
            "range": "stddev: 0.0000041765765803189885",
            "extra": "mean: 198.94228769053373 usec\nrounds: 2819"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 108.28235746784266,
            "unit": "iter/sec",
            "range": "stddev: 0.00017400237546652165",
            "extra": "mean: 9.2351147812512 msec\nrounds: 96"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 3970.1595428077953,
            "unit": "iter/sec",
            "range": "stddev: 0.000006505097092686999",
            "extra": "mean: 251.87904647599507 usec\nrounds: 2625"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 7320.448079250126,
            "unit": "iter/sec",
            "range": "stddev: 0.00000405354393874091",
            "extra": "mean: 136.6036599364059 usec\nrounds: 3764"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 5995.325297821948,
            "unit": "iter/sec",
            "range": "stddev: 0.0000035111639529343595",
            "extra": "mean: 166.7966207543887 usec\nrounds: 3710"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 7252.456860754842,
            "unit": "iter/sec",
            "range": "stddev: 0.000002694943349373367",
            "extra": "mean: 137.88430861426994 usec\nrounds: 4423"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 7369.514468227359,
            "unit": "iter/sec",
            "range": "stddev: 0.0000026869730941014088",
            "extra": "mean: 135.6941497721948 usec\nrounds: 4607"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 14946.568870241208,
            "unit": "iter/sec",
            "range": "stddev: 0.000002463757777724556",
            "extra": "mean: 66.90498727042375 usec\nrounds: 7463"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 17.15129707995754,
            "unit": "iter/sec",
            "range": "stddev: 0.000088883898045994",
            "extra": "mean: 58.30462823529354 msec\nrounds: 17"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 13.249670534875502,
            "unit": "iter/sec",
            "range": "stddev: 0.0002095264034760319",
            "extra": "mean: 75.47357478571419 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 13.16616515505356,
            "unit": "iter/sec",
            "range": "stddev: 0.00026792974505670137",
            "extra": "mean: 75.9522600714279 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 31.770957615852378,
            "unit": "iter/sec",
            "range": "stddev: 0.00014652267291590933",
            "extra": "mean: 31.475286709678585 msec\nrounds: 31"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 3999.8215920013577,
            "unit": "iter/sec",
            "range": "stddev: 0.000004312216064153578",
            "extra": "mean: 250.01115099727193 usec\nrounds: 2457"
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
          "id": "9b91a4333fc954571961ff9bdf50b28a562b0812",
          "message": "Merge branch 'development'",
          "timestamp": "2021-08-05T18:35:07+03:00",
          "tree_id": "16e2295bc291bf21f950a08844a9036d9e4e3c15",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/9b91a4333fc954571961ff9bdf50b28a562b0812"
        },
        "date": 1628177794051,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 6199.6999425848135,
            "unit": "iter/sec",
            "range": "stddev: 0.000003050751463464721",
            "extra": "mean: 161.29812882251755 usec\nrounds: 2616"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 4565.979125204043,
            "unit": "iter/sec",
            "range": "stddev: 0.00000339537673591522",
            "extra": "mean: 219.01107573620635 usec\nrounds: 2852"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 9375.068343641808,
            "unit": "iter/sec",
            "range": "stddev: 0.0000024758477608581317",
            "extra": "mean: 106.66588907356629 usec\nrounds: 2407"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 7446.553600861127,
            "unit": "iter/sec",
            "range": "stddev: 0.0000025690491778461705",
            "extra": "mean: 134.29031114264174 usec\nrounds: 4236"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 9386.220379689063,
            "unit": "iter/sec",
            "range": "stddev: 0.0000023577117660828737",
            "extra": "mean: 106.53915628956572 usec\nrounds: 5541"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 9516.774484334861,
            "unit": "iter/sec",
            "range": "stddev: 0.000004152758346038859",
            "extra": "mean: 105.07761864548283 usec\nrounds: 5921"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 33006.285856519506,
            "unit": "iter/sec",
            "range": "stddev: 0.000005038501181217008",
            "extra": "mean: 30.29725926591879 usec\nrounds: 11062"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 17.28168726846241,
            "unit": "iter/sec",
            "range": "stddev: 0.00006667066984535713",
            "extra": "mean: 57.86472029411815 msec\nrounds: 17"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 13.33568827617579,
            "unit": "iter/sec",
            "range": "stddev: 0.00007056022602504922",
            "extra": "mean: 74.98675578571375 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 13.26019284324967,
            "unit": "iter/sec",
            "range": "stddev: 0.00008899613926996528",
            "extra": "mean: 75.41368453846185 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 32.238169696847464,
            "unit": "iter/sec",
            "range": "stddev: 0.00011436684899583565",
            "extra": "mean: 31.019130719998316 msec\nrounds: 25"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 5070.021928431698,
            "unit": "iter/sec",
            "range": "stddev: 0.000004046399454842786",
            "extra": "mean: 197.23780569709064 usec\nrounds: 3335"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 108.60520789409142,
            "unit": "iter/sec",
            "range": "stddev: 0.00009820552233864846",
            "extra": "mean: 9.207661578947212 msec\nrounds: 95"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 3960.62732969736,
            "unit": "iter/sec",
            "range": "stddev: 0.000004098852774439371",
            "extra": "mean: 252.4852546721209 usec\nrounds: 2729"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 7313.471058584816,
            "unit": "iter/sec",
            "range": "stddev: 0.000002790699240576071",
            "extra": "mean: 136.7339792541004 usec\nrounds: 4049"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 5950.980039517075,
            "unit": "iter/sec",
            "range": "stddev: 0.0000030500907585106613",
            "extra": "mean: 168.0395486725831 usec\nrounds: 3729"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 7287.004576852941,
            "unit": "iter/sec",
            "range": "stddev: 0.00000419222002919646",
            "extra": "mean: 137.23059858868277 usec\nrounds: 4534"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 7348.109965323463,
            "unit": "iter/sec",
            "range": "stddev: 0.0000028605644130864657",
            "extra": "mean: 136.08941683223435 usec\nrounds: 4527"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 14936.150405069633,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014617603110853827",
            "extra": "mean: 66.95165573992745 usec\nrounds: 7474"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 17.073369424574683,
            "unit": "iter/sec",
            "range": "stddev: 0.0005700528160947397",
            "extra": "mean: 58.57074694117744 msec\nrounds: 17"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 13.20219890921361,
            "unit": "iter/sec",
            "range": "stddev: 0.00018055323058391282",
            "extra": "mean: 75.74495785714268 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 13.102573906002952,
            "unit": "iter/sec",
            "range": "stddev: 0.0005269314676851619",
            "extra": "mean: 76.32088223076913 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 32.1404480348388,
            "unit": "iter/sec",
            "range": "stddev: 0.00012276342845143",
            "extra": "mean: 31.113443064516247 msec\nrounds: 31"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 3997.4773764932006,
            "unit": "iter/sec",
            "range": "stddev: 0.000004183271311488596",
            "extra": "mean: 250.15776346363046 usec\nrounds: 2841"
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
          "id": "876149a7e6598a2f5d08f1c6ae77f5f7ed7f3676",
          "message": "Merge branch 'development'",
          "timestamp": "2021-08-05T18:37:08+03:00",
          "tree_id": "2acd76694b0ee9737b8d92d805c30ad6d33786f9",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/876149a7e6598a2f5d08f1c6ae77f5f7ed7f3676"
        },
        "date": 1628177978941,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 6155.909089283218,
            "unit": "iter/sec",
            "range": "stddev: 0.0000048239227576670545",
            "extra": "mean: 162.4455438662818 usec\nrounds: 2690"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 4525.065864890424,
            "unit": "iter/sec",
            "range": "stddev: 0.0000034669845773930325",
            "extra": "mean: 220.99125843866926 usec\nrounds: 2933"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 9412.185536220019,
            "unit": "iter/sec",
            "range": "stddev: 0.000002055691771196178",
            "extra": "mean: 106.24524943242939 usec\nrounds: 2642"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 7368.801678597184,
            "unit": "iter/sec",
            "range": "stddev: 0.000002900699602633539",
            "extra": "mean: 135.7072755675482 usec\nrounds: 4449"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 9362.700405589192,
            "unit": "iter/sec",
            "range": "stddev: 0.000001986836604060198",
            "extra": "mean: 106.80679255773649 usec\nrounds: 5751"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 9531.226163143552,
            "unit": "iter/sec",
            "range": "stddev: 0.0000021102882642788777",
            "extra": "mean: 104.91829517873741 usec\nrounds: 5932"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 32499.99778349819,
            "unit": "iter/sec",
            "range": "stddev: 0.000003877066130737469",
            "extra": "mean: 30.769232867694164 usec\nrounds: 10594"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 17.303234477743377,
            "unit": "iter/sec",
            "range": "stddev: 0.0002133441088237289",
            "extra": "mean: 57.79266305882114 msec\nrounds: 17"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 13.388763810101189,
            "unit": "iter/sec",
            "range": "stddev: 0.0001330346764542182",
            "extra": "mean: 74.68949442857057 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 13.30323166759847,
            "unit": "iter/sec",
            "range": "stddev: 0.00010568195682956838",
            "extra": "mean: 75.16970499999738 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 31.730581471154277,
            "unit": "iter/sec",
            "range": "stddev: 0.00009027341257140549",
            "extra": "mean: 31.51533800000113 msec\nrounds: 26"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 5058.843411511057,
            "unit": "iter/sec",
            "range": "stddev: 0.0000035814219802046176",
            "extra": "mean: 197.67364171117998 usec\nrounds: 3366"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 109.686686628701,
            "unit": "iter/sec",
            "range": "stddev: 0.000032594508460993144",
            "extra": "mean: 9.116876721648882 msec\nrounds: 97"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 3950.6102685049823,
            "unit": "iter/sec",
            "range": "stddev: 0.000003990673809404491",
            "extra": "mean: 253.12544949629444 usec\nrounds: 2881"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 7266.214625989944,
            "unit": "iter/sec",
            "range": "stddev: 0.000002828385013715237",
            "extra": "mean: 137.62324008751128 usec\nrounds: 4111"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 5921.27281415129,
            "unit": "iter/sec",
            "range": "stddev: 0.000003475072918408462",
            "extra": "mean: 168.88260875433627 usec\nrounds: 3701"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 7288.963402204043,
            "unit": "iter/sec",
            "range": "stddev: 0.000002734386062005484",
            "extra": "mean: 137.19371943857192 usec\nrounds: 4630"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 7310.289070476402,
            "unit": "iter/sec",
            "range": "stddev: 0.000002769077017647798",
            "extra": "mean: 136.79349617495103 usec\nrounds: 4575"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 14786.824084903592,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014371000488292736",
            "extra": "mean: 67.62777417639914 usec\nrounds: 7497"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 17.213003586645314,
            "unit": "iter/sec",
            "range": "stddev: 0.00009127614746904304",
            "extra": "mean: 58.09561329411729 msec\nrounds: 17"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 13.251344200028209,
            "unit": "iter/sec",
            "range": "stddev: 0.0005961160948545897",
            "extra": "mean: 75.46404235714225 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 13.196328647144876,
            "unit": "iter/sec",
            "range": "stddev: 0.00018622006614237328",
            "extra": "mean: 75.77865228571413 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 31.72178151404732,
            "unit": "iter/sec",
            "range": "stddev: 0.00016507910385833225",
            "extra": "mean: 31.52408068749768 msec\nrounds: 32"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 4038.338049815777,
            "unit": "iter/sec",
            "range": "stddev: 0.000004182306734798071",
            "extra": "mean: 247.62661958070063 usec\nrounds: 2768"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "fb5b174aab85bd9857e200d0efc5f4ba017445e1",
          "message": "Merge pull request #19 from tchar/development\n\nAdd CodeQL",
          "timestamp": "2021-08-05T21:53:28+03:00",
          "tree_id": "27ccf7245d3db9c91a65b83bf762a28a0c5f0c5d",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/fb5b174aab85bd9857e200d0efc5f4ba017445e1"
        },
        "date": 1628189666840,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 5405.618470586211,
            "unit": "iter/sec",
            "range": "stddev: 0.00002311522165381976",
            "extra": "mean: 184.99270813161095 usec\nrounds: 2275"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 3866.37316093184,
            "unit": "iter/sec",
            "range": "stddev: 0.0000061414636791612595",
            "extra": "mean: 258.64032217702146 usec\nrounds: 2719"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 8261.886098625346,
            "unit": "iter/sec",
            "range": "stddev: 0.000005806431986794767",
            "extra": "mean: 121.03773739586958 usec\nrounds: 2281"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 6524.548687227197,
            "unit": "iter/sec",
            "range": "stddev: 0.000007610754080634535",
            "extra": "mean: 153.26730597591418 usec\nrounds: 3765"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 8221.625976617954,
            "unit": "iter/sec",
            "range": "stddev: 0.000007232783149879823",
            "extra": "mean: 121.63044181819612 usec\nrounds: 4907"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 8292.813175326735,
            "unit": "iter/sec",
            "range": "stddev: 0.000005599311979462184",
            "extra": "mean: 120.58634131240997 usec\nrounds: 5013"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 28805.57814518784,
            "unit": "iter/sec",
            "range": "stddev: 0.000004085451740205929",
            "extra": "mean: 34.715498330209925 usec\nrounds: 11976"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 15.3258298867137,
            "unit": "iter/sec",
            "range": "stddev: 0.0006391093127839372",
            "extra": "mean: 65.24932140000601 msec\nrounds: 15"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 12.100192017391526,
            "unit": "iter/sec",
            "range": "stddev: 0.001310713126967164",
            "extra": "mean: 82.643316615365 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 12.021730413312627,
            "unit": "iter/sec",
            "range": "stddev: 0.0012991430103560988",
            "extra": "mean: 83.18270046154251 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 27.852744670917865,
            "unit": "iter/sec",
            "range": "stddev: 0.0007335635168510372",
            "extra": "mean: 35.90310440910116 msec\nrounds: 22"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 4406.294313199232,
            "unit": "iter/sec",
            "range": "stddev: 0.000009080462865079851",
            "extra": "mean: 226.94807221670592 usec\nrounds: 2631"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 97.70624168078055,
            "unit": "iter/sec",
            "range": "stddev: 0.00017535644045272127",
            "extra": "mean: 10.23476067442175 msec\nrounds: 86"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 3452.147749739747,
            "unit": "iter/sec",
            "range": "stddev: 0.000012477010616129755",
            "extra": "mean: 289.6747394648415 usec\nrounds: 2468"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 6420.541853737341,
            "unit": "iter/sec",
            "range": "stddev: 0.000005538275464198064",
            "extra": "mean: 155.750094428231 usec\nrounds: 3643"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 5221.867623747188,
            "unit": "iter/sec",
            "range": "stddev: 0.000009158359135665494",
            "extra": "mean: 191.50236506424588 usec\nrounds: 3246"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 6432.72481899471,
            "unit": "iter/sec",
            "range": "stddev: 0.000006372712405085536",
            "extra": "mean: 155.45511865316777 usec\nrounds: 3919"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 6597.966458393029,
            "unit": "iter/sec",
            "range": "stddev: 0.000008371294409746309",
            "extra": "mean: 151.5618495950274 usec\nrounds: 4202"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 13162.590325661968,
            "unit": "iter/sec",
            "range": "stddev: 0.000004695199323197217",
            "extra": "mean: 75.9728879543099 usec\nrounds: 6658"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 15.273371577132705,
            "unit": "iter/sec",
            "range": "stddev: 0.0008392792793239398",
            "extra": "mean: 65.4734283749896 msec\nrounds: 16"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 12.112221961394965,
            "unit": "iter/sec",
            "range": "stddev: 0.0009349098184676638",
            "extra": "mean: 82.56123469230332 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 11.859915264299692,
            "unit": "iter/sec",
            "range": "stddev: 0.0014997161450106791",
            "extra": "mean: 84.31763446153494 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 27.212867787167752,
            "unit": "iter/sec",
            "range": "stddev: 0.0006197305671602373",
            "extra": "mean: 36.747321444436324 msec\nrounds: 27"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 3583.4643644573125,
            "unit": "iter/sec",
            "range": "stddev: 0.000012454699618854974",
            "extra": "mean: 279.05956311956857 usec\nrounds: 2321"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "484aee6d209cffb842c91caae6d3ed492aae1941",
          "message": "Merge pull request #20 from tchar/development\n\nCodacy integration",
          "timestamp": "2021-08-05T22:50:35+03:00",
          "tree_id": "b79ca44beed7fb2212f08ccad47db81695762103",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/484aee6d209cffb842c91caae6d3ed492aae1941"
        },
        "date": 1628193093818,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 4225.514291025665,
            "unit": "iter/sec",
            "range": "stddev: 0.00004072599654902081",
            "extra": "mean: 236.65758322574945 usec\nrounds: 2325"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 2993.2842728177334,
            "unit": "iter/sec",
            "range": "stddev: 0.00017123610580382462",
            "extra": "mean: 334.0811993972922 usec\nrounds: 2322"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 7158.063042551701,
            "unit": "iter/sec",
            "range": "stddev: 0.00003697152727922168",
            "extra": "mean: 139.7025974841821 usec\nrounds: 2544"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 5744.582814771193,
            "unit": "iter/sec",
            "range": "stddev: 0.00004722905417972729",
            "extra": "mean: 174.07704479926278 usec\nrounds: 4509"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 7406.417645974763,
            "unit": "iter/sec",
            "range": "stddev: 0.00004516895578221722",
            "extra": "mean: 135.01804081268352 usec\nrounds: 5758"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 7119.907284587971,
            "unit": "iter/sec",
            "range": "stddev: 0.00004599552693868013",
            "extra": "mean: 140.45126713442448 usec\nrounds: 6128"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 27470.99227784513,
            "unit": "iter/sec",
            "range": "stddev: 0.000015375064526288634",
            "extra": "mean: 36.402034185218795 usec\nrounds: 12286"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 14.955265633179364,
            "unit": "iter/sec",
            "range": "stddev: 0.0025199625308098376",
            "extra": "mean: 66.8660807857151 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 11.384815884757614,
            "unit": "iter/sec",
            "range": "stddev: 0.003816031303109471",
            "extra": "mean: 87.83629090909012 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 10.92057033464855,
            "unit": "iter/sec",
            "range": "stddev: 0.0037142721797485583",
            "extra": "mean: 91.57030899999991 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 28.56616770355812,
            "unit": "iter/sec",
            "range": "stddev: 0.0023192099157622334",
            "extra": "mean: 35.00644574999967 msec\nrounds: 24"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 3950.78341915777,
            "unit": "iter/sec",
            "range": "stddev: 0.000048066581989127637",
            "extra": "mean: 253.11435578849841 usec\nrounds: 2479"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 86.70709345550077,
            "unit": "iter/sec",
            "range": "stddev: 0.0008647732744256226",
            "extra": "mean: 11.533081783132465 msec\nrounds: 83"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 2574.18535979939,
            "unit": "iter/sec",
            "range": "stddev: 0.00017027130337414473",
            "extra": "mean: 388.47241368738554 usec\nrounds: 1958"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 5477.165390704763,
            "unit": "iter/sec",
            "range": "stddev: 0.00007015544331546185",
            "extra": "mean: 182.57619200199593 usec\nrounds: 4026"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 4055.4464718120125,
            "unit": "iter/sec",
            "range": "stddev: 0.00008284393658531114",
            "extra": "mean: 246.58197487025154 usec\nrounds: 3661"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 5314.660850117582,
            "unit": "iter/sec",
            "range": "stddev: 0.00005005894808077563",
            "extra": "mean: 188.15876086954367 usec\nrounds: 2346"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 5357.349938990278,
            "unit": "iter/sec",
            "range": "stddev: 0.000032057391293172304",
            "extra": "mean: 186.65945129365102 usec\nrounds: 3131"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 11349.008884193378,
            "unit": "iter/sec",
            "range": "stddev: 0.00005729458815107234",
            "extra": "mean: 88.11342119863662 usec\nrounds: 5406"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 14.38300180026764,
            "unit": "iter/sec",
            "range": "stddev: 0.0015783044135761278",
            "extra": "mean: 69.52651566666646 msec\nrounds: 15"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 10.660985083720941,
            "unit": "iter/sec",
            "range": "stddev: 0.005401040027839053",
            "extra": "mean: 93.79996240000139 msec\nrounds: 10"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 11.023530387022943,
            "unit": "iter/sec",
            "range": "stddev: 0.003000255859939665",
            "extra": "mean: 90.71503999999985 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 27.738645748986162,
            "unit": "iter/sec",
            "range": "stddev: 0.002968764673524031",
            "extra": "mean: 36.050786655168615 msec\nrounds: 29"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 3027.361231596282,
            "unit": "iter/sec",
            "range": "stddev: 0.00006375231214391489",
            "extra": "mean: 330.3206731866336 usec\nrounds: 2454"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "committer": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "distinct": true,
          "id": "1aa7f7baef27914c12acfca51647082434163519",
          "message": "Merge branch 'development'",
          "timestamp": "2021-08-05T23:10:36+03:00",
          "tree_id": "22391497c29c474dfe0970dbac18b05d4e872979",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/1aa7f7baef27914c12acfca51647082434163519"
        },
        "date": 1628194295943,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 6153.1275506609645,
            "unit": "iter/sec",
            "range": "stddev: 0.000018165874240865423",
            "extra": "mean: 162.51897783145753 usec\nrounds: 2481"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 4533.89339968956,
            "unit": "iter/sec",
            "range": "stddev: 0.000003731995159874846",
            "extra": "mean: 220.56098629678215 usec\nrounds: 3065"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 9267.270081033936,
            "unit": "iter/sec",
            "range": "stddev: 0.0000020540071549194742",
            "extra": "mean: 107.90664254477318 usec\nrounds: 2515"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 7320.905976555595,
            "unit": "iter/sec",
            "range": "stddev: 0.0000028877780967001382",
            "extra": "mean: 136.59511585074185 usec\nrounds: 4290"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 9269.694370218152,
            "unit": "iter/sec",
            "range": "stddev: 0.0000025737579017793477",
            "extra": "mean: 107.87842188333832 usec\nrounds: 5575"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 9403.30112991863,
            "unit": "iter/sec",
            "range": "stddev: 0.0000020803497923187825",
            "extra": "mean: 106.34563183542899 usec\nrounds: 5541"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 33130.1703626893,
            "unit": "iter/sec",
            "range": "stddev: 0.000004052533341619715",
            "extra": "mean: 30.183967937761796 usec\nrounds: 11696"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 17.547128286168157,
            "unit": "iter/sec",
            "range": "stddev: 0.00009010260423352712",
            "extra": "mean: 56.98938217647091 msec\nrounds: 17"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 13.4989414973762,
            "unit": "iter/sec",
            "range": "stddev: 0.0006169234955289475",
            "extra": "mean: 74.07988249999978 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 13.379523295956924,
            "unit": "iter/sec",
            "range": "stddev: 0.00007202194707668949",
            "extra": "mean: 74.74107842857032 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 32.072626202149,
            "unit": "iter/sec",
            "range": "stddev: 0.0003230832657392125",
            "extra": "mean: 31.17923657692227 msec\nrounds: 26"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 5043.481440648802,
            "unit": "iter/sec",
            "range": "stddev: 0.000008756142645837393",
            "extra": "mean: 198.2757370613737 usec\nrounds: 3362"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 110.51954820318346,
            "unit": "iter/sec",
            "range": "stddev: 0.00002581919104931184",
            "extra": "mean: 9.048173072166028 msec\nrounds: 97"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 3947.0687674707024,
            "unit": "iter/sec",
            "range": "stddev: 0.000003807560978974981",
            "extra": "mean: 253.35256589431148 usec\nrounds: 2891"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 7249.309824326578,
            "unit": "iter/sec",
            "range": "stddev: 0.0000027348444551671887",
            "extra": "mean: 137.94416630453432 usec\nrounds: 4143"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 5844.544221446185,
            "unit": "iter/sec",
            "range": "stddev: 0.0000030075462734392853",
            "extra": "mean: 171.09974056326982 usec\nrounds: 3338"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 7261.5083607384095,
            "unit": "iter/sec",
            "range": "stddev: 0.0000027980830456953897",
            "extra": "mean: 137.71243525750234 usec\nrounds: 4487"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 7276.214470324813,
            "unit": "iter/sec",
            "range": "stddev: 0.000002830785044925542",
            "extra": "mean: 137.434101767943 usec\nrounds: 4412"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 14737.355992167795,
            "unit": "iter/sec",
            "range": "stddev: 0.0000030714047743581337",
            "extra": "mean: 67.85477670020677 usec\nrounds: 7734"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 17.406370141395993,
            "unit": "iter/sec",
            "range": "stddev: 0.00008782156803942765",
            "extra": "mean: 57.45023183333271 msec\nrounds: 18"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 13.448418856522867,
            "unit": "iter/sec",
            "range": "stddev: 0.0001094344952679203",
            "extra": "mean: 74.35818371428634 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 13.355358507246299,
            "unit": "iter/sec",
            "range": "stddev: 0.00013686385896829418",
            "extra": "mean: 74.87631271428796 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 32.17496915536581,
            "unit": "iter/sec",
            "range": "stddev: 0.00005839378687839412",
            "extra": "mean: 31.080060874999482 msec\nrounds: 32"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 3982.126338446899,
            "unit": "iter/sec",
            "range": "stddev: 0.00000602866177014766",
            "extra": "mean: 251.122117936122 usec\nrounds: 2849"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "committer": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "distinct": true,
          "id": "bf9448239da3a291f574855bb3c6f7717b4e9c70",
          "message": "Merge branch 'development'",
          "timestamp": "2021-08-05T23:35:44+03:00",
          "tree_id": "d1d40d1e231b97d46d28b1e5d5208af3559990e2",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/bf9448239da3a291f574855bb3c6f7717b4e9c70"
        },
        "date": 1628195816317,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 4467.302502225629,
            "unit": "iter/sec",
            "range": "stddev: 0.00006999917714288896",
            "extra": "mean: 223.84873186935422 usec\nrounds: 1958"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 3142.413553774492,
            "unit": "iter/sec",
            "range": "stddev: 0.0001270148480504809",
            "extra": "mean: 318.2267333333182 usec\nrounds: 2580"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 6363.671592770717,
            "unit": "iter/sec",
            "range": "stddev: 0.0000624945188215626",
            "extra": "mean: 157.14198720374316 usec\nrounds: 2110"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 4886.865402480219,
            "unit": "iter/sec",
            "range": "stddev: 0.00012188722473262434",
            "extra": "mean: 204.6301499305613 usec\nrounds: 3595"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 6309.488869154757,
            "unit": "iter/sec",
            "range": "stddev: 0.00009664161738149163",
            "extra": "mean: 158.49144371879427 usec\nrounds: 5206"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 6652.695309199335,
            "unit": "iter/sec",
            "range": "stddev: 0.00009145987161434161",
            "extra": "mean: 150.31501572260524 usec\nrounds: 4325"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 25418.26060210923,
            "unit": "iter/sec",
            "range": "stddev: 0.000034313321467114845",
            "extra": "mean: 39.34179508400426 usec\nrounds: 11961"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 13.548709713404929,
            "unit": "iter/sec",
            "range": "stddev: 0.002911457040265316",
            "extra": "mean: 73.80776628571591 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 10.590504626203193,
            "unit": "iter/sec",
            "range": "stddev: 0.0026559247316258706",
            "extra": "mean: 94.42420689999835 msec\nrounds: 10"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 10.701863911434895,
            "unit": "iter/sec",
            "range": "stddev: 0.002210984655677423",
            "extra": "mean: 93.44166663636084 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 26.209220300961867,
            "unit": "iter/sec",
            "range": "stddev: 0.0014758805483703534",
            "extra": "mean: 38.15451159999981 msec\nrounds: 20"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 3712.799987471659,
            "unit": "iter/sec",
            "range": "stddev: 0.00006574128651188279",
            "extra": "mean: 269.33850554146863 usec\nrounds: 2346"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 85.46828706826683,
            "unit": "iter/sec",
            "range": "stddev: 0.0007636906946501717",
            "extra": "mean: 11.700246188405076 msec\nrounds: 69"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 2760.9604134317524,
            "unit": "iter/sec",
            "range": "stddev: 0.00010529716025858499",
            "extra": "mean: 362.192806218849 usec\nrounds: 2219"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 4975.071507994644,
            "unit": "iter/sec",
            "range": "stddev: 0.00006552214267207015",
            "extra": "mean: 201.00213602820773 usec\nrounds: 3661"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 4096.561512846077,
            "unit": "iter/sec",
            "range": "stddev: 0.000057250456140465354",
            "extra": "mean: 244.10716081381437 usec\nrounds: 3047"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 4788.48330435256,
            "unit": "iter/sec",
            "range": "stddev: 0.00020816504818457898",
            "extra": "mean: 208.83439211138855 usec\nrounds: 3879"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 5034.155144768019,
            "unit": "iter/sec",
            "range": "stddev: 0.00005908272412324885",
            "extra": "mean: 198.6430634819224 usec\nrounds: 3119"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 10499.709490691128,
            "unit": "iter/sec",
            "range": "stddev: 0.00012442138713672632",
            "extra": "mean: 95.24073031607054 usec\nrounds: 6452"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 13.464059179394656,
            "unit": "iter/sec",
            "range": "stddev: 0.00269517898394189",
            "extra": "mean: 74.2718066428582 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 10.651544489492823,
            "unit": "iter/sec",
            "range": "stddev: 0.0025695257195234",
            "extra": "mean: 93.88309845454305 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 10.433299508819912,
            "unit": "iter/sec",
            "range": "stddev: 0.002558269782286927",
            "extra": "mean: 95.84695609999869 msec\nrounds: 10"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 26.030939750245064,
            "unit": "iter/sec",
            "range": "stddev: 0.0013594761846727438",
            "extra": "mean: 38.41582399999929 msec\nrounds: 26"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 2880.134100495495,
            "unit": "iter/sec",
            "range": "stddev: 0.00007869228281174325",
            "extra": "mean: 347.20605538053286 usec\nrounds: 2221"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "committer": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "distinct": true,
          "id": "f3817a248e5e9ff4cee9e6c96f70237ba1c72ef3",
          "message": "Improve code quality",
          "timestamp": "2021-08-06T00:53:58+03:00",
          "tree_id": "284a03ca526fed29aa64f180bf5e8309c111b7a0",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/f3817a248e5e9ff4cee9e6c96f70237ba1c72ef3"
        },
        "date": 1628200496432,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 6190.203423952346,
            "unit": "iter/sec",
            "range": "stddev: 0.000016943484212744913",
            "extra": "mean: 161.54557960576938 usec\nrounds: 2638"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 4567.705243024017,
            "unit": "iter/sec",
            "range": "stddev: 0.0000037777305153354468",
            "extra": "mean: 218.92831231333068 usec\nrounds: 3013"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 9441.873371974398,
            "unit": "iter/sec",
            "range": "stddev: 0.0000022203254098835014",
            "extra": "mean: 105.91118527052319 usec\nrounds: 2607"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 7395.807642876915,
            "unit": "iter/sec",
            "range": "stddev: 0.0000028811545594870927",
            "extra": "mean: 135.2117372824217 usec\nrounds: 4423"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 9321.598552756152,
            "unit": "iter/sec",
            "range": "stddev: 0.000002228524951522514",
            "extra": "mean: 107.2777372186154 usec\nrounds: 5731"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 9349.147845452197,
            "unit": "iter/sec",
            "range": "stddev: 0.000004411642889848548",
            "extra": "mean: 106.96162008887693 usec\nrounds: 5625"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 33046.081469366145,
            "unit": "iter/sec",
            "range": "stddev: 0.000004080416688665348",
            "extra": "mean: 30.260773911333608 usec\nrounds: 10173"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 17.267717693593642,
            "unit": "iter/sec",
            "range": "stddev: 0.00008974350898383534",
            "extra": "mean: 57.911532823530116 msec\nrounds: 17"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 13.339399190087505,
            "unit": "iter/sec",
            "range": "stddev: 0.00013197177707901278",
            "extra": "mean: 74.96589507142863 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 13.251225321165135,
            "unit": "iter/sec",
            "range": "stddev: 0.00010214697260267079",
            "extra": "mean: 75.46471935714345 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 31.935025959146913,
            "unit": "iter/sec",
            "range": "stddev: 0.000114564612792782",
            "extra": "mean: 31.31358030769276 msec\nrounds: 26"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 5076.296186842413,
            "unit": "iter/sec",
            "range": "stddev: 0.0000044749166056724105",
            "extra": "mean: 196.99402146627418 usec\nrounds: 3028"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 109.37138138935234,
            "unit": "iter/sec",
            "range": "stddev: 0.000030975593211644785",
            "extra": "mean: 9.14315963917553 msec\nrounds: 97"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 3957.225826138231,
            "unit": "iter/sec",
            "range": "stddev: 0.0000043393441076978655",
            "extra": "mean: 252.70228284542404 usec\nrounds: 2938"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 7280.8347757132,
            "unit": "iter/sec",
            "range": "stddev: 0.000002850452217939765",
            "extra": "mean: 137.34688820789017 usec\nrounds: 4079"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 5869.591392455678,
            "unit": "iter/sec",
            "range": "stddev: 0.000004533217971467511",
            "extra": "mean: 170.3696106146883 usec\nrounds: 3693"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 7321.851570890964,
            "unit": "iter/sec",
            "range": "stddev: 0.0000032870324440344505",
            "extra": "mean: 136.5774750167893 usec\nrounds: 4503"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 7274.291561922992,
            "unit": "iter/sec",
            "range": "stddev: 0.000008387646107962428",
            "extra": "mean: 137.47043151727144 usec\nrounds: 4607"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 15023.319610220025,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015796708971710512",
            "extra": "mean: 66.56318483164816 usec\nrounds: 7542"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 17.13886608568331,
            "unit": "iter/sec",
            "range": "stddev: 0.0000856691368407085",
            "extra": "mean: 58.34691717647147 msec\nrounds: 17"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 13.257026733380256,
            "unit": "iter/sec",
            "range": "stddev: 0.00006845362874378569",
            "extra": "mean: 75.43169521428743 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 13.205719124538073,
            "unit": "iter/sec",
            "range": "stddev: 0.00007182813857116456",
            "extra": "mean: 75.72476671428367 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 31.744463071973925,
            "unit": "iter/sec",
            "range": "stddev: 0.00016483720647372327",
            "extra": "mean: 31.501556593750202 msec\nrounds: 32"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 3994.9118188559723,
            "unit": "iter/sec",
            "range": "stddev: 0.000004340290139569656",
            "extra": "mean: 250.3184163615334 usec\nrounds: 2457"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "committer": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "distinct": true,
          "id": "435790c9e7d8d769964f756db1f3f0c20399f837",
          "message": "Merge branch 'development'",
          "timestamp": "2021-08-06T01:03:02+03:00",
          "tree_id": "7966dd7bc5af5daf47fa9b7fd51d26b9565cb40c",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/435790c9e7d8d769964f756db1f3f0c20399f837"
        },
        "date": 1628201037559,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 6174.149261225426,
            "unit": "iter/sec",
            "range": "stddev: 0.000018360142210555273",
            "extra": "mean: 161.96563408017172 usec\nrounds: 2588"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 4564.437263207364,
            "unit": "iter/sec",
            "range": "stddev: 0.000003425241339338418",
            "extra": "mean: 219.08505744195827 usec\nrounds: 3064"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 9368.281788727196,
            "unit": "iter/sec",
            "range": "stddev: 0.0000021509391947148235",
            "extra": "mean: 106.74315979727412 usec\nrounds: 2572"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 7356.8304214816535,
            "unit": "iter/sec",
            "range": "stddev: 0.0000028266081791803857",
            "extra": "mean: 135.92810255351813 usec\nrounds: 4583"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 9360.878259136185,
            "unit": "iter/sec",
            "range": "stddev: 0.000002430437031577466",
            "extra": "mean: 106.82758308751676 usec\nrounds: 6090"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 9401.537751742946,
            "unit": "iter/sec",
            "range": "stddev: 0.0000020630052673362625",
            "extra": "mean: 106.36557831346373 usec\nrounds: 5893"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 32317.06474993544,
            "unit": "iter/sec",
            "range": "stddev: 0.000003749295225718188",
            "extra": "mean: 30.943404289277158 usec\nrounds: 13755"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 17.429632868315743,
            "unit": "iter/sec",
            "range": "stddev: 0.000137526497869186",
            "extra": "mean: 57.37355499999306 msec\nrounds: 17"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 13.442906838250721,
            "unit": "iter/sec",
            "range": "stddev: 0.00008365878117254453",
            "extra": "mean: 74.38867292857968 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 13.390520548260902,
            "unit": "iter/sec",
            "range": "stddev: 0.00006020089907774472",
            "extra": "mean: 74.67969571428463 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 32.06488958880559,
            "unit": "iter/sec",
            "range": "stddev: 0.00007627823996720293",
            "extra": "mean: 31.186759499995823 msec\nrounds: 26"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 5040.078777923537,
            "unit": "iter/sec",
            "range": "stddev: 0.0000037714892339614286",
            "extra": "mean: 198.40959716347732 usec\nrounds: 3314"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 110.2765253563633,
            "unit": "iter/sec",
            "range": "stddev: 0.000025512992169093115",
            "extra": "mean: 9.0681130618548 msec\nrounds: 97"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 3980.90102154579,
            "unit": "iter/sec",
            "range": "stddev: 0.00000386664522455697",
            "extra": "mean: 251.1994130443611 usec\nrounds: 2898"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 7289.119079931669,
            "unit": "iter/sec",
            "range": "stddev: 0.0000027200159953511175",
            "extra": "mean: 137.19078931680377 usec\nrounds: 4025"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 5877.358658172309,
            "unit": "iter/sec",
            "range": "stddev: 0.000006568564540718164",
            "extra": "mean: 170.14445742723677 usec\nrounds: 3723"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 7256.921357597318,
            "unit": "iter/sec",
            "range": "stddev: 0.000002495880552454343",
            "extra": "mean: 137.7994814499531 usec\nrounds: 4717"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 7290.32823194238,
            "unit": "iter/sec",
            "range": "stddev: 0.0000030006102754952807",
            "extra": "mean: 137.16803526328576 usec\nrounds: 4594"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 14839.279583473028,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013395422378809831",
            "extra": "mean: 67.38871616879108 usec\nrounds: 7663"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 17.32292665376236,
            "unit": "iter/sec",
            "range": "stddev: 0.00012327448352387387",
            "extra": "mean: 57.726966117634085 msec\nrounds: 17"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 13.37243979816333,
            "unit": "iter/sec",
            "range": "stddev: 0.00010726745181371749",
            "extra": "mean: 74.78066942857708 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 13.30153386305244,
            "unit": "iter/sec",
            "range": "stddev: 0.00011091436737808927",
            "extra": "mean: 75.17929964285486 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 32.202023419167766,
            "unit": "iter/sec",
            "range": "stddev: 0.0000697436430173567",
            "extra": "mean: 31.05394921875515 msec\nrounds: 32"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 4041.2071879002,
            "unit": "iter/sec",
            "range": "stddev: 0.0000040337913482822015",
            "extra": "mean: 247.45081197373528 usec\nrounds: 2973"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "aec876c7b19ac134a0150e1bf96818b3bfd74ca9",
          "message": "Merge pull request #21 from tchar/development\n\nUse black code styling, move config to pyproject.toml",
          "timestamp": "2021-08-06T10:13:56+03:00",
          "tree_id": "276391ff67f1d9fb7cca640809283fef3d6d0fa7",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/aec876c7b19ac134a0150e1bf96818b3bfd74ca9"
        },
        "date": 1628234099811,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 4162.318869753254,
            "unit": "iter/sec",
            "range": "stddev: 0.00008186856157913501",
            "extra": "mean: 240.25069469492155 usec\nrounds: 1998"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 3028.9736204840096,
            "unit": "iter/sec",
            "range": "stddev: 0.00005224472682388537",
            "extra": "mean: 330.14483626972185 usec\nrounds: 2327"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 6556.072531908841,
            "unit": "iter/sec",
            "range": "stddev: 0.00004217521840491491",
            "extra": "mean: 152.53034421643957 usec\nrounds: 2144"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 5072.393679487644,
            "unit": "iter/sec",
            "range": "stddev: 0.00004768857412333492",
            "extra": "mean: 197.1455811964912 usec\nrounds: 3159"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 6416.634783633499,
            "unit": "iter/sec",
            "range": "stddev: 0.000039798634911849516",
            "extra": "mean: 155.84493020401226 usec\nrounds: 4900"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 6388.001253059887,
            "unit": "iter/sec",
            "range": "stddev: 0.00005441371986043497",
            "extra": "mean: 156.54348839098844 usec\nrounds: 3704"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 24504.046932531015,
            "unit": "iter/sec",
            "range": "stddev: 0.000010919791468465772",
            "extra": "mean: 40.809585565738644 usec\nrounds: 3658"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 13.291449997713462,
            "unit": "iter/sec",
            "range": "stddev: 0.0014882010437462555",
            "extra": "mean: 75.23633615384557 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 10.169020210296074,
            "unit": "iter/sec",
            "range": "stddev: 0.002243610005544342",
            "extra": "mean: 98.33789090000096 msec\nrounds: 10"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 9.941399822263714,
            "unit": "iter/sec",
            "range": "stddev: 0.0033866483382327616",
            "extra": "mean: 100.58945599999963 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 25.05704285920937,
            "unit": "iter/sec",
            "range": "stddev: 0.0011556409495626948",
            "extra": "mean: 39.90893920000076 msec\nrounds: 20"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 3597.048358211835,
            "unit": "iter/sec",
            "range": "stddev: 0.000050852878960266746",
            "extra": "mean: 278.0057148014324 usec\nrounds: 2216"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 81.50736886871803,
            "unit": "iter/sec",
            "range": "stddev: 0.0005062115306157971",
            "extra": "mean: 12.268829357142863 msec\nrounds: 70"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 2584.581659134209,
            "unit": "iter/sec",
            "range": "stddev: 0.00004281549055383298",
            "extra": "mean: 386.90981051648527 usec\nrounds: 2111"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 5014.862582235897,
            "unit": "iter/sec",
            "range": "stddev: 0.00003179803236097316",
            "extra": "mean: 199.40725864399374 usec\nrounds: 2950"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 4044.6530983070384,
            "unit": "iter/sec",
            "range": "stddev: 0.00004282333030237923",
            "extra": "mean: 247.23999208203242 usec\nrounds: 3410"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 4915.160947993051,
            "unit": "iter/sec",
            "range": "stddev: 0.0000987567465378933",
            "extra": "mean: 203.45213729131657 usec\nrounds: 3773"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 5067.891330026414,
            "unit": "iter/sec",
            "range": "stddev: 0.00007830426070335517",
            "extra": "mean: 197.3207266847192 usec\nrounds: 3710"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 10690.767152738981,
            "unit": "iter/sec",
            "range": "stddev: 0.000017410320086057165",
            "extra": "mean: 93.53865683472486 usec\nrounds: 6306"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 13.009262074226232,
            "unit": "iter/sec",
            "range": "stddev: 0.0017351447500443117",
            "extra": "mean: 76.86831076923156 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 9.826285249761682,
            "unit": "iter/sec",
            "range": "stddev: 0.002812433747192648",
            "extra": "mean: 101.7678578000016 msec\nrounds: 10"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 9.93322552048741,
            "unit": "iter/sec",
            "range": "stddev: 0.0017871955318759577",
            "extra": "mean: 100.672233600001 msec\nrounds: 10"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 25.029483855949934,
            "unit": "iter/sec",
            "range": "stddev: 0.0014315117484973625",
            "extra": "mean: 39.952881400000706 msec\nrounds: 25"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 2752.8162953043466,
            "unit": "iter/sec",
            "range": "stddev: 0.00007860521022329634",
            "extra": "mean: 363.2643419416557 usec\nrounds: 2091"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "committer": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "distinct": true,
          "id": "b9c9854b44228f2f643ea1e4b4b7a3ea4adc7141",
          "message": "Merge branch 'development'",
          "timestamp": "2021-08-06T11:42:16+03:00",
          "tree_id": "9b8a83228fdb7a55578a739339b864bfd3b9ec38",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/b9c9854b44228f2f643ea1e4b4b7a3ea4adc7141"
        },
        "date": 1628239402294,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 4121.671079603826,
            "unit": "iter/sec",
            "range": "stddev: 0.00009705050422289395",
            "extra": "mean: 242.62003946615744 usec\nrounds: 1723"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 2971.363479487148,
            "unit": "iter/sec",
            "range": "stddev: 0.00008630290919181293",
            "extra": "mean: 336.54583389192027 usec\nrounds: 2089"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 6410.365361349709,
            "unit": "iter/sec",
            "range": "stddev: 0.00013499786499406805",
            "extra": "mean: 155.99734861125745 usec\nrounds: 2160"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 5204.043315287707,
            "unit": "iter/sec",
            "range": "stddev: 0.00005428438160710713",
            "extra": "mean: 192.15827759587256 usec\nrounds: 4276"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 6312.03999639354,
            "unit": "iter/sec",
            "range": "stddev: 0.00004788520311940985",
            "extra": "mean: 158.4273864822406 usec\nrounds: 4986"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 6388.186938007567,
            "unit": "iter/sec",
            "range": "stddev: 0.00008945686946794859",
            "extra": "mean: 156.538938153224 usec\nrounds: 3444"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 23444.704901809386,
            "unit": "iter/sec",
            "range": "stddev: 0.000079348482655777",
            "extra": "mean: 42.653554573972194 usec\nrounds: 10527"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 13.402837544893202,
            "unit": "iter/sec",
            "range": "stddev: 0.0022634348261271705",
            "extra": "mean: 74.61106624999896 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 10.28072428917661,
            "unit": "iter/sec",
            "range": "stddev: 0.0029061844055593778",
            "extra": "mean: 97.2694113636317 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 10.330946246735977,
            "unit": "iter/sec",
            "range": "stddev: 0.00312187169754437",
            "extra": "mean: 96.79655436363791 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 26.10920432954597,
            "unit": "iter/sec",
            "range": "stddev: 0.002978091444759454",
            "extra": "mean: 38.300669272727305 msec\nrounds: 22"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 3701.473474289673,
            "unit": "iter/sec",
            "range": "stddev: 0.00012061936368715279",
            "extra": "mean: 270.16268168500216 usec\nrounds: 2730"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 83.07788155460771,
            "unit": "iter/sec",
            "range": "stddev: 0.0011042412954038064",
            "extra": "mean: 12.036898164557703 msec\nrounds: 79"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 2494.177332666626,
            "unit": "iter/sec",
            "range": "stddev: 0.00022324399679846056",
            "extra": "mean: 400.9338016599082 usec\nrounds: 2289"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 5028.753335121506,
            "unit": "iter/sec",
            "range": "stddev: 0.00005246272477147588",
            "extra": "mean: 198.8564428117526 usec\nrounds: 3471"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 4117.171685850188,
            "unit": "iter/sec",
            "range": "stddev: 0.0000538325134948194",
            "extra": "mean: 242.88518339829736 usec\nrounds: 3337"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 4988.505957434543,
            "unit": "iter/sec",
            "range": "stddev: 0.0000889044768968006",
            "extra": "mean: 200.46082104195253 usec\nrounds: 3878"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 5091.735708220619,
            "unit": "iter/sec",
            "range": "stddev: 0.00012361756030871326",
            "extra": "mean: 196.3966822522814 usec\nrounds: 4085"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 10821.052925346365,
            "unit": "iter/sec",
            "range": "stddev: 0.000042554855698108006",
            "extra": "mean: 92.41244885307606 usec\nrounds: 6931"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 13.31910399494081,
            "unit": "iter/sec",
            "range": "stddev: 0.003536289950116392",
            "extra": "mean: 75.080125538463 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 10.265779414514583,
            "unit": "iter/sec",
            "range": "stddev: 0.004448807805370854",
            "extra": "mean: 97.41101572727344 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 10.246055655617225,
            "unit": "iter/sec",
            "range": "stddev: 0.002603829397010687",
            "extra": "mean: 97.59853290000109 msec\nrounds: 10"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 25.897170544137566,
            "unit": "iter/sec",
            "range": "stddev: 0.0023141830712396557",
            "extra": "mean: 38.61425703999828 msec\nrounds: 25"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 2878.7091874791904,
            "unit": "iter/sec",
            "range": "stddev: 0.0002477263015369557",
            "extra": "mean: 347.3779165847849 usec\nrounds: 2038"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "committer": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "distinct": true,
          "id": "286c742e8734df14a529fb07525d85f5b8a1a9f7",
          "message": "Merge branch 'development'",
          "timestamp": "2021-08-06T12:29:45+03:00",
          "tree_id": "62a94a8d538cb9d61dcd414ddb4cdb2383fcfa2b",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/286c742e8734df14a529fb07525d85f5b8a1a9f7"
        },
        "date": 1628242249853,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 5166.758810520799,
            "unit": "iter/sec",
            "range": "stddev: 0.00002484739119978353",
            "extra": "mean: 193.54493535942743 usec\nrounds: 2073"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 3808.848574031912,
            "unit": "iter/sec",
            "range": "stddev: 0.00000607012101854252",
            "extra": "mean: 262.5465361941222 usec\nrounds: 2307"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 8052.1902429675765,
            "unit": "iter/sec",
            "range": "stddev: 0.0000031771994059146174",
            "extra": "mean: 124.1898129360959 usec\nrounds: 2149"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 6301.094474494611,
            "unit": "iter/sec",
            "range": "stddev: 0.000004693819682062771",
            "extra": "mean: 158.7025879468672 usec\nrounds: 3468"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 7983.982670741396,
            "unit": "iter/sec",
            "range": "stddev: 0.000003598489877106506",
            "extra": "mean: 125.25077285859636 usec\nrounds: 4495"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 8018.617112045363,
            "unit": "iter/sec",
            "range": "stddev: 0.000004016453645148155",
            "extra": "mean: 124.70978299959297 usec\nrounds: 4447"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 28584.67782374606,
            "unit": "iter/sec",
            "range": "stddev: 0.000004390260027206783",
            "extra": "mean: 34.98377718881523 usec\nrounds: 9434"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 15.00722461299418,
            "unit": "iter/sec",
            "range": "stddev: 0.0002527516325571546",
            "extra": "mean: 66.63457273333127 msec\nrounds: 15"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 11.529590826485867,
            "unit": "iter/sec",
            "range": "stddev: 0.0015238688917993605",
            "extra": "mean: 86.73334683333185 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 10.98321523081996,
            "unit": "iter/sec",
            "range": "stddev: 0.008520890647003404",
            "extra": "mean: 91.04801999999997 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 25.938641720581817,
            "unit": "iter/sec",
            "range": "stddev: 0.0002789230794142381",
            "extra": "mean: 38.552519857141135 msec\nrounds: 21"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 4227.52261674951,
            "unit": "iter/sec",
            "range": "stddev: 0.000005639996528783162",
            "extra": "mean: 236.54515673978528 usec\nrounds: 2552"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 93.71964767825975,
            "unit": "iter/sec",
            "range": "stddev: 0.00008289569715068721",
            "extra": "mean: 10.670121204819372 msec\nrounds: 83"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 3348.4065361844832,
            "unit": "iter/sec",
            "range": "stddev: 0.000008466771308795674",
            "extra": "mean: 298.6495185675699 usec\nrounds: 2262"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 6228.961708567866,
            "unit": "iter/sec",
            "range": "stddev: 0.00000433317741923134",
            "extra": "mean: 160.5403993131811 usec\nrounds: 3203"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 5018.661616503487,
            "unit": "iter/sec",
            "range": "stddev: 0.00000503842156111609",
            "extra": "mean: 199.2563110275409 usec\nrounds: 2929"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 6229.858662016843,
            "unit": "iter/sec",
            "range": "stddev: 0.000004569103837414003",
            "extra": "mean: 160.5172852631398 usec\nrounds: 3800"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 6295.945603670084,
            "unit": "iter/sec",
            "range": "stddev: 0.00000406473936462798",
            "extra": "mean: 158.8323760956689 usec\nrounds: 3765"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 12742.241100368612,
            "unit": "iter/sec",
            "range": "stddev: 0.0000036088515119802596",
            "extra": "mean: 78.47913032904954 usec\nrounds: 6169"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 14.799301594911496,
            "unit": "iter/sec",
            "range": "stddev: 0.0002356259650923182",
            "extra": "mean: 67.57075619999759 msec\nrounds: 15"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 11.500990449004503,
            "unit": "iter/sec",
            "range": "stddev: 0.0002674777311751183",
            "extra": "mean: 86.94903316666587 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 11.439803365262145,
            "unit": "iter/sec",
            "range": "stddev: 0.00027523119782435306",
            "extra": "mean: 87.4140899166657 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 25.960762799260706,
            "unit": "iter/sec",
            "range": "stddev: 0.0002154563758139161",
            "extra": "mean: 38.519669384617515 msec\nrounds: 26"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 3421.389035793452,
            "unit": "iter/sec",
            "range": "stddev: 0.000006515759854374309",
            "extra": "mean: 292.27895148383516 usec\nrounds: 2123"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "committer": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "distinct": true,
          "id": "aa29613ce4336aaa3a386c9aaa5455e794078f0d",
          "message": "Merge branch 'development'",
          "timestamp": "2021-08-06T21:39:13+03:00",
          "tree_id": "5c9e40624afb3254949745739d8bb3b56fd7b288",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/aa29613ce4336aaa3a386c9aaa5455e794078f0d"
        },
        "date": 1628275222678,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 4167.250327240451,
            "unit": "iter/sec",
            "range": "stddev: 0.00003721028322089542",
            "extra": "mean: 239.96638585956964 usec\nrounds: 2164"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 2899.7594098978507,
            "unit": "iter/sec",
            "range": "stddev: 0.00009145879655852634",
            "extra": "mean: 344.85619620257626 usec\nrounds: 2212"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 6609.461223240383,
            "unit": "iter/sec",
            "range": "stddev: 0.00005417813713158891",
            "extra": "mean: 151.2982626305107 usec\nrounds: 2296"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 5262.343449378069,
            "unit": "iter/sec",
            "range": "stddev: 0.000050218479028568134",
            "extra": "mean: 190.02940602787626 usec\nrounds: 4081"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 6611.46375389754,
            "unit": "iter/sec",
            "range": "stddev: 0.000038060563958393024",
            "extra": "mean: 151.25243625671962 usec\nrounds: 3569"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 6406.780493137867,
            "unit": "iter/sec",
            "range": "stddev: 0.00011694087373614159",
            "extra": "mean: 156.08463581217953 usec\nrounds: 5110"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 24476.647924876474,
            "unit": "iter/sec",
            "range": "stddev: 0.000033901968704865366",
            "extra": "mean: 40.85526756233908 usec\nrounds: 9452"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 13.3273036920794,
            "unit": "iter/sec",
            "range": "stddev: 0.004180158783443671",
            "extra": "mean: 75.03393207692218 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 10.423998666471022,
            "unit": "iter/sec",
            "range": "stddev: 0.0044306604135101535",
            "extra": "mean: 95.93247581818271 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 10.61641257930325,
            "unit": "iter/sec",
            "range": "stddev: 0.002549227881543447",
            "extra": "mean: 94.19377709090782 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 27.50677292392993,
            "unit": "iter/sec",
            "range": "stddev: 0.0013728715755304368",
            "extra": "mean: 36.3546826363639 msec\nrounds: 22"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 3681.684949321142,
            "unit": "iter/sec",
            "range": "stddev: 0.00009079460462126074",
            "extra": "mean: 271.61476708765855 usec\nrounds: 2692"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 85.96805673683328,
            "unit": "iter/sec",
            "range": "stddev: 0.0006049321464808679",
            "extra": "mean: 11.632227573332443 msec\nrounds: 75"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 2520.823799074898,
            "unit": "iter/sec",
            "range": "stddev: 0.00004943654500962224",
            "extra": "mean: 396.695715252682 usec\nrounds: 2216"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 5095.5987183768775,
            "unit": "iter/sec",
            "range": "stddev: 0.000060463488336113334",
            "extra": "mean: 196.24779251034394 usec\nrounds: 3605"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 4116.043649683545,
            "unit": "iter/sec",
            "range": "stddev: 0.00005852326525521893",
            "extra": "mean: 242.9517481129928 usec\nrounds: 3577"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 5048.576189078537,
            "unit": "iter/sec",
            "range": "stddev: 0.00006579420148109959",
            "extra": "mean: 198.07564797442808 usec\nrounds: 4369"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 5105.439871544883,
            "unit": "iter/sec",
            "range": "stddev: 0.000039943908654258065",
            "extra": "mean: 195.86950882988353 usec\nrounds: 3341"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 10498.750946515866,
            "unit": "iter/sec",
            "range": "stddev: 0.00006187367661891096",
            "extra": "mean: 95.24942586926132 usec\nrounds: 7190"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 12.489194289057467,
            "unit": "iter/sec",
            "range": "stddev: 0.004673622322436653",
            "extra": "mean: 80.06921638461179 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 10.694253412401624,
            "unit": "iter/sec",
            "range": "stddev: 0.0017192006319997465",
            "extra": "mean: 93.50816381818174 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 10.563270963332073,
            "unit": "iter/sec",
            "range": "stddev: 0.0018053837541305985",
            "extra": "mean: 94.66764636363739 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 28.17715976773835,
            "unit": "iter/sec",
            "range": "stddev: 0.0009448119745610881",
            "extra": "mean: 35.489737370370364 msec\nrounds: 27"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 2940.2560381085327,
            "unit": "iter/sec",
            "range": "stddev: 0.00012715459634319172",
            "extra": "mean: 340.10643530326706 usec\nrounds: 2589"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "a62ce13de68d0eccea2c742ba9273b8811bf4580",
          "message": "Merge pull request #22 from tchar/development\n\nCode refactoring and typing",
          "timestamp": "2021-08-08T01:52:09+03:00",
          "tree_id": "29c47389c0120aa9a79adf81954ab5fd30945625",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/a62ce13de68d0eccea2c742ba9273b8811bf4580"
        },
        "date": 1628376794297,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 4553.806634653573,
            "unit": "iter/sec",
            "range": "stddev: 0.00015696860316161671",
            "extra": "mean: 219.59650029717918 usec\nrounds: 1683"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 3174.831240068368,
            "unit": "iter/sec",
            "range": "stddev: 0.00009491644360688356",
            "extra": "mean: 314.977371829838 usec\nrounds: 2563"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 7146.268386639504,
            "unit": "iter/sec",
            "range": "stddev: 0.00006604409271104161",
            "extra": "mean: 139.93317153741057 usec\nrounds: 2361"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 5271.004801568625,
            "unit": "iter/sec",
            "range": "stddev: 0.00017825572160553007",
            "extra": "mean: 189.7171483703458 usec\nrounds: 3835"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 7168.423345079926,
            "unit": "iter/sec",
            "range": "stddev: 0.000058293299477514645",
            "extra": "mean: 139.50068960231732 usec\nrounds: 1308"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 7215.049630797396,
            "unit": "iter/sec",
            "range": "stddev: 0.00006504677254002909",
            "extra": "mean: 138.59918519915732 usec\nrounds: 5297"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 25190.657291251748,
            "unit": "iter/sec",
            "range": "stddev: 0.00005528431571596642",
            "extra": "mean: 39.69725713934751 usec\nrounds: 8369"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 14.87540168679413,
            "unit": "iter/sec",
            "range": "stddev: 0.004028586884003544",
            "extra": "mean: 67.22507539999849 msec\nrounds: 15"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 10.986284851081066,
            "unit": "iter/sec",
            "range": "stddev: 0.007318798982669523",
            "extra": "mean: 91.02258074999743 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 11.06254899983244,
            "unit": "iter/sec",
            "range": "stddev: 0.003230309826802228",
            "extra": "mean: 90.39507983333195 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 29.139811305709898,
            "unit": "iter/sec",
            "range": "stddev: 0.0017275885446808386",
            "extra": "mean: 34.31731213043414 msec\nrounds: 23"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 3906.044476692204,
            "unit": "iter/sec",
            "range": "stddev: 0.00017675578665173454",
            "extra": "mean: 256.01346988420374 usec\nrounds: 2673"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 90.31420986864349,
            "unit": "iter/sec",
            "range": "stddev: 0.000848100630594438",
            "extra": "mean: 11.07245472727314 msec\nrounds: 88"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 2802.0186715747186,
            "unit": "iter/sec",
            "range": "stddev: 0.0001255531136936494",
            "extra": "mean: 356.88555902377544 usec\nrounds: 2499"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 5476.888794812974,
            "unit": "iter/sec",
            "range": "stddev: 0.00007604644318036675",
            "extra": "mean: 182.58541253331185 usec\nrounds: 3750"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 4369.927489925883,
            "unit": "iter/sec",
            "range": "stddev: 0.00007197565022083979",
            "extra": "mean: 228.83674896330163 usec\nrounds: 3135"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 5503.178587686932,
            "unit": "iter/sec",
            "range": "stddev: 0.00006437496565707799",
            "extra": "mean: 181.71316523098972 usec\nrounds: 4527"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 5471.828209191716,
            "unit": "iter/sec",
            "range": "stddev: 0.00010068053843231523",
            "extra": "mean: 182.7542754942808 usec\nrounds: 3844"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 11676.023376940944,
            "unit": "iter/sec",
            "range": "stddev: 0.00009043168874548111",
            "extra": "mean: 85.64559762486486 usec\nrounds: 7242"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 14.27540192361146,
            "unit": "iter/sec",
            "range": "stddev: 0.003863108309551263",
            "extra": "mean: 70.0505670769244 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 11.210930935693503,
            "unit": "iter/sec",
            "range": "stddev: 0.004978349229501826",
            "extra": "mean: 89.19865849999908 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 11.043766417783804,
            "unit": "iter/sec",
            "range": "stddev: 0.004683880690492444",
            "extra": "mean: 90.54881841666784 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 28.536272578146242,
            "unit": "iter/sec",
            "range": "stddev: 0.0019192265836045536",
            "extra": "mean: 35.04311914814774 msec\nrounds: 27"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 3145.5642057888776,
            "unit": "iter/sec",
            "range": "stddev: 0.00008760504085846025",
            "extra": "mean: 317.9079918825595 usec\nrounds: 2587"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "committer": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "distinct": true,
          "id": "8f9322470907d13385c5b6397a6f177eebec3cea",
          "message": "Merge branch 'development'",
          "timestamp": "2021-08-08T04:43:15+03:00",
          "tree_id": "26e56f6fadf7ddcefeb1acbcd6ff0537ce7044d7",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/8f9322470907d13385c5b6397a6f177eebec3cea"
        },
        "date": 1628387065994,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 4343.325814477857,
            "unit": "iter/sec",
            "range": "stddev: 0.00014696991913069565",
            "extra": "mean: 230.2383110810252 usec\nrounds: 2202"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 3176.2416276152208,
            "unit": "iter/sec",
            "range": "stddev: 0.00011062113063517818",
            "extra": "mean: 314.83750836387657 usec\nrounds: 2451"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 6784.024260774478,
            "unit": "iter/sec",
            "range": "stddev: 0.0000586162313242054",
            "extra": "mean: 147.40513323073492 usec\nrounds: 1944"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 5130.12148086301,
            "unit": "iter/sec",
            "range": "stddev: 0.00008226298818381385",
            "extra": "mean: 194.92715791045478 usec\nrounds: 3369"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 6662.619558829314,
            "unit": "iter/sec",
            "range": "stddev: 0.00007404621335989535",
            "extra": "mean: 150.09111523932032 usec\nrounds: 4495"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 6619.07480239199,
            "unit": "iter/sec",
            "range": "stddev: 0.00007723926462684105",
            "extra": "mean: 151.07851623592796 usec\nrounds: 4527"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 23911.322225934604,
            "unit": "iter/sec",
            "range": "stddev: 0.00004171253765936302",
            "extra": "mean: 41.82119209264739 usec\nrounds: 9662"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 13.808358732543143,
            "unit": "iter/sec",
            "range": "stddev: 0.003711310358701911",
            "extra": "mean: 72.41990300000164 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 11.17510199142247,
            "unit": "iter/sec",
            "range": "stddev: 0.002114551476350255",
            "extra": "mean: 89.48464190909017 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 10.700251105127565,
            "unit": "iter/sec",
            "range": "stddev: 0.0018026175294558798",
            "extra": "mean: 93.45575072727027 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 26.562415711763023,
            "unit": "iter/sec",
            "range": "stddev: 0.0012184410344892435",
            "extra": "mean: 37.647178285714254 msec\nrounds: 21"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 3693.809801608547,
            "unit": "iter/sec",
            "range": "stddev: 0.00016156050482482",
            "extra": "mean: 270.7231973786331 usec\nrounds: 2518"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 85.53282878267734,
            "unit": "iter/sec",
            "range": "stddev: 0.0009677626286276476",
            "extra": "mean: 11.69141736842131 msec\nrounds: 76"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 2794.6132708135037,
            "unit": "iter/sec",
            "range": "stddev: 0.00011758103129837356",
            "extra": "mean: 357.8312643269253 usec\nrounds: 2251"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 5176.547316240101,
            "unit": "iter/sec",
            "range": "stddev: 0.00007094869435450389",
            "extra": "mean: 193.1789547953622 usec\nrounds: 3274"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 4163.62226206469,
            "unit": "iter/sec",
            "range": "stddev: 0.00010501975415568071",
            "extra": "mean: 240.1754859251118 usec\nrounds: 3659"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 5107.641933726602,
            "unit": "iter/sec",
            "range": "stddev: 0.00008548384689079582",
            "extra": "mean: 195.7850634354055 usec\nrounds: 4477"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 5145.292678598742,
            "unit": "iter/sec",
            "range": "stddev: 0.00009028301282113553",
            "extra": "mean: 194.35240373388007 usec\nrounds: 4285"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 11475.055557393018,
            "unit": "iter/sec",
            "range": "stddev: 0.00004343937788564278",
            "extra": "mean: 87.14554757477678 usec\nrounds: 5917"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 13.855304894395882,
            "unit": "iter/sec",
            "range": "stddev: 0.0026090571795046656",
            "extra": "mean: 72.17452142857387 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 10.525622458160475,
            "unit": "iter/sec",
            "range": "stddev: 0.0034308089437363573",
            "extra": "mean: 95.00625772727615 msec\nrounds: 11"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 10.559863159379505,
            "unit": "iter/sec",
            "range": "stddev: 0.0036107459549610207",
            "extra": "mean: 94.69819683333469 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 26.954537856496543,
            "unit": "iter/sec",
            "range": "stddev: 0.002406571421254368",
            "extra": "mean: 37.099504555555995 msec\nrounds: 27"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 2990.6926176678708,
            "unit": "iter/sec",
            "range": "stddev: 0.00014733927307249427",
            "extra": "mean: 334.3707053317287 usec\nrounds: 2457"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "committer": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "distinct": true,
          "id": "a25251e9d6e41a02fedf4900a9f82aac8e7a2a04",
          "message": "Merge branch 'development'",
          "timestamp": "2021-08-08T23:50:58+03:00",
          "tree_id": "a9b73fcdbb8760d8643c61a3ddfee59d59488310",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/a25251e9d6e41a02fedf4900a9f82aac8e7a2a04"
        },
        "date": 1628455919057,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 5234.2015449469745,
            "unit": "iter/sec",
            "range": "stddev: 0.000006025051807716854",
            "extra": "mean: 191.0511071101926 usec\nrounds: 2194"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 3796.8817532918024,
            "unit": "iter/sec",
            "range": "stddev: 0.000006226725897116559",
            "extra": "mean: 263.37401714789377 usec\nrounds: 2216"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 8126.259789742277,
            "unit": "iter/sec",
            "range": "stddev: 0.00000454254620634596",
            "extra": "mean: 123.05784282977186 usec\nrounds: 2106"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 6290.02249927172,
            "unit": "iter/sec",
            "range": "stddev: 0.000004918551704171933",
            "extra": "mean: 158.98194324675043 usec\nrounds: 3154"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 8100.495615720963,
            "unit": "iter/sec",
            "range": "stddev: 0.000003568293099648376",
            "extra": "mean: 123.44923661945562 usec\nrounds: 4615"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 8156.82231181955,
            "unit": "iter/sec",
            "range": "stddev: 0.000003985910807456682",
            "extra": "mean: 122.59676155394013 usec\nrounds: 4479"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 27842.15967454451,
            "unit": "iter/sec",
            "range": "stddev: 0.00000418820039914823",
            "extra": "mean: 35.91675400505222 usec\nrounds: 9488"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 14.889773389957922,
            "unit": "iter/sec",
            "range": "stddev: 0.0005834140571090692",
            "extra": "mean: 67.16018933333316 msec\nrounds: 15"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 11.568368206306594,
            "unit": "iter/sec",
            "range": "stddev: 0.0010716873075546855",
            "extra": "mean: 86.44261508333055 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 11.556823063394631,
            "unit": "iter/sec",
            "range": "stddev: 0.00016193112483329776",
            "extra": "mean: 86.52897033332845 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 25.650454704328222,
            "unit": "iter/sec",
            "range": "stddev: 0.00015750194811313476",
            "extra": "mean: 38.985663666666355 msec\nrounds: 21"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 4291.382216993441,
            "unit": "iter/sec",
            "range": "stddev: 0.000005659928679394494",
            "extra": "mean: 233.02515353680238 usec\nrounds: 2488"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 92.96137936094487,
            "unit": "iter/sec",
            "range": "stddev: 0.00005585398366037415",
            "extra": "mean: 10.757155357143096 msec\nrounds: 84"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 3368.36983750766,
            "unit": "iter/sec",
            "range": "stddev: 0.0000072371004332616475",
            "extra": "mean: 296.8795139015746 usec\nrounds: 2230"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 6363.820578191809,
            "unit": "iter/sec",
            "range": "stddev: 0.000004395110866060618",
            "extra": "mean: 157.1383083028617 usec\nrounds: 3276"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 5098.737641686892,
            "unit": "iter/sec",
            "range": "stddev: 0.000006754325505950172",
            "extra": "mean: 196.12697696466591 usec\nrounds: 2952"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 6389.852204678301,
            "unit": "iter/sec",
            "range": "stddev: 0.000004570793790971044",
            "extra": "mean: 156.4981423620181 usec\nrounds: 3751"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 6462.323980888476,
            "unit": "iter/sec",
            "range": "stddev: 0.000004129064083023042",
            "extra": "mean: 154.74309288073087 usec\nrounds: 3596"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 13249.728198093491,
            "unit": "iter/sec",
            "range": "stddev: 0.0000026521250389758374",
            "extra": "mean: 75.47324632243327 usec\nrounds: 6390"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 14.942015283331969,
            "unit": "iter/sec",
            "range": "stddev: 0.0002258603896279214",
            "extra": "mean: 66.9253766000035 msec\nrounds: 15"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 11.548651546676217,
            "unit": "iter/sec",
            "range": "stddev: 0.0003700534826039331",
            "extra": "mean: 86.59019591666588 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 11.493707329808062,
            "unit": "iter/sec",
            "range": "stddev: 0.00044794341014185485",
            "extra": "mean: 87.00412941667442 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 25.834894357137493,
            "unit": "iter/sec",
            "range": "stddev: 0.00026422585591757795",
            "extra": "mean: 38.707338461545774 msec\nrounds: 26"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 3439.060619725475,
            "unit": "iter/sec",
            "range": "stddev: 0.000007296644499878192",
            "extra": "mean: 290.7770785615944 usec\nrounds: 2113"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "committer": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "distinct": true,
          "id": "35e6abd08a8d162abab353141b0c33721bbb4dc9",
          "message": "Merge branch 'development'",
          "timestamp": "2021-08-09T05:45:35+03:00",
          "tree_id": "4c69195d67851d0c98d752ff2dc15005bc9e7a51",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/35e6abd08a8d162abab353141b0c33721bbb4dc9"
        },
        "date": 1628477197680,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 5383.15329766152,
            "unit": "iter/sec",
            "range": "stddev: 0.000008474536460484603",
            "extra": "mean: 185.76472649114544 usec\nrounds: 2329"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 3919.9774500174526,
            "unit": "iter/sec",
            "range": "stddev: 0.000008547244761568397",
            "extra": "mean: 255.10350831113783 usec\nrounds: 2707"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 8175.840407306638,
            "unit": "iter/sec",
            "range": "stddev: 0.000004657392984577844",
            "extra": "mean: 122.31158513151914 usec\nrounds: 2179"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 6272.615114760911,
            "unit": "iter/sec",
            "range": "stddev: 0.000005578173036650007",
            "extra": "mean: 159.4231403815562 usec\nrounds: 3405"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 8115.734384636277,
            "unit": "iter/sec",
            "range": "stddev: 0.0000056671078364597665",
            "extra": "mean: 123.21743820165905 usec\nrounds: 4361"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 8218.710449825036,
            "unit": "iter/sec",
            "range": "stddev: 0.000005687021467894251",
            "extra": "mean: 121.67358931853944 usec\nrounds: 4943"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 27972.983642027928,
            "unit": "iter/sec",
            "range": "stddev: 0.000004558980721515975",
            "extra": "mean: 35.748778635738844 usec\nrounds: 9970"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 15.200572897022793,
            "unit": "iter/sec",
            "range": "stddev: 0.0005676709438291047",
            "extra": "mean: 65.78699413335016 msec\nrounds: 15"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 11.797664091218163,
            "unit": "iter/sec",
            "range": "stddev: 0.0010081514881672147",
            "extra": "mean: 84.76254216666253 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 11.628254956780653,
            "unit": "iter/sec",
            "range": "stddev: 0.0010715899589031918",
            "extra": "mean: 85.99742641666808 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 25.819733537662593,
            "unit": "iter/sec",
            "range": "stddev: 0.0007686322555393875",
            "extra": "mean: 38.730066619058064 msec\nrounds: 21"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 4207.72362519709,
            "unit": "iter/sec",
            "range": "stddev: 0.000005343428496913723",
            "extra": "mean: 237.65819456670232 usec\nrounds: 2503"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 94.53607862907114,
            "unit": "iter/sec",
            "range": "stddev: 0.00007887616110252086",
            "extra": "mean: 10.577972076921819 msec\nrounds: 78"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 3416.2521601107064,
            "unit": "iter/sec",
            "range": "stddev: 0.0000062227461725357135",
            "extra": "mean: 292.71843913524054 usec\nrounds: 2407"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 6478.1341372722345,
            "unit": "iter/sec",
            "range": "stddev: 0.0000054899697485728745",
            "extra": "mean: 154.36543591255008 usec\nrounds: 3347"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 5276.463463396671,
            "unit": "iter/sec",
            "range": "stddev: 0.000008551186406408806",
            "extra": "mean: 189.52088021400985 usec\nrounds: 3189"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 6469.315451472364,
            "unit": "iter/sec",
            "range": "stddev: 0.000006166035277348871",
            "extra": "mean: 154.57586007379004 usec\nrounds: 4338"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 6496.789801732331,
            "unit": "iter/sec",
            "range": "stddev: 0.00009287199908545526",
            "extra": "mean: 153.92217241403682 usec\nrounds: 3973"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 13412.712542762989,
            "unit": "iter/sec",
            "range": "stddev: 0.000003166733020989546",
            "extra": "mean: 74.55613447404892 usec\nrounds: 7072"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 14.963587232737439,
            "unit": "iter/sec",
            "range": "stddev: 0.0004164585461258851",
            "extra": "mean: 66.82889500000329 msec\nrounds: 15"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 11.682288550669602,
            "unit": "iter/sec",
            "range": "stddev: 0.001093535860051789",
            "extra": "mean: 85.59966616666752 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 11.695017495680105,
            "unit": "iter/sec",
            "range": "stddev: 0.0011519723188832048",
            "extra": "mean: 85.50649884614359 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 27.023563304115477,
            "unit": "iter/sec",
            "range": "stddev: 0.0010843117846939625",
            "extra": "mean: 37.00474244444691 msec\nrounds: 27"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 3420.182176784264,
            "unit": "iter/sec",
            "range": "stddev: 0.000010614014184012589",
            "extra": "mean: 292.3820861905735 usec\nrounds: 2216"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "committer": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "distinct": true,
          "id": "b6a2d1267da8987455de7d7564a421000e325698",
          "message": "Merge branch 'development'",
          "timestamp": "2021-08-09T23:21:50+03:00",
          "tree_id": "b7ecd92fcfe7c8c1c98fad0b999c48cbc0faac42",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/b6a2d1267da8987455de7d7564a421000e325698"
        },
        "date": 1628540577535,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 5349.691180527482,
            "unit": "iter/sec",
            "range": "stddev: 0.00002050999784064384",
            "extra": "mean: 186.92667786879608 usec\nrounds: 2440"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 3933.366953857723,
            "unit": "iter/sec",
            "range": "stddev: 0.000012187403942870938",
            "extra": "mean: 254.23511503782564 usec\nrounds: 2773"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 8180.141845408456,
            "unit": "iter/sec",
            "range": "stddev: 0.00005121070494210179",
            "extra": "mean: 122.24726892251921 usec\nrounds: 2246"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 6362.477310583904,
            "unit": "iter/sec",
            "range": "stddev: 0.000007703549752836338",
            "extra": "mean: 157.17148387099346 usec\nrounds: 3937"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 8149.332416517659,
            "unit": "iter/sec",
            "range": "stddev: 0.000007249293798364556",
            "extra": "mean: 122.70943788881742 usec\nrounds: 4983"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 8269.070143021047,
            "unit": "iter/sec",
            "range": "stddev: 0.000006341009427963945",
            "extra": "mean: 120.93258162091935 usec\nrounds: 4331"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 28071.035738569874,
            "unit": "iter/sec",
            "range": "stddev: 0.000004601769555233534",
            "extra": "mean: 35.623908191816035 usec\nrounds: 10010"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 15.70663730274187,
            "unit": "iter/sec",
            "range": "stddev: 0.0006731360041976373",
            "extra": "mean: 63.66735162499948 msec\nrounds: 16"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 12.094720420736552,
            "unit": "iter/sec",
            "range": "stddev: 0.0010720870598868119",
            "extra": "mean: 82.68070407691998 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 12.176794588385764,
            "unit": "iter/sec",
            "range": "stddev: 0.0008313692142647798",
            "extra": "mean: 82.12341866666624 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 27.49338849303435,
            "unit": "iter/sec",
            "range": "stddev: 0.0006370990603929408",
            "extra": "mean: 36.37238095454685 msec\nrounds: 22"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 4319.80203591969,
            "unit": "iter/sec",
            "range": "stddev: 0.000013290891618947592",
            "extra": "mean: 231.49208961079142 usec\nrounds: 2801"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 100.84879718761057,
            "unit": "iter/sec",
            "range": "stddev: 0.00042539690725696235",
            "extra": "mean: 9.915834674157637 msec\nrounds: 89"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 3535.186844940569,
            "unit": "iter/sec",
            "range": "stddev: 0.000016698063987928215",
            "extra": "mean: 282.8704800797626 usec\nrounds: 2510"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 6580.780210481691,
            "unit": "iter/sec",
            "range": "stddev: 0.000008896970194243687",
            "extra": "mean: 151.9576658109971 usec\nrounds: 3896"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 5288.223730983124,
            "unit": "iter/sec",
            "range": "stddev: 0.00001164289681849495",
            "extra": "mean: 189.09941236810943 usec\nrounds: 3509"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 6527.33449129447,
            "unit": "iter/sec",
            "range": "stddev: 0.000009806404154072683",
            "extra": "mean: 153.20189295243006 usec\nrounds: 3746"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 6567.497200290413,
            "unit": "iter/sec",
            "range": "stddev: 0.000006702644415304753",
            "extra": "mean: 152.26500590754424 usec\nrounds: 4232"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 13598.29490113838,
            "unit": "iter/sec",
            "range": "stddev: 0.0000042773070679136724",
            "extra": "mean: 73.53863166449531 usec\nrounds: 6771"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 15.63325729108544,
            "unit": "iter/sec",
            "range": "stddev: 0.0011937864315947945",
            "extra": "mean: 63.966195999999975 msec\nrounds: 16"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 12.031948224801965,
            "unit": "iter/sec",
            "range": "stddev: 0.0006048575844609357",
            "extra": "mean: 83.11205976922818 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 12.090125258412883,
            "unit": "iter/sec",
            "range": "stddev: 0.0015024390040433077",
            "extra": "mean: 82.71212899999962 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 27.89391025637021,
            "unit": "iter/sec",
            "range": "stddev: 0.0012808672086074486",
            "extra": "mean: 35.85011892592676 msec\nrounds: 27"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 3544.946773400241,
            "unit": "iter/sec",
            "range": "stddev: 0.000017806722316065005",
            "extra": "mean: 282.09168258986875 usec\nrounds: 2533"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "committer": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "distinct": true,
          "id": "cdc539cc0e886bf19bd6779ef2fe6bbdab6a4e80",
          "message": "Merge branch 'development'",
          "timestamp": "2021-08-09T23:24:42+03:00",
          "tree_id": "b675f2031a203ba6f4e0f693756d47a6f4ac9318",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/cdc539cc0e886bf19bd6779ef2fe6bbdab6a4e80"
        },
        "date": 1628540843098,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 4259.045969803219,
            "unit": "iter/sec",
            "range": "stddev: 0.00005832027412604417",
            "extra": "mean: 234.7943664121106 usec\nrounds: 2358"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 3045.1029171004734,
            "unit": "iter/sec",
            "range": "stddev: 0.000046953964757212286",
            "extra": "mean: 328.39612559045895 usec\nrounds: 2540"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 7798.932316923933,
            "unit": "iter/sec",
            "range": "stddev: 0.000031727644796097466",
            "extra": "mean: 128.22267963910494 usec\nrounds: 2544"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 5689.063908754056,
            "unit": "iter/sec",
            "range": "stddev: 0.00004212291169315669",
            "extra": "mean: 175.77584221918275 usec\nrounds: 4145"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 7378.339753492868,
            "unit": "iter/sec",
            "range": "stddev: 0.00004582555719723374",
            "extra": "mean: 135.53184502334759 usec\nrounds: 5988"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 7792.951916502274,
            "unit": "iter/sec",
            "range": "stddev: 0.00004597980802128115",
            "extra": "mean: 128.3210791898267 usec\nrounds: 6415"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 27900.69490332462,
            "unit": "iter/sec",
            "range": "stddev: 0.000025962945824454588",
            "extra": "mean: 35.84140120756781 usec\nrounds: 10765"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 15.843929705423964,
            "unit": "iter/sec",
            "range": "stddev: 0.0024570522521741183",
            "extra": "mean: 63.1156549285663 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 12.117071020396375,
            "unit": "iter/sec",
            "range": "stddev: 0.003989851410023601",
            "extra": "mean: 82.52819499999002 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 11.68118417864588,
            "unit": "iter/sec",
            "range": "stddev: 0.0030633022597816493",
            "extra": "mean: 85.60775899998892 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 29.797384970820755,
            "unit": "iter/sec",
            "range": "stddev: 0.002011545902676041",
            "extra": "mean: 33.55999195832974 msec\nrounds: 24"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 4094.5947144130655,
            "unit": "iter/sec",
            "range": "stddev: 0.000051969962702475494",
            "extra": "mean: 244.2244152956036 usec\nrounds: 3465"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 93.23497775245795,
            "unit": "iter/sec",
            "range": "stddev: 0.0006223514589851501",
            "extra": "mean: 10.725588444446613 msec\nrounds: 81"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 2655.646520881634,
            "unit": "iter/sec",
            "range": "stddev: 0.00006312045971707737",
            "extra": "mean: 376.5561388298076 usec\nrounds: 2341"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 5927.367735767693,
            "unit": "iter/sec",
            "range": "stddev: 0.00012180612694693551",
            "extra": "mean: 168.70895219907987 usec\nrounds: 3933"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 4837.953216711813,
            "unit": "iter/sec",
            "range": "stddev: 0.00004487867232172324",
            "extra": "mean: 206.69898099586518 usec\nrounds: 3999"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 5864.076688896001,
            "unit": "iter/sec",
            "range": "stddev: 0.00003875960762793976",
            "extra": "mean: 170.5298298525944 usec\nrounds: 3591"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 5525.140474449798,
            "unit": "iter/sec",
            "range": "stddev: 0.00007144973342207872",
            "extra": "mean: 180.99087337676815 usec\nrounds: 3696"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 12143.712587716434,
            "unit": "iter/sec",
            "range": "stddev: 0.00002319224765098979",
            "extra": "mean: 82.34713995220181 usec\nrounds: 5852"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 14.983904640819768,
            "unit": "iter/sec",
            "range": "stddev: 0.004138460979263442",
            "extra": "mean: 66.73827843750146 msec\nrounds: 16"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 12.042638547700795,
            "unit": "iter/sec",
            "range": "stddev: 0.004084739990655513",
            "extra": "mean: 83.03828069230909 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 12.188058228300692,
            "unit": "iter/sec",
            "range": "stddev: 0.002490291301963213",
            "extra": "mean: 82.04752400000832 msec\nrounds: 12"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 30.653562146235167,
            "unit": "iter/sec",
            "range": "stddev: 0.004018532973522962",
            "extra": "mean: 32.622635999999716 msec\nrounds: 31"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 3345.0615795167537,
            "unit": "iter/sec",
            "range": "stddev: 0.0000647031534663987",
            "extra": "mean: 298.9481587195371 usec\nrounds: 2936"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "ee0903174c8b87cd1f7c3b6c1acef10702547507",
          "message": "Merge pull request #27 from tchar/development\n\nMerge branch development",
          "timestamp": "2021-08-12T09:39:56+03:00",
          "tree_id": "30997e4c4338a8dd5216d4bb07ea860293a33da1",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/ee0903174c8b87cd1f7c3b6c1acef10702547507"
        },
        "date": 1628750455031,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 5975.830180469523,
            "unit": "iter/sec",
            "range": "stddev: 0.000028258977207456918",
            "extra": "mean: 167.34076601912903 usec\nrounds: 2419"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 4390.821038954311,
            "unit": "iter/sec",
            "range": "stddev: 0.000025140761673862135",
            "extra": "mean: 227.74783830364294 usec\nrounds: 3018"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 9194.212992666571,
            "unit": "iter/sec",
            "range": "stddev: 0.000011820723415278641",
            "extra": "mean: 108.76406722332989 usec\nrounds: 2395"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 7070.304520630039,
            "unit": "iter/sec",
            "range": "stddev: 0.000014728725533968272",
            "extra": "mean: 141.436623710076 usec\nrounds: 4167"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 9357.586753082125,
            "unit": "iter/sec",
            "range": "stddev: 0.000014179036984834475",
            "extra": "mean: 106.86515940347849 usec\nrounds: 5163"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 9547.84019257909,
            "unit": "iter/sec",
            "range": "stddev: 0.000014333274596821305",
            "extra": "mean: 104.73572869152487 usec\nrounds: 5831"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 32190.15282271331,
            "unit": "iter/sec",
            "range": "stddev: 0.000006245363567284845",
            "extra": "mean: 31.065400823272945 usec\nrounds: 10204"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 17.83775022470768,
            "unit": "iter/sec",
            "range": "stddev: 0.002987093945463166",
            "extra": "mean: 56.06088141176378 msec\nrounds: 17"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 13.821495214236043,
            "unit": "iter/sec",
            "range": "stddev: 0.0028209229597822706",
            "extra": "mean: 72.35107233333244 msec\nrounds: 15"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 12.99269509754634,
            "unit": "iter/sec",
            "range": "stddev: 0.003106591944663936",
            "extra": "mean: 76.96632549999956 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 29.09025567901395,
            "unit": "iter/sec",
            "range": "stddev: 0.0015508520079405164",
            "extra": "mean: 34.37577211538267 msec\nrounds: 26"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 4895.959053542465,
            "unit": "iter/sec",
            "range": "stddev: 0.00002598516402931619",
            "extra": "mean: 204.25007420690156 usec\nrounds: 3625"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 108.67624978530294,
            "unit": "iter/sec",
            "range": "stddev: 0.0006266693592149998",
            "extra": "mean: 9.201642511363483 msec\nrounds: 88"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 4021.6566291645554,
            "unit": "iter/sec",
            "range": "stddev: 0.00003273410259810299",
            "extra": "mean: 248.65374948923386 usec\nrounds: 2447"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 7658.299662205191,
            "unit": "iter/sec",
            "range": "stddev: 0.000018741399872601945",
            "extra": "mean: 130.5772879239949 usec\nrounds: 3685"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 6040.119794443198,
            "unit": "iter/sec",
            "range": "stddev: 0.000022292876307252066",
            "extra": "mean: 165.55963027752895 usec\nrounds: 3316"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 7625.97130946006,
            "unit": "iter/sec",
            "range": "stddev: 0.000017772014044960496",
            "extra": "mean: 131.13083690198187 usec\nrounds: 4390"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 7295.305320283474,
            "unit": "iter/sec",
            "range": "stddev: 0.00001636983410019605",
            "extra": "mean: 137.07445488534302 usec\nrounds: 4278"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 14558.643809849313,
            "unit": "iter/sec",
            "range": "stddev: 0.000006659773972976608",
            "extra": "mean: 68.6877165937306 usec\nrounds: 6623"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 17.048946793137883,
            "unit": "iter/sec",
            "range": "stddev: 0.003701143366032096",
            "extra": "mean: 58.65464958823703 msec\nrounds: 17"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 13.025675293759164,
            "unit": "iter/sec",
            "range": "stddev: 0.003178463487981211",
            "extra": "mean: 76.7714515714297 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 13.333556321189784,
            "unit": "iter/sec",
            "range": "stddev: 0.003607833216551535",
            "extra": "mean: 74.99874571428425 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 28.011432647938836,
            "unit": "iter/sec",
            "range": "stddev: 0.007276596635341867",
            "extra": "mean: 35.69970920689709 msec\nrounds: 29"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 3795.2325807024254,
            "unit": "iter/sec",
            "range": "stddev: 0.000030756665498920296",
            "extra": "mean: 263.488463153665 usec\nrounds: 2429"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "a72d7b4bc57223e124b6b8e1242513bfa6bb264e",
          "message": "Merge pull request #52 from tchar/development\n\nEnable benchmark GH Actions",
          "timestamp": "2024-04-04T21:07:08-07:00",
          "tree_id": "cb749c35681aee08c438a2c9d358b5dd6e106383",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/a72d7b4bc57223e124b6b8e1242513bfa6bb264e"
        },
        "date": 1712290076056,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 12263.541141536516,
            "unit": "iter/sec",
            "range": "stddev: 0.000006984868591719678",
            "extra": "mean: 81.54251602035305 usec\nrounds: 3558"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 7629.276334239797,
            "unit": "iter/sec",
            "range": "stddev: 0.0000061911046211953474",
            "extra": "mean: 131.07403064063257 usec\nrounds: 4667"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 11045.471663499378,
            "unit": "iter/sec",
            "range": "stddev: 0.0000042232087801974965",
            "extra": "mean: 90.53483911461906 usec\nrounds: 3027"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 8429.63444004191,
            "unit": "iter/sec",
            "range": "stddev: 0.000006035863417899078",
            "extra": "mean: 118.62910629313461 usec\nrounds: 5212"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 10842.73770920428,
            "unit": "iter/sec",
            "range": "stddev: 0.0000049990240877339555",
            "extra": "mean: 92.22762984952693 usec\nrounds: 7243"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 11014.127067111034,
            "unit": "iter/sec",
            "range": "stddev: 0.000005581361546842411",
            "extra": "mean: 90.79248803893603 usec\nrounds: 7190"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 40411.815477504155,
            "unit": "iter/sec",
            "range": "stddev: 0.000009206298942989888",
            "extra": "mean: 24.745238197889552 usec\nrounds: 12985"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 17.959646488265175,
            "unit": "iter/sec",
            "range": "stddev: 0.00025749376741199183",
            "extra": "mean: 55.680383277777736 msec\nrounds: 18"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 13.881882545770157,
            "unit": "iter/sec",
            "range": "stddev: 0.0003764821324086495",
            "extra": "mean: 72.03633921428779 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 13.753879551892817,
            "unit": "iter/sec",
            "range": "stddev: 0.0008805426033287907",
            "extra": "mean: 72.70675857143009 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 35.85164692841655,
            "unit": "iter/sec",
            "range": "stddev: 0.00017691834414046615",
            "extra": "mean: 27.892721413793264 msec\nrounds: 29"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 5885.46829963142,
            "unit": "iter/sec",
            "range": "stddev: 0.00000756829233445038",
            "extra": "mean: 169.91001379832855 usec\nrounds: 3986"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 115.75408527769667,
            "unit": "iter/sec",
            "range": "stddev: 0.00006154951134207109",
            "extra": "mean: 8.639003950495374 msec\nrounds: 101"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 6172.0632686364615,
            "unit": "iter/sec",
            "range": "stddev: 0.00003209968650830962",
            "extra": "mean: 162.0203741399626 usec\nrounds: 4215"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 8555.444590710431,
            "unit": "iter/sec",
            "range": "stddev: 0.000007775407924086216",
            "extra": "mean: 116.88463286709936 usec\nrounds: 4862"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 6860.798270096341,
            "unit": "iter/sec",
            "range": "stddev: 0.000007054147559454645",
            "extra": "mean: 145.7556337662086 usec\nrounds: 4620"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 8477.68072724564,
            "unit": "iter/sec",
            "range": "stddev: 0.00000637961731937222",
            "extra": "mean: 117.95678938299619 usec\nrounds: 5802"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 8653.227963576357,
            "unit": "iter/sec",
            "range": "stddev: 0.00000763939045119807",
            "extra": "mean: 115.5638108933747 usec\nrounds: 5563"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 18938.93895293383,
            "unit": "iter/sec",
            "range": "stddev: 0.0000037742412592523536",
            "extra": "mean: 52.801268459925524 usec\nrounds: 9480"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 17.771370799297344,
            "unit": "iter/sec",
            "range": "stddev: 0.0005860019935094063",
            "extra": "mean: 56.2702793888887 msec\nrounds: 18"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 13.726144852446348,
            "unit": "iter/sec",
            "range": "stddev: 0.0002644873696803316",
            "extra": "mean: 72.85366799999744 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 13.60222020879157,
            "unit": "iter/sec",
            "range": "stddev: 0.00024961028922494384",
            "extra": "mean: 73.51740999999886 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 35.88901445737311,
            "unit": "iter/sec",
            "range": "stddev: 0.00015024622330681858",
            "extra": "mean: 27.863679599999664 msec\nrounds: 35"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 4786.523539579347,
            "unit": "iter/sec",
            "range": "stddev: 0.0000076060938582358075",
            "extra": "mean: 208.91989598109922 usec\nrounds: 3384"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "893a05a1ee72a72c6563f23076496d51bcde0092",
          "message": "Merge pull request #53 from tchar/development\n\nUpdate benchmark GH Actions",
          "timestamp": "2024-04-04T21:08:46-07:00",
          "tree_id": "969c0e85e08db96819f962f0dd7d4a8448df7351",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/893a05a1ee72a72c6563f23076496d51bcde0092"
        },
        "date": 1712290174020,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 12455.339901326837,
            "unit": "iter/sec",
            "range": "stddev: 0.0000056887815944026824",
            "extra": "mean: 80.28684948962913 usec\nrounds: 3528"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 7547.696239426956,
            "unit": "iter/sec",
            "range": "stddev: 0.000008637064209976912",
            "extra": "mean: 132.4907585411682 usec\nrounds: 4771"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 10858.465671496502,
            "unit": "iter/sec",
            "range": "stddev: 0.0000047659945599393045",
            "extra": "mean: 92.09404258881642 usec\nrounds: 2982"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 8341.802246682439,
            "unit": "iter/sec",
            "range": "stddev: 0.000007152334555808335",
            "extra": "mean: 119.87817145841635 usec\nrounds: 4765"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 10835.808444774453,
            "unit": "iter/sec",
            "range": "stddev: 0.000004693495409155138",
            "extra": "mean: 92.28660741804161 usec\nrounds: 7010"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 10987.483574638409,
            "unit": "iter/sec",
            "range": "stddev: 0.000005421274726771676",
            "extra": "mean: 91.01265027674084 usec\nrounds: 6325"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 42374.75052365262,
            "unit": "iter/sec",
            "range": "stddev: 0.0000041281090052716145",
            "extra": "mean: 23.598958994267658 usec\nrounds: 13681"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 17.3099339343455,
            "unit": "iter/sec",
            "range": "stddev: 0.003160980835788171",
            "extra": "mean: 57.77029558823736 msec\nrounds: 17"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 13.497963234478918,
            "unit": "iter/sec",
            "range": "stddev: 0.0010280980652315787",
            "extra": "mean: 74.08525142857262 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 13.523416492111762,
            "unit": "iter/sec",
            "range": "stddev: 0.0002819024178891634",
            "extra": "mean: 73.94581100000153 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 35.67734085943944,
            "unit": "iter/sec",
            "range": "stddev: 0.0004079006396615573",
            "extra": "mean: 28.02899476000107 msec\nrounds: 25"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 5833.863826853688,
            "unit": "iter/sec",
            "range": "stddev: 0.000006835079106567098",
            "extra": "mean: 171.4129828325662 usec\nrounds: 3728"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 112.2098985538324,
            "unit": "iter/sec",
            "range": "stddev: 0.00006908660558755503",
            "extra": "mean: 8.911869744898244 msec\nrounds: 98"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 6404.196871083788,
            "unit": "iter/sec",
            "range": "stddev: 0.000010310850685408105",
            "extra": "mean: 156.1476044740594 usec\nrounds: 4202"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 8422.884429365824,
            "unit": "iter/sec",
            "range": "stddev: 0.000008144316518722826",
            "extra": "mean: 118.72417440675866 usec\nrounds: 4931"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 6926.3047035643,
            "unit": "iter/sec",
            "range": "stddev: 0.000007808224609848679",
            "extra": "mean: 144.37713077875372 usec\nrounds: 4802"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 8522.317413219283,
            "unit": "iter/sec",
            "range": "stddev: 0.000006744412896900529",
            "extra": "mean: 117.3389761860856 usec\nrounds: 5753"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 8591.889594061144,
            "unit": "iter/sec",
            "range": "stddev: 0.00000691718736160167",
            "extra": "mean: 116.38883263714382 usec\nrounds: 5987"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 19409.708793150716,
            "unit": "iter/sec",
            "range": "stddev: 0.000005346690946585217",
            "extra": "mean: 51.520608096545956 usec\nrounds: 9436"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 17.041541381514897,
            "unit": "iter/sec",
            "range": "stddev: 0.0023934512847214014",
            "extra": "mean: 58.680137999999715 msec\nrounds: 17"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 12.903086916909945,
            "unit": "iter/sec",
            "range": "stddev: 0.0012701473898439717",
            "extra": "mean: 77.50083421428907 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 13.235556103801011,
            "unit": "iter/sec",
            "range": "stddev: 0.0005259765131579843",
            "extra": "mean: 75.55406000000394 msec\nrounds: 13"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 35.13854181812394,
            "unit": "iter/sec",
            "range": "stddev: 0.0004051636159460599",
            "extra": "mean: 28.45877911428342 msec\nrounds: 35"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 4766.972353212308,
            "unit": "iter/sec",
            "range": "stddev: 0.000012592122736677293",
            "extra": "mean: 209.7767567974529 usec\nrounds: 2648"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "tilemachos.charalampous@gmail.com",
            "name": "tchar",
            "username": "tchar"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "037965a44e6f6f496e7ad71ec1651b9edfcde32d",
          "message": "Merge pull request #57 from tchar/development\n\nFix fixerio not connecting on http connection.",
          "timestamp": "2024-05-29T14:57:26-07:00",
          "tree_id": "a656318c803eb40a9df720963b44debe309db541",
          "url": "https://github.com/tchar/ulauncher-albert-calculate-anything/commit/037965a44e6f6f496e7ad71ec1651b9edfcde32d"
        },
        "date": 1717019893792,
        "tool": "pytest",
        "benches": [
          {
            "name": "test/benchmark/test_query.py::test_single_handler[calculator]",
            "value": 12194.662510262677,
            "unit": "iter/sec",
            "range": "stddev: 0.000005460191124449406",
            "extra": "mean: 82.00308939738422 usec\nrounds: 3848"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[percentage]",
            "value": 7364.686069581119,
            "unit": "iter/sec",
            "range": "stddev: 0.00001813030112893565",
            "extra": "mean: 135.7831128919901 usec\nrounds: 4305"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[dec]",
            "value": 10926.058907232427,
            "unit": "iter/sec",
            "range": "stddev: 0.000008777964310477475",
            "extra": "mean: 91.52430977084126 usec\nrounds: 3183"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[hex]",
            "value": 8404.411318103625,
            "unit": "iter/sec",
            "range": "stddev: 0.000005978809782291452",
            "extra": "mean: 118.98513318189674 usec\nrounds: 5286"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[bin]",
            "value": 10907.13993454174,
            "unit": "iter/sec",
            "range": "stddev: 0.000005186360729883258",
            "extra": "mean: 91.68306320459936 usec\nrounds: 7183"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[oct]",
            "value": 11006.37428210556,
            "unit": "iter/sec",
            "range": "stddev: 0.000005359232627008073",
            "extra": "mean: 90.85644140103658 usec\nrounds: 7338"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[color]",
            "value": 41605.81544726824,
            "unit": "iter/sec",
            "range": "stddev: 0.000009914620543219324",
            "extra": "mean: 24.03510156572735 usec\nrounds: 9580"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[currency_no_target]",
            "value": 17.980360304163998,
            "unit": "iter/sec",
            "range": "stddev: 0.0002099066295809844",
            "extra": "mean: 55.6162381111136 msec\nrounds: 18"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[curency_target]",
            "value": 13.707109486352472,
            "unit": "iter/sec",
            "range": "stddev: 0.0006861802498624445",
            "extra": "mean: 72.95484150000065 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[units]",
            "value": 13.632055778384645,
            "unit": "iter/sec",
            "range": "stddev: 0.00022190935284725102",
            "extra": "mean: 73.35650735713882 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_calculation]",
            "value": 35.97429359844102,
            "unit": "iter/sec",
            "range": "stddev: 0.00011474659263375675",
            "extra": "mean: 27.79762713793318 msec\nrounds: 29"
          },
          {
            "name": "test/benchmark/test_query.py::test_single_handler[time_until]",
            "value": 5899.104986074825,
            "unit": "iter/sec",
            "range": "stddev: 0.000020280596314798503",
            "extra": "mean: 169.51724072728953 usec\nrounds: 4017"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[calculator]",
            "value": 112.01070592951044,
            "unit": "iter/sec",
            "range": "stddev: 0.001010918427580674",
            "extra": "mean: 8.927718039999775 msec\nrounds: 100"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[percentage]",
            "value": 6160.479475249346,
            "unit": "iter/sec",
            "range": "stddev: 0.00002919953220879404",
            "extra": "mean: 162.32502746217247 usec\nrounds: 4224"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[dec]",
            "value": 8529.325907445764,
            "unit": "iter/sec",
            "range": "stddev: 0.00000703075248105481",
            "extra": "mean: 117.24255947671546 usec\nrounds: 5044"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[hex]",
            "value": 6790.5229410242355,
            "unit": "iter/sec",
            "range": "stddev: 0.000008772320489856428",
            "extra": "mean: 147.26406326655703 usec\nrounds: 4647"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[bin]",
            "value": 8496.113681589515,
            "unit": "iter/sec",
            "range": "stddev: 0.000007298448647802428",
            "extra": "mean: 117.70087330245241 usec\nrounds: 6038"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[oct]",
            "value": 8495.576075839092,
            "unit": "iter/sec",
            "range": "stddev: 0.000009103613363124489",
            "extra": "mean: 117.70832149263427 usec\nrounds: 6137"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[color]",
            "value": 19800.444171778086,
            "unit": "iter/sec",
            "range": "stddev: 0.00000413773524489074",
            "extra": "mean: 50.50391755480502 usec\nrounds: 9570"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[currency_no_target]",
            "value": 17.603908670812803,
            "unit": "iter/sec",
            "range": "stddev: 0.0005940276245692477",
            "extra": "mean: 56.805566235298365 msec\nrounds: 17"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[curency_target]",
            "value": 13.70376179351512,
            "unit": "iter/sec",
            "range": "stddev: 0.0002525750988771791",
            "extra": "mean: 72.972663642856 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[units]",
            "value": 13.575491028807063,
            "unit": "iter/sec",
            "range": "stddev: 0.0005715835482693455",
            "extra": "mean: 73.66216057143049 msec\nrounds: 14"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_calculation]",
            "value": 35.941581818056356,
            "unit": "iter/sec",
            "range": "stddev: 0.0001111841628456282",
            "extra": "mean: 27.8229268000002 msec\nrounds: 35"
          },
          {
            "name": "test/benchmark/test_query.py::test_multihandler[time_until]",
            "value": 4879.2228561000975,
            "unit": "iter/sec",
            "range": "stddev: 0.00000991458615659542",
            "extra": "mean: 204.95067134508542 usec\nrounds: 3420"
          }
        ]
      }
    ]
  }
}