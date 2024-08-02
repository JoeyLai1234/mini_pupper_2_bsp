#!/usr/bin/python
from MangDang.mini_pupper.display import Display, BehaviorState
import time

disp = Display()

disp.show_image('/var/lib/mini_pupper_bsp/shutdown.png')
time.sleep(5)
disp.show_image('/var/lib/mini_pupper_bsp/sleep.gif')
