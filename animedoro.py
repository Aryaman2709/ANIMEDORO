import winsound
import threading
import webbrowser
import os
import sys

z = input("Enter how long is your anime(excluding the op and ending)(p.s. enter in minutes)(p.p.s. yes i know op and end can't be skipped but you have to): ")
y = input("do you want us to redirect you to your anime after the study session(y/n): ")

def restart():
        print("Program is now restarting")

        os.execv(sys.executable, ['python'] + sys.argv)

openAnotherFile=False

if(y=="y" or y=="Y"):
    y=True
    openAnotherFile=False
elif(y=="n" or y=="N"):
    y=False
    openAnotherFile=False
else:
    print("Invalid entry")
    y=False
    openAnotherFile=True

if(openAnotherFile):
    restart()

if(y):  
    x= input("Enter the anime link you want to watch after studying(p.s. mention the http(s))(p.p.s. if you have no specific anime leave the parameter empty): ")

p = input("Do you want us to redirect you to your study page after the anime session(y/n): ")

if(p=="y" or p=="Y"):
    p=True
    openAnotherFile=False
elif(p=="n" or p=="N"):
    p=False
    openAnotherFile=False
else:
    print("Invalid entry")
    p=False
    openAnotherFile=True

if(openAnotherFile):
    restart()

if(p):
    q = input("Enter the study link you want to be redirected to after watching anime(p.s. mention the http(s))(p.p.s. if you have no specific link leave the parameter empty): ")

delay = int(input("Enter first range(in minutes): "))*60
delay2 = int(input("Enter second range(in minutes): "))*60
delay3 = delay2 + int(z)*60

def fun():     
    print ("Hey its time to watch anime, stop studying")
    winsound.PlaySound("C:/Users/arrym/OneDrive/Documents/tunes that i can use/554950__waveplay__120-bpm-chunky-bass-drums-wip.wav", winsound.SND_FILENAME)
    if(y):
        if(x):
            webbrowser.open(x)
        else:
            webbrowser.open('https://aryaman2709.github.io/anime-web-page/')
    
def fun2():    
    print ("Hey its time to study, stop watching anime")
    winsound.PlaySound("C:/Users/arrym/OneDrive/Documents/tunes that i can use/554950__waveplay__120-bpm-chunky-bass-drums-wip.wav", winsound.SND_FILENAME)
    if(p):
        if(q):
            webbrowser.open(q)
        else:
            webbrowser.open('https://aryaman2709.github.io/study-web-page/index')

webbrowser.open('https://aryaman2709.github.io/study-web-page/index')
webbrowser.open('https://todoist.com/app/project/2267860984')

start_time = threading.Timer(delay,fun)
start_time.start()

start_time = threading.Timer(delay2,fun)
start_time.start()

start_time = threading.Timer(delay3,fun2)
start_time.start()


