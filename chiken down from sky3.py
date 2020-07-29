# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:08:35 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
import random
import time
mc = Minecraft.create()

pos=mc.player.getPos()

while True:
    x=pos.x+random.uniform(-20,20)
    z=pos.z+random.uniform(-20,20)
    y=pos.y+30
    mc.spawnEntity(x,y,z,12)
    time.sleep(0.1)