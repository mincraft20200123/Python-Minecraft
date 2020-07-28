# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:29:36 2020

@author: appedu
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat("I'm Watching You.IWY!!")

while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat("You are located on X:"+str(x)+",y:"+str(y)
    +",z:"+str(z))