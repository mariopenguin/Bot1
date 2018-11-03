import discord
from discord import client, Member, server

client = discord.Client()
diccionario={}
iniciado=False
def inicializar():
    x = client.get_all_members()
    for i in x:
        diccionario.update({i.name: 0})
    print(diccionario)




def sumarstrike(diccionario,message,nombre):
    if diccionario.get(nombre) == None:
         client.send_message(message.channel,"No existe ese usuario papu")
    else:
        aux = diccionario.get(nombre)
        aux = aux+1
        diccionario.update({nombre:aux})
        client.send_message(message.channel, "Has metido un strike a: " + nombre + " y lleva:" + str(diccionario.get(nombre)))
#Ping al bot
def numerostrikes(numero):
    if type(numero) is int:
        if numero>=3:
            return True
        else:
            return False
    else:
        return False
@client.event
async def on_message(message):



    if message.content.startswith('!Hola'):


        await client.send_message(message.channel,"Hola")

    elif message.content.startswith('!strike'):
        mensaje = (message.content).split(' ')
        sumarstrike(diccionario,message,mensaje[1])
        await client.send_message(message.channel,"Has metido un strike a: "+mensaje[1]+" y lleva: "+ str(diccionario.get(mensaje[1])))
        if(numerostrikes(diccionario.get(mensaje[1]))):
            server.server_voice_state(mensaje[1],True)
            await client.send_message(message.channel,':zap:'+ "Ohh Hitlario... yo te invocoo haz que "+mensaje[1]+" se quede Echenique y no pueda hablar más"+':zap:')



@client.event
async def on_ready():
    inicializar()
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run('NTA3Njc5Nzc2OTc1MzU1OTI3.Dr2rZA.Kt5qjj7kBKundrrjDy8pGP_Tsmg')
