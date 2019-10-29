import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sanfrancisco_2014_weather_stations.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	# print(header_row)

	# for index, header_item in enumerate(header_row):
	# 	print(index, header_item)

	'''
	0 STATION
	1 LATITUDE
	2 LONGITUDE
	3 ELEVATION
	4 DATE
	5 TAVG
	6 TMAX
	7 TMIN
	8 TOBS
	'''

	# I would like to select just one station, but first
	# I need to know what all the distinct available stations are ...
	stations = []
	for row in reader:
		station = row[0]
		if station in stations:
			continue
		else:
			stations.append(station)

	print(stations)
	'''
	['USC00046144', 'US1CANP0008', 'US1CACC0001', 'USC00040693', 
	'US1CACC0016', 'US1CAAL0003', 'US1CAAL0004', 'US1CASM0016', 
	'USR0000CBIR', 'USW00093227', 'US1CAMR0034', 'US1CAAL0016', 
	'US1CASO0002', 'US1CASF0003', 'USW00023230', 'USW00023234', 
	'USR0000CWOO', 'US1CAMR0008', 'USR0000CTRA']
	'''

	# Date ranges per station
	d_ranges_per_station = []
	for station in stations:
		station_dict = {}
		station_dict['station'] = station

		dates = []
		f.seek(1) # go back to the part of file *after* header row
		for row in reader:
			if row[0] == station:
				current_date = datetime.strptime(row[4], "%Y-%m-%d")
				dates.append(current_date)
			else:
				continue
		
		# As you add the min date / max date, convert them from datetime object 
		# to date object ... (how do I get it to look simpler?)
		dates.sort()
		station_dict['min_date'] = str(dates[0].date())
		station_dict['max_date'] = str(dates[-1].date())
		station_dict['num_dates'] = len(dates)

		d_ranges_per_station.append(station_dict)

	print(d_ranges_per_station)
	'''
	[{'station': 'USC00046144', 'min_date': '2014-01-01', 'max_date': '2014-12-31', 'num_dates': 365}, 
	{'station': 'US1CANP0008', 'min_date': '2014-01-02', 'max_date': '2014-12-25', 'num_dates': 106}, 
	{'station': 'US1CACC0001', 'min_date': '2014-01-01', 'max_date': '2014-12-31', 'num_dates': 365}, 
	{'station': 'USC00040693', 'min_date': '2014-01-01', 'max_date': '2014-12-31', 'num_dates': 365}, 
	{'station': 'US1CACC0016', 'min_date': '2014-01-01', 'max_date': '2014-12-31', 'num_dates': 361}, 
	{'station': 'US1CAAL0003', 'min_date': '2014-01-01', 'max_date': '2014-12-31', 'num_dates': 361}, 
	{'station': 'US1CAAL0004', 'min_date': '2014-01-01', 'max_date': '2014-12-31', 'num_dates': 323}, 
	{'station': 'US1CASM0016', 'min_date': '2014-01-01', 'max_date': '2014-12-31', 'num_dates': 184}, 
	{'station': 'USR0000CBIR', 'min_date': '2014-01-01', 'max_date': '2014-12-31', 'num_dates': 365}, 
	{'station': 'USW00093227', 'min_date': '2014-01-01', 'max_date': '2014-12-31', 'num_dates': 365}, 
	{'station': 'US1CAMR0034', 'min_date': '2014-10-31', 'max_date': '2014-12-31', 'num_dates': 61}, 
	{'station': 'US1CAAL0016', 'min_date': '2014-01-01', 'max_date': '2014-12-31', 'num_dates': 348}, 
	{'station': 'US1CASO0002', 'min_date': '2014-01-30', 'max_date': '2014-10-15', 'num_dates': 42}, 
	{'station': 'US1CASF0003', 'min_date': '2014-01-01', 'max_date': '2014-12-31', 'num_dates': 151}, 
	{'station': 'USW00023230', 'min_date': '2014-01-01', 'max_date': '2014-12-31', 'num_dates': 365}, 
	{'station': 'USW00023234', 'min_date': '2014-01-01', 'max_date': '2014-12-31', 'num_dates': 365}, 
	{'station': 'USR0000CWOO', 'min_date': '2014-01-01', 'max_date': '2014-12-31', 'num_dates': 365}, 
	{'station': 'US1CAMR0008', 'min_date': '2014-12-12', 'max_date': '2014-12-20', 'num_dates': 6}, 
	{'station': 'USR0000CTRA', 'min_date': '2014-01-01', 'max_date': '2014-12-31', 'num_dates': 365}]
	'''

	# just going to pick any station that has a full year's worth of data - USC00040693
	f.seek(1) # go back to the part of file *after* header row

	# get dates, highs, low
	dates, highs, lows = [], [], []
	for row in reader:
		# only work on the rows for station: USC00040693
		if row[0] == 'USC00040693':
			try:
				current_date = datetime.strptime(row[4], "%Y-%m-%d")
				high = int(row[6])
				low = int(row[7])
			except ValueError:
				print(str(current_date) + " missing data")
			else:
				dates.append(current_date)
				highs.append(high)
				lows.append(low)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='violet', alpha=0.1) # gray works?

# Format plot.
title = "Daily high and low temperatures - 2014\nfrom a San Francisco weather station"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()





