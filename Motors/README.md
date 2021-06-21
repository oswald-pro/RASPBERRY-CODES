# **Raspberry Pi Servo Motor control**

In addition to stepper motors, there are also small and cheap servo motors. The control of Raspberry Pi servo motors is very simple and thanks to the small size and weight they are used in many areas.
Unlike stepper motors, servomotors can be controlled with a single GPIO.

In this tutorial, I’ll show an example of how to use Python to control one or more servo motors.

Required Hardware Parts

    Servo motor*
    Jumper cable*
    (Breadboard*)
    if necessary, a battery holder* + (rechargeable) batteries*, as an external power supply

Of course, it is possible to supply the servo motor with an external power source, but this only makes sense when using several motors. For that, rechargeable batteries*/regular batteries would still be needed.

## Setup

In most cases, the colors of the servo are as follows and are connected to the Pi:

Black – comes to GND (pin 6) from the Pi
Red – comes to 3V3 (pin 1) from the Pi
Yellow/Orange – to a free GPIO pin (e.g., GPIO17, pin 11)

If you want to play it safe, you can set a ~ 1kΩ resistor between the data pin (yellow/orange) and the Pi. Normally this is not necessary.

If the servo motor does not rotate correctly, this may also influence the power supply of the Raspberry Pi (just look at the datasheet, what the engine consumes). In such a case an external power source makes sense (usually it is 4 to 6V).

## Software for controlling the Raspberry Pi servo motors

Unlike stepper motors, servo motors don’t occupy many GPIO pins to command a movement. For this, the rotation is controlled by the length of the pulse.

The angle of the motor is set along the length of the pulse, so PWM is particularly useful, which sends repetitive signals at even intervals (the Raspberry Pi Python library must be installed).

We either start python (sudo python) or open a new script (sudo nano servomotor.py) with the following content:




###Note:
If the servo motor shakes a bit while it is not moving, you can pause the pulse with ChangeDutyCycle(0)
