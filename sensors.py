import Adafruit_DHT
import datetime, time

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

while True:
    current = time.time()
    humidity, temperature  = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    dif = time.time() - current
    try:  
      if humidity > 20 or humidity < 100 or temperature > 8 or temperature < 50:
        print("the Temp is {0:.1f} and humidity of {1:.1f}%".format(temperature,humidity))
    except:
        print("e")
    if dif <= 1:
       dif = 1 - dif
       print(f"will sleep {dif}")
       time.sleep(dif)
    else:
       print(f"it took {dif}... no nap")
