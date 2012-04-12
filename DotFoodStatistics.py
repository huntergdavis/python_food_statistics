#! /usr/bin/env python

import sys
import time

print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
print "-------------------------------"
print "Processing .food file" 
print "---------------------"

# totals for statistics

# total for calories per day
caloPerDay = 0

# total breakfast calories
breakfastCalo = 0
# total lunch calories
lunchCalo = 0
# total dinner calories
dinnerCalo = 0

# total glasses of water per day
waterPerDay = 0

# earliest and latest hours of day
earliestHour = 24
latestHour = 0


fileIN = open(sys.argv[1], "r")
line = fileIN.readline()

while line:
        # split each line into component parts
        line = line.split(',')
        tim  = line[0]
        tim  = tim.split(':')
        hour = int(tim[0])

        # what was our earliest hour
        if hour < earliestHour:
                earliestHour = hour
        elif hour > latestHour:
                latestHour = hour

        # read in another line
        line = fileIN.readline()

# Calculate our time-based statistics
foodHours = latestHour - earliestHour
period = foodHours / 3;
if period < 1:
	period = 1

breakfastEndsAt = earliestHour + period
lunchEndsAt = earliestHour + (2*period)

# calculate our statistics on second pass
fileIN = open(sys.argv[1], "r")
line = fileIN.readline()

while line:
        # split each line into component parts
        line = line.split(',')
        tim  = line[0]
        tim  = tim.split(':')
        hour = int(tim[0])
        min  = tim[1]
        desc = line[1].strip(' ');
        calo = int(line[2])

        # calculate statistics based on component parts
        caloPerDay += calo

        # how many glasses of water today?
        if desc.lower() == 'water':
                waterPerDay += 1

	# how many calories per meal
	if hour < breakfastEndsAt:
		breakfastCalo += calo
	elif hour <= lunchEndsAt:
		lunchCalo += calo
	else:
		dinnerCalo += calo

        # read in another line
        line = fileIN.readline()


# Print out our statistics below
print "Total Daily Calories:" , caloPerDay
print "-------------------------------"
if caloPerDay < 2400:
	caloLeft = 2400 - caloPerDay
	print "You have",caloLeft,"calories left to eat today in your 2400 calorie diet"
else:
	caloMuch = caloPerDay - 2400
	print "You ate",caloMuch,"too many calories today in your 2400 calorie diet"
print "-------------------------------"
print "Your eating day was", foodHours , "hours long"
print breakfastCalo,"breakfast calories between",earliestHour,"and",breakfastEndsAt,"@",(breakfastCalo/period),"per hour"
print lunchCalo,"lunch calories between",breakfastEndsAt,"and",lunchEndsAt,"@",(lunchCalo/period),"per hour"
print dinnerCalo,"dinner calories between",lunchEndsAt,"and",latestHour,"@",(dinnerCalo/period),"per hour"
print "-------------------------------"
print waterPerDay , "glasses of water today with",(8-waterPerDay),"left to go"
print "-------------------------------"
print "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"

