# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 09:59:33 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.player.setPos(x+0.5)
mc.setBlock(x,y-1,