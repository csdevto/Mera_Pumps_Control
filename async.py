#read and control PI
import RPi.GPIO as GPIO
import datetime, time, Adafruit_DHT, asyncio, logging
GPIO.cleanup()
try:
	logging.basicConfig(filename='pumps.log', level=logging.DEBUG)
	GPIO.setmode(GPIO.BOARD)
	PoutON = 15 * 60
	PinON = 10 * 60
	OFF = 30 * 60
	PumpsOut = [18]
	PumpsIn = [38,13,15,16]

	async def RunPump(pumps,on,off):
		for x in pumps:
			GPIO.setup(x,GPIO.OUT)
		while True:
			for x in pumps:
				GPIO.output(x, GPIO.HIGH)
				a = str(datetime.datetime.now()) + ' ' + str(x) + ' - ON'
				logging.info(a)
			await asyncio.sleep(on)
			for x in pumps:
				GPIO.output(x, GPIO.LOW)
				b = str(datetime.datetime.now()) + ' ' + str(x) + ' - OFF'
				logging.info(b)
			await asyncio.sleep(off)
	async def TempHum():
		DHT_SENSOR = Adafruit_DHT.DHT22
		DHT_PIN = 4

		while True:
		    current = time.time()
		    humidity, temperature  = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
		    dif = time.time() - current
		    try:
			    if humidity > 20 or humidity < 100 or temperature > 8 or temperature < 50:
			        c = str(datetime.datetime.now()) + ("the Temp is {0:.1f} and humidity of {1:.1f}%").format(temperature,humidity)
			        logging.info(c)
		    except:
		    	logging.warning("Sensor Val not avail")
		    if dif <= OFF:
		       dif = OFF - dif
		       await asyncio.sleep(dif)

	loop = asyncio.get_event_loop()
	asyncio.ensure_future(RunPump(PumpsIn,PinON,OFF))
	asyncio.ensure_future(RunPump(PumpsOut,PoutON,OFF))
	asyncio.ensure_future(TempHum())
	loop.run_forever()
except:
	logging.warning("Catch All")
	

