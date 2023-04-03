from datetime import datetime
from datetime import timedelta
import time

#Generate datetime now
datetime_now = datetime.now()
print(datetime_now)

#modify datettime now minus one hour
datetime_now_minus_one_hour = datetime_now-timedelta(hours=1)
print(datetime_now_minus_one_hour)

#delete the decimals from timestamp
datetime_now_minus_one_hour_reformatted = datetime_now_minus_one_hour.strftime("%d/%m/%Y %H:%M:%S")
print(datetime_now_minus_one_hour_reformatted)

#convert datetime epoch using timestamp
epoch = datetime_now.timestamp()
print(epoch)

#turn epoch into custom datetime and format
ts_from_epoch = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch))
print(ts_from_epoch)