# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:00:58 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlocks(x-1,y,z-1,x+e1,y,z+1,)
    time.sleep(10)