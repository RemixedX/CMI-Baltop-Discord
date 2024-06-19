import discord
import asyncio
import mariadb
from discord import ui
from discord.utils import get
from discord.ext import commands, tasks
# ^^ You need to install mariadb, discord.py and asyncio (not required) for this to work ^^

token = "Your Token Here"

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(intents=intents, case_insensitive=False, help_command=None)

@bot.event
async def on_ready():
    print("ready")
    await bot.tree.sync()

@bot.tree.command(name="baltop", description="Shows the 10 most richest users")
async def baltop(interaction: discord.Interaction):
    
    # Embed loading - Uncomment if you want to enable this
    #embed = discord.Embed(title=":hourglass_flowing_sand: **Requesting Information from Database...**", color=discord.Color.blue())
    #embed.add_field(name="", value="", inline=True)
    #embed.set_footer(icon_url=interaction.user.display_avatar,text=f"Requested by {interaction.user.name}")

    # Your connection options
    try:
        conn = mariadb.connect(
            host="",
            port=3306,
            user="root",
            password="")
        conn.auto_reconnect = True
        message = await interaction.response.send_message(embed=embed)
    except mariadb.Error as e:
        await interaction.response.send_message(f"Error connecting to the database: {e}")
        sys.exit(1)
        return

    cur = conn.cursor()
    
    # Your desired path where it will pull data from
    # This assumes you have CMI installed
    cur.execute("SELECT Balance, username FROM cmi.cmi_users ORDER BY Balance DESC LIMIT 10")
    data = cur.fetchall()
    curend = conn.close
    
    if not data:
        embed = discord.Embed(title=":warning: No Data Found!", color=0xFFFF00)
        embed.add_field(name="There are no richest users yet!", value="Come back later!", inline=False)
        await interaction.edit_original_response(embed=embed)
        return

    richest_users = ""
    for i, value in enumerate(data, 1):
        balance = value[0]
        username = value[1]

        # Adjust the money prefixes to what you set your economy manager to
        # This is setup to prefix any numbers higher than 999. Remove, append, edit as you see fit
        # If a user's balance surpasses 999T it will overflow, add more prefixes to stick to the number preset, or change it depending on your own needs
        formatted_string = ""
        if balance > 1e12:
            formatted_string = f"**{username}** » **{'${:,.2f}T'.format(balance / 1e12)}**\n"
        elif balance > 1e9:
            formatted_string = f"**{username}** » **{'${:,.2f}B'.format(balance / 1e9)}**\n"
        elif balance > 1e6:
            formatted_string = f"**{username}** » **{'${:,.2f}M'.format(balance / 1e6)}**\n"
        elif balance > 1e3:
            formatted_string = f"**{username}** » **{'${:,.2f}K'.format(balance / 1e3)}**\n"
        else:
            formatted_string = f"**{username}** » **{'${:,.2f}'.format(balance)}**\n"

        richest_users += f"{i}. {formatted_string}\n"

    # The final Embed which will return the baltop
    embed = discord.Embed(title=":moneybag: **Leaderboards:**", color=0xDAA520)
    embed.set_thumbnail(url=bot.user.display_avatar.url)
    embed.description = richest_users
    curend
    await asyncio.sleep(4)    
    await interaction.edit_original_response(embed=embed)
    # Uncomment these if you want the leaderboard to delete itself. adjust the sleep duration to suit your needs (in seconds)
    #await asyncio.sleep(60)
    #await interaction.delete_original_response()
    return

bot.run(token)
# Invite the bot after you run this once for the slashcommand to appear