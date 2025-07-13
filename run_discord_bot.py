import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"🤖 Bot connected as {bot.user}")

@bot.command()
async def start(ctx):
    if isinstance(ctx.channel, discord.DMChannel):
        await ctx.send("Hi! I'm your washing machine assistant. What's the issue you're facing?")
    else:
        await ctx.send("Please DM me instead of using this command in a server.")

if __name__ == "__main__":
    bot.run(DISCORD_BOT_TOKEN)
