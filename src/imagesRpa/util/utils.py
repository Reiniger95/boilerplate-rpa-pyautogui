from datetime import timedelta
import re
import unicodedata
from decouple import config
import pyautogui
import time
import keyboard
import sys
import win32gui, win32con
import pygetwindow
import subprocess
import keyring
USUARIO = config('USUARIO')
PROCESS = config('PROCESS')
def removeAcents(string: str) -> str:
      regex = re.compile(r'[\u0300-\u036F]', flags=re.DOTALL)
      normalized = unicodedata.normalize('NFKD', string)
      return regex.sub('', normalized).lower()


  
def cliclaImagem(imageUrl):
  esperando = True
  count = 0
  while esperando == True:
    coords = pyautogui.locateOnScreen('src//imagesRpa//images//'+imageUrl)
    if coords != None:
      esperando = False
      pyautogui.click(coords)
    else:
      if count >= 5:
        break      
      else:
        print('procurando imagem: ', imageUrl) 
        time.sleep(1)
    count += 1

def escreveNaImagem(imageUrl, text):
  cliclaImagem(imageUrl)
  time.sleep(0.2)
  keyboard.press('home')
  time.sleep(0.2)
  keyboard.write(text, delay=0.1)

def existeImagem(imageUrl):
  coords = pyautogui.locateOnScreen('src//imagesRpa//images//'+imageUrl)
  if coords != None:
    return True
  else:
    return False

def fechaTudo():
  try:
    time.sleep(4)
    coords = pyautogui.locateOnScreen('src//imagesRpa//images//exit.png')
    pyautogui.click(coords)
    time.sleep(4)
  except:
    pass
  handle = win32gui.GetForegroundWindow()
  win32gui.CloseWindow(handle)
  sys.exit()

def paraEmcima(imageUrl):
  esperando = True
  count = 0
  while esperando == True:
    coords = pyautogui.locateOnScreen('src//imagesRpa//images//'+imageUrl)
    if coords != None:
      esperando = False
      pyautogui.moveTo(coords)
    else:
      if count >= 5:
        break      
      else: 
        time.sleep(1)
    count += 1




  
def existe_janela(nome):
    def cb(x, y): return y.append(x)
    wins = []
    win32gui.EnumWindows(cb, wins)
    nameRe = nome

    # now check to see if any match our regexp:
    tgtWin = -1
    for win in wins:
        txt = win32gui.GetWindowText(win)
        if nameRe == txt:
            # if nameRe.match(txt):
            tgtWin = win
            break

    if tgtWin >= 0:
        return True
    else:
        return False
def fechar_janelas(titulo):
    try:
        existe = existe_janela(titulo)
        if existe is True:
            win = pygetwindow.getWindowsWithTitle(titulo)[0]
            win.close()
    except:
        print('Não existe esta janela')