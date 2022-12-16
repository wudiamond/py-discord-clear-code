#import dc
import discord
#import 延遲
import time 

client = discord.Client()
@client.event
async def on_message(message):
    #輸入!clear指令
    if message.content.startswith("!clear"):
        #刪除我輸入的指令
        await message.delete()
 #偵測自己的文字
        tmp = message.content.split(" ")[1]
#給他延遲個0.01s    
        time.sleep(0.01)
#執行顯示數字
        messages = await message.channel.history(limit=int(tmp)).flatten()
        #開始刪除字
        for message in messages:
            await message.delete()
#放token
client.run('token')

