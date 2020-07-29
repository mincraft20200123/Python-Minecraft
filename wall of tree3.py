# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 15:15:37 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
z=0
def tree(x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,161)
    mc.setBlocks(x,y,z,x,y+4,z,17)
for i in range(10):
    for j in range(5):
        tree(x+i*5,y+j*i,z)
        z=z+1