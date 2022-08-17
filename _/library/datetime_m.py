from datetime import datetime, timedelta

dt1 = datetime(year=2018, month=1, day=1)
dt2 = datetime.now()

duration = dt2 - dt1
print(duration.days)