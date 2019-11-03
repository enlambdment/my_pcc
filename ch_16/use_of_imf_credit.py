import csv
from country_codes import get_country_code

from pygal.adapters import none_to_zero
from pygal.maps.world import World
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

# Load the file's contents
filename = 'API_DT.DOD.DIMF.CD_DS2_en_csv_v2_427046.csv'
with open(filename) as f:
	imf_reader = csv.reader(f)

	'''
	imf_header_row = next(imf_reader)
	print(imf_header_row) # ['\ufeff"Data Source"', 'World Development Indicators', '']
	'''

	# the headers are actually on row 5
	header_num = 5
	j = 0
	while j < header_num:
		j += 1
		imf_header_row = next(imf_reader)

	# print(imf_header_row[54])	# = 2010
	'''
	['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code', 
	'1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', 
	'1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', 
	'1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', 
	'1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', 
	'2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', 
	'2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '']
	'''



	# # all the countries are present in col 0
	# countries = []
	# for row in imf_reader:
	# 	country = row[0]
	# 	countries.append(country)

	# print(countries)

	# using the 2010 data - so i need row[54] for each row
	# Build a dictionary of population data (using only the 2010 data.)
	cc_imfcredits = {}
	for row in imf_reader:
		country_name = row[0]
		credit_val = row[54]
		'''	
		The value accessed may be blank: ''
		In this case, need the ability to populate
		an "n/a":
		'''
		if credit_val == '':
			imf_credit = None
		else:
			imf_credit = int(float(credit_val))
		code = get_country_code(country_name)
		if code:
			# Create an entry in the dictionary.
			cc_imfcredits[code] = imf_credit

	# (print statement to see what I got)
	print(cc_imfcredits)

	# Group the countries into 3 IMF-credit levels;
	# this time, we need a separate "n/a" level for countries
	# where values were unavailable.
	imf_credit_n, imf_credit_1, imf_credit_2, imf_credit_3 = {}, {}, {}, {}
	for cc, imf_credit in cc_imfcredits.items():
		# none_to_zero needed because pygal skips None's, when plotting
		if imf_credit == None:
			imf_credit_n[cc] = none_to_zero(imf_credit)
		elif imf_credit <  1000000000:		# x < 1B
			imf_credit_1[cc] = imf_credit
		elif imf_credit < 10000000000:		# 1B <= x < 10B
			imf_credit_2[cc] = imf_credit
		else:								# 10B <= x
			imf_credit_3[cc] = imf_credit

	# See how many countries are in each level.
	print(
		len(imf_credit_n),
		len(imf_credit_1),
		len(imf_credit_2),
		len(imf_credit_3))

	# Plot the data.
	wm_style = RS('#336699')
	wm = World(style=wm_style)
	wm.title = 'Use of IMF Credit in 2010 (in USD), by Country'
	wm.add('n/a', imf_credit_n)
	wm.add('0-1bn', imf_credit_1)
	wm.add('1bn-10bn', imf_credit_2)
	wm.add('>10bn', imf_credit_3)

	wm.render_to_file('use_of_imf_credit.svg')



