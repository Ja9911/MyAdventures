import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
Y = 2
X1 = -58
Z1 = 8
X2 = -52
Z2 = 15
rent = 0
while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    if pos.x>X1 and pos.x<X2 and pos.z>Z1 and pos.z<Z2 and pos.y == 2:
        rent = rent+1
        mc.postToChat("you owe rent:" +str(rent))
