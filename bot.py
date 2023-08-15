import discord 
from itertools import cycle
from discord.ext import commands, tasks
import random
import asyncio
import json 
from discord.utils import get
import datetime
import os
from discord.ext.commands import has_permissions
from operator import itemgetter

# WHITE      : 0xFFFFFF
# AQUA       : 0x1ABC9C
# GREEN      : 0x2ECC71
# BLUE       : 0x3498DB
# PURPLE     : 0x9B59B6
# PINK       : 0xE91E63
# GOLD       : 0xF1C40F
# ORANGE     : 0xE67E22
# RED        : 0xE74C3C
# NAVY       : 0x34495E
# DARK_AQUA  : 0x11806A
# DARK_GREEN : 0x1F8B4C
# DARK_BLUE  : 0x206694

#=======================================================================

NO_BANK_ACC = "you don\'t have a bank account yet, run the `plead` command"

def get_prefix(bot, message):
  if not message.guild:
    return commands.when_mentioned_or("le ")(bot, message)
  
  with open ('prefixes.json', 'r') as f:
    prefixes = json.load(f)

  if str(message.guild.id) not in prefixes:
    return commands.when_mentioned_or("le ")(bot, message)

  prefix = prefixes[str(message.guild.id)]
  return commands.when_mentioned_or(prefix)(bot, message)

def read_json(file_path):
  try:
    with open(file_path, "r") as file:
      data = json.load(file)
      return data
  except json.JSONDecodeError:
    return {}
  except FileNotFoundError:
    return {"blacklistedUsers": []}
    
def write_json(data, file_path):
  with open(file_path, "w") as file:
    if "blacklistedUsers" not in data:
      data["blacklistedUsers"] = []

    data["blacklistedUsers"] = list(set(data["blacklistedUsers"]))
    json.dump(data, file, indent = 4)

#=======================================================================

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = commands.when_mentioned and get_prefix, intents = intents)
epoch = datetime.datetime.utcfromtimestamp(0)
bot.remove_command("help")
status = cycle(['le help'])

random_colors = [0xFFFFFF, 0x1ABC9C, 0x2ECC71, 0x3498DB, 0x9B59B6, 0xE91E63, 0xF1C40F, 0xE67E22, 0xE74C3C, 0x34495E, 0x11806A, 0x1F8B4C, 0x206694]

NUMBERS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
VOWELS = ["a", "e", "i", "o", "u"]

START_BAL     = 100 
START_HEALTH  = 100

BALANCES_FILE = 'balances.json'
balances      = {} 

SHEEPS_FILE   = 'sheeps.json'
sheeps        = {}

WOOL_FILE     = 'wools.json'
wools         = {}

RICE_FILE     = 'rices.json'
rices         = {}

WHEAT_FILE    = 'wheats.json'
wheats        = {}

PIG_FILE      = 'pigs.json'
pigs          = {}

MEAT_FILE     = 'meats.json'
meats         = {}

HEALTH_FILE   = 'healths.json'
healths       = {}  

AMBULANCES_FILE = 'ambulances.json'
ambulances    = {}

BUFFALOS_FILE = 'buffalos.json'
buffalos      = {}

STOVES_FILE   = 'stoves.json'
stoves        = {}

SALADS_FILE   = 'salads.json'
salads        = {}

UNCOOKED_CHICKENS_FILE = 'uncooked_chickens.json'
uncooked_chickens = {}

COOKED_CHICKENS_FILE = 'cooked_chickens.json'
cooked_chickens = {}

MORRIS_FILE = 'morris.json'
morris = {}

DOUGLAS_FILE = 'douglas.json'
douglas = {}

LOCATIONS_FILE = 'locations.json'
locations = {}

CITIES_FILE = 'cities.json'
cities = {}

CITYPOP_FILE = 'citypop.json'
citypop = {}

ENTERTAINMENT_LVL_FILE = 'entertainment_lvl.json'
entertainment_lvl = {}

PC_FILE = 'pc_file.json'
pc = {}

PARK_LVL_FILE = 'park_lvl.json'
park_lvl = {}

POWER_LVL_FILE = 'power_lvl.json'
power_lvl = {}

BLACKLISTED_FILE = 'blacklist.json'
blacklisted = {}

BREAD_FILE = 'bread.json'
bread = {}

MOOSHROOM_COW_FILE = 'mooshroom_cows.json'
mooshroom_cows = {}

BOWLS_FILE = 'bowls.json'
bowls = {}

MUSHROOM_STEW_FILE = 'mushroom_stew.json'
mushroom_stew = {}

TIMES_MOOSHROOM = 'times_mooshroom.json'
times_mooshroom = {}

WATER_LVL_FILE = 'water_lvl.json'
water_lvl = {}

WASTE_LVL_FILE = 'waste_lvl.json'
waste_lvl = {}

COMMANDS_FILE = 'commands.json'
commands2 = {}

LEVEL_FILE = 'levels.json'
levels = {}

EXP_FILE = 'exp.json'
exp = {}

HEALTH_LVL_FILE = 'health_lvl.json'
health_lvl = {}

ALLOW_REACTION_MESSAGE = 'allowreactionmessage.json'
allowreactionmessage = {}

PERSONAL_STRING = 'personalstring.json'
personalstring = {}

ALLOW_MEMBER_MESSAGE_FILE = 'allowmembermessage.json'
allowmembermessage = {}

MEMBER_MESSAGE_FILE = 'membermessage.json'
membermessage = {}

CHANNEL_ID = 'channelid.json'
channel_id = {}

FIRE_LVL_FILE = 'fire_lvl.json'
fire_lvl = {}

POLICE_LVL_FILE = 'police_lvl.json'
police_lvl = {}

FLY_DELAY_SEC  = 0.5
FLY_DELAY_ITER = 5 

autoMeme = False

bot.blacklisted_users = []

@tasks.loop(seconds=20)
async def change_status():
  await bot.change_presence(status = discord.Status.idle, activity=discord.Game(name="le help"))

def openfile(FILE_NAME):
  try:
    with open(FILE_NAME, 'r') as fp:
      return json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {FILE_NAME} not found. Starting off with an empty dictionary')
    return {}

def savefile(f, FILE_NAME):
  try: 
    with open(FILE_NAME, 'w') as fp: 
      json.dump(f, fp) 
  except FileNotFoundError: 
    return

#======================================================================
# EVENTS

@bot.event
async def on_ready():
  change_status.start()
  print(f'{bot.user.name} is ready')

  try:
    data = read_json("blacklist.json")
    bot.blacklisted_users = data.get("blacklistedUsers", [])
  except Exception as e:
    print(e)

@bot.event
async def on_member_join(member):
  server = str(member.guild.id)

  membermessage = openfile(MEMBER_MESSAGE_FILE)
  allowmembermessage = openfile(ALLOW_MEMBER_MESSAGE_FILE)
  channel_id = openfile(CHANNEL_ID)

  membermessage[server] = membermessage[server] if server in membermessage else ''
  allowmembermessage[server] = allowmembermessage[server] if server in allowmembermessage else 0
  channel_id[server] = channel_id[server] if server in channel_id else 0

  if allowmembermessage[server] == 1:
    if membermessage[server] == '':
      return
    else:
      if channel_id[server] == 0:
        return
      else:
        channel = await bot.fetch_channel(channel_id[server])
        await channel.send(f'{member.mention}, {membermessage[server]}')
  else:
    return

@bot.event
async def on_message(message):
  if message.author.id == bot.user.id:
    return

  if str(message.author.id) in bot.blacklisted_users:
    return  

  await bot.process_commands(message)

@bot.event
async def on_command(ctx):
  user = str(ctx.message.author.id)

  levels = openfile(LEVEL_FILE)
  exp = openfile(EXP_FILE)
  commands2 = openfile(COMMANDS_FILE)

  levels[user] = levels[user] if user in levels else 0
  exp[user] = exp[user] if user in exp else 0
  commands2[user] = commands2[user] if user in commands2 else 0
  commands2[user] += 1

  MAX_XP = levels[user] * 100
  BEFORE_LEVEL_UP = MAX_XP - 10

  if exp[user] == BEFORE_LEVEL_UP:
    levels[user] += 1
    exp[user] = 10
  else:
    if exp[user] < MAX_XP:
      exp[user] += 10
    else:
      levels[user] += 1
      exp[user] = 10

  savefile(commands2, COMMANDS_FILE)
  savefile(levels, LEVEL_FILE)
  savefile(exp, EXP_FILE)

@bot.event
async def on_reaction_add(reaction, user):
  server = str(reaction.message.guild.id)

  allowreactionmessage = openfile(ALLOW_REACTION_MESSAGE)

  allowreactionmessage[server] = allowreactionmessage[server] if server in allowreactionmessage else 0
  channel = reaction.message.channel

  while allowreactionmessage[server] == 1:
    await channel.send(f'{user.name} reacted with {reaction.emoji} to the message: `{reaction.message.content}`')
    break

#============================================================================

#============================================================================
# ADMIN 

@bot.command()
async def blacklist(ctx, user: discord.Member):
  x = str(user.id)

  if str(ctx.message.author.id) == "707091184115253248":
    if x not in bot.blacklisted_users:
      bot.blacklisted_users.append(x)
      data = read_json("blacklist.json")

      if "blacklistedUsers" not in data:
        data["blacklistedUsers"] = []
        
      data["blacklistedUsers"].append(x)
      write_json(data, "blacklist.json")
      await ctx.send(f'**{user.name}** has been blacklisted')
    else:
      await ctx.send('alr blacklisted')
  else:
    await ctx.send('only owner can do this')

@bot.command()
async def unblacklist(ctx, user: discord.Member):
  x = str(user.id)

  if str(ctx.message.author.id) == "707091184115253248":
    if x in bot.blacklisted_users:
      bot.blacklisted_users.remove(x)
      data = read_json("blacklist.json")

      if "blacklistedUsers" not in data:
        data["blacklistedUsers"] = []

      if x in data["blacklistedUsers"]:
        data["blacklistedUsers"].remove(x)
        write_json(data, "blacklist.json")
        await ctx.send(f'**{user.name}** has been unblacklisted')
      else:
        await ctx.send(f'**{user.name}** was never blacklisted')
    else:
      await ctx.send(f'**{user.name}** was never blacklisted')
  else:
    await ctx.send(f'only owner can do this')

#============================================================================

#============================================================================
# SETTINGS

@bot.command(aliases = ['sp'])
async def setprefix(ctx, *, pre):
  await ctx.send('Would you like a space after the prefix?\nEx: [prefix] [command]\n`y` or `n`')
  msg = await bot.wait_for('message', check = lambda m: m.author == ctx.author)

  if msg.content.lower() == 'y':
    
    with open(r"prefixes.json", 'r') as f:
      prefixes = json.load(f)

    pre2 = pre + ' '
    prefixes[str(ctx.guild.id)] = pre2
    embed = discord.Embed(description = f'Changed prefix to `{pre} `', color = random.choice(random_colors))
    await ctx.send(embed = embed)

    with open(r"prefixes.json", 'w') as f:
      json.dump(prefixes, f, indent = 4)
  elif msg.content.lower() == 'n':
    with open(r"prefixes.json", 'r') as f:
      prefixes = json.load(f)

      prefixes[str(ctx.guild.id)] = pre
      embed = discord.Embed(description = f'Changed prefix to `{pre}`', color = random.choice(random_colors))
      await ctx.send(embed = embed)

    with open(r"prefixes.json", 'w') as f:
      json.dump(prefixes, f, indent = 4)
  else:
    await ctx.send('not an option; rerun the command')

@bot.command(aliases = ['rp'])
async def resetprefix(ctx):

  with open(r"prefixes.json", 'r') as f:
    prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = 'le '
    embed = discord.Embed(description = f'Changed prefix back to `le`', color = random.choice(random_colors))
    await ctx.send(embed = embed)

  with open(r"prefixes.json", 'w') as f:
    json.dump(prefixes, f, indent = 4)

#============================================================================

#=============================================================================================================
# MODERATION 

@bot.command(aliases = ['mm'])
@has_permissions(manage_guild = True)
async def membermessage(ctx):

  server = str(ctx.guild.id)
  allowmembermessage = openfile(ALLOW_MEMBER_MESSAGE_FILE)
  allowmembermessage[server] = allowmembermessage[server] if server in allowmembermessage else 0

  if allowmembermessage[server] == 0:
    await ctx.send('Sending messages when a member joins is set to: **True**\nCustomize the message in `le setmembermessage`')
    allowmembermessage[server] = 1
  else:
    await ctx.send('Sending messages when a member joins is set to: **False**')
    allowmembermessage[server] = 0

  savefile(allowmembermessage, ALLOW_MEMBER_MESSAGE_FILE)

@bot.command(aliases = ['smm'])
@has_permissions(manage_guild=True)
async def setmembermessage(ctx, *, string: str):
  server = str(ctx.guild.id)

  allowmembermessage = openfile(ALLOW_MEMBER_MESSAGE_FILE)
  membermessage = openfile(MEMBER_MESSAGE_FILE)

  allowmembermessage[server] = allowmembermessage[server] if server in allowmembermessage else 0
  membermessage[server] = membermessage[server] if server in membermessage else ''

  if allowmembermessage[server] == 1:
    await ctx.send(f'The final result will look like this:\n***member is mentioned here***, {string}\nGood? `y` or `n`')
    msg = await bot.wait_for('message', check = lambda m: m.author == ctx.author)
    if msg.content.lower() == 'y' or msg.content.lower() == 'Y':
      membermessage[server] = string
      await ctx.send('completed, btw you need to give me a proper channel id to send the messages to using `le setchannelid`\nif the id isn\'t valid, then you can guess why its not working')
    elif msg.content.lower() == 'N' or msg.content.lower() == 'n':
      await ctx.send('rip lol you chose not to use that')
      membermessage[server] == ''
  else:
    await ctx.send('you don\'t even have member joining messaging enabled! to do that do `le membermessage`')

  savefile(membermessage, MEMBER_MESSAGE_FILE)

@bot.command(aliases = ['vmm'])
async def viewmembermessage(ctx):
  server = str(ctx.guild.id)

  membermessage = openfile(MEMBER_MESSAGE_FILE)
  allowmembermessage = openfile(ALLOW_MEMBER_MESSAGE_FILE)

  if allowmembermessage[server] == 1:
    if server in membermessage:
      if membermessage[server] == '':
        await ctx.send('you don\'t have a member joining message set!')
      else:
        await ctx.send(f'{membermessage[server]}')
    else:
      await ctx.send('you don\'t have a member joining message set!')
  else:
    await ctx.send('you don\'t even have member joining messaging enabled! to do that use the command `membermessage`')

@bot.command(aliases = ['sci'])
@has_permissions(manage_guild = True)
async def setchannelid(ctx, id: int):
  server = str(ctx.guild.id)

  allowmembermessage = openfile(ALLOW_MEMBER_MESSAGE_FILE)
  channel_id = openfile(CHANNEL_ID)

  allowmembermessage[server] = allowmembermessage[server] if server in allowmembermessage else 0
  channel_id[server] = channel_id[server] if server in channel_id else 0
  
  with open(r"prefixes.json", 'r') as f:
    prefixes = json.load(f)

  x = prefixes[str(ctx.guild.id)] if str(ctx.guild.id) in prefixes else 'le '

  if len(str(id)) != 19:
    await ctx.send('that isn\'t a valid channel id')
    return
    
  if allowmembermessage[server] == 1:  
    channel_id[server] = id
    await ctx.send(f'set channel id as: `{id}`')
  else:
    await ctx.send(f'i can\'t do that without the member joining message function enabled buddy\nenable it by using `{x}membermessage`')

  savefile(channel_id, CHANNEL_ID)

@bot.command()
@has_permissions(manage_guild = True)
async def reactionmessage(ctx):
  server = str(ctx.guild.id)
  
  allowmembermessage = openfile(ALLOW_MEMBER_MESSAGE_FILE)
 
  allowreactionmessage[server] = allowreactionmessage[server] if server in allowreactionmessage else 0
  
  if allowreactionmessage[server] == 0:
    await ctx.send('Sending messages when reactions are executed is set to: **True**')
    allowreactionmessage[server] = 1
  else:
    await ctx.send('Sending messages when reactions are executed is set to: **False**')
    allowreactionmessage[server] = 0

  savefile(allowmembermessage, ALLOW_MEMBER_MESSAGE_FILE)

#============================================================================

#============================================================================
# FUN

@bot.command()
async def status(ctx, member: discord.Member = None):
  if member is None:
    member = ctx.message.author

  await ctx.send(member.status)

@bot.command()
async def fat(ctx, member: discord.Member = None):
  if member is None:
    embed = discord.Embed(title="fatness determiner", description=f"you are {random.randint(1, 100)}% fat", color = random.choice(random_colors))
    await ctx.send(embed=embed)
  else:
    embed = discord.Embed(title="fatness determiner", description=f"{member.name} is {random.randint(1, 100)}% fat", color = random.choice(random_colors))
    await ctx.send(embed=embed)

@bot.command()
async def slots(ctx):
  parrot = ':parrot:'
  slotspin = ':man_farmer_tone5:'
  slots = [':blue_heart:', ':blue_heart:', ':blue_heart:', ':purple_heart:', ':heart:', ':yellow_heart:', ':green_heart:', ':green_heart:', ':green_heart:', ':green_heart:', ':green_heart:', ':green_heart:']
  slot1 = slots[random.randint(0, 11)]
  slot2 = slots[random.randint(0, 11)]
  slot3 = slots[random.randint(0, 11)]
  slot4 = slots[random.randint(0, 11)]
  slot5 = slots[random.randint(0, 11)]
  slot6 = slots[random.randint(0, 11)]
  slot7 = slots[random.randint(0, 11)]
  slot8 = slots[random.randint(0, 11)]
  slot9 = slots[random.randint(0, 11)]
  slot10 = slots[random.randint(0, 11)]
  slot11 = slots[random.randint(0, 11)]
  slot12 = slots[random.randint(0, 11)]
  slot13 = slots[random.randint(0, 11)]
  slot14 = slots[random.randint(0, 11)]
  slot15 = slots[random.randint(0, 11)]
  slot16 = slots[random.randint(0, 11)]
  slot17 = slots[random.randint(0, 11)]
  slot18 = slots[random.randint(0, 11)]
  slot19 = slots[random.randint(0, 11)]
  slot20 = slots[random.randint(0, 11)]
  slot21 = slots[random.randint(0, 11)]
  slot22 = slots[random.randint(0, 11)]
  slot23 = slots[random.randint(0, 11)]
  slot24 = slots[random.randint(0, 11)]
  slot25 = slots[random.randint(0, 11)]

  slotOutput = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25)
  slotOutput1 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin, slotspin,)
  results0 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(parrot, parrot, parrot, parrot, parrot, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25)
  results1 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(slot1, slot2, slot3, slot4, slot5, parrot, parrot, parrot, parrot, parrot, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25)
  results2 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, parrot, parrot, parrot, parrot, parrot, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25)
  results3 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, parrot, parrot, parrot, parrot, parrot, slot21, slot22, slot23, slot24, slot25)
  results4 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, parrot, parrot, parrot, parrot, parrot)
  results5 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(parrot, slot2, slot3, slot4, slot5, parrot, slot7, slot8, slot9, slot10, parrot, slot12, slot13, slot14, slot15, parrot, slot17, slot18, slot19, slot20, parrot, slot22, slot23, slot24, slot25)
  results6 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(slot1, parrot, slot3, slot4, slot5, slot6, parrot, slot8, slot9, slot10, slot11, parrot, slot13, slot14, slot15, slot16, parrot, slot18, slot19, slot20, slot21, parrot, slot23, slot24, slot25)
  results7 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(slot1, slot2, parrot, slot4, slot5, slot6, slot7, parrot, slot9, slot10, slot11, slot12, parrot, slot14, slot15, slot16, slot17, parrot, slot19, slot20, slot21, slot22, parrot, slot24, slot25)
  results8 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(slot1, slot2, slot3, parrot, slot5, slot6, slot7, slot8, parrot, slot10, slot11, slot12, slot13, parrot, slot15, slot16, slot17, slot18, parrot, slot20, slot21, slot22, slot23, parrot, slot25)
  results9 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(slot1, slot2, slot3, slot4, parrot, slot6, slot7, slot8, slot9, parrot, slot11, slot12, slot13, slot14, parrot, slot16, slot17, slot18, slot19, parrot, slot21, slot22, slot23, slot24, parrot)
  results10 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(parrot, slot2, slot3, slot4, slot5, slot6, parrot, slot8, slot9, slot10, slot11, slot12, parrot, slot14, slot15, slot16, slot17, slot18, parrot, slot20, slot21, slot22, slot23, slot24, parrot)
  results11 = '| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n'.format(slot1, slot2, slot3, slot4, parrot, slot6, slot7, slot8, parrot, slot10, slot11, slot12, parrot, slot14, slot15, slot16, parrot, slot18, slot19, slot20, parrot, slot22, slot23, slot24, slot25)

  msg = await ctx.message.channel.send("{}\n {} Is Spinning".format(slotOutput1,ctx.message.author.mention))
  await asyncio.sleep(2)
  await msg.edit(content='| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n {} Is Spinning'.format(slot1, slotspin, slotspin, slotspin, slotspin, slot6, slotspin, slotspin, slotspin, slotspin, slot11, slotspin, slotspin, slotspin, slotspin, slot16, slotspin, slotspin, slotspin, slotspin, slot21, slotspin, slotspin, slotspin, slotspin, ctx.message.author.mention))
  await asyncio.sleep(2)
  await msg.edit(content='| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n {} Is Spinning'.format(slot1, slot2, slotspin, slotspin, slotspin, slot6, slot7, slotspin, slotspin, slotspin, slot11, slot12, slotspin, slotspin, slotspin, slot16, slot17, slotspin, slotspin, slotspin, slot21, slot22, slotspin, slotspin, slotspin, ctx.message.author.mention))
  await asyncio.sleep(2)
  await msg.edit(content='| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n {} Is Spinning'.format(slot1, slot2, slot3, slotspin, slotspin, slot6, slot7, slot8, slotspin, slotspin, slot11, slot12, slot13, slotspin, slotspin, slot16, slot17, slot18, slotspin, slotspin, slot21, slot22, slot23, slotspin, slotspin, ctx.message.author.mention))
  await asyncio.sleep(2)
  await msg.edit(content='| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n {} Is Spinning'.format(slot1, slot2, slot3, slot4, slotspin, slot6, slot7, slot8, slot9, slotspin, slot11, slot12, slot13, slot14, slotspin, slot16, slot17, slot18, slot19, slotspin, slot21, slot22, slot23, slot24, slotspin, ctx.message.author.mention))
  await asyncio.sleep(2)
  await msg.edit(content='| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n| {} | {} | {} | {} | {} |\n {} Is Spinning'.format(slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10, slot11, slot12, slot13, slot14, slot15, slot16, slot17, slot18, slot19, slot20, slot21, slot22, slot23, slot24, slot25, ctx.message.author.mention))

  if slot1 == slot2 == slot3 == slot4 == slot5:
      #await ctx.message.channel.send( "{}\n {} you Won".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} you Won".format(results0,ctx.message.author.mention),delete_after=3)
  elif slot6 == slot7 == slot8 == slot9 == slot10:
      #await ctx.message.channel.send( "{}\n {} you Won".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} you Won".format(results1,ctx.message.author.mention),delete_after=3)
  elif slot11 == slot12 == slot13 == slot14 == slot15:
      #await ctx.message.channel.send( "{}\n {} you Won".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} you Won".format(results2,ctx.message.author.mention),delete_after=3)
  elif slot16 == slot17 == slot18 == slot19 == slot20:
      #await ctx.message.channel.send( "{}\n {} you Won".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} you Won".format(results3,ctx.message.author.mention),delete_after=3)
  elif slot21 == slot22 == slot23 == slot24 == slot25:
      #await ctx.message.channel.send( "{}\n {} you Won".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} you Won".format(results4,ctx.message.author.mention),delete_after=3)
  elif slot1 == slot6 == slot11 == slot16 == slot21:
      #await ctx.message.channel.send( "{}\n {} you Won".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} you Won".format(results5,ctx.message.author.mention),delete_after=3)
  elif slot2 == slot7 == slot12 == slot17 == slot22:
      #await ctx.message.channel.send( "{}\n {} you Won".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} you Won".format(results6,ctx.message.author.mention),delete_after=3)
  elif slot3 == slot8 == slot13 == slot18 == slot23:
      #await ctx.message.channel.send( "{}\n {} you Won".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} you Won".format(results7,ctx.message.author.mention),delete_after=3)
  elif slot4 == slot9 == slot14 == slot19 == slot24:
      #await ctx.message.channel.send( "{}\n {} you Won".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} you Won".format(results8,ctx.message.author.mention),delete_after=3)
  elif slot5 == slot10 == slot15 == slot20 == slot25:
      #await ctx.message.channel.send( "{}\n {} you Won".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} you Won".format(results9,ctx.message.author.mention),delete_after=3)
  elif slot1 == slot7 == slot13 == slot19 == slot25:
      #await ctx.message.channel.send( "{}\n {} you Won".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} you Won".format(results10,ctx.message.author.mention),delete_after=3)
  elif slot5 == slot9 == slot13 == slot17 == slot21:
      #await ctx.message.channel.send( "{}\n {} you Won".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} you Won".format(results11,ctx.message.author.mention),delete_after=3)
  else:
      #await ctx.message.channel.send("{}\n {} you Lost".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} you Lost".format(slotOutput,ctx.message.author.mention))

@bot.command()
async def guess(ctx):
  await ctx.send('guess a number from 1-10')
  answer = random.randint(1, 10)
  msg = await bot.wait_for('message', check = lambda m: m.author == ctx.author, timeout = 6.0)

  if msg.content.startswith(f'{answer}'):
    await ctx.send('correct')
  else:
    await ctx.send(f'lol it was {answer}')

#============================================================================
# ECONOMY COMMANDS

#=============================================================================================================
# COLLECT

@bot.group()
async def collect(ctx):
  if ctx.subcommand_passed is None:
    await ctx.send('Proper Usage: `collect [power/water/waste/fire/police/health/entertainment/parks]`')
  elif ctx.invoked_subcommand is None:
    await ctx.send(f"that section doesn't exist buddy")

@collect.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def health(ctx):
  user = str(ctx.message.author.id)
  global health_lvl, citypop, cities, balances, buffalos
  citypop[user] = citypop[user] if user in citypop else 0
  cities[user] = cities[user] if user in cities else 0
  health_lvl[user] = health_lvl[user] if user in health_lvl else 0
  buffalos[user] = buffalos[user] if user in buffalos else 0
  balances[user] = balances[user] if user in balances else 0

  if cities[user] == 1:
    if health_lvl[user] > 0:
      if citypop[user] > 0:
        CHANCE_OF_BUFFALO_YEETING = random.randint(1,100)
        if CHANCE_OF_BUFFALO_YEETING < 25 or CHANCE_OF_BUFFALO_YEETING == 25:
          buffalos[user] += 1
          health_popz_added = health_lvl[user] * 7819
          HEALTH_REVENUE = health_popz_added * 120
          embed = discord.Embed(title = 'Collection Complete', description = f'you gained `{HEALTH_REVENUE:,d} coins` of **Health Revenue** from your population and 1 :water_buffalo: **Buffalo** HOW TF', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += HEALTH_REVENUE
        else:
          health_popz_added = health_lvl[user] * 7819
          HEALTH_REVENUE = health_popz_added * 120
          embed = discord.Embed(title = 'Collection Complete', description = f'you gained `{HEALTH_REVENUE:,d} coins` of **Health Revenue** from your population!', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += HEALTH_REVENUE
      else:
        await ctx.send('you don\'t have any population lmao')
        health.reset_cooldown(ctx)
    else:
      await ctx.send('you don\'t have any health levels!')
      health.reset_cooldown(ctx)
  else:
    await ctx.send('u dont even have a city')
    health.reset_cooldown(ctx)

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving buffalos = {buffalos}')
  try: 
    with open(BUFFALOS_FILE, 'w') as fp: 
      json.dump(buffalos, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {BUFFALOS_FILE} not found! Not sure what to do here!') 

@collect.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def waste(ctx):
  user = str(ctx.message.author.id)
  global waste_lvl, citypop, cities, balances, buffalos
  citypop[user] = citypop[user] if user in citypop else 0
  cities[user] = cities[user] if user in cities else 0
  waste_lvl[user] = waste_lvl[user] if user in waste_lvl else 0
  buffalos[user] = buffalos[user] if user in buffalos else 0
  balances[user] = balances[user] if user in balances else 0
  
  if cities[user] == 1:
    if waste_lvl[user] > 0:
      if citypop[user] > 0:
        CHANCE_OF_BUFFALO_YEETING = random.randint(1,100)
        if CHANCE_OF_BUFFALO_YEETING < 25 or CHANCE_OF_BUFFALO_YEETING == 25:
          buffalos[user] += 1
          waste_popz_added = waste_lvl[user] * 3142
          WASTE_REVENUE = waste_popz_added * 80
          embed = discord.Embed(title = 'Collection Complete', description = f'you gained `{WASTE_REVENUE:,d} coins` of **Waste Revenue** from your population and 1 :water_buffalo: **Buffalo** HOW TF', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += WASTE_REVENUE
        else:
          waste_popz_added = waste_lvl[user] * 3142
          WASTE_REVENUE = waste_popz_added * 80
          embed = discord.Embed(title = 'Collection Complete', description = f'you gained `{WASTE_REVENUE:,d} coins` of **Waste Revenue** from your population!', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += WASTE_REVENUE
      else:
        await ctx.send('you don\'t have any population lmao')
        waste.reset_cooldown(ctx)
    else:
      await ctx.send('you don\'t have any waste levels!')
      waste.reset_cooldown(ctx)
  else:
    await ctx.send(' u dont even have a city')
    waste.reset_cooldown(ctx)

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving buffalos = {buffalos}')
  try: 
    with open(BUFFALOS_FILE, 'w') as fp: 
      json.dump(buffalos, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {BUFFALOS_FILE} not found! Not sure what to do here!') 

@collect.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def water(ctx):
  user = str(ctx.message.author.id)
  global water_lvl, citypop, cities, balances, buffalos
  citypop[user] = citypop[user] if user in citypop else 0
  cities[user] = cities[user] if user in cities else 0
  water_lvl[user] = water_lvl[user] if user in water_lvl else 0
  buffalos[user] = buffalos[user] if user in buffalos else 0
  balances[user] = balances[user] if user in balances else 0
  
  if cities[user] == 1:
    if water_lvl[user] > 0:
      if citypop[user] > 0:
        CHANCE_OF_BUFFALO_YEETING = random.randint(1,100)
        if CHANCE_OF_BUFFALO_YEETING < 25 or CHANCE_OF_BUFFALO_YEETING == 25:
          buffalos[user] += 1
          water_popz_added = water_lvl[user] * 2227
          WATER_REVENUE = water_popz_added * 60
          embed = discord.Embed(title = 'Collection Complete', description = f'you gained `{WATER_REVENUE:,d} coins` of **Water Revenue** from your population and 1 :water_buffalo: **Buffalo** HOW TF', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += WATER_REVENUE
        else:
          water_popz_added = water_lvl[user] * 2227
          WATER_REVENUE = water_popz_added * 60
          embed = discord.Embed(title = 'Collection Complete', description = f'you gained `{WATER_REVENUE:,d} coins` of **Water Revenue** from your population!', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += WATER_REVENUE
      else:
        await ctx.send('you don\'t have any population lmao')
        water.reset_cooldown(ctx)
    else:
      await ctx.send('you don\'t have any water levels!')
      water.reset_cooldown(ctx)
  else:
    await ctx.send(' u dont even have a city')
    water.reset_cooldown(ctx)

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving buffalos = {buffalos}')
  try: 
    with open(BUFFALOS_FILE, 'w') as fp: 
      json.dump(buffalos, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {BUFFALOS_FILE} not found! Not sure what to do here!') 

@collect.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def fire(ctx):
  user = str(ctx.message.author.id)
  global fire_lvl, citypop, cities, balances, buffalos
  citypop[user] = citypop[user] if user in citypop else 0
  cities[user] = cities[user] if user in cities else 0
  fire_lvl[user] = fire_lvl[user] if user in fire_lvl else 0
  buffalos[user] = buffalos[user] if user in buffalos else 0
  balances[user] = balances[user] if user in balances else 0
  
  if cities[user] == 1:
    if fire_lvl[user] > 0:
      if citypop[user] > 0:
        CHANCE_OF_BUFFALO_YEETING = random.randint(1,100)
        if CHANCE_OF_BUFFALO_YEETING < 25 or CHANCE_OF_BUFFALO_YEETING == 25:
          buffalos[user] += 1
          fire_popz_added = fire_lvl[user] * 6231
          FIRE_REVENUE = fire_popz_added * 110
          embed = discord.Embed(title = 'Collection Complete', description = f'you gained `{FIRE_REVENUE:,d} coins` of **Fire Revenue** from your population and 1 :water_buffalo: **Buffalo** HOW TF', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += FIRE_REVENUE
        else:
          fire_popz_added = fire_lvl[user] * 6231
          FIRE_REVENUE = fire_popz_added * 60
          embed = discord.Embed(title = 'Collection Complete', description = f'you gained `{FIRE_REVENUE:,d} coins` of **Fire Revenue** from your population!', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += FIRE_REVENUE
      else:
        await ctx.send('you don\'t have any population lmao')
        fire.reset_cooldown(ctx)
    else:
      await ctx.send('you don\'t have any fire levels!')
      fire.reset_cooldown(ctx)
  else:
    await ctx.send(' u dont even have a city')
    fire.reset_cooldown(ctx)

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving buffalos = {buffalos}')
  try: 
    with open(BUFFALOS_FILE, 'w') as fp: 
      json.dump(buffalos, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {BUFFALOS_FILE} not found! Not sure what to do here!') 

@collect.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def police(ctx):
  user = str(ctx.message.author.id)
  global police_lvl, citypop, cities, balances, buffalos
  citypop[user] = citypop[user] if user in citypop else 0
  cities[user] = cities[user] if user in cities else 0
  police_lvl[user] = police_lvl[user] if user in police_lvl else 0
  buffalos[user] = buffalos[user] if user in buffalos else 0
  balances[user] = balances[user] if user in balances else 0
  
  if cities[user] == 1:
    if police_lvl[user] > 0:
      if citypop[user] > 0:
        CHANCE_OF_BUFFALO_YEETING = random.randint(1,100)
        if CHANCE_OF_BUFFALO_YEETING < 25 or CHANCE_OF_BUFFALO_YEETING == 25:
          buffalos[user] += 1
          police_popz_added = police_lvl[user] * 9331
          POLICE_REVENUE = police_popz_added * 130
          embed = discord.Embed(title = 'Collection Complete', description = f'you gained `{POLICE_REVENUE:,d} coins` of **Police Revenue** from your population and 1 :water_buffalo: **Buffalo** HOW TF', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += POLICE_REVENUE
        else:
          police_popz_added = police_lvl[user] * 9331
          POLICE_REVENUE = police_popz_added * 130
          embed = discord.Embed(title = 'Collection Complete', description = f'you gained `{POLICE_REVENUE:,d} coins` of **Police Revenue** from your population!', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += POLICE_REVENUE
      else:
        await ctx.send('you don\'t have any population lmao')
        police.reset_cooldown(ctx)
    else:
      await ctx.send('you don\'t have any police levels!')
      police.reset_cooldown(ctx)
  else:
    await ctx.send(' u dont even have a city')
    police.reset_cooldown(ctx)

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving buffalos = {buffalos}')
  try: 
    with open(BUFFALOS_FILE, 'w') as fp: 
      json.dump(buffalos, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {BUFFALOS_FILE} not found! Not sure what to do here!') 

@collect.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def entertainment(ctx):
  user = str(ctx.message.author.id)
  global entertainment_lvl, citypop, cities, balances, buffalos
  citypop[user] = citypop[user] if user in citypop else 0
  cities[user] = cities[user] if user in cities else 0
  entertainment_lvl[user] = entertainment_lvl[user] if user in entertainment_lvl else 0
  balances[user] = balances[user] if user in balances else 0
  buffalos[user] = buffalos[user] if user in buffalos else 0

  if cities[user] == 1:
    if entertainment_lvl[user] > 0:
      if citypop[user] > 0:
        CHANCE_OF_BUFFALO_YEETING = random.randint(1, 100)
        if CHANCE_OF_BUFFALO_YEETING < 25 or CHANCE_OF_BUFFALO_YEETING == 25:
          buffalos[user] += 1
          ent_popz_added = entertainment_lvl[user] * 867
          ENTERTAINMENT_REVENUE = ent_popz_added * 35
          embed = discord.Embed(title = 'Collection Complete', description = f'you gained `{ENTERTAINMENT_REVENUE:,d} coins` of **Entertainment Revenue** from your population and 1 :water_buffalo: **Buffalo** HOW TF', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += ENTERTAINMENT_REVENUE
        else:
          ent_popz_added = entertainment_lvl[user] * 867
          ENTERTAINMENT_REVENUE = ent_popz_added * 35
          embed = discord.Embed(title = 'Collection Complete', description = f'you gained `{ENTERTAINMENT_REVENUE:,d} coins` of **Entertainment Revenue** from your population!', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += ENTERTAINMENT_REVENUE
      else:
        await ctx.send('you don\'t have any population lmao')
        entertainment.reset_cooldown(ctx)
    else:
      await ctx.send('you don\'t have any entertainment levels!')
      entertainment.reset_cooldown(ctx)
  else:
    await ctx.send(' u dont even have a city')
    entertainment.reset_cooldown(ctx)

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving buffalos = {buffalos}')
  try: 
    with open(BUFFALOS_FILE, 'w') as fp: 
      json.dump(buffalos, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {BUFFALOS_FILE} not found! Not sure what to do here!') 

@collect.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def parks(ctx):
  user = str(ctx.message.author.id)
  global park_lvl, citypop, cities, balances
  citypop[user] = citypop[user] if user in citypop else 0
  cities[user] = cities[user] if user in cities else 0
  park_lvl[user] = park_lvl[user] if user in park_lvl else 0
  balances[user] = balances[user] if user in balances else 0

  if cities[user] == 1:
    if park_lvl[user] > 0:
      if citypop[user] > 0:
        CHANCE_OF_BUFFALO_YEETING = random.randint(1,100)
        if CHANCE_OF_BUFFALO_YEETING < 25 or CHANCE_OF_BUFFALO_YEETING == 25:
          buffalos[user] += 1
          park_popz_added = park_lvl[user] * 1001
          PARK_REVENUE = park_popz_added * 50
          embed = discord.Embed(title = 'Collection Complete', description = f'you gained `{PARK_REVENUE:,d} coins` of **Park Revenue** from your population and 1 :water_buffalo: **Buffalo** HOW TF', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += PARK_REVENUE
        else:
          park_popz_added = park_lvl[user] * 1001
          PARK_REVENUE = park_popz_added * 50
          embed = discord.Embed(title = 'Collection Complete', description = f'you gained `{PARK_REVENUE:,d} coins` of **Park Revenue** from your population!', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += PARK_REVENUE
      else:
        await ctx.send('you don\'t have any population lmao')
        parks.reset_cooldown(ctx)
    else:
      await ctx.send('you don\'t have any park levels!')
      parks.reset_cooldown(ctx)
  else:
    await ctx.send(' u dont even have a city')
    parks.reset_cooldown(ctx)

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving buffalos = {buffalos}')
  try: 
    with open(BUFFALOS_FILE, 'w') as fp: 
      json.dump(buffalos, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {BUFFALOS_FILE} not found! Not sure what to do here!') 

@collect.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def power(ctx):
  user = str(ctx.message.author.id)
  global power_lvl, citypop, cities, balances, buffalos
  citypop[user] = citypop[user] if user in citypop else 0
  cities[user] = cities[user] if user in cities else 0
  power_lvl[user] = power_lvl[user] if user in power_lvl else 0
  buffalos[user] = buffalos[user] if user in buffalos else 0
  balances[user] = balances[user] if user in balances else 0
  
  if cities[user] == 1:
    if power_lvl[user] > 0:
      if citypop[user] > 0:
        CHANCE_OF_BUFFALO_YEETING = random.randint(1,100)
        if CHANCE_OF_BUFFALO_YEETING < 25 or CHANCE_OF_BUFFALO_YEETING == 25:
          buffalos[user] += 1
          power_popz_added = power_lvl[user] * 2467
          POWER_REVENUE = power_popz_added * 75
          embed = discord.Embed(title = 'Collection Complete', description = f'you gained `{POWER_REVENUE:,d} coins` of **Power Revenue** from your population and 1 :water_buffalo: **Buffalo** HOW TF', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += POWER_REVENUE
        else:
          power_popz_added = power_lvl[user] * 2467
          POWER_REVENUE = power_popz_added * 75
          embed = discord.Embed(title = 'Collection Complete', description = f'you gained `{POWER_REVENUE:,d} coins` of **Power Revenue** from your population', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += POWER_REVENUE
      else:
        await ctx.send('you don\'t have any population lmao')
        power.reset_cooldown(ctx)
    else:
      await ctx.send('you don\'t have any power levels!')
      power.reset_cooldown(ctx)
  else:
    await ctx.send(' u dont even have a city')
    power.reset_cooldown(ctx)

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving buffalos = {buffalos}')
  try: 
    with open(BUFFALOS_FILE, 'w') as fp: 
      json.dump(buffalos, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {BUFFALOS_FILE} not found! Not sure what to do here!') 

#=============================================================================================================

@bot.command(aliases = ['cm'])
async def cowmarket(ctx):
  with open(r"prefixes.json", 'r') as f:
    prefixes = json.load(f)

  x = prefixes[str(ctx.guild.id)] if str(ctx.guild.id) in prefixes else 'le '
  embed = discord.Embed(title = 'Cow Market', description = f'{x}purchase [ex: mooshroom]\n{x}stew [ex: mooshroom]', color = random.choice(random_colors))
  embed.add_field(name = 'Basic Cows', value = '<:mooshroom:716492779391418440> **Mooshroom Cow**\n- Gives 15 ***mushroom stew*** every farm\n- Price: __14400__ coins\n- Can only be used 15 times, then it dies')
  await ctx.send(embed = embed)

@bot.command()
@commands.cooldown(1, 1800, commands.BucketType.user)
async def stew(ctx, arg):
  global mooshroom_cows, times_mooshroom, bowls, mushroom_stew
  user = str(ctx.message.author.id)
  mooshroom_cows[user] = mooshroom_cows[user] if user in mooshroom_cows else 0
  times_mooshroom[user] = times_mooshroom[user] if user in times_mooshroom else 0
  bowls[user] = bowls[user] if user in bowls else 0
  mushroom_stew[user] = mushroom_stew[user] if user in mushroom_stew else 0

  if mooshroom_cows[user] > 0: 
    if times_mooshroom[user] < 15:
      if bowls[user] > 15 or bowls[user] == 15:
        bowls[user] -= 15
        mushroom_stew[user] += 15
        times_mooshroom[user] += 1
        embed = discord.Embed(title = f'{ctx.message.author.name}\'s harvest ', description = f"you just recieved <:mushstew:716492699879997530> **15** mushroom stew from your <:mooshroom:716492779391418440> mooshroom cow", color = random.choice(random_colors))
        await ctx.send(embed = embed)   
      else:
        await ctx.send('you need at least 15 bowls for this!')
        stew.reset_cooldown(ctx)
    else:
      await ctx.send('your <:mooshroom:716492779391418440> mooshroom cow has been used 15 times, making it weak, resulting in its perish')
      await asyncio.sleep(3)
      await ctx.send('may it rest in peace')
      await asyncio.sleep(3)
      await ctx.send('<:mooshroom:716492779391418440>')
      mooshroom_cows[user] -= 1
      times_mooshroom[user] = 0
  else:
    await ctx.send('you don\'t have a cow')
    stew.reset_cooldown(ctx)

  print(f'In buy(): Saving sheeps = {bowls}')
  try: 
    with open(BOWLS_FILE, 'w') as fp: 
      json.dump(bowls, fp) 
  except FileNotFoundError: 
    print(f'In buy(): File {BOWLS_FILE} not found! Not sure what to do here!') 

  print(f'In beg(): Saving balances = {mooshroom_cows}')
  try: 
    with open(MOOSHROOM_COW_FILE, 'w') as fp: 
      json.dump(mooshroom_cows, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {MOOSHROOM_COW_FILE} not found! Not sure what to do here!') 
  
  print(f'In beg(): Saving balances = {times_mooshroom}')
  try: 
    with open(TIMES_MOOSHROOM, 'w') as fp: 
      json.dump(times_mooshroom, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {TIMES_MOOSHROOM} not found! Not sure what to do here!') 

  print(f'In beg(): Saving balances = {mushroom_stew}')
  try: 
    with open(MUSHROOM_STEW_FILE, 'w') as fp: 
      json.dump(mushroom_stew, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {MUSHROOM_STEW_FILE} not found! Not sure what to do here!') 

@bot.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
  user = str(ctx.message.author.id)
  global balances
  balances[user] += 5000
  embed = discord.Embed(title = f'{ctx.message.author.name}\'s daily coins', description = '__5000__ coins were added in your funds', color = random.choice(random_colors))
  await ctx.send(embed = embed)

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 

@bot.command()
async def profile(ctx, member: discord.Member = None):
  

  if member is None:
    member = ctx.message.author
  
  levels = openfile(LEVEL_FILE)
  exp = openfile(EXP_FILE)
  commands2 = openfile(COMMANDS_FILE)

  user = str(member.id)

  commands2[user] = commands2[user] if user in commands2 else 0
  exp[user] = exp[user] if user in exp else 0
  levels[user] = levels[user] if user in levels else 0

  if levels[user] in range(0, 6):
    embed = discord.Embed(title = f'{member.name}\'s Profile', color = random.choice(random_colors))
    embed.add_field(name = 'Commands Invoked', value = f'{commands2[user]}', inline = True)
    embed.add_field(name = '', value = f'Level: **{levels[user]}** Exp: **{exp[user]}**', inline = False)
    await ctx.send(embed = embed)
  elif levels[user] in range(6, 16):
    embed = discord.Embed(title = f'{member.name}\'s Profile', color = random.choice(random_colors))
    embed.add_field(name = 'Commands Invoked', value = f'{commands2[user]}', inline = True)
    embed.add_field(name = '', value = f'Level: **{levels[user]}** Exp: **{exp[user]}**', inline = False)
    await ctx.send(embed = embed)
  elif levels[user] in range(16, 26):
    embed = discord.Embed(title = f'{member.name}\'s Profile', color = random.choice(random_colors))
    embed.add_field(name = 'Commands Invoked', value = f'{commands2[user]}', inline = True)
    embed.add_field(name = '', value = f'Level: **{levels[user]}** Exp: **{exp[user]}**', inline = False)
    await ctx.send(embed = embed)
  else:
    embed = discord.Embed(title = f'{member.name}\'s Profile', color = random.choice(random_colors))
    embed.add_field(name = 'Commands Invoked', value = f'{commands2[user]}', inline = True)
    embed.add_field(name = '', value = f'Level: **{levels[user]}** Exp: **{exp[user]}**', inline = False)
    await ctx.send(embed = embed)

@bot.command()
@commands.cooldown(1, 3600, commands.BucketType.user)
async def work(ctx):
  user = str(ctx.message.author.id)
  global balances
  balances[user] = balances[user] if user in balances else 0

  actions = [    'clean the kitchen',    'wash 10 dishes',    'vacuum the living room',    'sweep the garage',    'mop the bathroom',    'scrub the toilet',    'dust the furniture',    'organize the closet',    'water the plants',    'mow the lawn',    'rake the leaves',    'trim the hedges',    'plant a garden',    'paint a room',    'install a shelf',    'assemble a piece of furniture',    'fix a leaky faucet',    'unclog a drain',    'change a lightbulb',    'clean the gutters',    'wash the car',    'detail the car',    'cut firewood',    'shovel snow',    'rake the roof',    'clean the pool',    'repair a fence',    'build a birdhouse',    'sew a patch on clothes',    'knit a scarf',    'bake a cake',    'cook a meal',    'make a smoothie',    'brew coffee',    'write a poem',    'paint a picture',    'play an instrument',    'read a book',    'watch a movie',    'learn a new language',    'exercise for 30 minutes',    'meditate for 10 minutes',    'call a friend',    'write a thank-you note',    'volunteer at a charity',    'donate to a cause',    'attend a lecture',    'take a class',    'learn a new skill',    'plan a trip',    'organize your finances',    'start a blog',    'create a budget',    'do your taxes',    'file paperwork',    'clean your computer',    'back up your files']
  answer = random.choice(actions)
  msg2 = await ctx.send(f'{ctx.message.author.mention}, do the work by typing it!\n**{answer}**')
  await msg2.edit()
  msg = await bot.wait_for('message', check = lambda m: m.author == ctx.author)
  if msg.content.lower() == answer:
    random_coins = random.randint(3000, 5000)
    balances[user] += random_coins
    await ctx.send(f'**Nice job {ctx.message.author.name}!** you earned **{random_coins}** coins from that hour of work')
  else:
    random_coins2 = random.randint(500, 1500)
    await ctx.send(f'**Not good {ctx.message.author.name}!** you only earned **{random_coins2}** coins from that hour of work')
    balances[user] += random_coins2

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 

@bot.command()
async def notebook(ctx):
  embed = discord.Embed(title = "Recipe notebook", description = "there is literally one recipe", color = random.choice(random_colors))
  embed.add_field(name = ":salad: Salad", value = "Ingredients | 5 Cooked Chicken, 9 Rice")
  await ctx.send(embed = embed)

@bot.command()
async def combine(ctx, arg1, arg2):
  global rices, cooked_chickens, salads
  user = str(ctx.message.author.id)
  cooked_chickens[user] = cooked_chickens[user] if user in cooked_chickens else 0
  rices[user] = rices[user] if user in rices else 0

  if arg1 == 'chicken' or arg1 == 'Chicken':
    if arg2 == 'Rice' or arg2 == 'rice':
      if cooked_chickens[user] == 5 or cooked_chickens[user] > 5:
        if rices[user] == 9 or rices[user] > 9:
          salads[user] += 20
          rices[user] -= 9
          cooked_chickens[user] -= 5
          embed = discord.Embed(title = 'Combine Complete', description = f'you got **20** salads for `5 cooked chicken` and `9 rice`', color = random.choice(random_colors))
          await ctx.send(embed = embed)
        else:
          await ctx.send('you need at least 9 or more rice for this!')
      else:
        await ctx.send('you need at least 5 cooked chickens for this!')
    else:
      await ctx.send('i think you put the ingredients in the wrong way\ncorrect way: `le combine chicken rice`')
  else:
    await ctx.send('i think you put the ingredients in the wrong way\ncorrect way: `le combine chicken rice`')

  print(f'In sell(): Saving rices = {rices}')
  try: 
    with open(RICE_FILE, 'w') as fp: 
      json.dump(rices, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {RICE_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving salads = {salads}')
  try: 
    with open(SALADS_FILE, 'w') as fp: 
      json.dump(salads, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {SALADS_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving cooked chicken = {cooked_chickens}')
  try: 
    with open(COOKED_CHICKENS_FILE, 'w') as fp: 
      json.dump(cooked_chickens, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {COOKED_CHICKENS_FILE} not found! Not sure what to do here!') 

@bot.command()
async def pharmacy(ctx):
  embed = discord.Embed(title = "Mr. Morale's pharmacy", description = "`buy <item> <amount>` or `sell <item> <amount>`", color = random.choice(random_colors))
  embed.add_field(name = ":medical_symbol: Meds", value = ":ambulance: Ambulance | Price: :cut_of_meat: __15200__ | Puts your health back to 100\n:french_bread: Bread | Price: __1200__ coins | Puts health exactly at 60")
  await ctx.send(embed = embed)

@bot.command()
async def popeyes(ctx):
  with open(r"prefixes.json", 'r') as f:
    prefixes = json.load(f)

  x = prefixes[str(ctx.guild.id)] if str(ctx.guild.id) in prefixes else 'le '

  embed = discord.Embed(title = "Mr. Morale's Popeyes", description = f"`{x}buy <item> <amount>` | `{x}cook <item> <amount>`", color = random.choice(random_colors))
  embed.add_field(name = ":hatched_chick: Uncooked Chicken [ANIMAL]", value = "Price: __10,000__ coins")
  await ctx.send(embed = embed)

@bot.command()
async def shop(ctx):
  embed = discord.Embed(title = "Mr. Morale's secret shop", description = "`le buy <item> <amount>` or `le sell <item> <amount>`\n`le farm`\nGoods are not able to be purchased", color = random.choice(random_colors))
  embed.add_field(name = "Animals\n", value = "\n:sheep: **Sheep** ─ __100__ coins ─ Item\n :pig2: **Pig** ─ __200__ coins ─ Item\n :water_buffalo: **Buffalo** ─ __10,000,000__ coins ─ Item", inline = True)
  embed.add_field(name = "Materials\n", value = "\n:cooking: **Stove** ─ __19,500__ coins ─ Item", inline = False)
  embed.add_field(name = "Crops\n", value = "\n:rice: **Rice** ─ __30__ coins ─ Item", inline = False)
  embed.add_field(name = "Miscellaneous\n", value = "\n:desktop: **PC** ─ __1,500__ coins ─ Item\n<:bowl:716492750996111441> **Bowl** ─ __50__ coins ─ Item")
  await ctx.send(embed=embed)

@bot.command()
async def jetshop(ctx):
  global morris, douglas
  user = str(ctx.message.author.id)
  with open(r"prefixes.json", 'r') as f:
    prefixes = json.load(f)

  x = prefixes[str(ctx.guild.id)] if str(ctx.guild.id) in prefixes else 'le '
  morris[user] = morris[user] if user in morris else 0
  douglas[user] = douglas[user] if user in douglas else 0
  embed = discord.Embed(title = 'Jet shop', description = f'`{x}buy [Morris/Douglas]` or `{x}fly [Morris/Douglas]`', color = random.choice(random_colors))
  embed.add_field(name = ':airplane_small: Morris X8200', value = 'small but fiesty jet, 25% chance of getting air sickness\n`Price: 1500 Meat, 3 Salads, 5000 wheat, 10000 coins`', inline = True)
  embed.add_field(name = ':airplane: Douglas 900ER', value = 'Wanna travel far without problems, here\'s your answer!\n`Price: 5000 Meat, 20 Salads, 10 Stoves, 75000 coins`', inline = False)
  await ctx.send(embed = embed)

@bot.command(name= 'health')
async def health1(ctx):
  global healths, HEALTH_FILE
  user = str(ctx.message.author.id)
  
  print(f'In health(): Author Id = {ctx.message.author.id}, Author Name = {user}')
  if user in healths:
    embed = discord.Embed(title = f"{ctx.message.author}'s health :heartpulse:", description = "your health is deprived everytime you harvest.\nTo regenerate, go to `le pharmacy` to buy meds.\nDose them to regenerate health.", color = random.choice(random_colors))
    embed.add_field(name = "your health", value = f'{healths[user]}/100')
    await ctx.send(embed = embed)
  else: 
    print(f'In plead(): No record for {user} found. Creating a new record with a starting balance of {START_HEALTH}') 
    healths[user] = START_HEALTH
    await ctx.send(f'hey you don\'t have a health bar yet. I just created you one with {START_HEALTH}') 

  print(f'In health(): Saving healths = {healths}')
  try: 
    with open(HEALTH_FILE, 'w') as fp: 
      json.dump(healths, fp) 
  except FileNotFoundError: 
   print(f'In beg(): File {HEALTH_FILE} not found! Not sure what to do here!') 

@bot.command(aliases = ['lb'])
async def leaderboard(ctx):
  global balances

  await ctx.send('do you want the leaderboard for this server\'s members or every member? \ntype `server` for this server and `global` for every member')
  msg = await bot.wait_for('message', check = lambda m: m.author == ctx.author)

  if msg.content.lower() == 'server': 
    guild_members = ctx.guild.members
    guild_balances = {}
    
    for member in guild_members:
      if str(member.id) in balances:
        guild_balances[member.id] = balances[str(member.id)]

    sorted_balances = dict(sorted(guild_balances.items(), key=itemgetter(1), reverse=True)[:3])
    first_place = None
    second_place = None
    third_place = None

    for member_id, balance in sorted_balances.items():
      member = await bot.fetch_user(member_id)
      if first_place is None:
        first_place = f"{member.name}#{member.discriminator}"
        first_balance = balance
      elif second_place is None:
        second_place = f"{member.name}#{member.discriminator}"
        second_balance = balance
      elif third_place is None:
        third_place = f"{member.name}#{member.discriminator}"
        third_balance = balance

    embed = discord.Embed(title = f"{ctx.guild.name}'s Money Leaderboard", color = random.choice(random_colors))
    embed.add_field(name = f":first_place: `{first_balance:,d}` - {first_place}", value = f'', inline = False)
    embed.add_field(name = f":second_place: `{second_balance:,d}` - {second_place}", value = f"", inline = False)
    embed.add_field(name = f":third_place: `{third_balance:,d}` - {third_place}", value = f'', inline = False)

    await ctx.send(embed = embed)
  elif msg.content.lower() == 'global':   
    sorted_balances = dict(sorted(balances.items(), key=itemgetter(1), reverse=True)[:3])
    first_place = None
    second_place = None
    third_place = None

    for member_id, balance in sorted_balances.items():
      member = await bot.fetch_user(member_id)
      if first_place is None:
        first_place = f"{member.name}#{member.discriminator}"
        first_balance = balance
      elif second_place is None:
        second_place = f"{member.name}#{member.discriminator}"
        second_balance = balance
      elif third_place is None:
        third_place = f"{member.name}#{member.discriminator}"
        third_balance = balance

    embed = discord.Embed(title = "Global Money Leaderboard", color = random.choice(random_colors))
    embed.add_field(name = f":first_place: `{first_balance:,d}` - {first_place}", value = f'', inline = False)
    embed.add_field(name = f":second_place: `{second_balance:,d}` - {second_place}", value = f"", inline = False)
    embed.add_field(name = f":third_place: `{third_balance:,d}` - {third_place}", value = f'', inline = False)

    await ctx.send(embed = embed)
  else:
    await ctx.send("not an option; rerun the command")

@stew.error
async def stew_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    m, s = divmod(error.retry_after, 60)
    await ctx.send(f'wait **{round(m)} minutes and {round(s)} seconds** to get more stew  ')
  elif isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Proper Usage: `stew [ex: mooshroom]`')

@setmembermessage.error
async def setmembermessage_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Proper Usage: `setmembermessage [message]`')
  elif isinstance(error, commands.MissingPermissions):
    await ctx.send('you don\'t have the perm: `Manage Server`!')
    
@reactionmessage.error
async def reactionmessage_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send('you don\'t have the perm: `Manage Server`!')
  
@membermessage.error
async def membermessage_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send('you don\'t have the perm: `Manage Server`!')

@setchannelid.error
async def setchannelid_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send('you don\'t have the perm: `Manage Server`!') 
  elif isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Proper Usage: `setchannelid [channel id]`')

@power.error
async def power_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    m, s = divmod(error.retry_after, 60)
    h, m = divmod(m, 60)
    await ctx.send(f'wait **{round(h)} hours and {round(m)} minutes** to get more revenue  ')

@entertainment.error
async def entertainment_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    m, s = divmod(error.retry_after, 60)
    h, m = divmod(m, 60)
    await ctx.send(f'wait **{round(h)} hours and {round(m)} minutes** to get more revenue  ')

@fire.error
async def fire_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    m, s = divmod(error.retry_after, 60)
    h, m = divmod(m, 60)
    await ctx.send(f'wait **{round(h)} hours and {round(m)} minutes** to get more revenue  ')

@police.error
async def police_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    m, s = divmod(error.retry_after, 60)
    h, m = divmod(m, 60)
    await ctx.send(f'wait **{round(h)} hours and {round(m)} minutes** to get more revenue  ')

@waste.error
async def waste_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    m, s = divmod(error.retry_after, 60)
    h, m = divmod(m, 60)
    await ctx.send(f'wait **{round(h)} hours and {round(m)} minutes** to get more revenue  ')

@water.error
async def water_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    m, s = divmod(error.retry_after, 60)
    h, m = divmod(m, 60)
    await ctx.send(f'wait **{round(h)} hours and {round(m)} minutes** to get more revenue ')

@parks.error
async def parks_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    m, s = divmod(error.retry_after, 60)
    h, m = divmod(m, 60)
    await ctx.send(f'wait **{round(h)} hours and {round(m)} minutes** to get more revenue  ')

@health.error
async def health_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    m, s = divmod(error.retry_after, 60)
    h, m = divmod(m, 60)
    await ctx.send(f'wait **{round(h)} hours and {round(m)} minutes** to get more revenue  ')

@profile.error
async def profile_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    global commands2, levels, exp
    user = str(ctx.message.author.id)
    commands2[user] = commands2[user] if user in commands2 else 0
    exp[user] = exp[user] if user in exp else 0
    levels[user] = levels[user] if user in levels else 0
    
    if levels[user] in range(0, 6):
      embed = discord.Embed(title = f'{ctx.message.author.name}\'s Profile', color = random.choice(random_colors))
      embed.add_field(name = '\nRandom', value = f'<:pepe_cry:712063226292076564> Commands invoked: {commands2[user]}', inline = True)
      embed.add_field(name = '\nLow Sped', value = f'Level: **{levels[user]}** Exp: **{exp[user]}**', inline = False)
      await ctx.send(embed = embed)
    elif levels[user] in range(6, 16):
      embed = discord.Embed(title = f'{ctx.message.author.name}\'s Profile', color = random.choice(random_colors))
      embed.add_field(name = '\nRandom', value = f'<:pepe_cry:712063226292076564> Commands invoked: {commands2[user]}', inline = True)
      embed.add_field(name = '\nSped', value = f'Level: **{levels[user]}** Exp: **{exp[user]}**', inline = False)
      await ctx.send(embed = embed)
    elif levels[user] in range(16, 26):
      embed = discord.Embed(title = f'{ctx.message.author.name}\'s Profile', color = random.choice(random_colors))
      embed.add_field(name = '\nRandom', value = f'<:pepe_cry:712063226292076564> Commands invoked: {commands2[user]}', inline = True)
      embed.add_field(name = '\nMediocre Sped', value = f'Level: **{levels[user]}** Exp: **{exp[user]}**', inline = False)
      await ctx.send(embed = embed)
    elif levels[user] in range(26, 101):
      embed = discord.Embed(title = f'{ctx.message.author.name}\'s Profile', color = random.choice(random_colors))
      embed.add_field(name = '\nRandom', value = f'<:pepe_cry:712063226292076564> Commands invoked: {commands2[user]}', inline = True)
      embed.add_field(name = '\nUltimate Sped', value = f'Level: **{levels[user]}** Exp: **{exp[user]}**', inline = False)
      await ctx.send(embed = embed)
    else:
      embed = discord.Embed(title = f'{ctx.message.author.name}\'s Profile', color = random.choice(random_colors))
      embed.add_field(name = '\nRandom', value = f'<:pepe_cry:712063226292076564> Commands invoked: {commands2[user]}', inline = True)
      embed.add_field(name = '\nUltimate Sped', value = f'Level: **{levels[user]}** Exp: **{exp[user]}**', inline = False)
      await ctx.send(embed = embed)

@setprefix.error
async def setprefix_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Proper Usage: `setprefix [prefix]`')

@combine.error
async def combine_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Proper Usage: `combine [chicken] [rice]` See the command `notebook` for amounts of the recipe')
    
@daily.error
async def daily_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    m, s = divmod(error.retry_after, 60 )
    h, m = divmod(m, 60)
    await ctx.send(f'wait **{round(h)} hours and {round(m)} minutes** to get ur daily coins ')
    return

@work.error
async def work_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    m, s = divmod(error.retry_after, 60)
    await ctx.send(f'wait **{round(m)} minutes and {round(s)} seconds** to work again ')
    return

#=============================================================================================================

f = open("token.txt", "r")

async def load():
  for filename in os.listdir('./econ'):
    if filename.endswith('.py'):
      await bot.load_extension(f'econ.{filename[:-3]}')

  for filename in os.listdir('./help'):
    if filename.endswith('.py'):
      await bot.load_extension(f'help.{filename[:-3]}')

  for filename in os.listdir('./moderation'):
    if filename.endswith('.py'):
      await bot.load_extension(f'moderation.{filename[:-3]}')

async def main():
  await load()
  await bot.start(f.readline())
            
if __name__ == '__main__':
  asyncio.run(main())
