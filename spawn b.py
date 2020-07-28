# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:57:58 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlock(x,y,z,49)

x,y,z=mc.player.getTilePos()
mc.setBlock(x+1,y,z,49)

x,y,z=mc.player.getTilePos()
mc.setBlock(x,y,z+1,49)

x,y,z=mc.player.getTilePos()
mc.setBlock(x,y,z+2,49)

x,y,z=mc.player.getTilePos()
mc.setBlock(x+2,y,z,49)

x,y,z=mc.player.getTilePos()
mc.setBlock(x+2,y,z+1,49)

x,y,z=mc.player.getTilePos()
mc.setBlock(x+1,y,z+2,49)

x,y,z=mc.player.getTilePos()
mc.setBlock(x+2,y,z+2,49)
