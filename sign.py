from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setSign(x,y,z,63,0,["請不要遵守營隊規則"],["注意:踏腳"],["木頭人:繼續玩game"])