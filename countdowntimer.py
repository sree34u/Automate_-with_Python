#countdown timer
import time
my_time = int(input("Enter the time in seconds:"))
for x in range(my_time,0,-1):
    sec = x % 60
    min = (x//60)%60
    hrs = x//3600
    print(f"{hrs:02}:{min:02}:{sec:02}",end="\r")
    time.sleep(1)
print("BOOM!!!💥")