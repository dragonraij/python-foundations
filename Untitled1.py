import time
import webbrowser
i=0
while i< 3:
    time.sleep(10)
    webbrowser.open("www.google.com")
    i=i+1
    print("Current time is "+time.ctime())