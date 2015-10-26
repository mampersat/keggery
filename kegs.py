import json
from datetime import datetime
from pprint import pprint

with open('kegs.json') as data_file:
    dict = json.load(data_file)

counts = {}
counts['Total'] = 0
stats = {}
dates = {}

for keg in dict['objects']:
    counts['Total'] += 1

    name = "%s %s" % (keg['beverage']['producer']['name'], keg['beverage']['name'])
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1

    date_format = '%Y-%m-%dT%H:%M:%S+00:00'
    start_time = datetime.strptime(keg['start_time'],date_format)
    end_time = datetime.strptime(keg['end_time'],date_format)
    delta = end_time - start_time

    print "\"%s\",%s,%s,%s days" % (name, start_time, end_time, delta.days)

    if name not in stats:
        stats[name] = {}
        stats[name]['days'] = []

    stats[name]['days'].append(delta.days)

    if start_time.date() not in dates:
        dates[start_time.date()] = {}

    if name not in dates[start_time.date()]:
        dates[start_time.date()][name] = []


    dates[start_time.date()][name].append(stats[name])

    #pprint(keg)

for name in sorted(counts, key=counts.get, reverse=True):
    if name in stats:
        stats[name]['min'] = min(stats[name]['days'])
        stats[name]['max'] = max(stats[name]['days'])
        stats[name]['avg'] = sum(stats[name]['days'])/float(len(stats[name]['days']))

for name in sorted(counts, key=counts.get, reverse=True):
    print "\n%s: %s kegs" % (name, counts[name])
    if name in stats:
        pprint(stats[name])

print "\n"
pprint(dates)
