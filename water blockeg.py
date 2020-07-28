# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:20:32 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
a=0
x,y,z=mc.player.getTilePos()

while a<20:
    mc.setBlocks(x,y,z,x,y+9,z+60,19)
    x=x-5
    a=a+1