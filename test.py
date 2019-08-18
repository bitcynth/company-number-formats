#!/usr/bin/env python3

import re
import csv

country_formats = {}

with open('formats.txt') as f:
    reader = csv.reader(f, doublequote=True, quoting=csv.QUOTE_ALL, escapechar='\\')
    for row in reader:
        country = row[0]
        country_formats[country] = re.compile(row[1])

# Sweden
assert country_formats['se'].match('555555-1234'), 'SE: 555555-1234 is a valid Swedish organization number'
assert country_formats['se'].match('5555551234'), 'SE: 5555551234 is a valid Swedish organization number (I think)'
assert not country_formats['se'].match('555555-134'), 'SE: 555555-1234 is not a valid Swedish organization number'

# Germany
assert country_formats['de'].match('HRB 151080'), 'DE: HRB 151080 is a valid German company number.'
assert country_formats['de'].match('HRA 12345'), 'DE: HRA 12345 is a valid German company number.'
assert not country_formats['de'].match('HRC 12345'), 'DE: HRC 12345 is not a valid German company number.'