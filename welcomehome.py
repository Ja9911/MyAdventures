import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    if pos.x == -58 and pos.z == 8 and pos.y == 2:
        mc.postToChat("welcome home")
