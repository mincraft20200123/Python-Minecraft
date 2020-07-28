# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:39:36 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
while True:
    color=random.randrange(0,16)
    mc.setBlocks(x-50,y-1,z-50,x+50,y-1,z+50,95,color)
    time.sleep(1)