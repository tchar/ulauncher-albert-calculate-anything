window.BENCHMARK_DATA = {
  "lastUpdate": 1627766877579,
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
      }
    ]
  }
}