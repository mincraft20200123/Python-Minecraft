# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 10:59:34 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
import random
for i in range(30):
    r=random.randrange(1,7)
    #x+
    if r==1:
        mc.setBlocks(x,y,z,x+4,y,z,133)
        x=x+4
    #x-
    elif r==2:
        mc.setBlocks(x,y,z,x-4,y,z,46)
        x=x-4
    #z+
    elif r==3:
        mc.setBlocks(x,y,z,x,y,z+4,57)
        z=z+4
    #z-
    elif r==4:
        mc.setBlocks(x,y,z,x,y,z-4,213)
        z=z-4
    #y+
    elif r==5:
        mc.setBlocks(x,y,z,x,y+4,z,89)
        y=y+4
    #y-
    else:
        mc.setBlocks(x,y,z,x,y-4,z,169)
        y=y-4