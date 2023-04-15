#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into fields
    passenger_id, flight_id, from_airport, to_airport, departure_time, flight_time = line.split(',')
    # emit (passenger_id, 1) key-value pair
    print(f"{passenger_id}\t1")
