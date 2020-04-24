import os
import requests
from playsound import playsound
import time



response = requests.get('https://api.nomics.com/v1/currencies/ticker?key=bcbd33571b255a696995dad391a822e6&ids=BTC&interval=1d,30d&convert=USD')
data = response.json()
def PrintPrice(Bitcoin):
  return print("Okay - Bitcoin Price is :"+ Bitcoin)
bit = data[0]['price']
def Ask():
  bitcoinPrice = data[0]['price']
  ask = input('do you want to customize price? (Y/N)')
  if str(ask) == "Y":
    alert_amount = input('Alert if Bitcoin drops below: ')
    alert_amounthigher = input('Alert if Bitcoin increase') 


  if str(ask) == "N":
    while True:
      PrintPrice(bit)
      time.sleep(180)
Ask()
playsound('alert.mp3')