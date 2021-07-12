import time
from threading import Thread
import time


def car(velocity, pilot):
    v0 = 0
    while v0 <= 100:
        v0 += velocity
        time.sleep(0.5)
        print('pilot: {} Km/h: {} \n' .format(pilot, v0))


p_car1 = Thread(target=car, args=[1, 'Bruna'])
p_car2 = Thread(target=car, args=[2, 'Python'])

p_car1.start()
p_car2.start()