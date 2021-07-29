import pyautogui
import time
import os

#nani
print("1. Spam some words repeteadly. \n2. Spam one of the lyrics")
nani = int(input("Choice (1 or 2) > "))


if nani == 1:
  words = input("Words to spam > ")
  time1 = int(input("Start after how many seconds? \n>"))
  time.sleep(time1)

  while True:
    pyautogui.write(words)
    pyautogui.press("enter")

elif nani == 2:
  print(os.listdir('txt_files'))

  file_name = input("File name > ")
  time2 = int(input("Start after how many seconds? \n>")) 
  time.sleep(time2)
  text = open('./txt_files/' + file_name, 'r')
  
  for line in text:
    pyautogui.typewrite(line)
    pyautogui.press("enter")