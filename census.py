from census import Census
from us import states





c = Census("0ce452c10608a1ce5cbc4c43d1d2520323845086")


x=c.acs.get('NAME,B01001_004E', {'for': 'zip code tabulation area:*'},year=2013)




