import serial
import time
import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import keyboard
import os

#odczyt
print("Press ‘Enter’ to finish saving. Press ‘Esc’ to cancell the measurement")
dose = input("Enter dose: ")
grind = input("Grind setting: ")
if grind == "":
    grind = '5_00'

ser = serial.Serial('COM4', 9600, timeout=0) 

data = b''

moment=time.strftime("%Y-%m-%d__%H_%M_%S",time.localtime())

while True:
    if keyboard.is_pressed('ENTER'):
        print("przyjąłem")
        sys.exit(0)
    if keyboard.is_pressed('Esc'):   
        if os.path.isfile('./Data/'+moment+'dose_'+dose+'_on_'+grind+'.csv'):
            os.remove('./Data/'+moment+'dose_'+dose+'_on_'+grind+'.csv')
        sys.exit(0)
    data=ser.readline()
    if data != b'':

        print(data)
        f = open('./Data/'+moment+'dose_'+dose+'_on_'+grind+'.csv', 'a')
        f.write(data.decode('ascii').replace("\n",""))
        f.close()
