import pyautogui
from PIL import Image , ImageGrab
import time
# from numpy import asarray

# while True:
#     pyautogui.keyDown('h') 
def hit(key):
    pyautogui.keyDown(key)

def Takescreenshot():
    image = ImageGrab.grab().convert('L')
    return image

def isCollide(data):
    for i in range(220,280):
        for j in range(450 , 563):
            if data[i,j] < 100:
                pyautogui.keyDown("down")
                pyautogui.keyUp("down")
                return

    for i in range(310,425):
        for j in range(583 , 690):
            if data[i,j] < 100:
                hit("up")
                return

    return
if __name__ == "__main__":
    print("Hey dino game about to start in 3 seconds")
    time.sleep(4)
    while True:
        # image = Takescreenshot() 
        image = ImageGrab.grab().convert('L')   
        data = image.load()
        # break
        isCollide(data)
    # image = ImageGrab.grab().convert('L')
    # data = image.load()
    # for i in range(250,300):
    #     for j in range(450 , 563):
    #         data[i,j] = 100
             

    # for i in range(310,425):
    #     for j in range(583 , 670):
    #         data[i,j] = 100
                
    # image.show()  
        # print(asarray(image))
        

         
