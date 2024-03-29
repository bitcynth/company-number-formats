#!/usr/bin/env python3

import csv

country_names = {
    'se': 'Sweden',
    'dk': 'Denmark',
    'uk': 'United Kingdom',
    'de': 'Germany'
}

lines = []

with open('formats.txt') as f:
    reader = csv.reader(f, doublequote=True, quoting=csv.QUOTE_ALL, escapechar='\\')
    for row in reader:
        country = country_names[row[0]]
        format_regex = row[1]
        src = row[2]
        comments = row[3]
        lines.append(f'### {country}\n')
        lines.append(f'- Format: {format_regex}\n')
        lines.append(f'- Source: {src}\n')
        lines.append(f'- Comments: {comments}\n')
        lines.append('\n')

with open('formats.md', 'w+') as f:
    f.writelines(lines)