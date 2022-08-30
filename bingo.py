import numpy as n
import pydirectinput as p
import keyboard as k
card_y = n.array([555, 585, 620, 655, 690])
card_x1 = n.array([125, 160, 195, 230, 265])
card_x2 = n.array([320, 355, 390, 425, 460])
card_x3 = n.array([515, 550, 585, 620, 655])
card_x4 = n.array([710, 745, 780, 815, 850])
card_x5 = n.array([905, 940, 975, 1010, 1045])
card_x6 = n.array([1100, 1135, 1170, 1205, 1240])

p.PAUSE=0.006
while True:
    if k.is_pressed("t"):
        print("You stopped the program")
        break
    for x in card_x1:
        for y in card_y:
            p.click(x,y)
    for x in card_x2:
        for y in card_y:
            p.click(x,y)
    for x in card_x3:
        for y in card_y:
            p.click(x,y)
    for x in card_x4:
        for y in card_y:
            p.click(x,y)
    for x in card_x5:
        for y in card_y:
            p.click(x,y)
    for x in card_x6:
        for y in card_y:
            p.click(x,y)
    p.click(685, 460)