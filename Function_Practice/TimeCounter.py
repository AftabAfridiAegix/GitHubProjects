import time
my_time = int(input("Enter the time in seconds: "))

for x in range(my_time,0,-1): 
    seconds= x % 60 # 3665 % 60 = 5 , seconds = 5

    minutes = int(x/60)  % 60 # 3665 / 60 = 61.08 , 61 % 60 = 1 ,minutes = 1

    hours = int (x/3600) #   1 hour = 3600 seconds, 3665 / 3600 = 1.01,hours = 1
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    
print("TIME'S UP! ")





