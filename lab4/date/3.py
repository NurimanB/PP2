import datetime

date = datetime.datetime.now()
micro = date.replace(microsecond=0)

print(date)
print(micro)