# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:45:50 2020

@author: appedu
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
for i in range(20):
    mc.setBlock(x,y-35,z+i,1)
 