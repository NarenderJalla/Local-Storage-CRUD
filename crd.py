import threading 
from threading import*
import time
d={} 
#CREATE
def create(key,value,timeout=0):
    if key in d:
        print("this key already exists")
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024):
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    d[key]=l
            else:
                print("limit exceeded!")
        else:
            print("Invalind key_name!")
#READ
def read(key):
    if key not in d:
        print("given key does not exist, Please enter a valid key") 
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                stri=str(key)+":"+str(b[0]) 
                return stri
            else:
                print("time-to-live of",key,"has expired") 
        else:
            stri=str(key)+":"+str(b[0])
            return stri
#DELETE			
def delete(key):
    if key not in d:
        print("given key does not exist, Please enter a valid key") 
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del d[key]
                print("key is deleted")
            else:
                print("time-to-live of",key,"has expired") 
        else:
            del d[key]
            print("key is deleted")
#UPDATE			
def modify(key,value):
    b=d[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in d:
                print("given key does not exist, Please enter a valid key") 
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                d[key]=l
        else:
            print("time-to-live of",key,"has expired") 
    else:
        if key not in d:
            print("given key does not exist, Please enter a valid key") 
     	 else:
            l=[]
            l.append(value)
            l.append(b[1])
            d[key]=l