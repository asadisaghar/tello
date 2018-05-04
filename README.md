
## ~~DISCLAIMER~~

~~I do not own a Tello. This code and documentation is based on the Tello SDK
documentation as of 3/19/2018.~~

## WHAT THE BLEEP IS THIS

- A Python interface for the Ryze Tello drone.
- The tello module provides a Tello class, which interacts with the Tello API.
- The Tello has an IP of 192.168.10.1. The device sending commands must be
connected to the Tello WiFi network and have an IP in the 192.168.10.0/24
range.

## CREATE A MAGIC TELLO OBJECT

- Tello objects require a minimum of 2 parameters to initialize, the local IP
address and port to bind.
    
        drone = tello.Tello('192.168.10.2', 8888)

- Methods that require distance or speed parameters expect feet or MPH. Include
parameter imperial=False for meters and KPH.

        drone = tello.Tello('192.168.10.2', 8888, imperial=False)

- If you send a command to the Tello and it doesn't respond within .3 seconds, a
RuntimeError is raised. You may specify the number of seconds to wait with the
timeout parameter.

        drone = tello.Tello('192.168.10.2', 8888, imperial=False, timeout=.5)

- When you initialize a Tello object, it attempts to connect to the Tello and
enter command mode. If this fails, a RuntimeError is raised.

## DO VARIOUS THINGS

- Once initialized, a number of methods are available to send commands to the
Tello. It will respond with 'OK', 'FALSE' or a numeric value, which the methods
return.

- These methods do what you'd expect. Responses are 'OK' or 'FALSE'.

      drone.takeoff()
      drone.land()

- Methods that perform vertical or horizontal movements require a single
parameter, distance. Responses are 'OK' or 'FALSE'.

- The unit of distance is feet or meters. The SDK accepts distances of 1 to 500
centimeters. Realistically, this translates to .1 - 5 meters or .7 - 16.4 feet.

    drone.move_forward(distance)
    drone.move_backward(distance)
    drone.move_right(distance)
    drone.move_left(distance)
    drone.move_up(distance)
    drone.move_down(distance)

- Methods that rotate require a single parameter, degrees. The SDK accepts values
from 1 to 360. Responses are 'OK' or 'FALSE'.

        drone.rotate_cw(degrees)
        drone.rotate_ccw(degrees)

- The method to set speed requires a single parameter, speed. Responses are 'OK'
or 'FALSE'.

- The unit of speed is KPH or MPH. The SDK accepts speeds from 1 to 100
centimeters/second. Realistically, this translates to .1 to 3.6 KPH or .1 to 
2.2 MPH.

        drone.set_speed(speed)

- The method to flip requires a single parameter, direction. The SDK accepts 'l',
'r', 'f', 'b', 'lf', 'lb', 'rf' or 'rb'. Responses are 'OK' or 'FALSE'.

        drone.flip(direction)

- Methods that retrieve information from the Tello take no parameters. Responses
are numeric values.

- Get current speed in KPH or MPH:

        drone.get_speed()

- Get percent battery life remaining:

        drone.get_battery()

- Get elapsed flight time in seconds:

        drone.get_flight_time()
