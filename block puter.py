# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:01:27 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()

try:
    s=int(input("請輸入要放的方塊ID:"))
    mc.setBlock(x,y,z,s)
except:
    print("只能輸入數字!!!!!!")