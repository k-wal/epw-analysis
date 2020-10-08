# Analysis of articles in EPW

## File Structure
- Corpus(processed) in dataset/final, sorted by year.
	- all.txt contains all articles of that year
	- in_title.txt contains all articles of that year where title satisfies conditions
	- in_abstract.txt contains all articles of that year where abstract satisfies conditions
- dataset/authors_counts.md contains a table of total articles by an author where abstract satidfies conditions, and author's name.
- dataset/counts.txt contains table to put under 'Corpus' subheading in README.txt

## Conditions

Current conditions for consideration :
- Presence of either of the following words
	+ environmental
	+ ecology
	+ ecological
	+ environment-friendly
	+ climate change
	+ wildlife
	+ forest
	+ water
	+ pollution
	+ conservation
	+ mineral extraction
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
| 1966 | 427 | 0 | 2 |
| 1967 | 1092 | 6 | 2 |
| 1968 | 1194 | 3 | 8 |
| 1969 | 1193 | 4 | 13 |
| 1970 | 1227 | 2 | 14 |
| 1971 | 1247 | 6 | 12 |
| 1972 | 1128 | 5 | 5 |
| 1973 | 985 | 3 | 5 |
| 1974 | 856 | 7 | 7 |
| 1975 | 736 | 5 | 10 |
| 1976 | 746 | 4 | 6 |
| 1977 | 890 | 3 | 9 |
| 1978 | 799 | 3 | 3 |
| 1979 | 780 | 2 | 5 |
| 1980 | 820 | 9 | 10 |
| 1981 | 869 | 6 | 7 |
| 1982 | 920 | 4 | 9 |
| 1983 | 936 | 7 | 16 |
| 1984 | 901 | 6 | 5 |
| 1985 | 967 | 5 | 14 |
| 1986 | 1062 | 10 | 11 |
| 1987 | 1117 | 21 | 20 |
| 1988 | 1207 | 12 | 23 |
| 1989 | 1233 | 9 | 18 |
| 1990 | 1084 | 7 | 24 |
| 1991 | 1137 | 16 | 26 |
| 1992 | 1060 | 21 | 29 |
| 1993 | 1068 | 10 | 24 |
| 1994 | 1299 | 25 | 36 |
| 1995 | 1113 | 20 | 37 |
| 1996 | 1025 | 18 | 44 |
| 1997 | 1010 | 18 | 34 |
| 1998 | 995 | 19 | 33 |
| 1999 | 979 | 14 | 32 |
| 2000 | 870 | 19 | 53 |
| 2001 | 930 | 24 | 43 |
| 2002 | 948 | 35 | 53 |
| 2003 | 929 | 29 | 64 |
| 2004 | 1023 | 29 | 55 |
| 2005 | 1053 | 36 | 66 |
| 2006 | 891 | 41 | 68 |
| 2007 | 761 | 23 | 51 |
| 2008 | 754 | 28 | 49 |
| 2009 | 801 | 23 | 67 |
| 2010 | 896 | 28 | 67 |
| 2011 | 828 | 27 | 58 |
| 2012 | 824 | 25 | 56 |
| 2013 | 850 | 23 | 53 |
| 2014 | 1017 | 33 | 51 |
| 2015 | 1127 | 32 | 69 |
| 2016 | 1079 | 44 | 81 |
| 2017 | 1120 | 47 | 84 |
| 2018 | 948 | 39 | 69 |
| 2019 | 885 | 33 | 66 |
