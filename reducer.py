#!/usr/bin/env python

from operator import itemgetter
import sys

current_passenger_id = None
passenger_count = 0
max_count = 0
max_passengers = []

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    passenger_id, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently ignore/discard this line
        continue
    # this if condition works as a groupby based on passenger_id
    if current_passenger_id == passenger_id:
        passenger_count += count
    else:
        if current_passenger_id:
            # we have moved onto a new passenger_id, so emit the count for the previous passenger_id
            if passenger_count > max_count:
                max_count = passenger_count
                max_passengers = [current_passenger_id]
            elif passenger_count == max_count:
                max_passengers.append(current_passenger_id)
            print(f"{current_passenger_id}\t{passenger_count}")
        current_passenger_id = passenger_id
        passenger_count = count

# emit the count for the last passenger_id
if current_passenger_id == passenger_id:
    if passenger_count > max_count:
        max_count = passenger_count
        max_passengers = [current_passenger_id]
    elif passenger_count == max_count:
        max_passengers.append(current_passenger_id)
    print(f"{current_passenger_id}\t{passenger_count}")

# output
# print the passenger_id(s) with the maximum count
if max_passengers:
    print("Passenger(s) with the highest count:")
    for passenger_id in sorted(max_passengers):
        print(passenger_id) 