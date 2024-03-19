import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="m!",intents=discord.Intents.all())

@bot.event
async def on_ready():
	guild_count = 0
	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")
		guild_count += 1
	print(f"Infelizmente Minnie está em {str(guild_count)} servers.")


@bot.command()
async def d(ctx,n):
        try:
                n.lstrip()
                n = int(n)
                rolls = []
                for _ in range(3):
                        rolls.append(random.randint(1, n))
                roll = random.choice(rolls)
                desvio = ''
                if n <= 13:
                        if roll < 6:
                                desvio = 'Você foi atingido!'
                        elif roll >= 6:
                                desvio = 'Você desviou!'
                await ctx.send(f'[ :game_die: ] O resultado é `[{roll}]`. {desvio}')
        except:
                await ctx.send("[ :x: ] Digite um número válido!")


@bot.command()
async def rolls(ctx,*,text : str):
        count, _, text = text.partition('d')
        size = text 
        try:
                count, size = int(count),int(size)
        except ValueError:
                await ctx.send('[ :x: ] Insira números válidos...')
        return await _dice(ctx,count,size)
async def _dice(ctx,count,size):
        rolls = [random.randint(1,size) for _ in range(count)]
        rolls.sort(reverse=True)
        desvio = ''
        if len(rolls) == 1:
                if rolls[0] < 6:
                        desvio = 'Você foi atingido!'
                elif rolls[0] >= 6 and rolls[0] <= 13:
                        desvio = 'Você desviou!'
        await ctx.send(f"[ :game_die: ] O resultado é `{rolls}`. {desvio}")


@bot.command()
async def say(ctx,*,text):
        await ctx.message.delete()
        await ctx.send(text)


@bot.command()
async def clear(ctx, amount):
        amount.lstrip()
        try:
                amount = int(amount)
                await ctx.channel.purge(limit=amount+1)
                await ctx.send(f'[ :white_check_mark: ] Eu apaguei {amount} mensagens!')
        except:
                await ctx.send('[ :no_entry_sign: ] Por favor digite um número válido')

@bot.command()
async def choose(ctx,*, text):
        args = []
        while text:
                arg, _, text = text.partition(",")
                args.append(arg)
                if text.count(",") == 0:
                        args.append(text)
                        break
        choice = random.choice(args)
        choice = choice.lstrip()
        await ctx.send(f"[ :brain: ] Eu escolhi... **{choice}**!")

 
bot.run(DISCORD_TOKEN)
