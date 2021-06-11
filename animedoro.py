import winsound
import threading
import webbrowser

z = input("Enter how long is your anime(excluding the op and ending)(p.s. enter in minutes)(p.p.s yes i know op and end can't be skipped but you have to: ")
y = input("do you want us to redirect you to your anime after the study session(p.s. if no, leave the parameter empty): ")

if(y):  
    x= input("Enter the anime link you want to watch after studying(p.s. mention the http(s))(p.p.s. if you have no specific anime leave the parameter empty): ")

p = input("Do you want us to redirect you to your study page after the anime session(p.s. if no, leave the parameter empty): ")
if(p):
    q = input("Enter the study link you want to be redirected to after watching anime(p.s. mention the http(s))(p.p.s. if you have no specific link leave the parameter empty): ")

delay = int(input("Enter first range(in minutes): "))*60
delay2 = int(input("Enter second range(in minutes): "))*60
delay3 = delay2 + int(z)*60


def fun():         # user defined function which adds +10 to given number
    print ("Hey its time to watch anime, stop studying")
    winsound.PlaySound("C:/Users/arrym/OneDrive/Documents/tunes that i can use/554950__waveplay__120-bpm-chunky-bass-drums-wip.wav", winsound.SND_FILENAME)
    if(y):
        if(x):
            webbrowser.open(x)
        else:
            webbrowser.open('https://aryaman2709.github.io/anime-web-page/')
    
def fun2():         # user defined function which adds +10 to given number
    print ("Hey its time to study, stop watching anime")
    winsound.PlaySound("C:/Users/arrym/OneDrive/Documents/tunes that i can use/554950__waveplay__120-bpm-chunky-bass-drums-wip.wav", winsound.SND_FILENAME)
    if(p):
        if(q):
            webbrowser.open(q)
        else:
            webbrowser.open('https://aryaman2709.github.io/study-web-page/index')

start_time = threading.Timer(delay,fun)
start_time.start()


start_time = threading.Timer(delay2,fun)
start_time.start()

start_time = threading.Timer(delay3,fun2)
start_time.start()





