from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
time.sleep(5)

x=166
y=66
z=188

mc.player.setTilePos(x,y,z)
time.sleep(0.5)
