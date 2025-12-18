# You are helping a travel blog store and manage recent trip details. Each trip includes a city name, the date it was visited (in the format dd-mm-yyyy), and a short comment. Your task is to:
# Create a Python module named tripdata.py with a function that returns trip details in dictionary format.
# In your main file, import the function and use it to build a list of trip dictionaries.
# For each trip:
# Convert the date string into a date object.
# Format the date to display as "Month Day, Year" (e.g., “May 15, 2023”).
# Convert the list of trip dictionaries to a JSON string and print it.

import tripdata as td
import json

trips_log = []

trips_log.append(td.log_trip('Alaska', '02-07-2020', 'chilly'))
trips_log.append(td.log_trip('Tokyo', '05-08-2022', 'bustling'))
trips_log.append(td.log_trip('Sydney', '25-02-2024', 'peaceful'))

trips_log_json = json.dumps(trips_log)

print(trips_log_json)