#conversion of an entered minutes into days and hours and minutes and seconds
import time
print("Current time is :", time.time())

#decompse into days hours and minutes

print("in seconds", int(time.time()))
print("in milliseconds is", float(time.time())-int(time.time()))
print("in minutes is", int(time.time()//60))
print("in hours is", int(time.time())//(60*60))
print("in days is", int(time.time())//(60*60*24))
print("in weeks is", int(time.time())//(60*60*24*7))
print("in years is", int(time.time())//(60*60*24*7*54))
