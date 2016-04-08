import RPI.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
print "Backlight on"
GPIO.output(17,GPIO.HIGH)