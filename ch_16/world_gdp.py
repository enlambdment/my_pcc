import json
from pygal.maps.world import World
from country_codes import get_country_code

# Load the file's contents
filename = 'gdp_json.json'
with open(filename) as f:
	gdp_data = json.load(f)

# # Work out what the most recent available year in the file is:
# years = []
# for gdp_dict in gdp_data:	# gdp_data is a list of dicts
# 	yr = gdp_dict['Year']
# 	if yr not in years:
# 		years.append(yr)

# # sort 'years' in place
# years.sort()

# max_yr = years[-1]
# print(max_yr)	# 2016

# Generate the dictionary whose keys are the country codes
# and whose values are the 2016 GDP for that country code's country.
cc_gdps = {}
for gdp_dict in gdp_data:
	# (in this file, the year values are numeric, not string)
	if gdp_dict['Year'] == 2016:
		country_name = gdp_dict['Country Name']
		# (keep only the int part. also, store in millions)
		gdp = int(float(gdp_dict['Value']) / 1000000)
		code = get_country_code(country_name)
		if code:
			cc_gdps[code] = gdp

# Let's further divide into 3 groups:
c_gdps_1, c_gdps_2, c_gdps_3 = {}, {}, {}
for c, gdp in cc_gdps.items():
	if gdp < 100000:		# 0-100k
		c_gdps_1[c] = gdp
	elif gdp < 1000000: 	# 100k-1m
		c_gdps_2[c] = gdp
	else:					# >1m
		c_gdps_3[c] = gdp

# See how many countries are in each level.
print(
	len(c_gdps_1),
	len(c_gdps_2),
	len(c_gdps_3))

# First, do a basic world map of GDPs
wm = World()
wm.title = 'World GDP (millions) in 2016, by Country'
wm.add('0-100k (MM)', c_gdps_1)
wm.add('100k-1m (MM)', c_gdps_2)
wm.add('>1m (MM)', c_gdps_3)

wm.render_to_file('world_gdp.svg')