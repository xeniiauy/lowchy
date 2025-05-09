import discord
import os
from discord.ext import commands
from simpleeval import simple_eval
from dotenv import load_dotenv

bot = discord.Bot()
# Create a bot instance
prefix='/'

client = discord.Client(intents=discord.Intents.default())
bot = commands.Bot(command_prefix = prefix)
# Define a command to respond to mentions of the bot
@bot.slash_command()
async def lowchi(ctx):
    await ctx.send(f"Hi {ctx.author.mention}!")

# Define a command to handle math questions
@bot.slash_command()
async def math(ctx, *, question: str):
    # Check if the question is valid
    if 'what is' in question.lower():
        # Extract the math expression
        expression = question.lower().replace('what is', '').strip()
        # Evaluate the expression
        try:
            result = simple_eval(expression)
            # Respond to the user
            await ctx.send(f"Hi {ctx.author.name}, the answer is {result}! Do you want to know why?")
            # Wait for user response
            response = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.content.lower() in ['yes', 'no'], timeout=30)
            if response.content.lower() == 'yes':
                if '^' in expression:
                    await ctx.send("The ^ operator denotes exponentiation.")
                elif '/' in expression:
                    await ctx.send("Division operation returns the quotient of the division.")
                elif '*' in expression:
                    await ctx.send("Multiplication operation results from repeated addition.")
                elif '+' in expression or '-' in expression:
                    await ctx.send("Addition or subtraction is the result of combining numbers.")
            else:
                await ctx.send("Alright, feel free to ask if you have any other questions!")
        except Exception as e:
            await ctx.send("Sorry, I couldn't understand the expression. Please provide a valid math question.")

# Run the bot with your Discord bot token
load_dotenv()  # Load from .env
token = os.getenv("DISCORD_TOKEN")
bot.run(token)
