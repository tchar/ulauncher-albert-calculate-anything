window.BENCHMARK_DATA = {
  "lastUpdate": 1628194296906,
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
      }
    ]
  }
}