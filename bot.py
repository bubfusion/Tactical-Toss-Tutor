
from typing import List, Literal, Union, NamedTuple
import discord
from discord.ext import commands
from discord import app_commands
from config import BOT_TOKEN
from pretty_help import PrettyHelp

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='$', intents=intents, help_command=None)

maps_list = ["mirage", "inferno", "nuke", "overpass"]
coming_soon = ["anubis", "vertigo", "ancient", "dust2"]

maps_list_display = ["Mirage", "Inferno", "Nuke", "Overpass"]
coming_soon_display = ["Anubis", "Vertigo", "Ancient", "Dust 2 (use dust2 in commands)"]

mirage = {
    "jungle": "https://imgur.com/iKj3upn",
    "ct" : "https://imgur.com/a/oKP0u9A",
    "stairs" : "https://imgur.com/49rLNUu",
    "con" : "https://imgur.com/9u2Y08P",
    "cat" : "https://imgur.com/7wWqKUX",
    "marketwindow" : "https://imgur.com/a/VbEsDo6"
}

inferno = {
    "coffin" : "https://imgur.com/Xm2ZAeM",
    "ct" : "https://imgur.com/xXfbicf",
    "halfwall" : "https://imgur.com/MIcZ4WK",
    "library" : "https://imgur.com/t1VZ9IE",
    "arch" : "https://imgur.com/sBCAqI6",
    "short" : "https://imgur.com/KSCNlHY",
    "long" : "https://imgur.com/OzKDwuZ"
}

nuke = {
    "cross" : "https://imgur.com/vK7bMMC \nhttps://imgur.com/N7534PS",
    "red": "https://imgur.com/CTvJNnM \nhttps://imgur.com/RoDHKsB",
    "locker" : "https://imgur.com/HsQbzjT \nhttps://imgur.com/1s7eSEi",
    "garage" : "https://imgur.com/o65YSwo \nhttps://imgur.com/x8PuUzf",
    "decon" : "https://imgur.com/ycVfmwQ \nhttps://imgur.com/EMf37B2",
    "right" : "https://imgur.com/IkORnKL \nhttps://imgur.com/3UL4eBq",
    "unbreakable" : "https://imgur.com/g8dkN8x \nhttps://imgur.com/77EWSFX",
    "lurk" : "https://imgur.com/AXgpP4y \nhttps://imgur.com/dvRkJi3",
    "mini" : "https://imgur.com/mW2t4kQ \nhttps://imgur.com/c7DZJnQ"
}

overpass = {
    "heaven" : "https://imgur.com/05Tgd87",
    "heaven2" : "https://imgur.com/o2F50ma",
    "bathroom" : "https://imgur.com/Q7EBDtt",
    "garbage" : "https://imgur.com/tdz4nzK",
    "bank" : "https://imgur.com/siFBiSz",
    "cross" : "https://imgur.com/1FDi8np",
    "ramp" : "https://imgur.com/EZlW9ee"
}

map_to_dictionary = {
    "mirage" : mirage,
    "inferno" : inferno,
    "nuke" : nuke,
    "overpass" : overpass
}

def get_map_areas(map):
    return list(map_to_dictionary[map].keys())

def list_to_newline_string(list):
    final_string = ""
    for x in list:
        final_string += "\n" + x
    return final_string

def dictionary_keys(d):
    all_keys = ""
    for keys in d.keys():
        all_keys += "\n" + keys
    return all_keys


@client.event
async def on_ready():
    print("Go go go!")
    await client.tree.sync()
    await client.change_presence(activity=discord.CustomActivity(name=' /help | TacToss.xyz '))

@client.tree.command(description="The help command")
async def help (interaction: discord.Interaction):
     await interaction.response.send_message("## Commands \nSee available maps:```/maps``` \nView lineup for specific map: ```/lineups <map>```\nGet a GIF for a specific area you want to smoke```/smoke <map> <area>```\nView commands```/help```\nInvite the bot to your own server```/invite```\nJoin the official Tactical Toss Tutor```/join```\nLink to the Tactical Toss Tutor website```/info```\n")

@client.tree.command(description = "Lists maps with smoke lineups", name="maps")
async def maps(interaction: discord.Interaction):
    await interaction.response.send_message(f"The current maps with smokes are ```{list_to_newline_string(maps_list_display)} \n```Maps that are coming soon are```{list_to_newline_string(coming_soon_display)}```")


@client.tree.command(description = "Get an invite link to the offical Tactical Toss Tutor Discord!")
async def join(interaction: discord.Interaction):
    await interaction.response.send_message("Here is an invite to the Tactical Toss Tutor Discord: https://discord.gg/h572hfZDBh")

@client.tree.command(description = "Get a link to invite the Tactical Toss Tutor bot to your own server!")
async def invite(interaction: discord.Interaction):
    await interaction.response.send_message("You can add me to your own server with this link: https://discord.com/oauth2/authorize?client_id=1194043397451808868")

@client.tree.command(description = "Get a link to the Tactical Toss Tutor website")
async def info(interaction: discord.Interaction):
    await interaction.response.send_message("The offical Tactical Toss Tutor Website: http://tactoss.xyz/")

async def map_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> List[app_commands.Choice[str]]:
    maps = maps_list
    return [
        app_commands.Choice(name=map, value=map)
        for map in maps if current.lower() in map.lower()
    ]

@client.tree.command(description = "Displays lineups for given map. Usage: $lineups <map>")
@app_commands.autocomplete(map=map_autocomplete)
async def lineups(interaction: discord.Interaction, map: str):
    map = map.lower()

    if(map in coming_soon):
        await interaction.response.send_message("That map is coming soon! To see the current available maps, try $maps")

    elif(map not in maps_list):
        await interaction.response.send_message('Oh no! Looks like you typed in an invalid map. To see the current available maps, try $maps')

    else:
         map_dic = map_to_dictionary[map]
         await interaction.response.send_message(f"The current lineups for {map} are ```{dictionary_keys(map_dic)}```")

async def area_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> List[app_commands.Choice[str]]:
    areas = get_map_areas(interaction.namespace.map)
    return [
        app_commands.Choice(name=area, value=area)
        for area in areas if current.lower() in area.lower()
    ]

@client.tree.command(description = "Get GIF of lineup. Usage: $smoke <map> <area>")
@app_commands.autocomplete(map=map_autocomplete, area=area_autocomplete)
async def smoke(interaction: discord.Interaction, map: str, area: str):
    map = map.lower()
    if(map in coming_soon):
        await interaction.response.send_message("That map is coming soon! To see the current available maps, try ``$maps``")

    elif(map not in maps_list):
        await interaction.response.send_message('Oh no! Looks like you typed in an invalid map. To see the current available maps, try ``$maps``')

    else:
        map_dic = map_to_dictionary[map]
        if(area in map_dic):
            print("Smoke call")
            await interaction.response.send_message(f'Smoke for {area} \n {map_dic[area]}')
        else:   
            await interaction.response.send_message(f'Uh oh, that smoke isnt added yet! To see the current lineups for a map, try ``$lineups <map>``')

@client.command()
async def smoke(ctx, map, area):
    await ctx.send("Tactical Toss Tutor now uses slash commands. Try using /smoke!")

@client.command()
async def maps(ctx):
    await ctx.send("Tactical Toss Tutor now uses slash commands. Try using /maps!")
@client.command()
async def lineups(ctx, map):
    await ctx.send("Tactical Toss Tutor now uses slash commands. Try using /lineups!")

@client.command()
async def join(ctx):
    await ctx.send("Tactical Toss Tutor now uses slash commands. Try using /join!")

@client.command()
async def invite(ctx):
    await ctx.send("Tactical Toss Tutor now uses slash commands. Try using /invite!")

@client.command()
async def info(ctx):
    await ctx.send("Tactical Toss Tutor now uses slash commands. Try using /info!")

@client.command()
async def help(ctx):
    await ctx.send("Tactical Toss Tutor now uses slash commands. Try using /help!")

client.run(BOT_TOKEN)

