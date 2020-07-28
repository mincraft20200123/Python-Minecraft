# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 13:49:39 2020

@author: appedu
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    x,y,z=mc.player.getTilePos()
    a=mc.getBlock(x-1,y,z)
    b=mc.getBlock(x+1,y,z)
    c=mc.getBlock(x,y,z-1)
    d=mc.getBlock(x,y,z+1)
    if a==8 or b==8 or c==8 or d==8:
        mc.setBlocks(x-1,y-1,z-1,x+1,y-1,z+1,19)