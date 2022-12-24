import time
import keyboard as kb
import pyautogui as pt


def cautare_google():
    if pt.locateOnScreen(r'D:\PycharmProjects\IA\Screenshot 2022-11-04 101531.png', confidence=0.7) != None:
        camp_google=pt.locateOnScreen(r'D:\PycharmProjects\IA\Screenshot 2022-11-04 101531.png', confidence=0.7)
        pt.click(camp_google)
        time.sleep(3)
        pt.write("https://youtube.com")
        pt.press('enter')
        time.sleep(5)
    else:
        print("Imaginea nu se afla pe ecran")
def cautare_yt():
    if pt.locateOnScreen(r'D:\PycharmProjects\IA\ytsearch.png', confidence=0.7) != None:
        camp_youtube = pt.locateOnScreen(r'D:\PycharmProjects\IA\ytsearch.png', confidence=0.7)
        pt.click(camp_youtube)
        time.sleep(5)
        pt.write("Zona IT")
        pt.press('enter')
        time.sleep(5)
    else:
        print("Imaginea nu se afla pe ecran")
def canal():
    if pt.locateOnScreen(r'D:\PycharmProjects\IA\zona.png', confidence=0.7) != None:
        camp_zona = pt.locateOnScreen(r'D:\PycharmProjects\IA\zona.png', confidence=0.7)
        pt.click(camp_zona)
        time.sleep(5)
def subs_yt():
    if pt.locateOnScreen(r'D:\PycharmProjects\IA\subs.png', confidence=0.7) != None:
        camp_IT = pt.locateOnScreen(r'D:\PycharmProjects\IA\subs.png', confidence=0.7)
        pt.click(camp_IT)
        time.sleep(5)
    else:
        print("Imaginea nu se afla pe ecran")

def viewvideo():
    pt.scroll(-300, 1365, 676)
    pt.click(802, 420)
    time.sleep(10)
    pt.click(25, 57)
    time.sleep(3)
    pt.click(987, 473)
    time.sleep(10)


def coordonate():
    print(pt.position())
time.sleep(2)
coordonate()
cautare_google()
cautare_yt()
canal()
subs_yt()
viewvideo()
