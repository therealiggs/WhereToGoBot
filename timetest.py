import time

date = time.ctime(time.time())
day = date[:3]
month = date[4:7]
hour = date[11:13]
workdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
weekend = ['Sat', 'Sun']
