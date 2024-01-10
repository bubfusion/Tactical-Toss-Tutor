
import discord
from discord.ext import commands
from config import BOT_TOKEN


intents = discord.Intents.default()
intents.message_content = True

help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)

client = commands.Bot(command_prefix='$', intents=intents, help_command=help_command)

maps_list = ["mirage", "inferno"]
coming_soon = ["anubis", "vertigo", "overpass", "nuke", "vertigo", "ancient", "dust2", "italy"]

maps_list_display = ["Mirage (WIP)", "Inferno (WIP)"]
coming_soon_display = ["Anubis", "Vertigo", "Overpass", "Nuke", "Vertigo", "Ancient", "Dust 2 (use dust2 in commands)", "Italy"]


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

map_to_dictionary = {
    "mirage" : mirage,
    "inferno" : inferno
}

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
    await client.change_presence(activity=discord.CustomActivity(name='TacToss.xyz | $help',emoji='🤖'))


@client.command(name = "smoke", aliases=["smokes"], brief = "Get GIF of lineup. Usage: $smoke <map> <area>")
async def smoke(ctx, map, area):
    map = map.lower()

    if(map in coming_soon):
        await ctx.send("That map is coming soon! To see the current available maps, try ``$maps``")

    elif(map not in maps_list):
        await ctx.send('Oh no! Looks like you typed in an invalid map. To see the current available maps, try ``$maps``')

    else:
         map_dic = map_to_dictionary[map]
         if(area in map_dic):
             await ctx.send(f'Smoke for {area} \n {map_dic[area]}')
         else:   
            await ctx.send(f'Uh oh, that smoke isnt added yet! To see the current lineups for a map, try ``$lineups <map>``')

@client.command(brief = "Lists maps with smoke lineups")
async def maps(ctx):
    await ctx.send(f"The current maps with smokes are ```{list_to_newline_string(maps_list_display)} \n```Maps that are coming soon are```{list_to_newline_string(coming_soon_display)}```")

@client.command(brief = "Displays lineups for given map. Usage: $lineups <map>")
async def lineups(ctx, map):
    map = map.lower()

    if(map in coming_soon):
        await ctx.send("That map is coming soon! To see the current available maps, try $maps")

    elif(map not in maps_list):
        await ctx.send('Oh no! Looks like you typed in an invalid map. To see the current available maps, try $maps')

    else:
         map_dic = map_to_dictionary[map]
         await ctx.send(f"The current lineups for {map} are ```{dictionary_keys(map_dic)}```")


client.run(BOT_TOKEN)

