# Analysis of articles in EPW

## File Structure
- Corpus(processed) in [dataset/final](dataset/final), sorted by year.
	- all.txt contains all articles of that year
	- in_title.txt contains all articles of that year where title satisfies conditions
	- in_abstract.txt contains all articles of that year where abstract satisfies conditions
- [dataset/authors_counts.md](dataset/author_counts.md) contains a table of total articles by an author where abstract satidfies conditions, and author's name.
- [dataset/counts.txt](dataset/counts.txt) contains table to put under 'Corpus' subheading in README.txt

## Conditions

Current conditions for consideration :
- Presence of either of the following words
	+ environmental
	+ ecology
	+ ecological
	+ environment-friendly
	+ wildlife
	+ forest
	+ water
	+ pollution
	+ conservation
	+ smog
	+ biodiversity
	+ emission
	+ renewable
	+ global warming 
	+ biosphere
	+ greenhouse
	+ radiation
	+ fossil fuel
	+ ozone
	+ carbon
	+ pollutant
	+ pollute
	+ contaminated
	+ toxin
	+ weather events
	+ natural resources
- Presnce of both words at the same time
	+ climate, change
	+ mineral, extraction
- Presence of the word 'environment' in the presence of one of the following words
	+ nature
	+ natural
	+ earth
- Presence of the word 'displacement' in the presence of one of the following words
	+ industry
	+ industrial
	+ mining
	+ dams
	+ dam
	+ land

## Corpus

| Year  | Total | in Title | in Abstract | 
| ----- | ----- | -------- | ----------- |
| 1966 | 427 | 1 | 2 |
| 1967 | 1092 | 6 | 2 |
| 1968 | 1194 | 5 | 10 |
| 1969 | 1193 | 5 | 13 |
| 1970 | 1227 | 2 | 15 |
| 1971 | 1247 | 6 | 12 |
| 1972 | 1128 | 5 | 7 |
| 1973 | 985 | 3 | 5 |
| 1974 | 856 | 7 | 11 |
| 1975 | 736 | 5 | 10 |
| 1976 | 746 | 4 | 7 |
| 1977 | 890 | 3 | 9 |
| 1978 | 799 | 3 | 4 |
| 1979 | 780 | 3 | 5 |
| 1980 | 820 | 9 | 12 |
| 1981 | 869 | 7 | 10 |
| 1982 | 920 | 4 | 9 |
| 1983 | 936 | 8 | 18 |
| 1984 | 901 | 8 | 6 |
| 1985 | 967 | 6 | 15 |
| 1986 | 1062 | 10 | 14 |
| 1987 | 1117 | 22 | 24 |
| 1988 | 1207 | 15 | 24 |
| 1989 | 1233 | 10 | 19 |
| 1990 | 1084 | 9 | 26 |
| 1991 | 1137 | 17 | 27 |
| 1992 | 1060 | 23 | 30 |
| 1993 | 1068 | 12 | 24 |
| 1994 | 1299 | 27 | 39 |
| 1995 | 1113 | 22 | 39 |
| 1996 | 1025 | 19 | 47 |
| 1997 | 1010 | 24 | 41 |
| 1998 | 995 | 20 | 36 |
| 1999 | 979 | 16 | 38 |
| 2000 | 870 | 20 | 56 |
| 2001 | 930 | 25 | 45 |
| 2002 | 948 | 36 | 54 |
| 2003 | 929 | 33 | 69 |
| 2004 | 1023 | 29 | 61 |
| 2005 | 1053 | 37 | 71 |
| 2006 | 891 | 42 | 71 |
| 2007 | 761 | 27 | 57 |
| 2008 | 754 | 31 | 54 |
| 2009 | 801 | 27 | 71 |
| 2010 | 896 | 30 | 78 |
| 2011 | 828 | 30 | 64 |
| 2012 | 824 | 27 | 64 |
| 2013 | 850 | 25 | 58 |
| 2014 | 1017 | 37 | 56 |
| 2015 | 1127 | 33 | 77 |
| 2016 | 1079 | 47 | 89 |
| 2017 | 1120 | 49 | 88 |
| 2018 | 948 | 43 | 78 |
| 2019 | 885 | 35 | 67 |
