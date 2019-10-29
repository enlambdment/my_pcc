from country_codes import get_country_code

import json

filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)

# pop_data is a list of dicts
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		code = get_country_code(country_name)
		# We *only* want to see the country names which fail
		# to come back with codes.
		if not code:
			print('ERROR - ' + country_name)

'''
ERROR - Arab World
ERROR - Caribbean small states
ERROR - East Asia & Pacific (all income levels)
ERROR - East Asia & Pacific (developing only)
ERROR - Euro area
ERROR - Europe & Central Asia (all income levels)
ERROR - Europe & Central Asia (developing only)
ERROR - European Union
ERROR - Heavily indebted poor countries (HIPC)
ERROR - High income
ERROR - High income: nonOECD
ERROR - High income: OECD
ERROR - Latin America & Caribbean (all income levels)
ERROR - Latin America & Caribbean (developing only)
ERROR - Least developed countries: UN classification
ERROR - Low & middle income
ERROR - Low income
ERROR - Lower middle income
ERROR - Middle East & North Africa (all income levels)
ERROR - Middle East & North Africa (developing only)
ERROR - Middle income
ERROR - North America
ERROR - OECD members
ERROR - Other small states
ERROR - Pacific island small states
ERROR - Small states
ERROR - South Asia
ERROR - Sub-Saharan Africa (all income levels)
ERROR - Sub-Saharan Africa (developing only)
ERROR - Upper middle income
ERROR - World
ERROR - American Samoa
ERROR - Antigua and Barbuda
ERROR - Aruba
ERROR - Bahamas, The
ERROR - Barbados
ERROR - Bermuda
ERROR - Bolivia				# bo Bolivia, Plurinational State of
ERROR - Cayman Islands
ERROR - Channel Islands
ERROR - Comoros
ERROR - Congo, Dem. Rep.	# cd Congo, the Democratic Republic of the
ERROR - Congo, Rep.			# cg Congo (?)
ERROR - Curacao
ERROR - Dominica
ERROR - Egypt, Arab Rep.	# eg Egypt
ERROR - Faeroe Islands
ERROR - Fiji
ERROR - French Polynesia
ERROR - Gambia, the         # gm Gambia
ERROR - Gibraltar			
ERROR - Grenada
ERROR - Hong Kong SAR, China	hk Hong Kong
ERROR - Iran, Islamic Rep.	# ir Iran, Islamic Republic of
ERROR - Isle of Man
ERROR - Kiribati
ERROR - Korea, Dem. Rep.	# kp Korea, Democratic People's Republic of
ERROR - Korea, Rep.			# kr Korea, Republic of
ERROR - Kosovo
ERROR - Kyrgyz Republic		# kg Kyrgyzstan
ERROR - Lao PDR				# la Lao People's Democratic Republic
ERROR - Libya				# ly Libyan Arab Jamahiriya
ERROR - Macao SAR, China	# mo Macao
ERROR - Macedonia, FYR		# mk Macedonia, the former Yugoslav Republic of
ERROR - Marshall Islands
ERROR - Micronesia, Fed. Sts.
ERROR - Moldova				# md Moldova, Republic of
ERROR - New Caledonia
ERROR - Northern Mariana Islands
ERROR - Palau
ERROR - Qatar
ERROR - Samoa
ERROR - Sint Maarten (Dutch part)
ERROR - Slovak Republic		# sk Slovakia
ERROR - Solomon Islands
ERROR - St. Kitts and Nevis
ERROR - St. Lucia
ERROR - St. Martin (French part)
ERROR - St. Vincent and the Grenadines
ERROR - Tanzania			# tz Tanzania, United Republic of
ERROR - Tonga
ERROR - Trinidad and Tobago
ERROR - Turks and Caicos Islands
ERROR - Tuvalu
ERROR - Vanuatu
ERROR - Venezuela, RB 		# ve Venezuela, Bolivarian Republic of
ERROR - Vietnam				# vn Viet Nam
ERROR - Virgin Islands (U.S.)
ERROR - West Bank and Gaza
ERROR - Yemen, Rep.			# ye Yemen
'''