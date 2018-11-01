import discord

cliente = discord.client()

#Ping al bot
@discord.client.event
async def on_message(message):
    if message.content.startswith('!Ratambo'):
        await discord.client.send_message("Estoy vivo!")
    pass
