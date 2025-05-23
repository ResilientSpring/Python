import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

year = ["1960", "70", "80", "90", "2000", "2010",
        "'11", "'12", "'13", "'14", "'15", "'16", "'17", "'18", "'19", "'20", "'21/08"]

northTW = [(829012 + 898655 + 339456 + 489676 + 464792 + 234442 + 108035), # 1960
           (1240576 + 1769568 + 412787 + 726750 + 587652 + 324040), # 1970
           (2258757 + 2220427 + 442988 + 1052800 + 641937 + 344867), # 1980
           (3048034 + 2719659 + 450943 + 1355175 + 374492 + 352919 + 324426), # 1990
           (3567896 + 2646474 + 465186 + 1732617 + 439713 + 388425 + 368439), # 2000
           (3897367 + 2618772 + 460486 + 2002060 + 513015 + 384134 + 415344), # 2010
           (3916451 + 2650968 + 459061 + 2013305 + 517641 + 379927 + 420052), # 2011
           (3939305 + 2673226 + 458595 + 2030161 + 523993 + 377153 + 425071), # 2012
           (3954929 + 2686516 + 458456 + 2044023 + 530486 + 374914 + 428483), # 2013
           (3966818 + 2702315 + 458777 + 2058328 + 537630 + 373077 + 431988), # 2014
           (3970644 + 2704810 + 458117 + 2105780 + 542042 + 372105 + 434060), # 2015
           (3979208 + 2695704 + 457538 + 2147763 + 547481 + 372100 + 437337), # 2016
           (3986689 + 2683257 + 456607 + 2188017 + 552169 + 371458 + 441132), # 2017
           (3995717 + 2668572 + 455221 + 2220872 + 557010 + 370155 + 445635), # 2018
           (4018696 + 2645041 + 454178 + 2249037 + 563933 + 368893 + 448803), # 2019
           (4030954 + 2602418 + 453087 + 2268807 + 570775 + 367577 + 451412), # 2020
           (4019898 + 2553798 + 451635 + 2272976 + 573858 + 365591 + 452781), # 2021/08
           ]

centralTW = [(298119 + 605437 + 435084 + 880684 + 412942 + 672557), # 1960
             (448140 + 785903 + 524744 + 1050246 + 511040 + 800578), # 1970
             (593427 + 1013176 + 542745 + 1166352 + 524245 + 796276), # 1980
             (761802 + 1258157 + 547609 + 1245288 + 536479 + 753639), # 1990
             (965790 + 1494308 + 559703 + 1310531 + 541537 + 743368), # 2000
             (2648419 + 560968 + 1307286 + 526491 + 717653), # 2010
             (2664394 + 562010 + 1303039 + 522807 + 713556), # 2011
             (2684893 + 563976 + 1299868 + 520196 + 710991), # 2012
             (2701661 + 565554 + 1296013 + 517222 + 707792), # 2013
             (2719835 + 567132 + 1291474 + 514315 + 705356), # 2014
             (2744445 + 563912 + 1289072 + 509490 + 699633), # 2015
             (2767239 + 559189 + 1287146 + 505163 + 694873), # 2016
             (2787070 + 553807 + 1282458 + 501051 + 690373), # 2017
             (2803894 + 548863 + 1277824 + 497031 + 686022), # 2018
             (2815261 + 545459 + 1272802 + 494112 + 681306), # 2019
             (2820787 + 542590 + 1266670 + 490832 + 676873), # 2020
             (2818139 + 539879 + 1259246 + 487185 + 672557), # 2021/08
             ]

southTW = [(337602 + 787203 + 467931 + 617380 + 710273 + 645400), # 1960
           (474835 + 934865 + 828191 + 830661 + 849914 + 828761), # 1970
           (583799 + 962827 + 1202123 + 1000645 + 825967 + 888270), # 1980
           (683251 + 1026983 + 1386723 + 1119263 + 257597 + 552277 + 893282), # 1990
           (734650 + 1107687 + 1490560 + 1234707 + 266183 + 562305 + 907590), # 2000
           (1873794 + 2773483 + 543248 + 873509 + 272390), # 2010
           (1876960 + 2774470 + 537942 + 864529 + 271526), # 2011
           (1881645 + 2778659 + 533723 + 858441 + 271220), # 2012
           (1883208 + 2779877 + 529229 + 852286 + 270872), # 2013
           (1884284 + 2778992 + 524783 + 847917 + 270883), # 2014
           (1885541 + 2778918 + 519839 + 841253 + 270366), # 2015
           (1886033 + 2779371 + 515320 + 835792 + 269874), # 2016
           (1886522 + 2776912 + 511182 + 829939 + 269398), # 2017
           (1883831 + 2773533 + 507068 + 825406 + 268622), # 2018
           (1880906 + 2773198 + 503113 + 819184 + 267690), # 2019
           (1874917 + 2765932 + 499481 + 812658 + 266005), # 2020
           (1867554 + 2753530 + 495662 + 807159 + 264858), # 2021/08
           ]

eastTW = [(252264 + 208272), # 1960
          (335799 + 291761), # 1970
          (355178 + 281218), # 1980
          (352233 + 256803), # 1990
          (353630 + 245312), # 2000
          (338805 + 230673), # 2010
          (336838 + 228290), # 2011
          (335190 + 226252), # 2012
          (333897 + 224821), # 2013
          (333392 + 224470), # 2014
          (331945 + 222452), # 2015
          (330911 + 220802), # 2016
          (329237 + 219540), # 2017
          (327968 + 218919), # 2018
          (326247 + 216781), # 2019
          (324372 + 215261), # 2020
          (322506 + 213956), # 2021/08
          ]

outlyingTW = [(0 + 0 + 96986), # 1960
              (61305 + 16939 + 119153), # 1970
              (51883 + 9058 + 107043), # 1980
              (42754 + 5585 + 95932), # 1990
              (53832 + 6733 + 89496), # 2000
              (107308 + 96918), # 2010 Fujian + Penghu
              (113989 + 97157), # 2011
              (124421 + 98843), # 2012
              (132878 + 100400), # 2013
              (140229 + 101758), # 2014
              (145346 + 102304), # 2015
              (147709 + 103263), # 2016
              (150336 + 104073), # 2017
              (152329 + 104440), # 2018
              (153274 + 105207), # 2019
              (153876 + 105952), # 2020
              (140004 + 13420 + 105645) # 2021/08
              ]

x = range(10, 22)

date = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

south = np.array(southTW)
central = np.array(centralTW)
north = np.array(northTW)
east = np.array(eastTW)
outlying = np.array(outlyingTW)

print(south)
print(central)
print(north)
print(east)
print(outlying)

Total1960 = south[0] + central[0] + north[0] + east[0] + outlying[0]
Total1970 = south[1] + central[1] + north[1] + east[1] + outlying[1]
Total1980 = south[2] + central[2] + north[2] + east[2] + outlying[2]
Total1990 = south[3] + central[3] + north[3] + east[3] + outlying[3]
Total2000 = south[4] + central[4] + north[4] + east[4] + outlying[4]
Total2010 = south[5] + central[5] + north[5] + east[5] + outlying[5]
Total2015 = south[10] + central[10] + north[10] + east[10] + outlying[10]
Total2020 = south[15] + central[15] + north[15] + east[15] + outlying[15]
Total2021 = south[16] + central[16] + north[16] + east[16] + outlying[16]

totality = [Total1960, Total1970, Total1980, Total1990, Total2000, Total2010, Total2020, Total2021]

print(totality)

cm = 1/2.54
figure, axes = plt.subplots(figsize=(18*cm, 15*cm))

p1 = axes.bar(year, south, color='g', label="South Taiwan")
p2 = axes.bar(year, central, color='y', bottom=south, label="Central Taiwan")
p3 = axes.bar(year, north, color='b', bottom=south + central, label="North Taiwan")
p4 = axes.bar(year, east, color='r', bottom=south + central + north, label="Eastern Taiwan")
p5 = axes.bar(year, outlying, color='k', bottom=south + central + north + east, label="Outlying Islands")

axes.yaxis.set_major_locator(ticker.MultipleLocator(5000000))
axes.yaxis.set_minor_locator(ticker.MultipleLocator(1000000))

plt.xticks(rotation=27)
plt.xlabel('Year')
plt.ylabel('Population (Unit: 10 millions)')
plt.title("The composition of Taiwan's population in history")
plt.legend()

axes.bar_label(container=p1, fmt='{:.2f}'.format(p1), label_type='center')
axes.bar_label(container=p2, fmt='{:.2f}'.format(p2), label_type='center')
axes.bar_label(container=p3, fmt='{:.2f}'.format(p3), label_type='center')

plt.show()

