import datetime

arr = [list(map(int, input().split())) for i in range(3)]
for a in arr:
    time = datetime.timedelta(hours=a[3], minutes=a[4], seconds=a[5])\
           - datetime.timedelta(hours=a[0], minutes=a[1],seconds=a[2])
    print(time.seconds//3600, (time.seconds%3600)//60, time.seconds%60)