import pygame
import time

def date_time_water():
    file = open("reports.txt" , "a")
    import datetime
    file.write(str("Water drank at: ")+str(datetime.datetime.now())+str("\n"))
    file.close()
def date_time_eye():
    file = open("reports.txt" , "a")
    import datetime
    file.write(str("eye exercise done at: ")+str(datetime.datetime.now())+str("\n"))
    file.close()
def date_time_exer():
    file = open("reports.txt" , "a")
    import datetime
    file.write(str("physical exercise done at: ")+str(datetime.datetime.now())+str("\n"))
    file.close()
def music1():
    print("Time for some water: ")
    pygame.mixer.init()
    pygame.mixer.music.load("audio1.mp3")
    pygame.mixer.music.set_volume(.7)
    pygame.mixer.music.play()
def music2():
    print("Time for eye exercise: ")
    pygame.mixer.init()
    pygame.mixer.music.load("audio1.mp3")
    pygame.mixer.music.set_volume(.7)
    pygame.mixer.music.play()    
def music3():
    print("Time for exercise: ")
    pygame.mixer.init()
    pygame.mixer.music.load("audio1.mp3")
    pygame.mixer.music.set_volume(.7)
    pygame.mixer.music.play()
def water():
    music1()
    water = input("Enter (Done) if water taken: ").lower()
    if water == "done":
        pygame.mixer.quit()
    else:
        pass
def water_time():
    time.sleep(900)
def eye():
    music2()
    water = input("Enter (Done) if eye exersize is done: ").lower()
    if water == "done":
        pygame.mixer.quit()
    else:
        pass  
def exer():
    music3()
    water = input("Enter (Done) if eye exersize is done: ").lower()
    if water == "done":
        pygame.mixer.quit()
    else:
        pass
a = 2    
while a>1:
    pygame.mixer.init()
    evening = "17:00:00"
    morning = "09:00:00"
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time >= evening:
        break
    elif current_time <= morning:
        break
    water_time()
    water()
    date_time_water() 
    water_time()  
    eye()
    date_time_eye()
    water()
    date_time_water() 
    water_time()    
    exer()
    date_time_exer()  
    water()   
    a = a-1
while True:
    pygame.mixer.init()
    evening = "17:00:00"
    morning = "09:00:00"
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time >= evening:
        break
    elif current_time <= morning:
        break
    water()
    date_time_water() 
    water_time()  
    eye()
    date_time_eye()
    water()
    date_time_water() 
    water_time()    
    exer()
    date_time_exer()  
    water()    