#Auther Vu Tuan Thinh
# HN 11/07/2022
from asyncore import read
import os
from pickle import FALSE
#from tkinter.messagebox import NO
from urllib import response
import requests
import time
import json
import random
class Parking():
    balance_xe1 = 100
    balance_xe2 = 100
    Xe_List = []
    max_slot_car = 2
    rfid = None
    check_card = None
    #doc the tu
    def Read_RFID(self):
        self.rfid = None
        dev = os.open("/dev/rfid_rc522_dev", os.O_RDONLY)
        start = time.time()
        while (self.rfid == b'' or self.rfid == None):
            self.rfid = os.read(dev, 4)
            time_out = time.time()
            if time_out-start > 5:
                start = time_out
        os.close(dev)
        try:
            self.rfid = str(int(self.rfid[0]))+'.'+str(int(self.rfid[1])) + \
                '.'+str(int(self.rfid[2]))+'.'+str(int(self.rfid[3]))
            print(self.rfid)
            self.check_card = True
        except:
            print("Error")
            self.check_card = False
    #Hien thi LCD
    def LCD_Print(self, text):
        dev = os.open(
            "/sys/devices/virtual/alphalcd/lcdi2c/clear", os.O_WRONLY)
        os.write(dev, b'1')
        os.close(dev)
        dev = os.open(
            "/sys/devices/virtual/alphalcd/lcdi2c/position", os.O_WRONLY)
        os.write(dev, b'11')
        os.close(dev)
        dev = os.open("/dev/lcdi2c", os.O_WRONLY)
        os.write(dev, bytes(text, 'utf-8'))
        os.close(dev)
    # Dinh danh nguoi dung
    def LCD_Print_Ver2(self, text):
        dev = os.open("/dev/lcdi2c", os.O_WRONLY)
        os.write(dev, bytes(text, 'utf-8'))
        os.close(dev)
    def identify(self):
        self.Read_RFID()
        if not self.check_card:
            self.LCD_Print("Invalid card\n Pls try again!")
            return False
        else:
            for x in self.Xe_List  :
              if(self.rfid == x):
                self.LCD_Print("Hen gap lai quy khach!!\n")
                time.sleep(1)
                self.Xe_List.remove(self.rfid)
                self.max_slot_car = self.max_slot_car +1
                return True
            self.LCD_Print("Valid card\n ")
            time.sleep(0.5)
            if(self.rfid == "179.108.248.173" and self.balance_xe1 >0):
                self.Xe_List.append('179.108.248.173')
                self.balance_xe1 =self.balance_xe1 - 10
                self.LCD_Print("Hi User1")
                self.LCD_Print_Ver2(" your\n balance is ")
                self.LCD_Print_Ver2(str(int(self.balance_xe1)))
                self.max_slot_car = self.max_slot_car -1
                time.sleep(2)
                return True
            elif(self.rfid == "17.9.59.29" and self.balance_xe2 >0):
                self.Xe_List.append('17.9.59.29')
                self.balance_xe2 =self.balance_xe2 - 10
                self.max_slot_car = self.max_slot_car -1
                self.LCD_Print("Hi User2")
                self.LCD_Print_Ver2(" your\n balance is ")
                self.LCD_Print_Ver2(str(int(self.balance_xe2)))
                time.sleep(2)
                return True
            else:
                self.LCD_Print("The ban da\n het tien !!!")
                time.sleep(1)
                return False
    def Check_slot_available(self):
        if(self.max_slot_car>0):
          self.LCD_Print("Hi")
          self.LCD_Print_Ver2(" bai xe con ")
          self.LCD_Print_Ver2(str(int(self.max_slot_car)))
          self.LCD_Print_Ver2("\n")
          self.LCD_Print_Ver2("cho trong !!!")
          time.sleep(1)
          return True
        else:
          return False
    def main(self):
      if(self.identify()):
            print(self.max_slot_car)
            if(self.Check_slot_available()):
              exec(open('open.py').read())
              return True
            else :
              self.LCD_Print("Bai xe da \n het cho trong ")
              time.sleep(2)
              return False
      else:
        self.LCD_Print("Invalid Card\n")
        return False

test = Parking()
test.max_slot_car =2
test.balance_xe1 = 100
test.balance_xe2 = 20
test.LCD_Print("Welcome to\n car parking!!!")
time.sleep(1)
start =time.time()
while 1:
  test.main()



