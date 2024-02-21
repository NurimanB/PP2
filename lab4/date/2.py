import datetime

today = datetime.datetime.now()

print("Yesterday: ", today.day - 1, today.strftime("%B"))
print("Today: ", today.day, today.strftime("%B"))
print("Tomorrow: ", today.day + 1, today.strftime("%B"))