
import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='$', intents=intents)

maps_list = ["mirage"]
coming_soon = ["anubis", "vertigo", "overpass", "nuke", "vertigo", "ancient", "dust2", "italy"]

maps_list_display = ["Mirage"]
coming_soon_display = ["Anubis", "Vertigo", "Overpass", "Nuke", "Vertigo", "Ancient", "Dust 2 (use dust2 in commands)", "Italy"]


mirage = {
    "jungle": "https://imgur.com/Q7tpOYV"
}

map_to_dictionary = {
    "mirage" : mirage
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

@client.command(aliases=["smoke", "smokes"])
async def _smoke(ctx, map, smoke):
    map = map.lower()

    if(map in coming_soon):
        await ctx.send("That map is coming soon!")

    elif(map not in maps_list):
        await ctx.send('Oh no! Looks like you typed in an invalid map')

    else:
         map_dic = map_to_dictionary[map]
         if(smoke in map_dic):
             await ctx.send(f'{map_dic[smoke]}')
         else:   
            await ctx.send(f'Uh oh, that smoke isnt added yet!')

@client.command(aliases=["map", "maps"])
async def _maps(ctx):
    await ctx.send(f"The current maps with smokes are ```{list_to_newline_string(maps_list_display)} \n```Maps that are coming soon are```{list_to_newline_string(coming_soon_display)}```")

@client.command()
async def lineups(ctx, map):
    map = map.lower()

    if(map in coming_soon):
        await ctx.send("That map is coming soon!")

    elif(map not in maps_list):
        await ctx.send('Oh no! Looks like you typed in an invalid map')

    else:
         map_dic = map_to_dictionary[map]
         await ctx.send(f"The current lineups for {map} are ```{dictionary_keys(map_dic)}```")

class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(color=discord.Color.blurple(), description='')
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)

client.help_command = MyHelpCommand()


client.run("MTE5NDA0MzM5NzQ1MTgwODg2OA.GN5UfP.lKwRvttz6kYbAQN4Rg0H4AF4HzAmqPgoGl77Uc")


