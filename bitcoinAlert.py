import os
import requests
import time
from pydub import AudioSegment
from pydub.playback import play



response = requests.get('https://api.nomics.com/v1/currencies/ticker?key=bcbd33571b255a696995dad391a822e6&ids=BTC&interval=1d,30d&convert=USD')
data = response.json()
bit = data[0]['price']
ask = input('do you want to customize price? (Y/N)')
if str(ask) == "Y":
  alert_amount = input('Alert if Bitcoin drops below: ')
  alert_amounthigher = input('Alert if Bitcoin increase')
while True:
  if alert_amount > bit:
    print("price is droped below:" + alert_amount + "price is now :"+ bit)
    song = AudioSegment.from_mp3("alert.mp3")
    time.sleep(180)
  if alert_amounthigher < bit:
    print("price is Increased :" + alert_amounthigher + "price is now :"+ bit)
    time.sleep(180)
def PrintPrice(Bitcoin):
  return print("Okay - Bitcoin Price is :"+ Bitcoin)
if str(ask) == "N":
  while True:
    PrintPrice(bit)
    time.sleep(180)