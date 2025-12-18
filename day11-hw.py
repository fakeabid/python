# You are building a simple activity tracker for a travel blog. Each time a traveler visits a place, the system stores the city name, a visit comment, and the visit date in the format "dd-mm-yyyy".
# Your task is to:
# Create a module called tracker.py that contains a function to return a travel record (as a dictionary).
# In the main file, use the function to create a list of at least 3 travel records.
# Convert the date string of each record into a readable format like "Month Day, Year" (e.g., "June 05, 2022").
# Convert the list of records into a JSON string and print it.
# Parse the JSON back to a Python object and display each record on a separate line.

import tripdata as td
import json

trips_log = []

trips_log.append(td.log_trip('Alaska', '02-07-2020', 'chilly'))
trips_log.append(td.log_trip('Tokyo', '05-08-2022', 'bustling'))
trips_log.append(td.log_trip('Sydney', '25-02-2024', 'peaceful'))

trips_log_json = json.dumps(trips_log)

print(trips_log_json)

trips_log_py = json.loads(trips_log_json)

for trip_log in trips_log_py:
    print(trip_log)