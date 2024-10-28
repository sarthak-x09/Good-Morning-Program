import time
localsamay = time.localtime()
samay = int(time.strftime("%H", localsamay))
if(samay >= 12):
    print("Good Afternoon Sir")
elif (samay >= 16):
    print("Good Evening Sir")
elif (samay < 12):
    print("Good Morning Sir")
