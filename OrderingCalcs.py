"""
OrderingCalcs
=============
This script reads in the 'kegs.json' file and performs various
claculations to generate a keg purchasing selection which
is written to the file 'suggestions'
"""

import json
from datetime import datetime
import numpy

with open('kegs.json') as data_file:
    dict = json.load(data_file)

stats = {}

#Drive through list collecting stats
for keg in dict['objects']:

    name = "%s %s" % (keg['beverage']['producer']['name'], keg['beverage']['name'])
  
    volume = keg['full_volume_ml']
    date_format = '%Y-%m-%dT%H:%M:%S+00:00'
    start_time = datetime.strptime(keg['start_time'],date_format)
    end_time = datetime.strptime(keg['end_time'],date_format)
    delta = end_time - start_time
    seconds = delta.total_seconds()
 
    if seconds > 0: #sainity check
        rate_ml_s = int(volume) / seconds
        rate_l_day = rate_ml_s * 86.4
        rate_l_week = rate_l_day * 7
 
        if 1 < rate_l_week < 1000: #sanity check
            
            if name not in stats:
                stats[name] = {}
                stats[name]['rate'] = []
                stats[name]['date'] = start_time

            stats[name]['rate'].append(rate_l_week)
            if stats[name]['date'] < start_time:
                stats[name]['date'] = start_time

#Average the rates
for name, stat in stats.iteritems():
    stat['rate'] = numpy.mean(stat['rate'])
    #print name, numpy.mean(stat['rate'])

f = open('suggestions', 'w')
s = "Subject: Beer Suggestions for {}\n".format(datetime.today() )
f.write(s)

#Display in order
for w in sorted(stats, key=lambda rate:stats[rate]['rate'], reverse=True):
    s = "{:3.0f} liters/wk {:3d} days ago, {}\n".format(
        stats[w]['rate'], (datetime.today() -stats[w]['date']).days, w)
    f.write(s)
    
f.close()