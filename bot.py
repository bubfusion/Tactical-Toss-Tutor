
from typing import List, Literal, Union, NamedTuple
import discord
from discord.ext import commands
from discord import app_commands
from config import BOT_TOKEN
from pretty_help import PrettyHelp

intents = discord.Intents.default()
client = commands.Bot(command_prefix='$', intents=intents, help_command=None)

maps_list = ["mirage", "inferno", "nuke", "overpass", "vertigo", "anubis"]
coming_soon = ["ancient", "dust 2"]

maps_list_display = ["Mirage", "Inferno", "Nuke", "Overpass", "Vertigo", "Anubis"]
coming_soon_display = ["Ancient", "Dust 2"]



vertigo = {
    "a left" : "https://imgur.com/eQrvQ9N \nhttps://imgur.com/NWb7hHM",
    "a right" : "https://imgur.com/81yaPTs \nhttps://imgur.com/BOQWlEE",
    "boost" : "https://imgur.com/88LzrIv \nhttps://imgur.com/LMzNecp",
    "mid heaven": "https://imgur.com/i7ZzrTj \nhttps://imgur.com/kQhOFSa",
    "b headshot" : "https://imgur.com/8qKATMI \nhttps://imgur.com/433jTiK",
    "gen right" : "https://imgur.com/DG1UT2h \nhttps://imgur.com/CbvUiZV",
    "gen left" : "https://imgur.com/V4gB1Tp \nhttps://imgur.com/ZcXtNfZ",
    "a ramp" : "https://imgur.com/ogsC8Cp \nhttps://imgur.com/Uy841QS"
}

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

anubis = {
    "window" : "https://imgur.com/b1YAWOV\nhttps://imgur.com/9vo2GX7",
    "con" : "https://imgur.com/CR5U3Xt\nhttps://imgur.com/N8AyjY9",
    "con deep": "https://imgur.com/Tay7XPE\nhttps://imgur.com/vRXRlkk",
    "temple mid" : "https://imgur.com/37vPkUV\nhttps://imgur.com/XFa33vy",
    "b left fast" : "https://imgur.com/11jJhI0\nhttps://imgur.com/kXYXAen",
    "b left" : "https://imgur.com/P7fBUTM\nhttps://imgur.com/IYyiDfz",
    "temple" : "https://imgur.com/VaVOA52\nhttps://imgur.com/Kr1N6U0",
    "b ct" : "https://imgur.com/Cg8XxPU\nhttps://imgur.com/BCKp4nP",
    "b right" : "https://imgur.com/CdiLuUo\nhttps://imgur.com/0nCYOqr",
    "a lurk" : "https://imgur.com/fssJf9r\nhttps://imgur.com/pUCMU1z",
    "heaven" : "**THIS IS A W+JUMP THROW**\nhttps://imgur.com/vS0gOWK\nhttps://imgur.com/bBnugST",
    "camera" : "https://imgur.com/eercpSO\nhttps://imgur.com/nkn27pT"


}

map_to_dictionary = {
    "mirage" : mirage,
    "inferno" : inferno,
    "nuke" : nuke,
    "overpass" : overpass,
    "vertigo" : vertigo,
    "anubis": anubis
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

@client.tree.command(description = "Displays lineups for given map. Usage: /lineups <map>")
@app_commands.autocomplete(map=map_autocomplete)
async def lineups(interaction: discord.Interaction, map: str):
    map = map.lower()

    if(map in coming_soon):
        await interaction.response.send_message("That map is coming soon! To see the current available maps, try /maps")

    elif(map not in maps_list):
        await interaction.response.send_message('Oh no! Looks like you typed in an invalid map. To see the current available maps, try /maps')

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

@client.tree.command(description = "Get GIF of lineup. Usage: /smoke <map> <area>")
@app_commands.autocomplete(map=map_autocomplete, area=area_autocomplete)
async def smoke(interaction: discord.Interaction, map: str, area: str):
    map = map.lower()
    if(map in coming_soon):
        await interaction.response.send_message("That map is coming soon! To see the current available maps, try ``/maps``")

    elif(map not in maps_list):
        await interaction.response.send_message('Oh no! Looks like you typed in an invalid map. To see the current available maps, try ``/maps``')

    else:
        map_dic = map_to_dictionary[map]
        if(area in map_dic):
            print("Smoke call")
            if map == "vertigo":
                await interaction.response.send_message(f'WARINING VERTIGO SMOKES MAY BE OUT OF DATE! Smoke for {area} \n{map_dic[area]}')
            else:
                await interaction.response.send_message(f'Smoke for {area} \n{map_dic[area]}')
        else:   
            await interaction.response.send_message(f'Uh oh, that smoke isnt added yet! To see the current lineups for a map, try ``/lineups <map>``')

client.run(BOT_TOKEN)

