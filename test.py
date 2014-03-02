#!/usr/bin/python
# Filename: Sox.py

### To-do:
###		- Output orderInfo and data together nicely
###		- Add searchability for schedule
### 	- Add ability to input
### 	- Time zone conversions
###		- Possibility to change .csv file to other files i.e other teams    
import csv
import time
import datetime
'''
dateToday = datetime.date.today().strftime("%x")
description = ['START DATE','START TIME','MATCHUP','LOCATION','EXTRA INFO','END DATE','END TIME (~)']

def full(inputDate = dateToday):
	with open('schedule_fixed.csv', 'rb') as f:
	    reader = csv.reader(f)
	    for row in reader:
	    	row.pop(2)
	    	row.pop(6)
	    	if row[0] == inputDate:
				if "" in row:											# Using list comprehension to look fot empty data strings
					emptyElement = row.index("")						# Get the index in the list of the empty string
					cleanRow = row[:emptyElement]+row[emptyElement+1:]
					print 'Game Info'								# Put everything except the empty element into a new list
					for desc, info in zip(description, cleanRow):
						print  desc + ": " + info							# print that list out
				else:
					print 'Game Info'
					for desc, info in zip(description, row):
						print  desc + ": " + info


def outputByDate():
	userDate = input("Please enter a date(mm/dd/yy) (Leave empty for today's date): ")
	if userDate == "":
		full()
	else:
		full(userDate)







if __name__ == "__main__":
    outputByDate()		# Outputs the game information for today's date

'''
night_game_times = ['07:05 PM', '06:10 PM', '08:05 PM', '08:10 PM', '07:10 PM', '07:07 PM', '07:15 PM', '07:08 PM', '10:05 PM', '10:10 PM', '08:15 PM', '09:05 PM']
day_game_times = ['01:05 PM','03:05 PM', '02:05 PM', '01:35 PM', '04:05 PM', '11:05 AM', '01:07 PM', '01:10 PM', '04:10 PM', '01:40 PM', '01:08 PM', '02:10 PM', '12:37 PM', '12:35 PM']



with open('schedule_fixed.csv', 'rb') as f:
	    reader = csv.reader(f)
	    for row in reader:
	    	if row[1] != "03:33 AM" and row[1] not in night_game_times and row[1] not in day_game_times:
	    		print row

