# IMDb Analyzer
#### It will analyse your ratings and report your:
- Total watch time, movie watch time and series watch time.
- Most watched genres
- Most watched actors
- Most watched directors
- Countries of origin
- Overall rating of movies and series
- Longest movie watched
- Longest series watched
- Series with most episodes

[![N|Solid](https://ia.media-imdb.com/images/M/MV5BMTk3ODA4Mjc0NF5BMl5BcG5nXkFtZTgwNDc1MzQ2OTE@._V1_.png)](https://www.imdb.com)


## How to run?
##### For Analyzing Rating Page
- Type ```python3 IMDb_Analyzer.py <username> <IMDb rating page url> ```
- ```<username>```: any username you want. It just store the data under this name.
- ```<IMDb rating page url>```: The url starts with "https[]()://www[]().imdb.com/user/..." \
e.g. "https://www.imdb.com/user/ur57861148/ratings" \
⚠️ Be sure that the rating page is public.

##### For Analyzing Watchlist Page
- Type ```python3 IMDb_Analyzer.py <username> <IMDb watchlist page url> -wl```
- ```<username>```: any username you want. It just store the data under this name.
- ```<IMDb watchlist page url>```: The url starts with "https[]()://www[]().imdb.com/user/..." \
e.g. "https://www.imdb.com/user/ur57861148/watchlist" \
⚠️ Be sure that the watchlist page is public.

##### If your data is already downloaded
If you already complete the first and second step below. You can directly analyse and print your data. If your rating/watchlist page is updated run the line above.
- Type ```python3 IMDb_Analyzer.py <username> ```
- ```<username>```: any username you want. It just store the data under this name.

## How to make your page public?
- Open IMDb web page.
- Go to account settings.
- Go to privacy settings.
- Pick "public" and save.

## How it works?
- First, it will download the rated pieces. (takes ~10 sec)
- Second, it will download the each pieces data. (takes ~1 second per piece)
- Third, it will analyse and print the data.

## Sample Output
```
==== IMDb ANALYSIS OF MALI ====
662 movies watched.
86 series watched.

=== RATINGS ===
Overall rating: 7.3
Overall movie rating: 7.2
Overall series rating: 8.2

=== TOTAL WATCH TIME ===
190 days 2 hours 31 minutes
=== MOVIES WATCH TIME ===
54 days 5 hours 38 minutes
=== SERIES WATCH TIME ===
135 days 20 hours 53 minutes

=== LONGEST MOVIE YOU WATCHED ===
The Irishman - 0 days 3 hours 29 minutes
=== LONGEST SERIES YOU WATCHED ===
House - 5 days 9 hours 4 minutes
=== SERIES WITH MOST EPISODES ===
Friends - 234 episodes

====== FAVORITE GENRES TOTAL ======
GENRE           PERCENTAGE(%) COUNT
Drama           15.78         372
Action          12.34         291
Comedy          11.49         271
Thriller        9.58          226
Adventure       8.65          204
Crime           7.85          185
Sci-Fi          7.8           184
Mystery         4.79          113
Fantasy         4.79          113
Romance         4.62          109
Family          2.21          52 
Biography       2.12          50 
Animation       1.65          39 
Horror          1.23          29 
War             1.15          27 
History         1.02          24 
Music           0.85          20 
Documentary     0.59          14 
Sport           0.55          13 
Musical         0.47          11 
Western         0.34          8  
Short           0.08          2  
Talk-Show       0.04          1  

====== FAVORITE MOVIE GENRES ======
GENRE           PERCENTAGE(%) COUNT
Drama           15.29         316
Action          13.01         269
Comedy          11.76         243
Thriller        9.58          198
Adventure       9.14          189
Sci-Fi          7.64          158
Crime           7.5           155
Romance         4.89          101
Fantasy         4.79          99 
Mystery         4.16          86 
Family          2.32          48 
Biography       2.23          46 
Animation       1.45          30 
Horror          1.35          28 
War             1.16          24 
Music           0.97          20 
History         0.82          17 
Sport           0.53          11 
Musical         0.53          11 
Western         0.39          8  
Documentary     0.34          7  
Short           0.1           2  
Talk-Show       0.05          1  

====== FAVORITE SERIES GENRES ======
GENRE           PERCENTAGE(%) COUNT
Drama           19.24         56 
Crime           10.31         30 
Thriller        9.62          28 
Comedy          9.62          28 
Mystery         9.28          27 
Sci-Fi          8.93          26 
Action          7.56          22 
Adventure       5.15          15 
Fantasy         4.81          14 
Animation       3.09          9  
Romance         2.75          8  
History         2.41          7  
Documentary     2.41          7  
Biography       1.37          4  
Family          1.37          4  
War             1.03          3  
Sport           0.69          2  
Horror          0.34          1  

====== MOST WATCHED CAST ======
#  ACTOR                          COUNT
1  Samuel L. Jackson              21 
2  Morgan Freeman                 18 
3  Brad Pitt                      16 
4  Robert De Niro                 16 
5  Woody Harrelson                16 
6  Tom Hanks                      15 
7  Johnny Depp                    15 
8  Robert Downey Jr.              15 
9  Paul Bettany                   14 
10 Bradley Cooper                 14 
11 Scarlett Johansson             14 
12 Hugh Jackman                   14 
13 Willem Dafoe                   13 
14 Elizabeth Banks                13 
15 Tom Cruise                     12 
16 Chris Evans                    12 
17 Mark Ruffalo                   12 
18 Michael Caine                  12 
19 Dwayne Johnson                 12 
20 Laurence Fishburne             11 
21 Jonah Hill                     11 
22 Jim Carrey                     11 
23 Chris Hemsworth                11 
24 Ethan Hawke                    11 
25 Stanley Tucci                  11 
26 Leonardo DiCaprio              11 
27 Jennifer Lawrence              11 
28 Al Pacino                      11 
29 Colin Farrell                  11 
30 Jason Statham                  11 

====== MOST WATCHED DIRECTOR ======
#  DIRECTOR                       COUNT
1  Quentin Tarantino              11 
2  Joel Coen                      10 
3  Christopher Nolan              9  
4  Martin Scorsese                9  
5  Michael Bay                    8  
6  Ethan Coen                     8  
7  Guy Ritchie                    7  
8  Ron Howard                     6  
9  Krzysztof Kieslowski           6  
10 Bryan Singer                   6  
11 David Yates                    6  
12 David Fincher                  6  
13 Terry Gilliam                  5  
14 Stanley Kubrick                5  
15 David Leitch                   5  
16 James Cameron                  5  
17 Steven Spielberg               5  
18 Shawn Levy                     5  
19 Fatih Akin                     5  
20 Martin McDonagh                5  
21 Todd Phillips                  5  
22 Doug Liman                     4  
23 Anthony Russo                  4  
24 Joe Russo                      4  
25 Zack Snyder                    4  
26 Richard Linklater              4  
27 Lana Wachowski                 4  
28 Lilly Wachowski                4  
29 Sam Raimi                      4  
30 Peter Farrelly                 4  

====== MOST WATCHED COUNTRY PRODUCTION ======
#  COUNTRY  COUNT
1  US       534
2  GB       94 
3  FR       24 
4  DE       19 
5  ES       8  
6  JP       7  
7  CA       6  
8  AU       6  
9  TR       5  
10 NZ       5  
11 KR       4  
12 IE       4  
13 SE       3  
14 DK       3  
15 HK       3  
16 BE       3  
17 IN       2  
18 PL       2  
19 GR       2  
20 CN       2  
21 IT       2  
22 NO       2  
23 CZ       1  
24 FI       1  
25 SUHH     1  
26 MA       1  
27 CH       1  
28 AR       1  
```



Data courtesy of IMDb.
