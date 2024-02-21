import datetime

def FiveDays():
    current = datetime.datetime.now()
    past = current.day - 5
    return past

print(FiveDays())