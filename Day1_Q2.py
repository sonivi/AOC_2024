from collections import Counter
 
def calculate_similarity_score(input_data):
    # Parse the input into two lists
    left_list = []
    right_list = []
 
    for line in input_data.strip().split("\n"):
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
 
    # Count occurrences in the right list
    right_counts = Counter(right_list)
 
    # Calculate the similarity score
    similarity_score = 0
    for number in left_list:
        similarity_score += number * right_counts.get(number, 0)
 
    return similarity_score
 
 
# Example Input
input_data = """
37033   48086
80098   34930
88073   69183
54342   63061
98409   87908
81400   96222
42062   53621
55208   48086
10847   20622
53237   11766
12609   19507
31524   33054
83455   96879
53344   76641
94982   66380
69183   70224
35580   12846
87598   24335
82193   11774
69512   57198
59322   57031
68842   58244
44042   39233
16249   57139
85264   31175
10891   68793
40085   98617
91566   98409
87478   49199
39821   33343
74610   62695
68536   31524
68470   52968
49918   78866
22935   44471
76024   92757
65243   98409
93508   26529
89938   19767
74104   28327
95395   51124
57361   30769
17053   38420
89386   27077
66052   49634
31107   86173
20356   70681
32859   77448
61081   68078
66997   11420
47491   52799
52909   18865
98231   14451
78232   81629
13844   65959
42821   44935
42441   17048
43148   63037
64953   17930
94799   43046
36346   50323
62122   36926
12807   35501
62695   49155
70681   87913
44566   67881
84508   75693
53457   53621
81188   75898
18550   78193
78314   72664
28118   75012
55363   82133
55936   96958
71769   62301
64882   55809
22070   52069
80402   18865
87887   59381
19262   90572
85007   46788
36926   95926
19398   39233
38479   40232
32794   85776
82010   48505
44551   59594
52215   96042
47295   62695
23560   64868
41516   29134
78567   96879
56100   44280
37923   53621
23366   20622
88384   38143
32427   93236
28815   77641
64098   70832
63820   52069
65685   41926
77989   34282
19213   73228
90916   59042
34392   59594
53405   20622
61530   85362
67067   58244
15915   52074
84869   45493
16808   52099
83066   30481
60279   34507
18216   69308
43386   89121
48876   20622
81226   81863
13439   96879
33538   20803
57046   57031
97890   31524
49650   81758
83353   53621
97124   11654
42320   55708
15216   67981
41159   54382
23511   59594
69428   62695
75545   54382
40455   50323
14796   17517
64841   54382
45297   98409
85055   15951
54382   89121
75123   48014
77380   73118
89593   29398
65102   84571
29684   50323
78501   98409
22658   48086
69048   37242
78675   43046
42018   64394
20090   98409
73590   59594
77407   70588
54617   60692
31801   30470
94282   59594
23846   84393
80158   75833
41973   18865
10733   72754
21476   89327
53199   42757
57875   22438
80198   27009
78998   36146
46245   29134
50181   37209
65481   89603
11531   16038
33594   38324
57846   75210
92753   46215
16725   78130
67071   32249
58481   81278
79423   50340
97039   64868
87562   54382
43046   90102
39144   51352
59594   15951
84863   15951
17517   18865
49574   65630
32557   63961
46236   13439
97729   58376
71110   50323
96590   53621
94510   30481
71029   34573
86457   21887
28954   17350
35852   31524
93863   39233
47572   73683
97380   18865
30754   30481
60704   89447
92001   69183
32801   66142
81487   31524
18073   52639
35906   59208
43812   17762
98364   54382
63099   93285
23874   11420
23929   15951
63965   58244
13509   50297
67586   72452
38100   76429
57896   36516
31621   59594
68378   13399
98229   89945
37332   42762
39317   13399
29751   70681
23350   49329
94426   54530
51125   98409
13568   25793
40634   93771
76318   20622
56797   62352
77125   92452
92723   78193
52702   97941
71042   48086
75241   48086
82106   86471
43549   51785
57031   93563
45097   85133
39233   38284
44072   23577
78219   48086
10218   75355
34441   52069
27486   64929
94555   15951
36126   33020
50417   20622
97392   18353
59162   90002
43315   19287
28705   67881
29116   18865
54164   39121
41481   91282
81138   85776
85885   67495
96203   95531
11050   37542
12902   95734
23499   10033
86109   18865
13588   75493
11234   42933
58393   31524
74806   69463
81423   40663
56077   58244
55377   18865
19426   52069
46626   54382
37701   33145
57512   74160
27195   70681
14778   22306
24054   25503
23289   29807
37933   36926
61780   11400
50323   83188
33579   91321
63956   13439
99407   96879
91416   76077
88001   95578
62066   33499
24116   98790
47745   19497
64915   31524
15961   93427
68594   81210
34351   59202
40327   98303
72705   67448
12525   23334
43151   82488
35068   49777
68599   69183
94043   78193
13678   98199
81582   69183
73934   36346
55739   43046
85642   75087
91889   62893
67778   92891
35695   73450
55718   78193
63959   34907
38017   98409
66723   17517
74248   43974
88967   64011
83130   20258
99204   59594
70476   66058
61286   50220
48510   31524
79991   38603
19872   59594
87662   98303
19340   52069
43964   15951
90112   80030
43191   15951
98554   72878
21344   54382
19604   98409
33237   10812
51468   40519
38791   85794
74239   29333
66680   95424
24080   97635
90972   18626
87429   97643
91221   28641
72127   62326
24113   72380
81008   23132
99596   15951
33037   17517
90429   94990
95722   78709
44529   11954
40869   74940
85270   98409
61916   88339
94503   31524
57636   10919
34500   53621
67881   27216
93866   48086
95505   41472
60258   13439
73971   96879
78155   84381
52246   30293
42752   11420
91033   69183
91316   64187
99667   30481
26343   66657
47584   85776
88747   93445
48170   29134
82355   98303
72601   67372
59362   16525
23719   70681
73439   89676
41361   45165
91378   13419
23936   33954
98014   13399
15650   65042
64527   77524
57963   13032
24657   39982
71342   37777
48315   75222
54519   66142
76974   53621
85608   27055
20837   93663
54927   24425
13139   20622
15005   11420
84490   76060
89171   70473
17832   96879
18470   54382
45260   83667
17276   27108
52681   32349
61355   13439
47525   11420
36905   70681
59209   75250
95591   47770
14642   68650
40203   73611
52858   61463
48675   42759
98405   64868
80951   82870
53621   79358
25327   78193
87475   48086
51819   24117
27015   17111
98465   66142
72427   73936
71733   96879
89121   60064
22901   30122
10856   48527
36754   64868
50122   50538
52355   73026
40825   40951
80386   16069
83603   36182
58594   13717
31497   71550
40053   48086
38188   39233
18994   96329
79861   50323
23321   85776
61404   10062
95531   53621
34909   98952
23995   93754
13871   98442
54796   30148
35319   93955
64282   26287
83133   82959
56071   47244
67009   47394
92507   47341
85776   46164
30709   57965
59236   35175
20724   66427
33428   94891
11751   44280
36923   59594
76810   42646
35667   96679
42268   98409
57684   38466
40804   66142
76968   66990
99714   52069
57148   28084
16707   54930
16915   32950
18508   45796
84647   62099
24717   15951
97165   52069
88312   54080
44527   62695
13285   75521
15532   45721
83771   98303
69300   69450
33929   98294
63656   85776
58244   89121
98243   65914
79896   43809
61035   98303
66387   66433
35297   91503
60092   18889
93026   91504
73054   33258
64475   70681
54041   12197
23521   20243
91854   58244
95611   62695
70144   14591
46105   93466
13551   22559
98318   32023
72900   96879
17675   99283
21850   56050
50581   44825
49017   89297
26268   73032
76642   24749
57925   72795
63723   27403
32025   20622
15951   48086
85672   58244
24553   57031
49464   62695
67767   85776
58337   85776
74953   59594
69307   20622
54291   39233
52996   15951
65777   98303
66534   75432
23911   73020
35599   53621
80629   79286
59328   98303
88093   18865
25517   18865
19457   58244
12955   55118
90990   19917
45463   45747
77714   64511
56882   42004
25038   31524
85217   20622
99959   36346
79460   26413
86151   41237
48086   30398
31177   36926
15315   83228
73930   58503
31633   37808
25732   52462
72722   22108
21950   54382
32065   92741
45641   26363
97024   96879
44240   57089
59276   20622
42165   57163
72746   70681
70771   36926
38232   78721
71104   91763
93422   84268
82725   93116
38739   25006
93983   67881
66261   37918
45318   60554
29927   61543
75323   14960
76535   13439
95437   57747
70363   58272
79957   15661
67064   32990
20092   96879
12567   69183
52045   86433
56000   76650
72348   62567
68077   58244
51346   64868
90427   68815
55238   84016
63141   23115
44187   48086
73242   46883
37067   74850
22831   78193
33348   54605
36004   75163
69742   62695
97982   85776
81147   69183
30121   44534
89460   70312
65414   48502
41797   70681
97715   59594
11895   62739
53566   36346
88592   13685
44867   18865
38494   93238
90302   57031
29959   77575
14477   64868
95081   94031
80618   98409
31630   59639
11480   15771
57197   12243
69484   97473
15324   54382
85375   28233
70310   39233
29134   66142
17677   70681
10533   50323
32670   13399
65046   89121
27250   57826
50565   18865
10750   15951
86359   36926
17412   20622
56284   58734
24630   32786
51890   31524
62891   15178
90991   54171
18599   35575
18865   35025
26344   13399
18002   85776
61277   96879
37141   57031
86471   75319
55111   37439
41036   72230
57319   96257
44621   10761
63452   89121
64428   44023
94409   64868
97533   68365
44422   53621
82027   13439
12954   54919
47142   25744
85528   66521
81778   62695
67727   32777
66391   39630
24686   62695
81899   59594
23924   99354
28401   50030
25839   98409
80138   30520
54999   14824
93520   54172
75113   64190
60779   18923
10355   41820
32709   20332
54938   70681
49081   57031
59825   82761
38481   66142
17642   85776
93320   64868
86185   89121
90785   20622
78441   70270
15058   58554
13159   99885
71048   82807
18657   62823
25375   54382
86493   57461
68185   49281
36666   48086
57255   76149
69221   70681
13455   45466
44124   44225
12571   79912
22123   18865
41374   19055
14066   88458
42576   53164
54786   71358
48734   32761
72366   76013
38118   52069
28516   98303
84839   92356
33967   51873
39686   42909
97775   58244
97891   20622
95436   31524
40160   26365
45663   83105
73959   62695
83007   21673
34716   18865
42940   60190
30448   98303
54016   56062
98158   11420
76233   67511
71248   14271
33181   52757
73295   59594
42588   69183
28020   18683
65760   13399
51626   35859
23978   66142
26564   53338
34634   15951
47149   30575
28625   20989
78780   85370
98473   26689
66142   58244
37914   48086
91597   96879
42550   89165
79970   74953
73019   69183
21908   27351
96153   79995
58843   53621
91807   12526
92395   71081
21579   48086
79524   98282
34060   85776
27571   41575
62300   37578
88423   72261
66840   95531
39956   44045
77892   67881
10204   80385
55417   42304
34672   18865
40908   48086
97799   20148
25065   53621
62503   98409
96437   67881
74378   31222
61972   70681
89255   70681
80855   18865
54885   38371
64050   15556
21358   10464
25723   92679
95201   53621
61421   49146
86050   89893
93226   78113
42266   75153
11881   17646
69987   30481
71028   85327
24743   32122
48190   85312
45256   64868
19567   11420
89596   50323
49101   86202
68965   39233
50874   13439
17159   24728
50369   35203
78343   56136
55351   73651
48074   59594
11532   42633
82644   92794
95771   34677
59150   28294
38484   64868
48890   64382
68966   28298
51394   66142
69899   91877
20622   27299
47091   19931
81236   72834
78009   41686
48131   52069
34760   83087
54872   88748
99903   44280
75164   77528
98303   81353
89179   47262
93330   85776
64653   62695
75680   59594
28615   46658
24345   58244
79606   36346
48948   97944
98505   89997
56392   90073
76055   90144
82417   29331
62098   20173
17254   59594
48731   89213
91622   10612
96177   62695
52069   59594
13399   98409
32967   62695
80796   97619
77193   28072
55904   13399
84250   81410
53217   64868
10500   80320
67277   53621
72249   93147
65047   54902
17107   63592
76194   12779
27559   83996
79679   50585
61580   69975
65266   31524
88473   84465
79876   62695
65441   16454
80352   69183
82496   39233
52114   67176
51220   91015
50000   53335
42335   68722
53404   43046
99871   66142
32080   89121
31786   17440
92788   21713
56249   44735
61367   48207
62686   18865
96072   82701
20243   17083
12117   35213
19815   26817
79102   94396
44142   48396
69916   20622
55931   67881
31342   63716
39653   62400
77941   81859
11114   80231
52176   70681
57866   95927
16866   98409
58810   52495
30481   13399
47222   62695
44280   37037
14384   62695
87330   99383
36889   98303
87970   58244
53739   41685
40509   84262
87526   11810
34019   89121
66761   29134
82984   80221
83300   43046
31073   13399
38528   10345
42647   69040
78499   66142
65835   13399
11888   52069
16021   52069
77506   18865
37718   48194
30087   28445
11104   52070
16603   52069
32201   52069
80129   87617
30931   20174
55331   36346
88876   58551
78652   57031
81997   26780
44346   20622
31652   15430
97390   65924
84105   42911
51646   52069
73632   39233
22774   58432
67720   10485
94677   22142
15291   23118
97553   91441
13036   16132
66370   89121
47010   64499
14579   36926
71383   38714
36373   44545
80180   48086
30591   52069
90029   94693
99057   45433
96879   59594
30934   96879
40909   64001
83174   44065
99020   88105
11420   41090
52834   64349
29417   40615
23216   84918
61489   62695
69615   63436
64767   37178
28368   31524
29166   83509
88181   26952
92376   46034
56924   13399
16465   18865
29356   68035
54993   36926
18295   67097
82237   43901
78347   15951
31212   15951
36998   54208
72196   14327
10596   59594
40421   66142
10375   71778
53059   29196
33476   68714
88721   27093
82358   83161
45486   51031
61135   70681
25501   16321
12221   62619
98976   89121
83483   36480
24673   41710
36211   39233
65135   61232
64780   43227
80301   70681
45462   68721
67491   81035
79555   81549
58586   95531
52960   12428
49575   44280
65496   13439
66682   98303
93266   13399
30310   69183
21871   50286
53042   52803
22862   21603
78193   85776
87258   87131
76615   84237
88433   86471
11880   74358
27516   54382
90874   52601
95239   98303
35641   18223
93150   13439
23926   14395
68954   80564
67708   28415
54348   11420
32006   70313
89793   59594
47625   20243
42304   15951
48069   91705
44492   92921
18981   42304
13501   71398
64868   18580
38280   87499
40480   96879
76161   87470
53440   26034
99706   54382
22102   95972
23433   56267
70986   83482
49356   98303
25792   48432
87046   20622
44220   54382
19076   22755
66811   96311
90099   15951
33595   70999
19173   20622
12964   56430
"""
 
# Calculate and print the result
result = calculate_similarity_score(input_data)
print("Similarity Score:", result)# your code goes here