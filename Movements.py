import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
    
lf1 = GPIO.PWM(3, 50)
lf2 = GPIO.PWM(5, 50)
lb1 = GPIO.PWM(7, 50)
lb2 = GPIO.PWM(11, 50)
    
rf1 = GPIO.PWM(8, 50)
rf2 = GPIO.PWM(10, 50)
rb1 = GPIO.PWM(12, 50)
rb2 = GPIO.PWM(16, 50)

lf1.start(0)
lf2.start(0)
lb1.start(0)
lb2.start(0)
rf1.start(0)
rf2.start(0)
rb1.start(0)
rb2.start(0)
    
lf1.ChangeDutyCycle(4.5)
rf1.ChangeDutyCycle(4.5)
lb1.ChangeDutyCycle(4.5)
rb1.ChangeDutyCycle(4.5)

lf2.ChangeDutyCycle(4.5)
rf2.ChangeDutyCycle(4.5)
lb2.ChangeDutyCycle(4.5)
rb2.ChangeDutyCycle(4.5)

time.sleep(2)

def reverse():
    rf1.ChangeDutyCycle(2)
    time.sleep(0.5)
    rf2.ChangeDutyCycle(2)
    time.sleep(0.5)
    rf1.ChangeDutyCycle(4.5)
    time.sleep(0.5)
    
    rb1.ChangeDutyCycle(2)
    time.sleep(0.5)
    rb2.ChangeDutyCycle(7)
    time.sleep(0.5)
    rb1.ChangeDutyCycle(4.5)
    time.sleep(0.5)
    
    rb2.ChangeDutyCycle(4.5)
    rf2.ChangeDutyCycle(4.5)
    lb2.ChangeDutyCycle(2)
    lf2.ChangeDutyCycle(7)
    time.sleep(0.5)
    
    lb1.ChangeDutyCycle(2)
    time.sleep(0.5)
    lb2.ChangeDutyCycle(4.5)
    time.sleep(0.5)
    lb1.ChangeDutyCycle(4.5)
    time.sleep(0.5)
    
    lf1.ChangeDutyCycle(2)
    time.sleep(0.5)
    lf2.ChangeDutyCycle(4.5)
    time.sleep(0.5)
    lf1.ChangeDutyCycle(4.5)
    time.sleep(0.5)
    
    time.sleep(1)

def forward():
    lb1.ChangeDutyCycle(2)
    time.sleep(0.5)
    lb2.ChangeDutyCycle(2)
    time.sleep(0.5)
    lb1.ChangeDutyCycle(4.5)
    time.sleep(0.5)
    
    lf1.ChangeDutyCycle(2)
    time.sleep(0.5)
    lf2.ChangeDutyCycle(7)
    time.sleep(0.5)
    lf1.ChangeDutyCycle(4.5)
    time.sleep(0.5)
    
    lf2.ChangeDutyCycle(4.5)
    rf2.ChangeDutyCycle(2)
    lb2.ChangeDutyCycle(4.5)
    rb2.ChangeDutyCycle(7)
    time.sleep(0.5)
    
    rb1.ChangeDutyCycle(2)
    time.sleep(0.5)
    rb2.ChangeDutyCycle(4.5)
    time.sleep(0.5)
    rb1.ChangeDutyCycle(4.5)
    time.sleep(0.5)
    
    rf1.ChangeDutyCycle(2)
    time.sleep(0.5)
    rf2.ChangeDutyCycle(4.5)
    time.sleep(0.5)
    rf1.ChangeDutyCycle(4.5)
    time.sleep(0.5)
    
    time.sleep(1)

def right():
    lf1.ChangeDutyCycle(2)
    time.sleep(0.5)
    lf2.ChangeDutyCycle(2)
    time.sleep(0.5)
    lf1.ChangeDutyCycle(4.5)
    time.sleep(0.5)
    
    rb1.ChangeDutyCycle(2)
    time.sleep(0.5)
    rb2.ChangeDutyCycle(2)
    time.sleep(0.5)
    rb1.ChangeDutyCycle(4.5)
    time.sleep(0.5)
    
    lf2.ChangeDutyCycle(4.5)
    rf2.ChangeDutyCycle(7)
    lb2.ChangeDutyCycle(7)
    rb2.ChangeDutyCycle(4.5)
    time.sleep(0.5)
    
    rf1.ChangeDutyCycle(2)
    time.sleep(0.5)
    rf2.ChangeDutyCycle(4.5)
    time.sleep(0.5)
    rf1.ChangeDutyCycle(4.5)
    time.sleep(0.5)
    
    lb1.ChangeDutyCycle(2)
    time.sleep(0.5)
    lb2.ChangeDutyCycle(4.5)
    time.sleep(0.5)
    lb1.ChangeDutyCycle(4.5)
    time.sleep(0.5)
    
    time.sleep(1)
    
def left():
    rf1.ChangeDutyCycle(2)
    time.sleep(0.5)
    rf2.ChangeDutyCycle(7)
    time.sleep(0.5)
    rf1.ChangeDutyCycle(4.5)
    time.sleep(0.5)
    
    lb1.ChangeDutyCycle(2)
    time.sleep(0.5)
    lb2.ChangeDutyCycle(7)
    time.sleep(0.5)
    lb1.ChangeDutyCycle(4.5)
    time.sleep(0.5)
    
    lf2.ChangeDutyCycle(2)
    rf2.ChangeDutyCycle(4.5)
    lb2.ChangeDutyCycle(4.5)
    rb2.ChangeDutyCycle(2)
    time.sleep(0.5)
    
    lf1.ChangeDutyCycle(2)
    time.sleep(0.5)
    lf2.ChangeDutyCycle(4.5)
    time.sleep(0.5)
    lf1.ChangeDutyCycle(4.5)
    time.sleep(0.5)
    
    rb1.ChangeDutyCycle(2)
    time.sleep(0.5)
    rb2.ChangeDutyCycle(4.5)
    time.sleep(0.5)
    rb1.ChangeDutyCycle(4.5)
    time.sleep(0.5)
    
    time.sleep(1)
    
d = 'w'

print("Enter directions: \n")

while(d!='c'):
    d = input()
    if d=='w':
        forward()
    elif d=='s':
        reverse()
    elif d=='a':
        left()
    elif d=='d':
        right()
    else:
        print('Enter valid direction')

lf1.stop()
lf2.stop()
rf1.stop()
rf2.stop()
lb1.stop()
lb2.stop()
rb1.stop()
rb2.stop()

GPIO.cleanup()