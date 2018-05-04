import tello
import time

speed = 0.1
delta_t = 0.5
delta_deg = 5

drone = tello.Tello('192.168.10.2', 8888, imperial=False, timeout=.3)
drone.takeoff()
time.sleep(delta_t)
drone.go_sin(speed, delta_t, delta_deg, direction='forward')
time.sleep(delta_t)
drone.move_up(speed*delta_t)
time.sleep(delta_t)
drone.go_sin(speed, delta_t, delta_deg, direction='back')
time.sleep(delta_t)
drone.land()
