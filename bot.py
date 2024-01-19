
import discord
from discord.ext import commands
from config import BOT_TOKEN
import KillReward
from pretty_help import PrettyHelp

intents = discord.Intents.default()
intents.message_content = True


help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)

client = commands.Bot(command_prefix='$', intents=intents, help_command=PrettyHelp(no_category = "Commands", show_index=False))


maps_list = ["mirage", "inferno", "nuke", "overpass"]
coming_soon = ["anubis", "vertigo", "vertigo", "ancient", "dust2"]

maps_list_display = ["Mirage", "Inferno", "Nuke", "Overpass"]
coming_soon_display = ["Anubis", "Vertigo", "Vertigo", "Ancient", "Dust 2 (use dust2 in commands)"]

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
    "cross" : "https://imgur.com/vK7bMMC",
    "red": "https://imgur.com/CTvJNnM",
    "locker" : "https://imgur.com/HsQbzjT",
    "garage" : "https://imgur.com/o65YSwo",
    "decon" : "https://imgur.com/ycVfmwQ",
    "right" : "https://imgur.com/IkORnKL",
    "unbreakable" : "https://imgur.com/g8dkN8x",
    "lurk" : "https://imgur.com/AXgpP4y",
    "mini" : "https://imgur.com/mW2t4kQ"
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
    await client.change_presence(activity=discord.CustomActivity(name='TacToss.xyz | $help'))


@client.command(name = "smoke", aliases=["smokes", "s"], brief = "Get GIF of lineup. Usage: $smoke <map> <area>")
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


@client.command(brief = "Lists maps with smoke lineups", aliases=["lineup", "l"])
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

@client.command(brief = "Get an invite link to the offical Tactical Toss Tutor Discord!")
async def join(ctx):
    await ctx.send("Here is an invite to the Tactical Toss Tutor Discord: https://discord.gg/h572hfZDBh")

@client.command(brief = "Get a link to invite the Tactical Toss Tutor bot to your own server!")
async def invite(ctx):
    await ctx.send("You can add me to your own server with this link: https://discord.com/api/oauth2/authorize?client_id=1194043397451808868&permissions=125952&scope=bot")

@client.command(brief = "Get a link to the Tactical Toss Tutor website")
async def info(ctx):
    await ctx.send("The offical Tactical Toss Tutor Website: http://tactoss.xyz/")

@client.command(brief = "Gets the kill reward for a weapon. Usage: $kr <weapon>")
async def kr(ctx, weapon):
    weapon = weapon.lower()
    if (weapon in KillReward.kill_reward):
        await ctx.send(F"{weapon} kill-reward: ${KillReward.kill_reward[weapon]}")
    else:
        await ctx.send("Can't find that weapon! Try $weapons to see the avaliable weapons")

@client.command(brief = "Get the list of weapons in CS2")
async def weapons(ctx):
    await ctx.send(F"```{dictionary_keys(KillReward.kill_reward_display)}```")

client.run(BOT_TOKEN)

