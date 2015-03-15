from census import Census
from us import states
import xml.etree.cElementTree as ET
import urllib2


tree = ET.parse(urllib2.urlopen('http://api.census.gov/data/2013/acs5/variables.xml'))
root = tree.getroot()

print root.tag

for child_of_root in root[0]:
	print child_child_of_root.attrib



c = Census("0ce452c10608a1ce5cbc4c43d1d2520323845086")





x=c.acs.get('NAME,B01001_004E', {'for': 'zip code tabulation area:*'},year=2013)

x=c.acs.get('NAME,B01001_004E', {'for': 'zip code tabulation area:*'},year=2013)


