from datetime import datetime

# returns a dictionary
def log_trip(destination, date_visited, remark):
    date_visited_obj = datetime.strptime(date_visited, "%d-%m-%Y")
    return {
        'destination': destination,
        'date_visited': date_visited_obj.strftime("%d %B, %Y"),
        'comment': remark
    }