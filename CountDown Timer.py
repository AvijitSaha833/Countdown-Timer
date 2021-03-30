import time

def countdown(t):
    hour,min,sec=map(int,t)
    temp=hour*3600+min*60+sec
    while temp>0:
        min,sec=divmod(temp,60)   #divmod() mod a number and give quotient and remender
        if min>60:
           hour,min=divmod(min,60)
        timer="{:02d}:{:02d}:{:02d}".format(hour,min,sec)  # look "https://pyformat.info/#number"
        time.sleep(1)
        print(timer,end="\r")
        temp-=1
    print("CountDown Completed!!")

if __name__=="__main__":
    f=0
    t=list(map(int,input("Enter the time in HH:MM:SS format\n").split(":")[:3]))
    countdown(t)
