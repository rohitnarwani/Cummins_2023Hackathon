
from . import messagebox
from . import plyer1
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from . import forms
from . import drowsi
import threading
import ctypes
from datetime import datetime,time,timedelta
# getting the library in which GetTickCount64() resides
lib = ctypes.windll.kernel32

# Create your views here.
def home(request):
    return render(request , "wocv/index.html")
def final(request):
     return render(request,"wocv/final.html")

def employees(request):
    if request.method == 'POST':
        endtime= request.POST['endtime']
        endtime=datetime.fromisoformat(endtime)
        now = datetime.now()
        t1=threading.Thread(target=tracking,args=(now,endtime))
        t1.start()
        return redirect('/final')

    return render(request , "wocv/main.html")
def tracking(start_time,endtime):
        print(endtime,"endtime")
        first_time = start_time
        time_change = timedelta(seconds=30)
        time_water=timedelta(minutes=1)
        time_detect=timedelta(minutes=2)
        i=1 
        j=1
        plyer1.notifi1()
        while(1):
            now = datetime.now()
            if(now-time_change>=first_time):
                print(now,first_time)
                print("alert")
                messagebox.actmind()

                i+=1
                time_change=timedelta(seconds=30*i)
            if(now-time_water>=first_time):
                 plyer1.waterremind()
                 j+=1
                 time_water=timedelta(minutes=i)
            if(now-time_detect>=first_time):
                 drowsi.drowsy1()
                 print(drowsi)
                 messagebox.mesgbox()
                 if(drowsi):
                        pass
                 time_detect=timedelta(minutes=2*i)
            
            if(now>=endtime):
                print("Office Finished")
                break
    
    
