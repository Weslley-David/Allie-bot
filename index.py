import os
import discord

class MyClient(discord.Client):
    @staticmethod
    def teste():
        resp = 4 + 3
        return str(resp)

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    ### função para ouvir o chat os comandos e retornar respostas ###
    async def on_message(self, message):
        print('Message from {0.author} with {0.id}: {0.content}'.format(message))
        print(message)
        #print('{0.id}')
        if message.content   == 'hello allie':
            #usuario = message.author.id
            await message.channel.send('your id is: {}'.format(message.author.id))
            #await message.channel.send('mensagem padrão retornada.')
        elif message.content == 'teste 2':
            retorno = 'mensagem por função retornada: ' + str(self.teste())
            await message.channel.send(retorno)


if __name__ == '__main__':
    # Coleta o token
    file = open('token.txt', 'r')
    token = str(file.readline())
    file.close

    # Inicia o bot
    client = MyClient()
    client.run(token)
