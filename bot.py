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
import aiohttp
import re
import urllib.parse, urllib.request

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

random_colors = [0xFFFFFF, 0x1ABC9C, 0x2ECC71, 0x3498DB, 0x9B59B6, 0xE91E63, 0xF1C40F, 0xE67E22, 0xE74C3C, 0x34495E, 0x11806A, 0x1F8B4C, 0x206694]

NUMBERS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
VOWELS = ["a", "e", "i", "o", "u"]

def get_prefix(bot, message):
  if not message.guild:
    return commands.when_mentioned_or("le ")(bot, message)
  
  with open ('prefixes.json', 'r') as f:
    prefixes = json.load(f)

  if str(message.guild.id) not in prefixes:
    return commands.when_mentioned_or("le ")(bot, message)

  prefix = prefixes[str(message.guild.id)]
  return commands.when_mentioned_or(prefix)(bot, message)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = commands.when_mentioned and get_prefix, intents = intents)
epoch = datetime.datetime.utcfromtimestamp(0)
bot.remove_command("help")
status = cycle(['le help'])
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

ALLOW_MEMBER_MESSAGE = 'allowmembermessage.json'
allowmembermessage = {}

MEMBER_MESSAGE = 'membermessage.json'
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

def read_json(filename):
  with open(f"{filename}.json", "r") as file:
    data = json.load(file)
  
  return data

def write_json(data, filename):
  with open(f'{filename}.json', 'w') as file:
    json.dump(data, file, indent = 4)

@tasks.loop(seconds=20)
async def change_status():
  await bot.change_presence(status = discord.Status.idle, activity=discord.Game(name="le help"))  
  #await bot.change_presence(activity=discord.Streaming(name="le help", url="https://www.twitch.tv/ninja"))  

@bot.event
async def on_ready():
  change_status.start()
  print(f'{bot.user.name} is ready')
  global balances, wools, sheeps, rices, wheats, pigs, meats, healths, ambulances, buffalos, stoves, uncooked_chickens, cooked_chickens, salads, morris, douglas, locations, cities, citypop, entertainment_lvl, pc, park_lvl, power_lvl, blacklisted, bread
  global mooshroom_cows, bowls, mushroom_stew, times_mooshroom, water_lvl, waste_lvl, commands2, levels, exp, health_lvl, allowreactionmessage, personalstring, allowmembermessage, membermessage, channel_id
  global fire_lvl, police_lvl

  # data = read_json("blacklist")
  # bot.blacklistedUsers = data["blacklistedUsers"]
  
  try:
    with open(MUSHROOM_STEW_FILE, 'r') as fp: 
      mushroom_stew = json.load(fp) 
  except FileNotFoundError:
    print(f'In on_ready(): File {MUSHROOM_STEW_FILE} not found. Starting off with an empty balances dictionary.') 
    mushroom_stew = {} 

  try:
    with open(TIMES_MOOSHROOM, 'r') as fp: 
      times_mooshroom = json.load(fp) 
  except FileNotFoundError:
    print(f'In on_ready(): File {TIMES_MOOSHROOM} not found. Starting off with an empty balances dictionary.') 
    times_mooshroom = {} 


  try:
    with open(BALANCES_FILE, 'r') as fp: 
      balances = json.load(fp) 
  except FileNotFoundError:
    print(f'In on_ready(): File {BALANCES_FILE} not found. Starting off with an empty balances dictionary.') 
    balances = {} 

  try:
    with open(SHEEPS_FILE, 'r') as fp:
      sheeps = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {SHEEPS_FILE} not found. Starting off with an empty dictionary')
    sheeps = {}

  try:
    with open(WOOL_FILE, 'r') as fp:
      wools = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {WOOL_FILE} not found. Starting off with an empty dictionary')
    wools = {}

  try:
    with open(RICE_FILE, 'r') as fp:
      rices = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {RICE_FILE} not found. Starting off with an empty dictionary')
    rices = {}

  try:
    with open(WHEAT_FILE, 'r') as fp:
      wheats = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {WHEAT_FILE} not found. Starting off with an empty dictionary')
    wheats = {}

  try:
    with open(PIG_FILE, 'r') as fp:
      pigs = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {PIG_FILE} not found. Starting off with an empty dictionary')
    pigs = {}

  try:
    with open(MEAT_FILE, 'r') as fp:
      meats = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {MEAT_FILE} not found. Starting off with an empty dictionary')
    meats = {}

  try:
    with open(HEALTH_FILE, 'r') as fp:
      healths = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {HEALTH_FILE} not found. Starting off with an empty dictionary')
    healths = {}

  try:
    with open(AMBULANCES_FILE, 'r') as fp:
      ambulances = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {AMBULANCES_FILE} not found. Starting off with an empty dictionary')
    ambulances = {}

  try:
    with open(BUFFALOS_FILE, 'r') as fp:
      buffalos = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {BUFFALOS_FILE} not found. Starting off with an empty dictionary')
    buffalos = {}

  try:
    with open(STOVES_FILE, 'r') as fp:
      stoves = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {STOVES_FILE} not found. Starting off with an empty dictionary')
    stoves = {}

  try:
    with open(UNCOOKED_CHICKENS_FILE, 'r') as fp:
      uncooked_chickens = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {UNCOOKED_CHICKENS_FILE} not found. Starting off with an empty dictionary')
    uncooked_chickens = {}

  try:
    with open(COOKED_CHICKENS_FILE, 'r') as fp:
      cooked_chickens = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {COOKED_CHICKENS_FILE} not found. Starting off with an empty dictionary')
    cooked_chickens = {}

  try:
    with open(SALADS_FILE, 'r') as fp:
      salads = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {SALADS_FILE} not found. Starting off with an empty dictionary')
    salads = {}

  try:
    with open(MORRIS_FILE, 'r') as fp:
      morris = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {MORRIS_FILE} not found. Starting off with an empty dictionary')
    morris = {}

  try:
    with open(DOUGLAS_FILE, 'r') as fp:
      douglas = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {DOUGLAS_FILE} not found. Starting off with an empty dictionary')
    douglas = {}

  try:
    with open(LOCATIONS_FILE, 'r') as fp:
      locations = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {LOCATIONS_FILE} not found. Starting off with an empty dictionary')
    locations = {}

  try:
    with open(CITIES_FILE, 'r') as fp:
      cities = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {CITIES_FILE} not found. Starting off with an empty dictionary')
    cities = {}

  try:
    with open(CITYPOP_FILE, 'r') as fp:
      citypop = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {CITYPOP_FILE} not found. Starting off with an empty dictionary')
    citypop = {}

  try:
    with open(ENTERTAINMENT_LVL_FILE, 'r') as fp:
      entertainment_lvl = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {ENTERTAINMENT_LVL_FILE} not found. Starting off with an empty dictionary')
    entertainment_lvl = {}

  try:
    with open(PC_FILE, 'r') as fp:
      pc = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {PC_FILE} not found. Starting off with an empty dictionary')
    pc = {}

  try:
    with open(PARK_LVL_FILE, 'r') as fp:
      park_lvl = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {PARK_LVL_FILE} not found. Starting off with an empty dictionary')
    park_lvl = {}

  try:
    with open(POWER_LVL_FILE, 'r') as fp:
      power_lvl = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {POWER_LVL_FILE} not found. Starting off with an empty dictionary')
    power_lvl = {}

  try:
    with open(BLACKLISTED_FILE, 'r') as fp:
      blacklisted = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {BLACKLISTED_FILE} not found. Starting off with an empty dictionary')
    blacklisted = {}

  try:
    with open(BREAD_FILE, 'r') as fp:
      bread = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {BREAD_FILE} not found. Starting off with an empty dictionary')
    bread = {}

  try:
    with open(MOOSHROOM_COW_FILE, 'r') as fp:
      mooshroom_cows = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {MOOSHROOM_COW_FILE} not found. Starting off with an empty dictionary')
    mooshroom_cows = {}

  try:
    with open(BOWLS_FILE, 'r') as fp:
      bowls = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {BOWLS_FILE} not found. Starting off with an empty dictionary')
    bowls = {}

  try:
    with open(WATER_LVL_FILE, 'r') as fp:
      water_lvl = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {WATER_LVL_FILE} not found. Starting off with an empty dictionary')
    water_lvl = {}

  try:
    with open(WASTE_LVL_FILE, 'r') as fp:
      waste_lvl = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {WASTE_LVL_FILE} not found. Starting off with an empty dictionary')
    waste_lvl = {}

  try:
    with open(COMMANDS_FILE, 'r') as fp:
      commands2 = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {COMMANDS_FILE} not found. Starting off with an empty dictionary')
    commands2 = {}

  try:
    with open(LEVEL_FILE, 'r') as fp:
      levels = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {LEVEL_FILE} not found. Starting off with an empty dictionary')
    levels = {}
  
  try:
    with open(EXP_FILE, 'r') as fp:
      exp = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {EXP_FILE} not found. Starting off with an empty dictionary')
    exp = {}

  try:
    with open(HEALTH_LVL_FILE, 'r') as fp:
      health_lvl = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {HEALTH_LVL_FILE} not found. Starting off with an empty dictionary')
    health_lvl = {}

  try:
    with open(ALLOW_REACTION_MESSAGE, 'r') as fp:
      allowreactionmessage = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {ALLOW_REACTION_MESSAGE} not found. Starting off with an empty dictionary')
    allowreactionmessage = {}

  try:
    with open(PERSONAL_STRING, 'r') as fp:
      personalstring = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {PERSONAL_STRING} not found. Starting off with an empty dictionary')
    personalstring = {}

  try:
    with open(ALLOW_MEMBER_MESSAGE, 'r') as fp:
      allowmembermessage = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {ALLOW_MEMBER_MESSAGE} not found. Starting off with an empty dictionary')
    allowmembermessage = {}

  try:
    with open(MEMBER_MESSAGE, 'r') as fp:
      membermessage = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {MEMBER_MESSAGE} not found. Starting off with an empty dictionary')
    membermessage = {}

  try:
    with open(CHANNEL_ID, 'r') as fp:
      channel_id = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {CHANNEL_ID} not found. Starting off with an empty dictionary')
    channel_id = {}

  try:
    with open(FIRE_LVL_FILE, 'r') as fp:
      fire_lvl = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {FIRE_LVL_FILE} not found. Starting off with an empty dictionary')
    fire_lvl = {}

  try:
    with open(POLICE_LVL_FILE, 'r') as fp:
      police_lvl = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {POLICE_LVL_FILE} not found. Starting off with an empty dictionary')
    police_lvl = {}

# @bot.event
# async def on_command_error(ctx, error):
#   if isinstance(error, CommandNotFound):
#     await ctx.send('thats not a command you bot')

@bot.event
async def on_member_join(member):
  global membermessage, allowmembermessage, channel_id
  server = str(member.guild.id)
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
        channel = bot.get_channel(channel_id[server])
        await channel.send(f'{member.mention}, {membermessage[server]}')
  else:
    return


@bot.command(helpinfo='Searches the web (or images if typed first)', aliases=['search'])
async def google(ctx, *, searchquery: str):
  searchquerylower = searchquery.lower()
  if searchquerylower.startswith('images '):
    await ctx.send('<https://www.google.com/search?tbm=isch&q={}>'.format(urllib.parse.quote_plus(searchquery[7:])))
  else:
    await ctx.send('<https://www.google.com/search?q={}>'.format(urllib.parse.quote_plus(searchquery)))



@bot.command()
async def servers(ctx):
  servers = bot.guilds
  servers.sort(key=lambda x: x.member_count, reverse=True)
  await ctx.send('***Top servers with Dr. Sped:***')
  for x in servers[:5]:
    async with ctx.channel.typing():
      await ctx.send('**{}**, **{}** Members, {} region, Owned by <@{}>, Created at {}\n{}'.format(x.name, x.member_count, x.region, x.owner_id, x.created_at, x.icon_url_as(format='png',size=32)))
  y = 0
  for x in  bot.guilds:
    y += x.member_count
  await ctx.send('**Total number of Dr. Sped users:** ***{}***!\n**Number of servers:** ***{}***!'.format(y, len(bot.guilds)))



@bot.command()
async def slots(ctx):
  parrot = ':parrot:'
  slotspin = '<:pepe_cry:712063226292076564>'
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
      #await ctx.message.channel.send( "{}\n {} You Won".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} You Won".format(results0,ctx.message.author.mention),delete_after=3)
  elif slot6 == slot7 == slot8 == slot9 == slot10:
      #await ctx.message.channel.send( "{}\n {} You Won".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} You Won".format(results1,ctx.message.author.mention),delete_after=3)
  elif slot11 == slot12 == slot13 == slot14 == slot15:
      #await ctx.message.channel.send( "{}\n {} You Won".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} You Won".format(results2,ctx.message.author.mention),delete_after=3)
  elif slot16 == slot17 == slot18 == slot19 == slot20:
      #await ctx.message.channel.send( "{}\n {} You Won".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} You Won".format(results3,ctx.message.author.mention),delete_after=3)
  elif slot21 == slot22 == slot23 == slot24 == slot25:
      #await ctx.message.channel.send( "{}\n {} You Won".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} You Won".format(results4,ctx.message.author.mention),delete_after=3)
  elif slot1 == slot6 == slot11 == slot16 == slot21:
      #await ctx.message.channel.send( "{}\n {} You Won".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} You Won".format(results5,ctx.message.author.mention),delete_after=3)
  elif slot2 == slot7 == slot12 == slot17 == slot22:
      #await ctx.message.channel.send( "{}\n {} You Won".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} You Won".format(results6,ctx.message.author.mention),delete_after=3)
  elif slot3 == slot8 == slot13 == slot18 == slot23:
      #await ctx.message.channel.send( "{}\n {} You Won".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} You Won".format(results7,ctx.message.author.mention),delete_after=3)
  elif slot4 == slot9 == slot14 == slot19 == slot24:
      #await ctx.message.channel.send( "{}\n {} You Won".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} You Won".format(results8,ctx.message.author.mention),delete_after=3)
  elif slot5 == slot10 == slot15 == slot20 == slot25:
      #await ctx.message.channel.send( "{}\n {} You Won".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} You Won".format(results9,ctx.message.author.mention),delete_after=3)
  elif slot1 == slot7 == slot13 == slot19 == slot25:
      #await ctx.message.channel.send( "{}\n {} You Won".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} You Won".format(results10,ctx.message.author.mention),delete_after=3)
  elif slot5 == slot9 == slot13 == slot17 == slot21:
      #await ctx.message.channel.send( "{}\n {} You Won".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} You Won".format(results11,ctx.message.author.mention),delete_after=3)
  else:
      #await ctx.message.channel.send("{}\n {} You Lost".format(slotOutput,ctx.message.author.mention),delete_after=5)
      await msg.edit(content="{}\n {} You Lost".format(slotOutput,ctx.message.author.mention))

@bot.command()
async def logout(ctx):
  dev = str(ctx.message.author.id)
  if dev == '486662307217276948':
    await ctx.send('done')
    await bot.logout()
  else:
    return

@bot.event
async def on_command(ctx):
  global commands2
  global levels, exp
  user = str(ctx.message.author.id)
  levels[user] = levels[user] if user in levels else 0
  exp[user] = exp[user] if user in exp else 0
  commands2[user] = commands2[user] if user in commands2 else 0
  commands2[user] += 1

  MAX_XP = levels[user] * 100
  BEFORE_LEVEL_UP = MAX_XP - 10


  if exp[user] == BEFORE_LEVEL_UP:
    levels[user] += 1
    exp[user] = 0
    exp[user] += 10
  else:
    if exp[user] < MAX_XP:
      exp[user] += 10
    else:
      levels[user] += 1
      exp[user] = 0
      exp[user] += 10



  try: 
    with open(COMMANDS_FILE, 'w') as fp: 
      json.dump(commands2, fp) 
  except FileNotFoundError: 
    return

  try: 
    with open(LEVEL_FILE, 'w') as fp: 
      json.dump(levels, fp) 
  except FileNotFoundError: 
    return
    
  try: 
    with open(EXP_FILE, 'w') as fp: 
      json.dump(exp, fp) 
  except FileNotFoundError: 
    return


@bot.event
async def on_reaction_add(reaction, user):
  global allowreactionmessage
  server = str(reaction.message.guild.id)
  allowreactionmessage[server] = allowreactionmessage[server] if server in allowreactionmessage else 0
  channel = reaction.message.channel
  while allowreactionmessage[server] == 1:
    await channel.send(f'{user.name} reacted with {reaction.emoji} to the message: `{reaction.message.content}`')
    break



@bot.event
async def on_message(message):

  if message.author.id == bot.user.id:
    return
  
  # if message.author.id in bot.blacklisted_users:
  #   return

  if message.content.lower() == 'Dr. Sped#9675':
    embed = discord.Embed(title = "Dr. Sped Command Center", description = 'head into a world full of memes', color = random.choice(random_colors))
  
    embed.add_field(name = ':smile: Fun', value = f'`le help fun`')

    embed.add_field(name = ':hammer: Moderation', value = "`le help moderation`")

    embed.add_field(name = ':money_with_wings: Currency', value = "`le help currency`")

    embed.add_field(name = ':alien: Other', value = "`le help other`")

    embed.add_field(name = ':axe: Settings', value = "`le help settings`")

    embed.add_field(name = ':b: Text', value = '`le help text`')

    embed.set_footer(text = 'use `le` before each command!')

    await message.channel.send(embed = embed)

  await bot.process_commands(message)



@bot.command()
async def blacklist(ctx, user: discord.Member):
  if ctx.message.author.id == 486662307217276948 or ctx.message.author.id == 494264415613616157:
    bot.blacklisted_users.append(user.id)
    data = read_json("blacklist")
    data["blacklistedUsers"].append(user.id)
    write_json(data, "blacklist")
    await ctx.send(f'**{user.name}** has been blacklisted')
  else:
    await ctx.send('only the **OWNER** of this bot can do that lmao')

@bot.command()
async def unblacklist(ctx, user: discord.Member):
  if ctx.message.author.id == 486662307217276948 or ctx.message.author.id == 494264415613616157:
    bot.blacklisted_users.remove(user.id)
    data = read_json("blacklist")
    data["blacklistedUsers"].remove(user.id)
    write_json(data, "blacklist")
    await ctx.send(f'**{user.name}** has been unblacklisted')
  else:
    await ctx.send('only the **OWNER** of this bot can do that lmao')

@bot.command(aliases = ['sp'])
async def setprefix(ctx, *, pre):

  await ctx.send('Would you like a space after the prefix?\nEx: [prefix] meme\n`y` or `n`')
  msg = await bot.wait_for('message', check = lambda m: m.author == ctx.author)
  if msg.content.lower() == 'Y' or msg.content.lower() == 'y': 
    with open(r"prefixes.json", 'r') as f:
      prefixes = json.load(f)

    pre2 = pre + ' '
    prefixes[str(ctx.guild.id)] = pre2
    embed = discord.Embed(description = f'Changed prefix to `{pre}`', color = random.choice(random_colors))
    await ctx.send(embed = embed)

    with open(r"prefixes.json", 'w') as f:
      json.dump(prefixes, f, indent = 4)
  elif msg.content.lower() == 'n' or msg.content.lower() == 'N':
    with open(r"prefixes.json", 'r') as f:
      prefixes = json.load(f)

      prefixes[str(ctx.guild.id)] = pre
      embed = discord.Embed(description = f'Changed prefix to `{pre}`', color = random.choice(random_colors))
      await ctx.send(embed = embed)

    with open(r"prefixes.json", 'w') as f:
      json.dump(prefixes, f, indent = 4)
  else:
    await ctx.send('dos that look like an option')


@bot.command(aliases = ['rp'])
async def resetprefix(ctx):

  with open(r"prefixes.json", 'r') as f:
    prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = 'le '
    embed = discord.Embed(description = f'Changed prefix back to `le`', color = random.choice(random_colors))
    await ctx.send(embed = embed)

  with open(r"prefixes.json", 'w') as f:
    json.dump(prefixes, f, indent = 4)

@bot.command(aliases = ['tbg'])
async def thotsbegone(ctx):
  await ctx.send('thots')
  await asyncio.sleep(1.5)
  await ctx.send('be')
  await asyncio.sleep(1.5)
  await ctx.send('**GONE**')

@bot.command()
async def info(ctx):
  embed = discord.Embed(title = 'Dr. Sped info', color = random.choice(random_colors))

  embed.add_field(name = 'Library', value = 'discord.py', inline = True)

  embed.add_field(name = 'Creator', value = 'oofma#5318, (13 year old loser)', inline = False)

  embed.add_field(name = 'Version', value = 'v2.12.3', inline = False)

  embed.add_field(name = 'Other Devs', value = 'ya boi got no friends :<', inline = False)

  embed.add_field(name = 'Command Count', value = '102', inline = False)

  embed.add_field(name = 'time it took for that loser of an owner to write this shit bot', value = '9 months, 26 days',inline = False)

  await ctx.send(embed = embed)

@bot.group(invoke_without_command = True, pass_context = True)
async def help(ctx):
  embed = discord.Embed(title = "Dr. Sped Command Center", description = 'head into a world full of memes', color = random.choice(random_colors))
  
  embed.add_field(name = ':smile: Fun', value = f'`le help fun`', inline = True)

  embed.add_field(name = ':hammer: Moderation', value = "`le help moderation`", inline = False)

  embed.add_field(name = ':money_with_wings: Currency', value = "`le help currency`", inline = False)

  embed.add_field(name = ':alien: Other', value = "`le help other`", inline = False)

  embed.add_field(name = ':axe: Settings', value = "`le help settings`", inline = False)

  embed.add_field(name = ':b: Text', value = '`le help text`', inline = False)

  embed.set_footer(text = 'use `le` before each command!')

  await ctx.send(embed = embed)





@help.command(name = 'currency')
async def currency_subcommand(ctx):
  embed = discord.Embed(title = ":money_with_wings: Currency Commands", description = '`plead`, `bal`, `buy`, `sell`, `notebook`, `combine`, `pharmacy`, `rice`, `sheep`, `buffalo`, `pig`, `farm`, `cook`, `shop`, `popeyes`, `grab`, `use`, `health`, `jetshop`, `fly`, `get`, `city`, `upgrade`, `requirements`, `create`, `work`, `purchase`, `cowmarket`, `twitch`, `profile`', color = random.choice(random_colors))
  embed.set_footer(text = 'use `le` before each command!')
  await ctx.send(embed = embed)





@help.command(name = 'fun')
async def fun_subcommand(ctx):
  embed = discord.Embed(title = ":smile: Fun Commands", description = '`redditr8`, `yo`, `meme`, `thotsbegone`, `automemez`, `stopmemez`, `youtube`, `urban`, `supreme`, `reverse`, `dog`, `cat`, `birb`, `duck`, `coinflip`', color = random.choice(random_colors))
  embed.set_footer(text = 'use `le` before each command!')
  await ctx.send(embed = embed)




@help.command(name = 'moderation')
async def mod_subcommand(ctx):
  embed = discord.Embed(title = ":hammer: Moderation Commands", description = '`kick`, `ban`, `unban`, `purge`, `userinfo`, `warn`, `credits`, `createrole`, `reactionmessage`, `membermessage`, `setmembermessage`, `setchannelid`, `viewmembermessage`, `info`, `autopurge`, `stoppurge`, `new`, `delete`, `lock`, `unlock`', color = random.choice(random_colors))
  embed.set_footer(text = 'use `le` before each command!')
  await ctx.send(embed = embed)


@help.command(name = 'other')
async def other_subcommand(ctx):
  embed = discord.Embed(title = ':alien: Other Commands', description = '`mainstuff`, `dmdev`', color = random.choice(random_colors))
  embed.set_footer(text = 'use `le` before each command!')
  await ctx.send(embed = embed)




@help.command(name = 'settings')
async def settings_subcommand(ctx):
  embed = discord.Embed(title = ':axe: Setting Commands', description = '`setprefix`, `resetprefix`', color = random.choice(random_colors))
  embed.set_footer(text = 'use `le` before each command!')
  await ctx.send(embed = embed)





@help.command(name = 'text')
async def text_subcommand(ctx):
  embed = discord.Embed(title = ':b: Text Commands', description = '`greenify`, `bify`, `echo`, `ubi`, `underline`, `bold`, `italics`, `codeblock`, `strikethrough`, `underlineitalics`, `underlinebold`, `bolditalics`', color = random.choice(random_colors))
  embed.set_footer(text = 'use `le` before each command!')
  await ctx.send(embed = embed)










@bot.command()
async def yo(ctx):
  await ctx.send(':l')





@bot.command()
async def redditr8(ctx):  
  embed = discord.Embed(title="reddit r8 determiner", description=f"You are {random.randint(1, 100)}% redditor", color = random.choice(random_colors))
  await ctx.send(embed=embed)

# @bot.command(aliases = ['sps'])
# async def setpersonalstring(ctx, *, string: str):
#   global personalstring
#   user = str(ctx.message.author.id)
#   personalstring[user] = personalstring[user] if user in personalstring else ''

#   await ctx.send(f'String: `{string}` added to dictionary: `personalstring` defined on with open as file, not fp')
#   personalstring[user] = string

#   print(f'In beg(): Saving balances = {personalstring}')
#   try: 
#     with open(PERSONAL_STRING, 'w') as fp: 
#       json.dump(personalstring, fp) 
#   except FileNotFoundError: 
#     print(f'In balances(): File {PERSONAL_STRING} not found! Not sure what to do here!') 

# @bot.command(aliases = ['ps'])
# async def showpersonalstring(ctx):
#   global personalstring
#   user = str(ctx.message.author.id)
#   personalstring[user] = personalstring[user] if user in personalstring else ''
  
#   await ctx.send(f'{personalstring[user]}')

@bot.command(aliases = ['mm'])
@has_permissions(manage_guild = True)
async def membermessage(ctx):
  global allowmembermessage
  server = str(ctx.guild.id)
  allowmembermessage[server] = allowmembermessage[server] if server in allowmembermessage else 0
  if allowmembermessage[server] == 0:
    await ctx.send('Sending messages when a member joins is set to: **True**\nCustomize the message in `le setmembermessage`')
    allowmembermessage[server] = 1
  else:
    await ctx.send('Sending messages when a member joins is set to: **False**')
    allowmembermessage[server] = 0

  print(f'In beg(): Saving balances = {allowmembermessage}')
  try: 
    with open(ALLOW_MEMBER_MESSAGE, 'w') as fp: 
      json.dump(allowmembermessage, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {ALLOW_MEMBER_MESSAGE} not found! Not sure what to do here!') 

@bot.command(aliases = ['smm'])
@has_permissions(manage_guild=True)
async def setmembermessage(ctx, *, string: str):
  global allowmembermessage, membermessage
  server = str(ctx.guild.id)
  allowmembermessage[server] = allowmembermessage[server] if server in allowmembermessage else 0
  membermessage[server] = membermessage[server] if server in membermessage else ''

  if allowmembermessage[server] == 1:
    await ctx.send(f'The final result will look like this:\n***member is mentioned here***, {string}\nGood? `y` or `n`')
    msg = await bot.wait_for('message', check = lambda m: m.author == ctx.author)
    if msg.content.lower() == 'y' or msg.content.lower() == 'Y':
      membermessage[server] = string
      await ctx.send('completed, btw you need to give me a proper channel id to send the messages to using `le setchannelid`\nif the id is not proper, then you can guess why its not working')
    elif msg.content.lower() == 'N' or msg.content.lower() == 'n':
      await ctx.send('rip lol you chose not to use that')
      membermessage[server] == ''
  else:
    await ctx.send('you don\'t even have member joining messaging enabled! to do that do `le membermessage`')

  print(f'In beg(): Saving balances = {membermessage}')
  try: 
    with open(MEMBER_MESSAGE, 'w') as fp: 
      json.dump(membermessage, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {MEMBER_MESSAGE} not found! Not sure what to do here!') 
  
@bot.command()
async def viewmembermessage(ctx):
  global membermessage
  server = str(ctx.guild.id)
  if server in membermessage:
    if membermessage[server] == '':
      await ctx.send('You don\'t have a member joining message set!')
    else:
      await ctx.send(f'{membermessage[server]}')
  else:
    await ctx.send('You don\'t have a member joining message set!')

@bot.command()
@has_permissions(manage_guild = True)
async def setchannelid(ctx, id: int):
  global channel_id, allowmembermessage
  server = str(ctx.guild.id)
  allowmembermessage[server] = allowmembermessage[server] if server in allowmembermessage else 0
  channel_id[server] = channel_id[server] if server in channel_id else 0
  
  if allowmembermessage[server] == 1:
    if len(str(id)) < 18 or len(str(id)) > 18:
      await ctx.send('thats not a valid channel id you sped')
    else:
      channel_id[server] = id
      await ctx.send(f'set channel id as: `{id}`')
  else:
    await ctx.send('if you don\'t have member joining message allowed, how tf u gonna set channel id?\nallow it using `le membermessage`')

  print(f'In beg(): Saving balances = {channel_id}')
  try: 
    with open(CHANNEL_ID, 'w') as fp: 
      json.dump(channel_id, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {CHANNEL_ID} not found! Not sure what to do here!')

@bot.command()
@has_permissions(manage_guild = True)
async def reactionmessage(ctx):
  global allowreactionmessage
  server = str(ctx.guild.id) 
  allowreactionmessage[server] = allowreactionmessage[server] if server in allowreactionmessage else 0
  if allowreactionmessage[server] == 0:
    await ctx.send('Sending messages when reactions are executed is set to: **True**')
    allowreactionmessage[server] = 1
  else:
    await ctx.send('Sending messages when reactions are executed is set to: **False**')
    allowreactionmessage[server] = 0

  print(f'In beg(): Saving balances = {allowreactionmessage}')
  try: 
    with open(ALLOW_REACTION_MESSAGE, 'w') as fp: 
      json.dump(allowreactionmessage, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {ALLOW_REACTION_MESSAGE} not found! Not sure what to do here!') 

@bot.command(pass_context=True)
async def automemez(ctx, timeout: float):
  global autoMeme
  autoMeme = True
  while autoMeme == True:
    await meme(ctx)
    await asyncio.sleep(timeout)

@bot.command()
async def stopmemez(ctx):
  global autoMeme
  autoMeme = False
  await ctx.send('done')

@bot.command(pass_context=True)
async def meme(ctx):
  embed = discord.Embed(color = random.choice(random_colors))

  async with aiohttp.ClientSession() as cs:
    async with cs.get('https://www.reddit.com/u/kerdaloo/m/dankmemer/top/.json?sort=top&t=day&limit=500') as r:
      res = await r.json()
      embed.set_image(url = res['data']['children'] [random.randint(0, 30)]['data']['url'])
      await ctx.send(embed=embed)


@bot.command()
async def darkhumor(ctx):
  embed = discord.Embed(color = random.choice(random_colors))

  async with aiohttp.ClientSession() as cs:
    async with cs.get('https://www.reddit.com/r/DarkHumorAndMemes/new.json?sort=hot') as r:
      res = await r.json()
      embed.set_image(url = res['data']['children'] [random.randint(0, 25)]['data']['url'])
      await ctx.send(embed=embed)

#------------------------
#------------------------
#MOD COMMANDS
#------------------------
#------------------------   





@bot.command()
async def credits(ctx):
  await ctx.send('My Creator: bald rat#5318')







    




@bot.command()
async def guess(ctx):
  await ctx.send('guess a number from 1-10')
  answer = random.randint(1, 10)
  msg = await bot.wait_for('message', check = lambda m: m.author == ctx.author, timeout = 6.0)



  if msg.content.startswith(f'{answer}'):
    await ctx.send('correct, noice')
  else:
    await ctx.send(f'no stoopid it was **{answer}**')



#------------------------
#------------------------
#CURRENCY COMMANDS
#------------------------
#------------------------

@bot.command(aliases = ['cm'])
async def cowmarket(ctx):
  embed = discord.Embed(title = 'Cow Market', description = 'le purchase [ex: mooshroom]\nle stew [ex: mooshroom]', color = random.choice(random_colors))
  embed.add_field(name = 'Basic Cows', value = '<:mooshroom:716492779391418440> **Mooshroom Cow**\n- Gives 15 ***mushroom stew*** every farm\n- Price: __14400__ coins\n- Can only be used 15 times, then it dies')
  await ctx.send(embed = embed)

@bot.command()
async def purchase(ctx, arg, amount : int):
  global balances, mooshroom_cows
  user = str(ctx.message.author.id)
  balances[user] = balances[user] if user in balances else 0
  mooshroom_cows[user] = mooshroom_cows[user] if user in mooshroom_cows else 0

  if arg == 'mooshroom' or arg == 'Mooshroom':
    if balances[user] == 14400 or balances[user] > 14400:
      price_for_mcow = 14400 * amount
      if balances[user] > price_for_mcow or balances[user] == price_for_mcow:
        mooshroom_cows[user] += amount
        balances[user] -= price_for_mcow
        embed = discord.Embed(title = 'Purchase Complete', description = f'You bought **{amount}** mooshroom cows for `{price_for_mcow} coins`', color = random.choice(random_colors))
        await ctx.send(embed = embed)
      else:
        await ctx.send('u don\'t got the money man')
    else:
      await ctx.send('u don\'t got the money man')
  else:
    await ctx.send('not an option  :l')

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 

  print(f'In beg(): Saving balances = {mooshroom_cows}')
  try: 
    with open(MOOSHROOM_COW_FILE, 'w') as fp: 
      json.dump(mooshroom_cows, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {MOOSHROOM_COW_FILE} not found! Not sure what to do here!') 

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
        embed = discord.Embed(title = f'{ctx.message.author.name}\'s harvest ', description = f"You just recieved <:mushstew:716492699879997530> **15** mushroom stew from your <:mooshroom:716492779391418440> mooshroom cow", color = random.choice(random_colors))
        await ctx.send(embed = embed)   
      else:
        await ctx.send('You need at least 15 bowls for this!')
    else:
      await ctx.send('your <:mooshroom:716492779391418440> mooshroom cow has been used 15 times, making it weak, resulting in its perish')
      await asyncio.sleep(3)
      await ctx.send('may it rest in peace')
      await asyncio.sleep(3)
      await ctx.send('<:mooshroom:716492779391418440>')
      mooshroom_cows[user] -= 1
      times_mooshroom[user] = 0
  else:
    await ctx.send('YOU DONT EVEN HAVE A COW LMAO')

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
async def setbank(ctx, member: discord.Member, amount: int):
  global balances
  user = str(ctx.message.author.id)
  member2 = str(member.id)
  if user == '486662307217276948':
    if member2 in balances:
      balances[member2] = amount
      await ctx.send(f'{member.name}\'s bank account value has been set to : **{amount}**')
    else:
      await ctx.send(f'{member.name} doesn\'t have a bank account')
  else:
    await ctx.send('AHAAAA you thought only the **OWNER** of this bot can use this ')

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 

@bot.command()
@commands.cooldown(1, 90, commands.BucketType.user)
async def twitch(ctx):
  global balances, pc
  user = str(ctx.message.author.id)
  pc[user] = pc[user] if user in pc else 0
  if pc[user] > 0:
    await ctx.send('whatcha wanna stream today?\n`fortnite`, `minecraft`, `pubg`, or `geo dash`')
    msg = await bot.wait_for('message', check = lambda m: m.author == ctx.author)
    
    if msg.content.lower() == 'fortnite' or msg.content.lower() == 'FORTNITE' or msg.content.lower() == 'Fortnite' or msg.content.lower() == 'f' or msg.content.lower() == 'F':
      CHANCE = random.randint(1, 100)
      if CHANCE < 75 or CHANCE == 75:
        random_coins = random.randint(500, 1000)
        await ctx.send(f'you streamed fortnite and turns out people actually liked it\nyou earned **{random_coins}** coins')
        balances[user] += random_coins
      else:
        await ctx.send('welp, nobody watched ur stream giving you **0** coins lmaooo')
    elif msg.content.lower() == 'mc' or msg.content.lower() == 'minecraft' or msg.content.lower() == 'MINECRAFT' or msg.content.lower() == 'Minecraft' or msg.content.lower() == 'MC' or msg.content.lower() == 'Mc' or msg.content.lower() == 'm' or msg.content.lower() == 'M':
      CHANCE = random.randint(1, 100)
      if CHANCE < 75 or CHANCE == 75:
        random_coins = random.randint(500, 1000)
        await ctx.send(f'you streamed sum mc and turns out people actually liked it\nyou earned **{random_coins}** coins')
        balances[user] += random_coins
      else:
        await ctx.send('welp, nobody watched ur stream giving you **0** coins lmaooo')
    elif msg.content.lower() == 'pubg' or msg.content.lower() == 'PUBG' or msg.content.lower() == 'Pubg' or msg.content.lower() == 'p' or msg.content.lower() == 'P':
      CHANCE = random.randint(1, 100)
      if CHANCE < 75 or CHANCE == 75:
        random_coins = random.randint(500, 1000)
        await ctx.send(f'you streamed pubg and turns out people actually liked it\nyou earned **{random_coins}** coins')
        balances[user] += random_coins
      else:
        await ctx.send('welp, nobody watched ur stream giving you **0** coins lmaooo')
    elif msg.content.lower() == 'geo' or msg.content.lower() == 'geo dash' or msg.content.lower() == 'Geo dash' or msg.content.lower() == 'geo Dash' or msg.content.lower() == 'GEO DASH' or msg.content.lower() == 'gd' or msg.content.lower() == 'GD' or msg.content.lower() == 'Gd':
      CHANCE = random.randint(1, 100)
      if CHANCE < 75 or CHANCE == 75:
        random_coins = random.randint(500, 1000)
        await ctx.send(f'you streamed geo dash and turns out people actually liked it\nyou earned **{random_coins}** coins')
        balances[user] += random_coins
      else:
        await ctx.send('welp, nobody watched ur stream giving you **0** coins lmaooo')
    else:
      await ctx.send('dos that look like an option ')
  else:
    await ctx.send('u don\'t have a pc ')

  print(f'In buy(): Saving sheeps = {pc}')
  try: 
    with open(PC_FILE, 'w') as fp: 
      json.dump(pc, fp) 
  except FileNotFoundError: 
    print(f'In buy(): File {PC_FILE} not found! Not sure what to do here!') 

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 





@bot.command()
async def city(ctx):
  global locations, cities, citypop, entertainment_lvl, park_lvl, power_lvl, water_lvl, waste_lvl, health_lvl, fire_lvl, police_lvl
  user = str(ctx.message.author.id)
  cities[user] = cities[user] if user in cities else 0
  locations[user] = locations[user] if user in locations else 0
  citypop[user] = citypop[user] if user in citypop else 0
  entertainment_lvl[user] = entertainment_lvl[user] if user in entertainment_lvl else 0
  park_lvl[user] = park_lvl[user] if user in park_lvl else 0
  power_lvl[user] = power_lvl[user] if user in power_lvl else 0
  water_lvl[user] = water_lvl[user] if user in water_lvl else 0
  waste_lvl[user] = waste_lvl[user] if user in waste_lvl else 0
  health_lvl[user] = health_lvl[user] if user in health_lvl else 0
  fire_lvl[user] = fire_lvl[user] if user in fire_lvl else 0 
  police_lvl[user] = police_lvl[user] if user in police_lvl else 0

  ent_pop_added = entertainment_lvl[user] * 867
  park_pop_added = park_lvl[user] * 1001
  power_pop_added = power_lvl[user] * 2467
  water_pop_added = water_lvl[user] * 2227
  waste_pop_added = waste_lvl[user] * 3142
  health_pop_added = health_lvl[user] * 7819
  fire_pop_added = fire_lvl[user] * 6231
  police_pop_added = police_lvl[user] * 9331

  #medium then advanced then normal

  if locations[user] == 1:
    if cities[user] == 1:
      if power_lvl[user] == 4 and water_lvl[user] in [5, 6, 7] and waste_lvl[user] in [3, 4] and health_lvl[user] in [2, 3] and park_lvl[user] == 5 and entertainment_lvl[user] in [3, 4, 5, 6] and fire_lvl[user] in [2, 3] and police_lvl[user] in [2, 3]:
        embed = discord.Embed(title = f':city_dusk: {ctx.message.author.name}\'s Medium city', description = '`le requirements [medium/advanced city]`\n`le upgrade [Section]`\n`le collect [section]`', color = random.choice(random_colors))
        embed.add_field(name = '__**Overview**__', value = f':man: **Population**: __**{citypop[user]:,d}**__', inline = False)
        embed.add_field(name = '__**Basic City Needs**__', value = f':cloud_lightning: **Power**: Lvl: {power_lvl[user]:,d}\n\tPopulation Added: **{power_pop_added:,d}**\n:cup_with_straw: **Water**: Lvl: {water_lvl[user]:,d}\n\tPopulation Added: **{water_pop_added:,d}**\n:wastebasket: **Waste**: Lvl: {waste_lvl[user]:,d}\n\tPopulation Added: **{waste_pop_added:,d}**', inline = True)
        embed.add_field(name = '__**Urgent Needs**__', value = f':fire_engine: **Fire Station**: Lvl : {fire_lvl[user]:,d}\n\tPopulation Added: **{fire_pop_added:,d}**\n:police_car: **Police Station**: Lvl: {police_lvl[user]:,d}\n\tPopulation Added: **{police_pop_added:,d}**\n:ambulance: **Health**: Lvl: {health_lvl[user]:,d}\n\tPopulation Added: **{health_pop_added:,d}**', inline = False)
        embed.add_field(name = '__**Population Boosters**__', value = f':musical_note: **Entertainment**: Lvl: {entertainment_lvl[user]:,d}\n\tPopulation Added: **{ent_pop_added:,d}**\n:island: **Parks**: Lvl: {park_lvl[user]:,d}\n\tPopulation Added: **{park_pop_added:,d}**', inline = False)
        await ctx.send(embed = embed)
      elif power_lvl[user] == 5 and water_lvl[user] == 8 and waste_lvl[user] == 5 and health_lvl[user] == 4 and entertainment_lvl[user] == 7 and park_lvl[user] == 6 and fire_lvl[user] == 4 and police_lvl[user] == 4:
        embed = discord.Embed(title = f':city_dusk: {ctx.message.author.name}\'s Advanced city', description = '`le requirements [medium/advanced city]`\n`le upgrade [Section]`\n`le collect [section]`', color = random.choice(random_colors))
        embed.add_field(name = '__**Overview**__', value = f':man: **Population**: __**{citypop[user]:,d}**__', inline = False)
        embed.add_field(name = '__**Basic City Needs**__', value = f':cloud_lightning: **Power**: Lvl: {power_lvl[user]:,d}\n\tPopulation Added: **{power_pop_added:,d}**\n:cup_with_straw: **Water**: Lvl: {water_lvl[user]:,d}\n\tPopulation Added: **{water_pop_added:,d}**\n:wastebasket: **Waste**: Lvl: {waste_lvl[user]:,d}\n\tPopulation Added: **{waste_pop_added:,d}**', inline = True)
        embed.add_field(name = '__**Urgent Needs**__', value = f':fire_engine: **Fire Station**: Lvl : {fire_lvl[user]:,d}\n\tPopulation Added: **{fire_pop_added:,d}**\n:police_car: **Police Station**: Lvl: {police_lvl[user]:,d}\n\tPopulation Added: **{police_pop_added:,d}**\n:ambulance: **Health**: Lvl: {health_lvl[user]:,d}\n\tPopulation Added: **{health_pop_added:,d}**', inline = False)
        embed.add_field(name = '__**Population Boosters**__', value = f':musical_note: **Entertainment**: Lvl: {entertainment_lvl[user]:,d}\n\tPopulation Added: **{ent_pop_added:,d}**\n:island: **Parks**: Lvl: {park_lvl[user]:,d}\n\tPopulation Added: **{park_pop_added:,d}**', inline = False)
        await ctx.send(embed = embed)
      else:
        embed = discord.Embed(title = f':city_dusk: {ctx.message.author.name}\'s city', description = '`le requirements [medium/advanced city]`\n`le upgrade [Section]`\n`le collect [section]`', color = random.choice(random_colors))
        embed.add_field(name = '__**Overview**__', value = f':man: **Population**: __**{citypop[user]:,d}**__', inline = False)
        embed.add_field(name = '__**Basic City Needs**__', value = f':cloud_lightning: **Power**: Lvl: {power_lvl[user]:,d}\n\tPopulation Added: **{power_pop_added:,d}**\n:cup_with_straw: **Water**: Lvl: {water_lvl[user]:,d}\n\tPopulation Added: **{water_pop_added:,d}**\n:wastebasket: **Waste**: Lvl: {waste_lvl[user]:,d}\n\tPopulation Added: **{waste_pop_added:,d}**', inline = True)
        embed.add_field(name = '__**Urgent Needs**__', value = f':fire_engine: **Fire Station**: Lvl : {fire_lvl[user]:,d}\n\tPopulation Added: **{fire_pop_added:,d}**\n:police_car: **Police Station**: Lvl: {police_lvl[user]:,d}\n\tPopulation Added: **{police_pop_added:,d}**\n:ambulance: **Health**: Lvl: {health_lvl[user]:,d}\n\tPopulation Added: **{health_pop_added:,d}**', inline = False)
        embed.add_field(name = '__**Population Boosters**__', value = f':musical_note: **Entertainment**: Lvl: {entertainment_lvl[user]:,d}\n\tPopulation Added: **{ent_pop_added:,d}**\n:island: **Parks**: Lvl: {park_lvl[user]:,d}\n\tPopulation Added: **{park_pop_added:,d}**', inline = False)
        await ctx.send(embed = embed)
    else:
      await ctx.send('You don\'t have a city! To get one, do `le create`')
  else:
    await ctx.send('You must be in Texas in order to view/create your city')


@bot.command()
async def youtube(ctx, *, search):
  
  query_string = urllib.parse.urlencode({'search_query': search})
  htm_content = urllib.request.urlopen('https://www.youtube.com/results?' + query_string)
  search_results = re.findall('href=\"\\/watch\\?v=(.{11})', htm_content.read().decode())
  await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])


@bot.group(invoke_without_command = True, pass_context = True)
async def upgrade(ctx):
  await ctx.send('__**Upgrading in your city**__\n\t- First, spend your money on the URGENT needs for the city such as: Fire, Health, and Police\n\t- Boost population by upgrading Parks and Entertainment\n\t- The more population you get, the more revenue you get!\n\t- Find the requirements to get medium and advanced city with `le requirements [advanced city/medium city]`\n\t- Do `le collect [fire/health/police/entertainment/park]`\n\t- Do `le upgrade [section of city]` to upgrade the section\'s levels for revenue!')





@upgrade.command()
async def shop(ctx):
  embed = discord.Embed(title = 'Upgrading costs', description = 'The price of each item multiplies depending what level you are upgrading to\nEX: Upgrading to lvl 3 Entertainment costs 300 Meat, 36000 coins, 30 rice, and 6 salads', color = random.choice(random_colors))
  embed.add_field(name = '**Entertainment**', value = 'Price: __100 Meat__, __12,000 coins__, __10 rice__, __2 salads__\nAdds 867 population every level upgrade', inline = True)
  embed.add_field(name = '**Parks**', value = 'Price: __230 Wheat__, __19,000 coins__, __420 wool__, __10 salads__\nAdds 1,001 population every level upgrade', inline = False)
  embed.add_field(name = '**Power**', value = 'Price: __150 Meat__, __10,400 coins__, __20 salads__\nAdds 2,467 population every level upgrade', inline = False)
  embed.add_field(name = '**Water**', value = 'Price: __260 Wheat__, __11,200 coins__, __12 salads__\nAdds 2,227 population every level upgrade', inline = False)
  embed.add_field(name = '**Waste**', value = 'Price: __320 Meat__, __15,600 coins__, __22 salads__\nAdds 3,142 population every level upgrade', inline = False)
  embed.add_field(name = '**Health**', value = 'Price: __720 Meat__, __28,920 coins__, __80 salads__\nAdds 7,819 population every level upgrade', inline = False)
  embed.add_field(name = '**Fire**', value = 'Price: __949 Wheat__, __26,200 coins__, __60 salads__\nAdds 6,231 population every level upgrade', inline = False)
  embed.add_field(name = '**Police**', value = 'Price: __1,001 Meat__, __42,620 coins__, __90 salads__\nAdds 9,331 population every level upgrade', inline = False)
  await ctx.send(embed = embed)


@bot.command()
async def key(ctx):
  embed = discord.Embed(title = 'Price Key', value = 'money money moneyyyyyy', color = random.choice(random_colors))
  embed.add_field(name = 'Pig', value = '- Price: __200__ coins\n- Gives 6 meat per pig every farm\n- 1 meat sells for __25__ coins')
  embed.add_field(name = 'Sheep', value = '- Price: __100__ coins\n- Gives 3 wool per sheep every farm\n- 1 wool sells for __15__ coins')
  embed.add_field(name = 'Rice', value = '- Price: __30__ coins\n- Gives 4 wheat per rice every farm\n- 1 wheat sells for __10__ coins')
  await ctx.send(embed = embed)




@upgrade.command()
async def parks(ctx):
  global wheats, balances, wools, salads, park_lvl, citypop, cities
  user = str(ctx.message.author.id)
  park_lvl[user] = park_lvl[user] if user in park_lvl else 0
  cities[user] = cities[user] if user in cities else 0
  citypop[user] = citypop[user] if user in citypop else 0
  salads[user] = salads[user] if user in salads else 0
  wools[user] = wools[user] if user in wools else 0
  wheats[user] = wheats[user] if user in wheats else 0
  balances[user] = balances[user] if user in balances else 0
  PARK_LEVEL_USER_UPGRADING_TO = park_lvl[user] + 1
  WOOL_COST = PARK_LEVEL_USER_UPGRADING_TO * 420
  WHEAT_COST = PARK_LEVEL_USER_UPGRADING_TO * 230
  COINS_COST = PARK_LEVEL_USER_UPGRADING_TO * 19000
  SALADS_COST = PARK_LEVEL_USER_UPGRADING_TO * 10
  if cities[user] == 1:
    if park_lvl[user] < 6:
      await ctx.send(f'Are you sure you want to do this?\n**It will cost you** __{WOOL_COST}__ **wool,** __{WHEAT_COST}__ **wheat,** __{COINS_COST}__ **coins, and** __{SALADS_COST}__ **salads**\n`y` or `n`')
      msg = await bot.wait_for('message', check = lambda m: m.author == ctx.author)
      if msg.content.lower() == 'y' or msg.content.lower() == 'Y':
        if salads[user] == SALADS_COST or salads[user] > SALADS_COST:
          if balances[user] == COINS_COST or balances[user] > COINS_COST:
            if wools[user] == WOOL_COST or wools[user] > WOOL_COST:
              if wheats[user] == WHEAT_COST or wheats[user] > WHEAT_COST:
                park_lvl[user] = PARK_LEVEL_USER_UPGRADING_TO
                balances[user] -= COINS_COST
                salads[user] -= SALADS_COST
                wheats[user] -= WHEAT_COST
                wools[user] -= WOOL_COST
                citypop[user] += 1001
                await ctx.send(f'Congratulations {ctx.message.author.mention}! Your __**Park**__ level is now **{PARK_LEVEL_USER_UPGRADING_TO}**\nGo check in `le city`!')
                await asyncio.sleep(1)
                await ctx.send(f'Congratulations {ctx.message.author.mention}! Your __**Population**__ is now **{citypop[user]:,d}**\nGo check in `le city`!')
              else:
                await ctx.send('You don\'t have enough wheat for this!')
            else:
              await ctx.send('You don\'t have enough wool for this!')
          else:
            await ctx.send('You don\'t have enough coins for this!')
        else:
          await ctx.send('You don\'t have enough salads for this!')
      elif msg.content.lower() == 'n' or msg.content.lower() == 'N':
        msg = await ctx.send('Cancelling purchase')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Cancelling purchase.')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Cancelling purchase..')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Cancelling purchase...')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Done')
      else:
        await ctx.send('not an option ')
    else:
      await ctx.send('You have reached the maximum level for parks!')
  else:
    await ctx.send('u don\'t have a city ')

  print(f'In sell(): Saving salads = {salads}')
  try: 
    with open(SALADS_FILE, 'w') as fp: 
      json.dump(salads, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {SALADS_FILE} not found! Not sure what to do here!') 

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 

  print(f'In beg(): Saving balances = {wools}')
  try: 
    with open(WOOL_FILE, 'w') as fp: 
      json.dump(wools, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {WOOL_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {citypop}')
  try: 
    with open(CITYPOP_FILE, 'w') as fp: 
      json.dump(citypop, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {CITYPOP_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {wheats}')
  try: 
    with open(WHEAT_FILE, 'w') as fp: 
      json.dump(wheats, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {WHEAT_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {park_lvl}')
  try: 
    with open(PARK_LVL_FILE, 'w') as fp: 
      json.dump(park_lvl, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {PARK_LVL_FILE} not found! Not sure what to do here!') 

@upgrade.command()
async def police(ctx):
  global meats, balances, salads, cities, citypop, police_lvl
  user = str(ctx.message.author.id)
  police_lvl[user] = police_lvl[user] if user in police_lvl else 0
  cities[user] = cities[user] if user in cities else 0
  citypop[user] = citypop[user] if user in citypop else 0
  salads[user] = salads[user] if user in salads else 0
  meats[user] = meats[user] if user in meats else 0
  balances[user] = balances[user] if user in balances else 0
  POLICE_LEVEL_USER_IS_UPGRADE_TO = police_lvl[user] + 1
  MEAT_COST = POLICE_LEVEL_USER_IS_UPGRADE_TO * 1001
  COINS_COST = POLICE_LEVEL_USER_IS_UPGRADE_TO * 42620
  SALADS_COST = POLICE_LEVEL_USER_IS_UPGRADE_TO * 90  


  if cities[user] == 1:
    if police_lvl[user] < 4:
      await ctx.send(f'Are you sure you want to do this?\n**It will cost you** __{MEAT_COST}__ **meat**, __{COINS_COST}__ **coins, and** __{SALADS_COST}__ **salads**\n`y` or `n`')
      msg = await bot.wait_for('message', check = lambda m: m.author == ctx.author)
      if msg.content.lower() == 'y' or msg.content.lower() == 'Y':
        if salads[user] == SALADS_COST or salads[user] > SALADS_COST:
          if balances[user] == COINS_COST or balances[user] > COINS_COST:
            if meats[user] == MEAT_COST or meats[user] > MEAT_COST:
              police_lvl[user] = POLICE_LEVEL_USER_IS_UPGRADE_TO
              balances[user] -= COINS_COST
              salads[user] -= SALADS_COST
              meats[user] -= MEAT_COST
              citypop[user] += 9331
              await ctx.send(f'Congratulations {ctx.message.author.mention}! Your __**Police**__ level is now **{POLICE_LEVEL_USER_IS_UPGRADE_TO}**\nGo check in `le city`!')
              await asyncio.sleep(1)
              await ctx.send(f'Congratulations {ctx.message.author.mention}! Your __**Population**__ is now **{citypop[user]:,d}**\nGo check in `le city`!')
            else:
                await ctx.send('You don\'t have enough meat for this!')
          else:
            await ctx.send('You don\'t have enough coins for this!')
        else:
          await ctx.send('You don\'t have enough salads for this!')
      elif msg.content.lower() == 'n' or msg.content.lower() == 'N':
        msg = await ctx.send('Cancelling purchase')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Cancelling purchase.')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Cancelling purchase..')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Cancelling purchase...')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Done')
      else:
        await ctx.send('not an option ')
    else:
      await ctx.send('You have reached the maximum level for police!')
  else:
    await ctx.send('u don\'t have a city ')

  print(f'In sell(): Saving salads = {salads}')
  try: 
    with open(SALADS_FILE, 'w') as fp: 
      json.dump(salads, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {SALADS_FILE} not found! Not sure what to do here!') 

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {citypop}')
  try: 
    with open(CITYPOP_FILE, 'w') as fp: 
      json.dump(citypop, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {CITYPOP_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {meats}')
  try: 
    with open(MEAT_FILE, 'w') as fp: 
      json.dump(meats, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {MEAT_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {police_lvl}')
  try: 
    with open(POLICE_LVL_FILE, 'w') as fp: 
      json.dump(police_lvl, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {POLICE_LVL_FILE} not found! Not sure what to do here!') 

@upgrade.command()
async def health(ctx):
  global meats, balances, salads, cities, citypop, health_lvl
  user = str(ctx.message.author.id)
  health_lvl[user] = health_lvl[user] if user in health_lvl else 0
  cities[user] = cities[user] if user in cities else 0
  citypop[user] = citypop[user] if user in citypop else 0
  salads[user] = salads[user] if user in salads else 0
  meats[user] = meats[user] if user in meats else 0
  balances[user] = balances[user] if user in balances else 0
  HEALTH_LEVEL_USER_IS_UPGRADE_TO = health_lvl[user] + 1
  MEAT_COST = HEALTH_LEVEL_USER_IS_UPGRADE_TO * 720
  COINS_COST = HEALTH_LEVEL_USER_IS_UPGRADE_TO * 28290
  SALADS_COST = HEALTH_LEVEL_USER_IS_UPGRADE_TO * 80  


  if cities[user] == 1:
    if health_lvl[user] < 4:
      await ctx.send(f'Are you sure you want to do this?\n**It will cost you** __{MEAT_COST}__ **meat**, __{COINS_COST}__ **coins, and** __{SALADS_COST}__ **salads**\n`y` or `n`')
      msg = await bot.wait_for('message', check = lambda m: m.author == ctx.author)
      if msg.content.lower() == 'y' or msg.content.lower() == 'Y':
        if salads[user] == SALADS_COST or salads[user] > SALADS_COST:
          if balances[user] == COINS_COST or balances[user] > COINS_COST:
            if meats[user] == MEAT_COST or meats[user] > MEAT_COST:
              health_lvl[user] = HEALTH_LEVEL_USER_IS_UPGRADE_TO
              balances[user] -= COINS_COST
              salads[user] -= SALADS_COST
              meats[user] -= MEAT_COST
              citypop[user] += 7819
              await ctx.send(f'Congratulations {ctx.message.author.mention}! Your __**Health**__ level is now **{HEALTH_LEVEL_USER_IS_UPGRADE_TO}**\nGo check in `le city`!')
              await asyncio.sleep(1)
              await ctx.send(f'Congratulations {ctx.message.author.mention}! Your __**Population**__ is now **{citypop[user]:,d}**\nGo check in `le city`!')
            else:
                await ctx.send('You don\'t have enough meat for this!')
          else:
            await ctx.send('You don\'t have enough coins for this!')
        else:
          await ctx.send('You don\'t have enough salads for this!')
      elif msg.content.lower() == 'n' or msg.content.lower() == 'N':
        msg = await ctx.send('Cancelling purchase')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Cancelling purchase.')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Cancelling purchase..')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Cancelling purchase...')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Done')
      else:
        await ctx.send('not an option ')
    else:
      await ctx.send('You have reached the maximum level for health!')
  else:
    await ctx.send('u don\'t have a city ')

  print(f'In sell(): Saving salads = {salads}')
  try: 
    with open(SALADS_FILE, 'w') as fp: 
      json.dump(salads, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {SALADS_FILE} not found! Not sure what to do here!') 

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {citypop}')
  try: 
    with open(CITYPOP_FILE, 'w') as fp: 
      json.dump(citypop, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {CITYPOP_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {meats}')
  try: 
    with open(MEAT_FILE, 'w') as fp: 
      json.dump(meats, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {MEAT_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {health_lvl}')
  try: 
    with open(HEALTH_LVL_FILE, 'w') as fp: 
      json.dump(health_lvl, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {HEALTH_LVL_FILE} not found! Not sure what to do here!') 

@upgrade.command()
async def waste(ctx):
  global meats, balances, salads, cities, citypop, waste_lvl
  user = str(ctx.message.author.id)
  waste_lvl[user] = waste_lvl[user] if user in waste_lvl else 0
  cities[user] = cities[user] if user in cities else 0
  citypop[user] = citypop[user] if user in citypop else 0
  salads[user] = salads[user] if user in salads else 0
  meats[user] = meats[user] if user in meats else 0
  balances[user] = balances[user] if user in balances else 0
  WASTE_LEVEL_USER_UPGRADING_TO = waste_lvl[user] + 1
  MEAT_COST = WASTE_LEVEL_USER_UPGRADING_TO * 320
  COINS_COST = WASTE_LEVEL_USER_UPGRADING_TO * 15600
  SALADS_COST = WASTE_LEVEL_USER_UPGRADING_TO * 22  

  if cities[user] == 1:
    if waste_lvl[user] < 5:
      await ctx.send(f'Are you sure you want to do this?\n**It will cost you** __{MEAT_COST}__ **meat**, __{COINS_COST}__ **coins, and** __{SALADS_COST}__ **salads**\n`y` or `n`')
      msg = await bot.wait_for('message', check = lambda m: m.author == ctx.author)
      if msg.content.lower() == 'y' or msg.content.lower() == 'Y':
        if salads[user] == SALADS_COST or salads[user] > SALADS_COST:
          if balances[user] == COINS_COST or balances[user] > COINS_COST:
            if meats[user] == MEAT_COST or meats[user] > MEAT_COST:
              waste_lvl[user] = WASTE_LEVEL_USER_UPGRADING_TO
              balances[user] -= COINS_COST
              salads[user] -= SALADS_COST
              meats[user] -= MEAT_COST
              citypop[user] += 3142
              await ctx.send(f'Congratulations {ctx.message.author.mention}! Your __**Waste**__ level is now **{WASTE_LEVEL_USER_UPGRADING_TO}**\nGo check in `le city`!')
              await asyncio.sleep(1)
              await ctx.send(f'Congratulations {ctx.message.author.mention}! Your __**Population**__ is now **{citypop[user]:,d}**\nGo check in `le city`!')
            else:
                await ctx.send('You don\'t have enough meat for this!')
          else:
            await ctx.send('You don\'t have enough coins for this!')
        else:
          await ctx.send('You don\'t have enough salads for this!')
      elif msg.content.lower() == 'n' or msg.content.lower() == 'N':
        msg = await ctx.send('Cancelling purchase')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Cancelling purchase.')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Cancelling purchase..')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Cancelling purchase...')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Done')
      else:
        await ctx.send('not an option ')
    else:
      await ctx.send('You have reached the maximum level for waste!')
  else:
    await ctx.send('u don\'t have a city ')

  print(f'In sell(): Saving salads = {salads}')
  try: 
    with open(SALADS_FILE, 'w') as fp: 
      json.dump(salads, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {SALADS_FILE} not found! Not sure what to do here!') 

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {citypop}')
  try: 
    with open(CITYPOP_FILE, 'w') as fp: 
      json.dump(citypop, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {CITYPOP_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {meats}')
  try: 
    with open(MEAT_FILE, 'w') as fp: 
      json.dump(meats, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {MEAT_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {waste_lvl}')
  try: 
    with open(WASTE_LVL_FILE, 'w') as fp: 
      json.dump(waste_lvl, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {WASTE_LVL_FILE} not found! Not sure what to do here!') 

@upgrade.command()
async def fire(ctx):
  global fire_lvl, wheats, balances, salads, cities, citypop
  user = str(ctx.message.author.id)
  fire_lvl[user] = fire_lvl[user] if user in fire_lvl else 0
  cities[user] = cities[user] if user in cities else 0
  citypop[user] = citypop[user] if user in citypop else 0
  salads[user] = salads[user] if user in salads else 0
  wheats[user] = wheats[user] if user in wheats else 0
  balances[user] = balances[user] if user in balances else 0
  FIRE_LEVEL_USER_UPGRADING_TO = fire_lvl[user] + 1
  WHEAT_COST = FIRE_LEVEL_USER_UPGRADING_TO * 949
  COINS_COST = FIRE_LEVEL_USER_UPGRADING_TO * 26200
  SALADS_COST = FIRE_LEVEL_USER_UPGRADING_TO * 60
  if cities[user] == 1:
    if fire_lvl[user] < 4:
      await ctx.send(f'Are you sure you want to do this?\n**It will cost you** __{WHEAT_COST}__ **wheat**, __{COINS_COST}__ **coins, and** __{SALADS_COST}__ **salads**\n`y` or `n`')
      msg = await bot.wait_for('message', check = lambda m: m.author == ctx.author)
      if msg.content.lower() == 'y' or msg.content.lower() == 'Y':
        if salads[user] == SALADS_COST or salads[user] > SALADS_COST:
          if balances[user] == COINS_COST or balances[user] > COINS_COST:
            if wheats[user] == WHEAT_COST or wheats[user] > WHEAT_COST:
              fire_lvl[user] = FIRE_LEVEL_USER_UPGRADING_TO
              balances[user] -= COINS_COST
              salads[user] -= SALADS_COST
              wheats[user] -= WHEAT_COST
              citypop[user] += 6231
              await ctx.send(f'Congratulations {ctx.message.author.mention}! Your __**Fire**__ level is now **{FIRE_LEVEL_USER_UPGRADING_TO}**\nGo check in `le city`!')
              await asyncio.sleep(1)
              await ctx.send(f'Congratulations {ctx.message.author.mention}! Your __**Population**__ is now **{citypop[user]:,d}**\nGo check in `le city`!')
            else:
                await ctx.send('You don\'t have enough wheat for this!')
          else:
            await ctx.send('You don\'t have enough coins for this!')
        else:
          await ctx.send('You don\'t have enough salads for this!')
      elif msg.content.lower() == 'n' or msg.content.lower() == 'N':
        msg = await ctx.send('Cancelling purchase')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Cancelling purchase.')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Cancelling purchase..')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Cancelling purchase...')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Done')
      else:
        await ctx.send('not an option ')
    else:
      await ctx.send('You have reached the maximum level for fire!')
  else:
    await ctx.send('u don\'t have a city ')

  print(f'In sell(): Saving salads = {salads}')
  try: 
    with open(SALADS_FILE, 'w') as fp: 
      json.dump(salads, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {SALADS_FILE} not found! Not sure what to do here!') 

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {citypop}')
  try: 
    with open(CITYPOP_FILE, 'w') as fp: 
      json.dump(citypop, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {CITYPOP_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {wheats}')
  try: 
    with open(WHEAT_FILE, 'w') as fp: 
      json.dump(wheats, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {WHEAT_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {fire_lvl}')
  try: 
    with open(FIRE_LVL_FILE, 'w') as fp: 
      json.dump(fire_lvl, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {FIRE_LVL_FILE} not found! Not sure what to do here!') 

@upgrade.command()
async def water(ctx):
  global wheats, balances, salads, water_lvl, cities, citypop
  user = str(ctx.message.author.id)
  water_lvl[user] = water_lvl[user] if user in water_lvl else 0
  cities[user] = cities[user] if user in cities else 0
  citypop[user] = citypop[user] if user in citypop else 0
  salads[user] = salads[user] if user in salads else 0
  wheats[user] = wheats[user] if user in wheats else 0
  balances[user] = balances[user] if user in balances else 0
  WATER_LEVEL_USER_UPGRADING_TO = water_lvl[user] + 1
  WHEAT_COST = WATER_LEVEL_USER_UPGRADING_TO * 260
  COINS_COST = WATER_LEVEL_USER_UPGRADING_TO * 11200
  SALADS_COST = WATER_LEVEL_USER_UPGRADING_TO * 12
  if cities[user] == 1:
    if water_lvl[user] < 8:
      await ctx.send(f'Are you sure you want to do this?\n**It will cost you** __{WHEAT_COST}__ **wheat**, __{COINS_COST}__ **coins, and** __{SALADS_COST}__ **salads**\n`y` or `n`')
      msg = await bot.wait_for('message', check = lambda m: m.author == ctx.author)
      if msg.content.lower() == 'y' or msg.content.lower() == 'Y':
        if salads[user] == SALADS_COST or salads[user] > SALADS_COST:
          if balances[user] == COINS_COST or balances[user] > COINS_COST:
            if wheats[user] == WHEAT_COST or wheats[user] > WHEAT_COST:
              water_lvl[user] = WATER_LEVEL_USER_UPGRADING_TO
              balances[user] -= COINS_COST
              salads[user] -= SALADS_COST
              wheats[user] -= WHEAT_COST
              citypop[user] += 2227
              await ctx.send(f'Congratulations {ctx.message.author.mention}! Your __**Water**__ level is now **{WATER_LEVEL_USER_UPGRADING_TO}**\nGo check in `le city`!')
              await asyncio.sleep(1)
              await ctx.send(f'Congratulations {ctx.message.author.mention}! Your __**Population**__ is now **{citypop[user]:,d}**\nGo check in `le city`!')
            else:
                await ctx.send('You don\'t have enough wheat for this!')
          else:
            await ctx.send('You don\'t have enough coins for this!')
        else:
          await ctx.send('You don\'t have enough salads for this!')
      elif msg.content.lower() == 'n' or msg.content.lower() == 'N':
        msg = await ctx.send('Cancelling purchase')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Cancelling purchase.')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Cancelling purchase..')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Cancelling purchase...')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Done')
      else:
        await ctx.send('not an option ')
    else:
      await ctx.send('You have reached the maximum level for water!')
  else:
    await ctx.send('u don\'t have a city ')

  print(f'In sell(): Saving salads = {salads}')
  try: 
    with open(SALADS_FILE, 'w') as fp: 
      json.dump(salads, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {SALADS_FILE} not found! Not sure what to do here!') 

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {citypop}')
  try: 
    with open(CITYPOP_FILE, 'w') as fp: 
      json.dump(citypop, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {CITYPOP_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {wheats}')
  try: 
    with open(WHEAT_FILE, 'w') as fp: 
      json.dump(wheats, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {WHEAT_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {water_lvl}')
  try: 
    with open(WATER_LVL_FILE, 'w') as fp: 
      json.dump(water_lvl, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {WATER_LVL_FILE} not found! Not sure what to do here!') 

@upgrade.command()
async def power(ctx):
  global meats, balances, power_lvl, cities, citypop, salads
  user = str(ctx.message.author.id)
  power_lvl[user] = power_lvl[user] if user in power_lvl else 0
  cities[user] = cities[user] if user in cities else 0
  citypop[user] = citypop[user] if user in citypop else 0
  salads[user] = salads[user] if user in salads else 0
  meats[user] = meats[user] if user in meats else 0
  balances[user] = balances[user] if user in balances else 0
  LEVEL_USER_IS_UPGRADING_TO = power_lvl[user] + 1
  COST_FOR_MEAT = LEVEL_USER_IS_UPGRADING_TO * 150
  COST_FOR_BALANCES = LEVEL_USER_IS_UPGRADING_TO * 10400
  COST_FOR_SALADS = LEVEL_USER_IS_UPGRADING_TO * 20
  if cities[user] == 1:
    if power_lvl[user] < 5:
      await ctx.send(f'Are you sure you want to do this?\n**It will cost you** __{COST_FOR_MEAT}__ **meat,** __{COST_FOR_BALANCES}__ **coins, and** __{COST_FOR_SALADS}__ **salads**\n`y` or `n`')
      msg = await bot.wait_for('message', check = lambda m: m.author == ctx.author)
      if msg.content.lower() == 'y' or msg.content.lower() == 'Y':
        if salads[user] == COST_FOR_SALADS or salads[user] > COST_FOR_SALADS:
          if balances[user] == COST_FOR_BALANCES or balances[user] > COST_FOR_BALANCES:
            if meats[user] == COST_FOR_MEAT or balances[user] > COST_FOR_MEAT:
              power_lvl[user] = LEVEL_USER_IS_UPGRADING_TO
              balances[user] -= COST_FOR_BALANCES
              meats[user] -= COST_FOR_MEAT
              salads[user] -= COST_FOR_SALADS
              citypop[user] += 2467
              await ctx.send(f'Congratulations {ctx.message.author.mention}! Your __**Power**__ level is now **{LEVEL_USER_IS_UPGRADING_TO}**\nGo check in `le city`!')
              await asyncio.sleep(1)
              await ctx.send(f'Congratulations {ctx.message.author.mention}! Your __**Population**__ is now **{citypop[user]:,d}**\nGo check in `le city`!')
            else:
              await ctx.send('You don\'t have enough meat for this!')
          else:
            await ctx.send('You don\'t have enough coins for this!')
        else:
          await ctx.send('You don\'t have enough salads for this!')
      elif msg.content.lower() == 'n' or msg.content.lower() == 'N':
        msg = await ctx.send('Cancelling purchase')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Cancelling purchase.')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Cancelling purchase..')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Cancelling purchase...')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Done')
      else:
        await ctx.send('not an option ')
    else:
      await ctx.send('You have reached the maximum level for power!')
  else:
    await ctx.send('u don\'t have a city ')

  print(f'In sell(): Saving salads = {salads}')
  try: 
    with open(SALADS_FILE, 'w') as fp: 
      json.dump(salads, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {SALADS_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {meats}')
  try: 
    with open(MEAT_FILE, 'w') as fp: 
      json.dump(meats, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {MEAT_FILE} not found! Not sure what to do here!') 

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {citypop}')
  try: 
    with open(CITYPOP_FILE, 'w') as fp: 
      json.dump(citypop, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {CITYPOP_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {power_lvl}')
  try: 
    with open(POWER_LVL_FILE, 'w') as fp: 
      json.dump(power_lvl, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {POWER_LVL_FILE} not found! Not sure what to do here!') 





@upgrade.command()
async def entertainment(ctx):
  global meats, balances, rices, salads, citypop, entertainment_lvl, cities
  user = str(ctx.message.author.id)
  entertainment_lvl[user] = entertainment_lvl[user] if user in entertainment_lvl else 0
  cities[user] = cities[user] if user in cities else 0
  citypop[user] = citypop[user] if user in citypop else 0
  salads[user] = salads[user] if user in salads else 0
  meats[user] = meats[user] if user in meats else 0
  rices[user] = rices[user] if user in rices else 0
  balances[user] = balances[user] if user in balances else 0
  LEVEL_USER_IS_UPGRADING_TO = entertainment_lvl[user] + 1
  COST_FOR_LUIUT_MEAT = LEVEL_USER_IS_UPGRADING_TO * 100
  COST_FOR_LUIUT_COINS = LEVEL_USER_IS_UPGRADING_TO * 12000
  COST_FOR_LUIUT_RICE = LEVEL_USER_IS_UPGRADING_TO * 10
  COST_FOR_LUIUT_SALADS = LEVEL_USER_IS_UPGRADING_TO * 2
  if cities[user] == 1:
    if entertainment_lvl[user] < 7:
      await ctx.send(f'Are you sure you want to do this?\n**It will cost you** __{COST_FOR_LUIUT_MEAT}__ **meat,** __{COST_FOR_LUIUT_COINS}__ **coins,** __{COST_FOR_LUIUT_RICE}__ **rice, and** __{COST_FOR_LUIUT_SALADS}__ **salads**\n`y` or `n`')
      msg = await bot.wait_for('message', check = lambda m: m.author == ctx.author)
      if msg.content.lower() == 'y' or msg.content.lower() == 'Y':
        if salads[user] == COST_FOR_LUIUT_SALADS or salads[user] > COST_FOR_LUIUT_SALADS:
          if balances[user] == COST_FOR_LUIUT_COINS or balances[user] > COST_FOR_LUIUT_COINS:
            if meats[user] == COST_FOR_LUIUT_MEAT or meats[user] > COST_FOR_LUIUT_MEAT:
              if rices[user] == COST_FOR_LUIUT_RICE or rices[user] > COST_FOR_LUIUT_RICE:
                entertainment_lvl[user] = LEVEL_USER_IS_UPGRADING_TO
                balances[user] -= COST_FOR_LUIUT_COINS
                meats[user] -= COST_FOR_LUIUT_MEAT
                rices[user] -= COST_FOR_LUIUT_RICE
                salads[user] -= COST_FOR_LUIUT_SALADS
                citypop[user] += 867
                await ctx.send(f'Congratulations {ctx.message.author.mention}! Your __**Entertainment**__ level is now **{LEVEL_USER_IS_UPGRADING_TO}**\nGo check in `le city`!')
                await asyncio.sleep(1)
                await ctx.send(f'Congratulations {ctx.message.author.mention}! Your __**Population**__ is now **{citypop[user]:,d}**\nGo check in `le city`!')
              else:
                await ctx.send('You don\'t have enough rice for this!')
            else:
              await ctx.send('You don\'t have enough meat for this!')
          else:
            await ctx.send('You don\'t have enough coins for this!')
        else:
          await ctx.send('You don\'t have enough salads for this!')
      elif msg.content.lower() == 'n' or msg.content.lower() == 'N':
        msg = await ctx.send('Cancelling purchase')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Cancelling purchase.')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Cancelling purchase..')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Cancelling purchase...')
        await asyncio.sleep(0.7)
        await msg.edit(content = 'Done')
      else:
        await ctx.send('not an option ')
    else:
      await ctx.send('You have reached the maximum level for entertainment!')
  else:
    await ctx.send('u don\'t have a city ')

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 

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

  print(f'In sell(): Saving meats = {meats}')
  try: 
    with open(MEAT_FILE, 'w') as fp: 
      json.dump(meats, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {MEAT_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {entertainment_lvl}')
  try: 
    with open(ENTERTAINMENT_LVL_FILE, 'w') as fp: 
      json.dump(entertainment_lvl, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {ENTERTAINMENT_LVL_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {citypop}')
  try: 
    with open(CITYPOP_FILE, 'w') as fp: 
      json.dump(citypop, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {CITYPOP_FILE} not found! Not sure what to do here!') 





@bot.command()
async def requirements(ctx, *, message: str):
  if message == 'medium city' or message == 'Medium city' or message == 'medium City' or message == 'Medium City':
    await ctx.send('__**Requirements for Medium City**__\n\t- LVL 3 Entertainment\n\t- LVL 5 Parks\n\t- LVL 2 Health\n\t- LVL 2 Fire\n\t- LVL 2 Police\n\t- LVL 3 Waste\n\t- LVL 5 Water\n\t- LVL 4 Power\nbtw you have to have all at the requirements or between medium and advanced')
  elif message == 'advanced city' or message == 'Advanced city' or message == 'advanced City' or message == 'Advanced City':
    await ctx.send('__**Requirements for Advanced City**__\n\t- LVL 7 Entertainment\n\t- LVL 6 Parks\n\t- LVL 4 Health\n\t- LVL 4 Fire\n\t- LVL 4 Police\n\t- LVL 5 Waste\n\t- LVL 8 Water\n\t- LVL 5 Power\nbtw you have to have all at the requirements or between medium and advanced')
  else:
    await ctx.send('not an option ')





@bot.group(invoke_without_command = True, pass_context = True)
async def collect(ctx):
  await ctx.send('Proper Usage: `le collect [section]`')

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
          embed = discord.Embed(title = 'Collection Complete', description = f'You gained `{HEALTH_REVENUE:,d} coins` of **Health Revenue** from your population and 1 :water_buffalo: **Buffalo** HOW TF', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += HEALTH_REVENUE
        else:
          health_popz_added = health_lvl[user] * 7819
          HEALTH_REVENUE = health_popz_added * 120
          embed = discord.Embed(title = 'Collection Complete', description = f'You gained `{HEALTH_REVENUE:,d} coins` of **Health Revenue** from your population!', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += HEALTH_REVENUE
      else:
        await ctx.send('You don\'t have any population lmao')
    else:
      await ctx.send('You don\'t have any health levels!')
  else:
    await ctx.send(' u dont even have a city')

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
          embed = discord.Embed(title = 'Collection Complete', description = f'You gained `{WASTE_REVENUE:,d} coins` of **Waste Revenue** from your population and 1 :water_buffalo: **Buffalo** HOW TF', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += WASTE_REVENUE
        else:
          waste_popz_added = waste_lvl[user] * 3142
          WASTE_REVENUE = waste_popz_added * 80
          embed = discord.Embed(title = 'Collection Complete', description = f'You gained `{WASTE_REVENUE:,d} coins` of **Waste Revenue** from your population!', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += WASTE_REVENUE
      else:
        await ctx.send('You don\'t have any population lmao')
    else:
      await ctx.send('You don\'t have any waste levels!')
  else:
    await ctx.send(' u dont even have a city')

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
          embed = discord.Embed(title = 'Collection Complete', description = f'You gained `{WATER_REVENUE:,d} coins` of **Water Revenue** from your population and 1 :water_buffalo: **Buffalo** HOW TF', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += WATER_REVENUE
        else:
          water_popz_added = water_lvl[user] * 2227
          WATER_REVENUE = water_popz_added * 60
          embed = discord.Embed(title = 'Collection Complete', description = f'You gained `{WATER_REVENUE:,d} coins` of **Water Revenue** from your population!', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += WATER_REVENUE
      else:
        await ctx.send('You don\'t have any population lmao')
    else:
      await ctx.send('You don\'t have any water levels!')
  else:
    await ctx.send(' u dont even have a city')

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
          embed = discord.Embed(title = 'Collection Complete', description = f'You gained `{FIRE_REVENUE:,d} coins` of **Fire Revenue** from your population and 1 :water_buffalo: **Buffalo** HOW TF', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += FIRE_REVENUE
        else:
          fire_popz_added = fire_lvl[user] * 6231
          FIRE_REVENUE = fire_popz_added * 60
          embed = discord.Embed(title = 'Collection Complete', description = f'You gained `{FIRE_REVENUE:,d} coins` of **Fire Revenue** from your population!', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += FIRE_REVENUE
      else:
        await ctx.send('You don\'t have any population lmao')
    else:
      await ctx.send('You don\'t have any fire levels!')
  else:
    await ctx.send(' u dont even have a city')

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
          embed = discord.Embed(title = 'Collection Complete', description = f'You gained `{POLICE_REVENUE:,d} coins` of **Police Revenue** from your population and 1 :water_buffalo: **Buffalo** HOW TF', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += POLICE_REVENUE
        else:
          police_popz_added = police_lvl[user] * 9331
          POLICE_REVENUE = police_popz_added * 130
          embed = discord.Embed(title = 'Collection Complete', description = f'You gained `{POLICE_REVENUE:,d} coins` of **Police Revenue** from your population!', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += POLICE_REVENUE
      else:
        await ctx.send('You don\'t have any population lmao')
    else:
      await ctx.send('You don\'t have any police levels!')
  else:
    await ctx.send(' u dont even have a city')

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
          embed = discord.Embed(title = 'Collection Complete', description = f'You gained `{ENTERTAINMENT_REVENUE:,d} coins` of **Entertainment Revenue** from your population and 1 :water_buffalo: **Buffalo** HOW TF', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += ENTERTAINMENT_REVENUE
        else:
          ent_popz_added = entertainment_lvl[user] * 867
          ENTERTAINMENT_REVENUE = ent_popz_added * 35
          embed = discord.Embed(title = 'Collection Complete', description = f'You gained `{ENTERTAINMENT_REVENUE:,d} coins` of **Entertainment Revenue** from your population!', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += ENTERTAINMENT_REVENUE
      else:
        await ctx.send('You don\'t have any population lmao')
    else:
      await ctx.send('You don\'t have any entertainment levels!')
  else:
    await ctx.send(' u dont even have a city')

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
          embed = discord.Embed(title = 'Collection Complete', description = f'You gained `{PARK_REVENUE:,d} coins` of **Park Revenue** from your population and 1 :water_buffalo: **Buffalo** HOW TF', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += PARK_REVENUE
        else:
          park_popz_added = park_lvl[user] * 1001
          PARK_REVENUE = park_popz_added * 50
          embed = discord.Embed(title = 'Collection Complete', description = f'You gained `{PARK_REVENUE:,d} coins` of **Park Revenue** from your population!', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += PARK_REVENUE
      else:
        await ctx.send('You don\'t have any population lmao')
    else:
      await ctx.send('You don\'t have any park levels!')
  else:
    await ctx.send(' u dont even have a city')

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
          embed = discord.Embed(title = 'Collection Complete', description = f'You gained `{POWER_REVENUE:,d} coins` of **Power Revenue** from your population and 1 :water_buffalo: **Buffalo** HOW TF', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += POWER_REVENUE
        else:
          power_popz_added = power_lvl[user] * 2467
          POWER_REVENUE = power_popz_added * 75
          embed = discord.Embed(title = 'Collection Complete', description = f'You gained `{POWER_REVENUE:,d} coins` of **Power Revenue** from your population', color = random.choice(random_colors))
          await ctx.send(embed = embed)
          balances[user] += POWER_REVENUE
      else:
        await ctx.send('You don\'t have any population lmao')
    else:
      await ctx.send('You don\'t have any power levels!')
  else:
    await ctx.send(' u dont even have a city')

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




@bot.command()
async def create(ctx):
  global locations, cities, citypop, balances
  user = str(ctx.message.author.id)
  cities[user] = cities[user] if user in cities else 0
  locations[user] = locations[user] if user in locations else 0
  citypop[user] = citypop[user] if user in citypop else 0
  balances[user] = balances[user] if user in balances else 0

  if locations[user] == 1:
    if cities[user] == 0:
      await ctx.send('This will cost you `350000` coins. And it will cost a lot to maintain it.\nYou up for it? `y` or `n`')
      msg = await bot.wait_for('message', check = lambda m: m.author == ctx.author)
      if msg.content.lower() == 'y' or msg.content.lower() == 'Y':
        if balances[user] > 350000 or balances[user] == 350000:
          await ctx.send(f'Congratulations {ctx.message.author.mention}! You started off with a **basic city**')
          balances[user] -= 350000
          cities[user] += 1
          citypop[user] = 0
        else:
          await ctx.send(' get more money')
      elif msg.content.lower() == 'n' or msg.content.lower() == 'N':
        await ctx.send('alri no city for u')
      else:
        await ctx.send('not an option ')
    else:
      await ctx.send('don\'t you already have a city my guy?')
  else:
    await ctx.send('You must be in Texas to create a city!')

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(CITYPOP_FILE, 'w') as fp: 
      json.dump(citypop, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {CITYPOP_FILE} not found! Not sure what to do here!') 

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(CITIES_FILE, 'w') as fp: 
      json.dump(cities, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {CITIES_FILE} not found! Not sure what to do here!') 





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
async def farm(ctx):
  global sheeps, wools, rices, wheats, pigs, meats, ambulances, buffalos, stoves, uncooked_chickens, cooked_chickens, salads, morris, douglas, locations, pc, bread, mooshroom_cows, bowls, mushroom_stew, commands2
  user = str(ctx.message.author.id)
  locations[user] = locations[user] if user in locations else 0
  morris[user] = morris[user] if user in morris else 0
  douglas[user] = douglas[user] if user in douglas else 0
  salads[user] = salads[user] if user in salads else 0
  cooked_chickens[user] = cooked_chickens[user] if user in cooked_chickens else 0
  uncooked_chickens[user] = uncooked_chickens[user] if user in uncooked_chickens else 0
  stoves[user] = stoves[user] if user in stoves else 0
  sheeps[user] = sheeps[user] if user in sheeps else 0
  buffalos[user] = buffalos[user] if user in buffalos else 0
  wools[user] = wools[user] if user in wools else 0
  rices[user] = rices[user] if user in rices else 0
  wheats[user] = wheats[user] if user in wheats else 0
  pigs[user] = pigs[user] if user in pigs else 0
  meats[user] = meats[user] if user in meats else 0
  ambulances[user] = ambulances[user] if user in ambulances else 0
  pc[user] = pc[user] if user in pc else 0
  bread[user] = bread[user] if user in bread else 0
  mooshroom_cows[user] = mooshroom_cows[user] if user in mooshroom_cows else 0
  bowls[user] = bowls[user] if user in bowls else 0
  mushroom_stew[user] = mushroom_stew[user] if user in mushroom_stew else 0
  commands2[user] = commands2[user] if user in commands2 else 0

  if locations[user] == 0:
    embed = discord.Embed(title = f"{ctx.message.author.name}'s California Farm", description = "`le <crop/animal>` to harvest the animals or crops\n `le shop` for more", color = random.choice(random_colors))
    embed.add_field(name = "Animals [NOT SELLABLE]\n", value = f":sheep: Sheep | {sheeps[user]}\n :pig2: Pigs | {pigs[user]}\n :water_buffalo: Buffalos | {buffalos[user]}\n :hatched_chick: Uncooked Chickens | {uncooked_chickens[user]}\n <:mooshroom:716492779391418440> Mooshroom Cows | {mooshroom_cows[user]}\n", inline = True)
    embed.add_field(name = "\nCrops [NOT SELLABLE]\n", value = f":rice: Rice | {rices[user]}\n", inline = False)
    embed.add_field(name = "\nGoods [SELLABLE]\n", value = f":scroll:  Wool | {wools[user]}\n :tanabata_tree: Wheat | {wheats[user]}\n :cut_of_meat: Meat | {meats[user]}\n :chicken: Chickens | {cooked_chickens[user]}\n", inline = False)
    embed.add_field(name = "\nMeds [NOT SELLABLE]\n", value = f":ambulance: Ambulances | {ambulances[user]}\n:french_bread: Bread | {bread[user]}", inline = False)
    embed.add_field(name = "\nMaterials [NOT SELLABLE]\n", value = f':cooking: Stoves | {stoves[user]}\n :desktop: PC | {pc[user]}', inline = False)
    embed.add_field(name = "\nDishes [NOT SELLABLE]\n", value = f':salad: Salads | {salads[user]}\n <:mushstew:716492699879997530> Mushroom Stew | {mushroom_stew[user]}', inline = False)
    embed.add_field(name = "\nJets [NOT SELLABLE]\n", value = f':airplane_small: Morris | {morris[user]}\n:airplane: Douglas | {douglas[user]}', inline = False)
    embed.add_field(name = "\nLocation [MISCELLANEOUS]", value = f':man_running: Location | California', inline = False)
    embed.add_field(name = '\nItems [MISCELLANEOUS]', value = f'<:bowl:716492750996111441> Bowl | {bowls[user]}', inline = False)
    await ctx.send(embed=embed)
  else:
    embed = discord.Embed(title = f"{ctx.message.author.name}'s California Farm", description = "`le <crop/animal>` to harvest the animals or crops\n `le shop` for more", color = random.choice(random_colors))
    embed.add_field(name = "Animals [NOT SELLABLE]\n", value = f":sheep: Sheep | {sheeps[user]}\n :pig2: Pigs | {pigs[user]}\n :water_buffalo: Buffalos | {buffalos[user]}\n :hatched_chick: Uncooked Chickens | {uncooked_chickens[user]}\n <:mooshroom:716492779391418440> Mooshroom Cows | {mooshroom_cows[user]}\n", inline = True)
    embed.add_field(name = "\nCrops [NOT SELLABLE]\n", value = f":rice: Rice | {rices[user]}\n", inline = False)
    embed.add_field(name = "\nGoods [SELLABLE]\n", value = f":scroll:  Wool | {wools[user]}\n :tanabata_tree: Wheat | {wheats[user]}\n :cut_of_meat: Meat | {meats[user]}\n :chicken: Chickens | {cooked_chickens[user]}\n", inline = False)
    embed.add_field(name = "\nMeds [NOT SELLABLE]\n", value = f":ambulance: Ambulances | {ambulances[user]}\n:french_bread: Bread | {bread[user]}", inline = False)
    embed.add_field(name = "\nMaterials [NOT SELLABLE]\n", value = f':cooking: Stoves | {stoves[user]}\n :desktop: PC | {pc[user]}', inline = False)
    embed.add_field(name = "\nDishes [NOT SELLABLE]\n", value = f':salad: Salads | {salads[user]}\n <:mushstew:716492699879997530> Mushroom Stew | {mushroom_stew[user]}', inline = False)
    embed.add_field(name = "\nJets [NOT SELLABLE]\n", value = f':airplane_small: Morris | {morris[user]}\n:airplane: Douglas | {douglas[user]}', inline = False)
    embed.add_field(name = "\nLocation [MISCELLANEOUS]", value = f':man_running: Location | Texas', inline = False)
    embed.add_field(name = '\nItems [MISCELLANEOUS]', value = f'<:bowl:716492750996111441> Bowl | {bowls[user]}', inline = False)
    await ctx.send(embed=embed)


@bot.command()
async def profile(ctx, member: discord.Member):
  global commands2, levels, exp
  user = str(member.id)
  commands2[user] = commands2[user] if user in commands2 else 0
  exp[user] = exp[user] if user in exp else 0
  levels[user] = levels[user] if user in levels else 0
  
  if levels[user] in range(0, 6):
    embed = discord.Embed(title = f'{member.name}\'s Profile', color = random.choice(random_colors))
    embed.add_field(name = '\nRandom', value = f'<:pepe_cry:712063226292076564> Commands invoked: {commands2[user]}', inline = True)
    embed.add_field(name = '\nLow Sped', value = f'Level: **{levels[user]}** Exp: **{exp[user]}**', inline = False)
    await ctx.send(embed = embed)
  elif levels[user] in range(6, 16):
    embed = discord.Embed(title = f'{member.name}\'s Profile', color = random.choice(random_colors))
    embed.add_field(name = '\nRandom', value = f'<:pepe_cry:712063226292076564> Commands invoked: {commands2[user]}', inline = True)
    embed.add_field(name = '\nSped', value = f'Level: **{levels[user]}** Exp: **{exp[user]}**', inline = False)
    await ctx.send(embed = embed)
  elif levels[user] in range(16, 26):
    embed = discord.Embed(title = f'{member.name}\'s Profile', color = random.choice(random_colors))
    embed.add_field(name = '\nRandom', value = f'<:pepe_cry:712063226292076564> Commands invoked: {commands2[user]}', inline = True)
    embed.add_field(name = '\nMediocre Sped', value = f'Level: **{levels[user]}** Exp: **{exp[user]}**', inline = False)
    await ctx.send(embed = embed)
  elif levels[user] in range(26, 101):
    embed = discord.Embed(title = f'{member.name}\'s Profile', color = random.choice(random_colors))
    embed.add_field(name = '\nRandom', value = f'<:pepe_cry:712063226292076564> Commands invoked: {commands2[user]}', inline = True)
    embed.add_field(name = '\nUltimate Sped', value = f'Level: **{levels[user]}** Exp: **{exp[user]}**', inline = False)
    await ctx.send(embed = embed)
  else:
    embed = discord.Embed(title = f'{member.name}\'s Profile', color = random.choice(random_colors))
    embed.add_field(name = '\nRandom', value = f'<:pepe_cry:712063226292076564> Commands invoked: {commands2[user]}', inline = True)
    embed.add_field(name = '\nUltimate Sped', value = f'Level: **{levels[user]}** Exp: **{exp[user]}**', inline = False)
    await ctx.send(embed = embed)


@bot.command()
@commands.cooldown(1, 600, commands.BucketType.user)
async def grab(ctx):
  global balances
  AIRDROP_LOOT = random.randint(500,1200)
  user = str(ctx.message.author.id)
  if user in balances:
    embed = discord.Embed(description = f'{ctx.message.author} just grabbed an airdrop for ¢{AIRDROP_LOOT}', color = random.choice(random_colors))
    balances[user] += AIRDROP_LOOT
    await ctx.send(embed=embed)
  else:
    print(f'In buy(): No record for {user} found. Creating a new record with a starting balance of {START_BAL}') 
    balances[user] = START_BAL 
    await ctx.send(f'hey you don\'t have a bank account yet. I just created one for you and started you off with le {START_BAL}') 





@bot.command()
async def give(ctx, amount: int, member: discord.Member):
  global balances

  primary_id = str(ctx.message.author.id)
  other_id = str(member.id)
  if primary_id not in balances:
    await ctx.send("You do not have a bank account. To get one, type in `le plead` or `le plead`")
  elif other_id not in balances:
    await ctx.send("The other party does not have an account")
  elif balances[primary_id] < amount:
    await ctx.send("You cannot afford this transaction")
  elif member is ctx.message.author:
    await ctx.send('r u rlly going to try to give urself coins')
  else:
    balances[primary_id] -= amount
    balances[other_id] += amount
    await ctx.send(f"You gave {member.name} {amount:,d} coins now they have {balances[other_id]:,d} and you have {balances[primary_id]:,d}")
    await member.send(f'{ctx.message.author.name} gave you {amount:,d} coins!')

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 





@bot.command()
@commands.cooldown(1, 3600, commands.BucketType.user)
async def work(ctx):
  user = str(ctx.message.author.id)
  global balances
  balances[user] = balances[user] if user in balances else 0

  random_work_shet = ['chop 10 wood', 'deliver chicken leg :b:is\nthe :b: counts btw', 'repost 4 memes', 'assassinate trump', 'rate tiktok 1 star on the app store', 'cook 12 meals']
  answer = random.choice(random_work_shet)
  msg2 = await ctx.send(f'{ctx.message.author.mention}, do the work by typing it!\n**{answer}**')
  await msg2.edit()
  msg = await bot.wait_for('message', check = lambda m: m.author == ctx.author)
  if msg.content.lower() == answer:
    random_coins = random.randint(3000, 5000)
    balances[user] += random_coins
    await ctx.send(f'**Nice job {ctx.message.author.name}!** You earned **{random_coins}** coins from that hour of work')
  else:
    random_coins2 = random.randint(500, 1500)
    await ctx.send(f'**Not good {ctx.message.author.name}!** You only earned **{random_coins2}** coins from that hour of work')
    balances[user] += random_coins2

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 





@bot.command()
async def notebook(ctx):
  embed = discord.Embed(title = "Grandma Esther's notebook", description = "only boomers keep recipes in a notebook", color = random.choice(random_colors))
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
          embed = discord.Embed(title = 'Combine Complete', description = f'You got **20** salads for `5 cooked chicken` and `9 rice`', color = random.choice(random_colors))
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
  embed = discord.Embed(title = "Crypto's underground pharmacy", description = "`buy <item> <amount>` or `sell <item> <amount>`\n No selling `ambulance` because it is too rare.", color = random.choice(random_colors))
  embed.add_field(name = ":medical_symbol: Meds", value = ":ambulance: Ambulance | Price: :cut_of_meat: __15200__ | Puts your health back to 100\n:french_bread: Bread | Price: __1200__ coins | Puts health exactly at 60")
  await ctx.send(embed = embed)





@bot.command()
@commands.cooldown(1, 1800, commands.BucketType.user)
async def rice(ctx):
  global rices, wheats, healths
  user = str(ctx.message.author.id)
  healths[user] = healths[user] if user in healths else 100
  if healths[user] > 5 or healths[user] == 5:
    if user in rices:
      wheats[user] = wheats[user] if user in wheats else 0
      wheat = rices[user] * 4
      wheats[user] += wheat
      healths[user] -= 5  
      embed = discord.Embed(title = f'{ctx.message.author}\'s harvest ', description = f"{ctx.message.author} just recieved :tanabata_tree: {wheat} wheat from his :rice: rice", color = random.choice(random_colors))
      await ctx.send(embed = embed)   
    else:
      await ctx.send('You don\'t have any rice')
  else:
    await ctx.send('You don\'t have enough health for this action!')

  print(f'In sell(): Saving rices = {rices}')
  try: 
    with open(RICE_FILE, 'w') as fp: 
      json.dump(rices, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {RICE_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving wheat = {wheats}')
  try: 
    with open(WHEAT_FILE, 'w') as fp: 
      json.dump(wheats, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {WHEAT_FILE} not found! Not sure what to do here!') 

  print(f'In pigs(): Saving healths = {healths}')
  try: 
    with open(HEALTH_FILE, 'w') as fp: 
      json.dump(healths, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {HEALTH_FILE} not found! Not sure what to do here!') 





@bot.command()
@commands.cooldown(1, 1800, commands.BucketType.user)
async def sheep(ctx):
  global sheeps, wools, healths
  user = str(ctx.message.author.id)
  healths[user] = healths[user] if user in healths else 100
  if healths[user] > 5 or healths[user] == 5:
    if user in sheeps:
      wools[user] = wools[user] if user in wools else 0
      wool = sheeps[user] * 3
      wools[user] += wool
      healths[user] -= 5
      embed = discord.Embed(title = f'{ctx.message.author}\'s harvest', description = f"{ctx.message.author} just recieved :scroll: {wool} wool from his :sheep: sheep", color = random.choice(random_colors))
      await ctx.send(embed = embed)   
    else:
      await ctx.send('You don\'t have any sheep')
  else:
    await ctx.send('You don\'t have enough health for this action!')


  print(f'In sell(): Saving sheep = {sheeps}')
  try: 
    with open(SHEEPS_FILE, 'w') as fp: 
      json.dump(sheeps, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {SHEEPS_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving wool = {wools}')
  try: 
    with open(WOOL_FILE, 'w') as fp: 
      json.dump(wools, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {WOOL_FILE} not found! Not sure what to do here!') 

  print(f'In pigs(): Saving healths = {healths}')
  try: 
    with open(HEALTH_FILE, 'w') as fp: 
      json.dump(healths, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {HEALTH_FILE} not found! Not sure what to do here!') 





@bot.command()
@commands.cooldown(1, 1800, commands.BucketType.user)
async def buffalo(ctx):
  global buffalos, meats, wheats, healths
  user = str(ctx.message.author.id)
  healths[user] = healths[user] if user in healths else 100
  if healths[user] > 20 or healths[user] == 20:
    if user in buffalos:
      wheats[user] = wheats[user] if user in wheats else 0
      meats[user] = meats[user] if user in meats else 0
      wheat2 = buffalos[user] * 10000
      wheats[user] += wheat2
      meat2 = buffalos[user] * 10000
      meats[user] += meat2
      healths[user] -= 20
      embed = discord.Embed(title = f'{ctx.message.author}\'s harvest ', description = f"{ctx.message.author} just recieved :cut_of_meat: {meat2} meat and :ear_of_rice: {wheat2} wheat from his :water_buffalo: Buffalos", color = random.choice(random_colors))
      await ctx.send(embed = embed)   
    else:
      await ctx.send('You don\'t have any buffalos!')
  else:
    await ctx.send('You don\'t have enough health for this action!')

  print(f'In sell(): Saving buffalos = {buffalos}')
  try: 
    with open(BUFFALOS_FILE, 'w') as fp: 
      json.dump(buffalos, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {BUFFALOS_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving wheats = {wheats}')
  try: 
    with open(WHEAT_FILE, 'w') as fp: 
      json.dump(wheats, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {WHEAT_FILE} not found! Not sure what to do here!') 
  
  print(f'In sell(): Saving meats = {meats}')
  try: 
    with open(MEAT_FILE, 'w') as fp: 
      json.dump(meats, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {MEAT_FILE} not found! Not sure what to do here!') 

  print(f'In pigs(): Saving healths = {healths}')
  try: 
    with open(HEALTH_FILE, 'w') as fp: 
      json.dump(healths, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {HEALTH_FILE} not found! Not sure what to do here!') 





@bot.command()
@commands.cooldown(1, 1800, commands.BucketType.user)
async def cook(ctx, arg):
  global uncooked_chickens, cooked_chickens, stoves, healths
  user = str(ctx.message.author.id)
  healths[user] = healths[user] if user in healths else 100
  stoves[user] = stoves[user] if user in stoves else 0
  cooked_chickens[user] = cooked_chickens[user] if user in cooked_chickens else 0
  uncooked_chickens[user] = uncooked_chickens[user] if user in uncooked_chickens else 0 
  if arg == "chicken" or arg == "chickens":
    if healths[user] > 10 or healths[user] == 10:
      if stoves[user] > 0:
        if user in uncooked_chickens:
          chicken = uncooked_chickens[user] * 3
          cooked_chickens[user] += chicken
          healths[user] -= 10
          stoves[user] -= 1
          embed = discord.Embed(title = f'{ctx.message.author}\'s harvest ', description = f"{ctx.message.author} just recieved :chicken: {chicken} chickens from his :hatched_chick: Uncooked Chickens!", color = random.choice(random_colors))
          await ctx.send(embed = embed)   
        else:
          await ctx.send('You don\'t have any uncooked chickens!')  
      else:
        await ctx.send('You don\'t have any stoves!')
    else:
      await ctx.send('You don\'t have enough health for this action!')
  else:
    await ctx.send('Specify what to cook!')

  print(f'In pigs(): Saving healths = {healths}')
  try: 
    with open(HEALTH_FILE, 'w') as fp: 
      json.dump(healths, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {HEALTH_FILE} not found! Not sure what to do here!') 

  print(f'In pigs(): Saving stoves = {stoves}')
  try: 
    with open(STOVES_FILE, 'w') as fp: 
      json.dump(stoves, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {STOVES_FILE} not found! Not sure what to do here!') 

  print(f'In pigs(): Saving uncooked chickens = {uncooked_chickens}')
  try: 
    with open(UNCOOKED_CHICKENS_FILE, 'w') as fp: 
      json.dump(uncooked_chickens, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {UNCOOKED_CHICKENS_FILE} not found! Not sure what to do here!') 

  print(f'In pigs(): Saving cooked chickens = {cooked_chickens}')
  try: 
    with open(COOKED_CHICKENS_FILE, 'w') as fp: 
      json.dump(cooked_chickens, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {COOKED_CHICKENS_FILE} not found! Not sure what to do here!') 





@bot.command()
@commands.cooldown(1, 1800, commands.BucketType.user)
async def pig(ctx):
  global pigs, meats, healths
  user = str(ctx.message.author.id)
  healths[user] = healths[user] if user in healths else 100
  if healths[user] > 5 or healths[user] == 5:
    if user in pigs:
      meats[user] = meats[user] if user in meats else 0
      meat = pigs[user] * 6
      meats[user] += meat
      healths[user] -= 5
      embed = discord.Embed(title = f'{ctx.message.author}\'s harvest ', description = f"{ctx.message.author} just recieved :cut_of_meat: {meat} meat from his :pig2: pig(s)", color = random.choice(random_colors))
      await ctx.send(embed = embed)   
    else:
      await ctx.send('You don\'t have any pigs')
  else:
    await ctx.send('You don\'t have enought health for this!')

  print(f'In sell(): Saving pigs = {pigs}')
  try: 
    with open(PIG_FILE, 'w') as fp: 
      json.dump(pigs, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {PIG_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {meats}')
  try: 
    with open(MEAT_FILE, 'w') as fp: 
      json.dump(meats, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {MEAT_FILE} not found! Not sure what to do here!') 

  print(f'In pigs(): Saving healths = {healths}')
  try: 
    with open(HEALTH_FILE, 'w') as fp: 
      json.dump(healths, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {HEALTH_FILE} not found! Not sure what to do here!') 





@bot.command()
async def sell(ctx, arg, amount: int):
  global balances, START_BAL, meats, wools, wheats
  user = str(ctx.message.author.id)
  if arg == "wheats" or arg == "wheat":
    if user in wheats:
      if user in balances:
        if wheats[user] > amount or wheats[user] == amount:
          balances[user] = balances[user] if user in balances else 0
          wheats[user] = wheats[user] if user in wheats else 0
          crypto_for_selling_wheat = amount * 10
          wheats[user] -= amount
          balances[user] += crypto_for_selling_wheat
          embed = discord.Embed(title = 'Sale Complete', description = f'You gained `{crypto_for_selling_wheat} coins` for selling **{amount}** wheat', color = random.choice(random_colors))
          await ctx.send(embed = embed)
        else:
          await ctx.send('um i don\'t think you have enough wheat for that **SCAMMER**')
      else:
        print(f'In buy(): No record for {user} found. Creating a new record with a starting balance of {START_BAL}') 
        balances[user] = START_BAL 
        await ctx.send(f'hey you don\'t have a bank account yet. I just created one for you and started you off with le {START_BAL}') 
    else:
      await ctx.send('you don\'t have any wheat with you')
  elif arg == "wool" or arg == "wools":
    if user in wools:
      if user in balances:
        if wools[user] > amount or wools[user] == amount:
          balances[user] = balances[user] if user in balances else 0
          wools[user] = wools[user] if user in wools else 0
          crypto_for_selling_wool = amount * 15
          wools[user] -= amount
          balances[user] += crypto_for_selling_wool
          embed = discord.Embed(title = 'Sale Complete', description = f'You gained `{crypto_for_selling_wool} coins` for selling **{amount}** wool', color = random.choice(random_colors))
          await ctx.send(embed = embed)
        else:
          await ctx.send('um i don\'t think you have enough wool for that **SCAMMER**')
      else:
        print(f'In buy(): No record for {user} found. Creating a new record with a starting balance of {START_BAL}') 
        balances[user] = START_BAL 
        await ctx.send(f'hey you don\'t have a bank account yet. I just created one for you and started you off with le {START_BAL}') 
    else:
      await ctx.send('you don\'t have any wool with you')
  elif arg == "meat" or arg == "meats":
    if user in meats:
      if user in balances:
        if meats[user] > amount or meats[user] == amount:
          balances[user] = balances[user] if user in balances else 0
          meats[user] = meats[user] if user in meats else 0
          crypto_for_selling_meat = amount * 20
          meats[user] -= amount
          balances[user] += crypto_for_selling_meat
          embed = discord.Embed(title = 'Sale Complete', description = f'You gained `{crypto_for_selling_meat} coins` for selling **{amount}** meat', color = random.choice(random_colors))
          await ctx.send(embed = embed)
        else:
          await ctx.send('um i don\'t think you have enough meat for that **SCAMMER**')
      else:
        print(f'In buy(): No record for {user} found. Creating a new record with a starting balance of {START_BAL}') 
        balances[user] = START_BAL 
        await ctx.send(f'hey you don\'t have a bank account yet. I just created one for you and started you off with le {START_BAL}') 
    else:
      await ctx.send('you don\'t have any meat with you')
  else:
    await ctx.send('bruh that aint even in the shop wtf')

  print(f'In sell(): Saving wool = {wools}')
  try: 
    with open(WOOL_FILE, 'w') as fp: 
      json.dump(wools, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {WOOL_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {meats}')
  try: 
    with open(MEAT_FILE, 'w') as fp: 
      json.dump(meats, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {MEAT_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving wheats = {wheats}')
  try: 
    with open(WHEAT_FILE, 'w') as fp: 
      json.dump(wheats, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {WHEAT_FILE} not found! Not sure what to do here!') 





@bot.command()
async def popeyes(ctx):
  embed = discord.Embed(title = "Dr. Sped's Popeyes", description = "`le buy <item> <amount>` | `le cook <item> <amount>`", color = random.choice(random_colors))
  embed.add_field(name = ":hatched_chick: Uncooked Chicken [ANIMAL]", value = "Price: __10,000__ coins")
  await ctx.send(embed = embed)





@bot.command()
async def shop(ctx):
  embed = discord.Embed(title = "Dr. Sped's secret shop", description = "`le buy <item> <amount>` or `le sell <item> <amount>`\n`le farm`\nGoods are not able to be purchased", color = random.choice(random_colors))
  embed.add_field(name = "Animals\n", value = "\n:sheep: **Sheep** ─ __100__ coins ─ Item\n :pig2: **Pig** ─ __200__ coins ─ Item\n :water_buffalo: **Buffalo** ─ __10,000,000__ coins ─ Item", inline = True)
  embed.add_field(name = "Materials\n", value = "\n:cooking: **Stove** ─ __19,500__ coins ─ Item", inline = False)
  embed.add_field(name = "Crops\n", value = "\n:rice: **Rice** ─ __30__ coins ─ Item", inline = False)
  embed.add_field(name = "Miscellaneous\n", value = "\n:desktop: **PC** ─ __1,500__ coins ─ Item\n<:bowl:716492750996111441> **Bowl** ─ __50__ coins ─ Item")
  await ctx.send(embed=embed)





@bot.command()
async def jetshop(ctx):
  global morris, douglas
  user = str(ctx.message.author.id)
  morris[user] = morris[user] if user in morris else 0
  douglas[user] = douglas[user] if user in douglas else 0
  embed = discord.Embed(title = 'Jet shop', description = '`le get [Morris/Douglas]` or `le fly [Morris/Douglas]`', color = random.choice(random_colors))
  embed.add_field(name = ':airplane_small: Morris X8200', value = 'small but fiesty jet, 25% chance of getting air sickness\n`Price: 1500 Meat, 3 Salads, 5000 wheat, 10000 coins`', inline = True)
  embed.add_field(name = ':airplane: Douglas 900ER', value = 'Wanna travel far without problems, here\'s your answer!\n`Price: 5000 Meat, 20 Salads, 10 Stoves, 75000 coins`', inline = False)
  await ctx.send(embed = embed)





@bot.command()
async def get(ctx, arg1):
  global balances, meats, salads, wheats, stoves
  user = str(ctx.message.author.id)
  morris[user] = morris[user] if user in morris else 0
  douglas[user] = douglas[user] if user in douglas else 0
  stoves[user] = stoves[user] if user in stoves else 0
  meats[user] = meats[user] if user in meats else 0
  balances[user] = balances[user] if user in balances else 0
  wheats[user] = wheats[user] if user in wheats else 0
  salads[user] = salads[user] if user in salads else 0
  if arg1 == "Morris" or arg1 == "morris":
    if balances[user] == 10000 or balances[user] > 10000:
      if meats[user] == 1500 or meats[user] > 1500:
        if salads[user] == 3 or salads[user] > 3:
          if wheats[user] == 5000 or wheats[user] > 5000:
            wheats[user] -= 5000
            salads[user] -= 3
            meats[user] -= 1500
            balances[user] -= 10000
            morris[user] += 1
            await ctx.send(f'Congratulations {ctx.message.author.mention}! You have bought a Morris X8200 jet!')
          else: 
            await ctx.send('You don\'t have enough wheat for this!')
        else:
          await ctx.send('You don\'t have enough salads for this!')
      else:
        await ctx.send('You don\'t have enough meat for this!')
    else:
      await ctx.send('You don\'t have enough money for this!')
  elif arg1 == "Douglas" or arg1 == "douglas":
    if balances[user] == 75000 or balances[user] > 75000:
      if meats[user] == 5000 or meats[user] > 5000:
        if salads[user] == 20 or salads[user] > 20:
          if stoves[user] == 10 or stoves[user] > 10:
            meats[user] -= 5000
            salads[user] -= 20
            stoves[user] -= 10
            balances[user] -= 75000
            douglas[user] += 1
            await ctx.send(f'Congratulations {ctx.message.author.mention}! You just cought a Douglas 900ER jet!')
          else:
            await ctx.send('You don\'t have enough stoves for this!')
        else:
          await ctx.send('You don\'t have enough salads for this!')
      else:
        await ctx.send('You don\'t have enough meat for this!')
    else:
      await ctx.send('You don\'t have enough money for this!')
  else: 
    await ctx.send('error occured')
    
  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 

  print(f'In buy(): Saving stoves = {stoves}')
  try: 
    with open(STOVES_FILE, 'w') as fp: 
      json.dump(stoves, fp) 
  except FileNotFoundError: 
    print(f'In pigs(): File {STOVES_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {meats}')
  try: 
    with open(MEAT_FILE, 'w') as fp: 
      json.dump(meats, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {MEAT_FILE} not found! Not sure what to do here!') 
  
  print(f'In sell(): Saving meats = {morris}')
  try: 
    with open(MORRIS_FILE, 'w') as fp: 
      json.dump(morris, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {MORRIS_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {douglas}')
  try: 
    with open(DOUGLAS_FILE, 'w') as fp: 
      json.dump(douglas, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {DOUGLAS_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving wheat = {wheats}')
  try: 
    with open(WHEAT_FILE, 'w') as fp: 
      json.dump(wheats, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {WHEAT_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving salads = {salads}')
  try: 
    with open(SALADS_FILE, 'w') as fp: 
      json.dump(salads, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {SALADS_FILE} not found! Not sure what to do here!') 

# 0 IS CALIFORNIA
# 1 IS TEXAS

@bot.command()
async def fly(ctx, arg1):
  global morris, douglas, locations, healths
  user = str(ctx.message.author.id)
  locations[user] = locations[user] if user in locations else 0
  morris[user] = morris[user] if user in morris else 0
  douglas[user] = douglas[user] if user in douglas else 0
  if arg1 == "morris" or arg1 == "Morris":
    if morris[user] == 1 or morris[user] > 1:
      await ctx.send('You have a 25% chance of getting air sick,causing you to lose about 5-9 health.\nStill wanna fly on this plane? `y` or `n`')
      msg = await bot.wait_for('message', check = lambda m: m.author == ctx.author)
      if msg.content.lower() == 'y':
        await ctx.send('Where do you want to travel? `Texas` or `California`?')
        msg = await bot.wait_for('message', check = lambda m: m.author == ctx.author)
        if msg.content.lower() == 'California' or msg.content.lower() == 'california':
          if locations[user] == 0:
            await ctx.send('how do you expect to travel to California if ur already here')
          elif locations[user] == 1:
            CHANCE_OF_GETTING_AIR_SICK = random.randint(1, 100)
            HEALTH_LOSS = random.randint(5, 9)
            msg_prefix = 'Travelling back to California' 
            msg_str = msg_prefix + '.' 
            msg = await ctx.send(msg_str)
            for i in range(FLY_DELAY_ITER): 
              await asyncio.sleep(FLY_DELAY_SEC)
              msg_str = msg_str + '.' 
              await msg.edit(content = msg_str)
            if CHANCE_OF_GETTING_AIR_SICK < 25 or CHANCE_OF_GETTING_AIR_SICK == 25:
              healths[user] -= HEALTH_LOSS
              await ctx.send(f'welp you got air sick, causing you to lose {HEALTH_LOSS} health')
            locations[user] = 0
            await ctx.send('You are in California now! Things to do are `le farm`')
          else:
            await ctx.send('Error Occured')
        elif msg.content.lower == "Texas" or msg.content.lower() == 'texas':
          if locations[user] == 1:
            await ctx.send('how do you expect to travel to Texas if ur already here')
          elif locations[user] == 0:
            CHANCE_OF_GETTING_AIR_SICK = random.randint(1, 100)
            HEALTH_LOSS = random.randint(5, 9)
            if CHANCE_OF_GETTING_AIR_SICK > 25:
              await ctx.send('Travelling to Texas!')
              await ctx.send(f'welp you got air sick, causing you to lose {HEALTH_LOSS} health')
              healths[user] -= HEALTH_LOSS
              locations[user] = 1
              await asyncio.sleep(1.5)
              await ctx.send('You are in Texas now! Things to do are `le city`')
            else:
              await ctx.send('Travelling to Texas!')
              locations[user] = 1
              await asyncio.sleep(1.5)
              await ctx.send('You are in Texas now! Things to do are `le city`')
          else:
            await ctx.send('Error Occured')
        else:
          await ctx.send('does that look like an option ')
      elif msg.content.lower() == 'n':
        await ctx.send('yeeting off this plane')
    else:
      await ctx.send('You don\'t have the Morris jet!')
  elif arg1 == "Douglas" or arg1 == "douglas":
    if douglas[user] == 1 or douglas[user] > 1:
      await ctx.send('Where do you want to travel? `Texas` or `California`?')
      msg = await bot.wait_for('message', check = lambda m: m.author == ctx.author)
      if msg.content.lower() == 'California' or msg.content.lower() == 'california':
        if locations[user] == 0:
          await ctx.send('how do you expect to travel to California if ur already here')
        elif locations[user] == 1:
            await ctx.send('Travelling back to california!')
            locations[user] = 0
            await asyncio.sleep(1.5)
            await ctx.send('You are in California now! Things to do are `le farm California`')
        else:
          await ctx.send('Error Occured')
      elif msg.content.lower == "Texas" or msg.content.lower() == 'texas':
        if locations[user] == 1:
          await ctx.send('how do you expect to travel to Texas if ur already here')
        elif locations[user] == 0:
            await ctx.send('Travelling to Texas!')
            locations[user] = 1
            await asyncio.sleep(1.5)
            await ctx.send('You are in Texas now! Things to do are `le city`')
        else:
          await ctx.send('Error Occured')
      else:
        await ctx.send('does that look like an option ')
    else:
      await ctx.send('You don\'t have the Douglas jet!')
  else:
    await ctx.send('error occured')
          
  print(f'In beg(): Saving balances = {locations}')
  try: 
    with open(LOCATIONS_FILE, 'w') as fp: 
      json.dump(locations, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {LOCATIONS_FILE} not found! Not sure what to do here!') 

  print(f'In beg(): Saving balances = {healths}')
  try: 
    with open(HEALTH_FILE, 'w') as fp: 
      json.dump(healths, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {HEALTH_FILE} not found! Not sure what to do here!') 





@bot.command()
async def use(ctx, arg):
  global ambulances, healths, bread
  user = str(ctx.message.author.id)

  if arg == "ambulances" or arg == "ambulance":
    if user in ambulances:
      if ambulances[user] > 1 or ambulances[user] == 1:
        if user in healths:
          if healths[user] < 100:
            healths[user] = 100
            ambulances[user] -= 1
            await ctx.send(f'{ctx.message.author.mention} has just healed themselves to 100 health!')
          else:
            await ctx.send('You can\'t dose that, you have full health!')
        else:
          healths[user] = 100
      else:
        await ctx.send('You don\'t have any ambulances with u')
    else:
      await ctx.send('Go buy some ambulances child')
  elif arg == 'bread' or arg == 'bread':
    if user in bread:
      if bread[user] > 1 or bread[user] == 1:
        if user in healths:
          if healths[user] < 60:
            healths[user] = 60
            bread[user] -= 1
            await ctx.send(f'{ctx.message.author.mention} has just healed themselves to 60 health!')
          else:
            await ctx.send('you dumbass you have more than 60 health smh smh')
        else:
          healths[user] = 100
      else:
        await ctx.send(' go get some bread first')
    else:
      await ctx.send('go get some bread first')
  else:
    await ctx.send('not an option !')

  print(f'In sell(): Saving meats = {bread}')
  try: 
    with open(BREAD_FILE, 'w') as fp: 
      json.dump(bread, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {BREAD_FILE} not found! Not sure what to do here!')   

  print(f'In buy(): Saving ambulances = {ambulances}')
  try: 
    with open(AMBULANCES_FILE, 'w') as fp: 
      json.dump(ambulances, fp) 
  except FileNotFoundError: 
    print(f'In pigs(): File {AMBULANCES_FILE} not found! Not sure what to do here!') 

  print(f'In buy(): Saving healths = {healths}')
  try: 
    with open(HEALTH_FILE, 'w') as fp: 
      json.dump(healths, fp) 
  except FileNotFoundError: 
    print(f'In pigs(): File {HEALTH_FILE} not found! Not sure what to do here!') 





@bot.command()
async def buy(ctx, arg, amount: int):
  global sheeps, wools, rices, wheats, pigs, meats, ambulances, buffalos, stoves, uncooked_chickens, cooked_chickens, salads, morris, douglas, locations, pc, bread, mooshroom_cows, bowls
  user = str(ctx.message.author.id)
  locations[user] = locations[user] if user in locations else 0
  morris[user] = morris[user] if user in morris else 0
  douglas[user] = douglas[user] if user in douglas else 0
  salads[user] = salads[user] if user in salads else 0
  cooked_chickens[user] = cooked_chickens[user] if user in cooked_chickens else 0
  uncooked_chickens[user] = uncooked_chickens[user] if user in uncooked_chickens else 0
  stoves[user] = stoves[user] if user in stoves else 0
  sheeps[user] = sheeps[user] if user in sheeps else 0
  buffalos[user] = buffalos[user] if user in buffalos else 0
  wools[user] = wools[user] if user in wools else 0
  rices[user] = rices[user] if user in rices else 0
  wheats[user] = wheats[user] if user in wheats else 0
  pigs[user] = pigs[user] if user in pigs else 0
  meats[user] = meats[user] if user in meats else 0
  ambulances[user] = ambulances[user] if user in ambulances else 0
  pc[user] = pc[user] if user in pc else 0
  bread[user] = bread[user] if user in bread else 0
  mooshroom_cows[user] = mooshroom_cows[user] if user in mooshroom_cows else 0
  bowls[user] = bowls[user] if user in bowls else 0

  if arg == "bowl" or arg == "bowls":
    if user in balances:
      if balances[user] > 50 or balances[user] == 50:
        price_for_bowl = amount * 50
        if balances[user] > price_for_bowl or balances[user] == price_for_bowl:
          bowls[user] = bowls[user] + amount if user in bowls else amount
          balances[user] -= price_for_bowl
          embed = discord.Embed(title = 'Purchase Complete', description = f'You bought **{amount}** bowls for `{price_for_bowl} coins`', color = random.choice(random_colors))
          await ctx.send(embed = embed)
        else:
          await ctx.send(f'You don\'t have enough to buy {amount} bowls')
      else:
        await ctx.send('you don\'t have enough money don\'t try to scam me')
    else:
      print(f'In beg(): No record for {user} found. Creating a new record with a starting balance of {START_BAL}') 
      balances[user] = START_BAL 
      await ctx.send(f'hey you don\'t have a bank account yet. I just created one for you and started you off with {START_BAL} coins') 
  elif arg == "sheep":
    if user in balances:
      if balances[user] > 100 or balances[user] == 100:
        price_for_sheep = amount * 100
        if balances[user] > price_for_sheep or balances[user] == price_for_sheep:
          sheeps[user] = sheeps[user] + amount if user in sheeps else amount
          balances[user] -= price_for_sheep
          embed = discord.Embed(title = 'Purchase Complete', description = f'You bought **{amount}** sheep for `{price_for_sheep} coins`', color = random.choice(random_colors))
          await ctx.send(embed = embed)
        else:
          await ctx.send(f'You don\'t have enough to buy {amount} sheeps')
      else:
        await ctx.send('you don\'t have enough money don\'t try to scam me')
    else:
      print(f'In beg(): No record for {user} found. Creating a new record with a starting balance of {START_BAL}') 
      balances[user] = START_BAL 
      await ctx.send(f'hey you don\'t have a bank account yet. I just created one for you and started you off with {START_BAL} coins')  
  elif arg == "rice":
    if user in balances:
      if balances[user] > 30 or balances[user] == 30:
        price_for_rice = amount * 30
        if balances[user] > price_for_rice or balances[user] == price_for_rice:
          rices[user] = rices[user] + amount if user in rices else amount
          balances[user] -= price_for_rice
          embed = discord.Embed(title = 'Purchase Complete', description = f'You bought **{amount}** rice for `{price_for_rice} coins`', color = random.choice(random_colors))
          await ctx.send(embed = embed)
        else:
          await ctx.send(f'You don\'t have enough to buy {amount} rice')
      else:
        await ctx.send('you don\'t have enough money don\'t try to scam me')
    else:
      print(f'In beg(): No record for {user} found. Creating a new record with a starting balance of {START_BAL}') 
      balances[user] = START_BAL 
      await ctx.send(f'hey you don\'t have a bank account yet. I just created one for you and started you off with {START_BAL} coins') 
  elif arg == "pig" or arg == "pigs":
    if user in balances:
      if balances[user] > 200 or balances[user] == 200:
        price_for_pigs = amount * 200
        if balances[user] > price_for_pigs or balances[user] == price_for_pigs:
          pigs[user] = pigs[user] + amount if user in pigs else amount
          balances[user] -= price_for_pigs
          embed = discord.Embed(title = 'Purchase Complete', description = f'You bought **{amount}** pigs for `{price_for_pigs} coins`', color = random.choice(random_colors))
          await ctx.send(embed = embed)
        else:
          await ctx.send(f'You don\'t have enough to buy {amount} pig(s)')
      else:
        await ctx.send('You don\'t have enough money don\'t try to scam me')
    else:
      print(f'In beg(): No record for {user} found. Creating a new record with a starting balance of {START_BAL}') 
      balances[user] = START_BAL 
      await ctx.send(f'hey you don\'t have a bank account yet. I just created one for you and started you off with {START_BAL} coins') 
  elif arg == "ambulance" or arg == "ambulances":
    if user in meats:
      if meats[user] > 15200 or meats[user] == 15200:
        price_for_ambulances = amount * 15200
        if meats[user] > price_for_ambulances or meats[user] == price_for_ambulances:
          ambulances[user] = ambulances[user] + amount if user in ambulances else amount
          meats[user] -= price_for_ambulances
          embed = discord.Embed(title = 'Purchase Complete', description = f'You bought **{amount}** ambulances for `{price_for_ambulances} meat`', color = random.choice(random_colors))
          await ctx.send(embed = embed)
        else:
          await ctx.send(f'You don\'t have enough to buy {amount} ambulances!')
      else:
        await ctx.send('oi go harvest more pigs to buy this ya **SCAMMER**')
    else:
      await ctx.send('You don\'t have any meat...')
  elif arg == "buffalo" or arg == "buffalos":
    if user in balances:
      if balances[user] > 10000000 or balances[user] == 10000000:
        price_for_buffalos = amount * 10000000
        if balances[user] > price_for_buffalos or balances[user] == price_for_buffalos:
          buffalos[user] = buffalos[user] + amount if user in buffalos else amount
          balances[user] -= price_for_buffalos
          embed = discord.Embed(title = 'Purchase Complete', description = f'You bought **{amount}** buffalo for `{price_for_buffalos} coins`', color = random.choice(random_colors))
          await ctx.send(embed = embed)
        else:
          await ctx.send(f'You don\'t have enough to buy {amount} buffalos!')
      else:
        await ctx.send('You don\'t have enough coins for that **SCAMMER**')
    else:
      await ctx.send('You don\'t have any coins!')
  elif arg == "stove" or arg == "stoves":
    if user in balances:
      if balances[user] > 19500 or balances[user] == 19500:
        price_for_stoves = amount * 19500
        if balances[user] > price_for_stoves or balances[user] == price_for_stoves:
          stoves[user] = stoves[user] + amount if user in stoves else amount
          balances[user] -= price_for_stoves
          embed = discord.Embed(title = 'Purchase Complete', description = f'You bought **{amount}** stoves for `{price_for_stoves} coins`', color = random.choice(random_colors))
          await ctx.send(embed = embed)
        else:
          await ctx.send(f'You don\'t have enough to buy {amount} stoves!')
      else:
        await ctx.send('You don\'t have enough coins for that **SCAMMER**')
    else:
      await ctx.send('You don\'t have any coins!')
  elif arg == "chicken" or arg == "chickens":
    if user in balances:
      if balances[user] > 10000 or balances[user] == 10000:
        price_for_uncooked_chickens = amount * 10000
        if balances[user] > price_for_uncooked_chickens or balances[user] == price_for_uncooked_chickens:
          uncooked_chickens[user] = uncooked_chickens[user] + amount if user in uncooked_chickens else amount
          balances[user] -= price_for_uncooked_chickens
          embed = discord.Embed(title = 'Purchase Complete', description = f'You bought **{amount}** uncooked chickens for `{price_for_uncooked_chickens} coins`', color = random.choice(random_colors))
          await ctx.send(embed = embed)
        else:
          await ctx.send(f'You don\'t have enough to buy {amount} uncooked chicken(s)!')
      else:
        await ctx.send('You don\'t have enough coins for that')
    else:
      await ctx.send('You don\'t have any coins!')
  elif arg == 'pc' or arg == 'PC':
    if user in balances:
      if balances[user] > 1500 or balances[user] == 1500:
        price_for_lap = amount * 1500
        if balances[user] > price_for_lap or balances[user] == price_for_lap:
          pc[user] += amount
          balances[user] -= price_for_lap
          embed = discord.Embed(title = 'Purchase Complete', description = f'You bought **{amount}** laptop(s) for `{price_for_lap} coins`', color = random.choice(random_colors))
          await ctx.send(embed = embed)
        else:
          await ctx.send('You don\'t have enough coins for dis!')
      else:
        await ctx.send('You don\'t have enough coins for this!')
    else:
      await ctx.send('bruh u dont even have a bank account. for one type in `le plead`')
  elif arg == 'bread' or arg == 'Bread':
    if user in balances:
      if balances[user] == 1200 or balances[user] > 1200:
        price_for_bread = amount * 1200
        if balances[user] > price_for_bread or balances[user] == price_for_bread:
          bread[user] += amount
          balances[user] -=  price_for_bread
          embed = discord.Embed(title = 'Purchase Complete', description = f'You bought **{amount}** bread for `{price_for_bread} coins`', color = random.choice(random_colors))
          await ctx.send(embed = embed)
        else:
          await ctx.send('You don\'t have enough coins for this!')
      else:
        await ctx.send('You don\'t have enough coins for this!')
    else:
      await ctx.send(' u don\'t even have a bank account. for one type in `le plead`')
  else:
    await ctx.send('bruh that aint even in the shop wtf')

  print(f'In sell(): Saving meats = {bread}')
  try: 
    with open(BREAD_FILE, 'w') as fp: 
      json.dump(bread, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {BREAD_FILE} not found! Not sure what to do here!') 


  print(f'In sell(): Saving meats = {meats}')
  try: 
    with open(MEAT_FILE, 'w') as fp: 
      json.dump(meats, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {MEAT_FILE} not found! Not sure what to do here!') 


  print(f'In buy(): Saving sheeps = {sheeps}')
  try: 
    with open(SHEEPS_FILE, 'w') as fp: 
      json.dump(sheeps, fp) 
  except FileNotFoundError: 
    print(f'In buy(): File {SHEEPS_FILE} not found! Not sure what to do here!') 

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 

  print(f'In buy(): Saving rice = {rices}')
  try: 
    with open(RICE_FILE, 'w') as fp: 
      json.dump(rices, fp) 
  except FileNotFoundError: 
    print(f'In rice(): File {RICE_FILE} not found! Not sure what to do here!') 

  print(f'In buy(): Saving pigs = {pigs}')
  try: 
    with open(PIG_FILE, 'w') as fp: 
      json.dump(pigs, fp) 
  except FileNotFoundError: 
    print(f'In pigs(): File {pigs} not found! Not sure what to do here!') 

  print(f'In buy(): Saving ambulances = {ambulances}')
  try: 
    with open(AMBULANCES_FILE, 'w') as fp: 
      json.dump(ambulances, fp) 
  except FileNotFoundError: 
    print(f'In pigs(): File {AMBULANCES_FILE} not found! Not sure what to do here!') 

  print(f'In buy(): Saving buffalos = {buffalos}')
  try: 
    with open(BUFFALOS_FILE, 'w') as fp: 
      json.dump(buffalos, fp) 
  except FileNotFoundError: 
    print(f'In pigs(): File {BUFFALOS_FILE} not found! Not sure what to do here!') 

  print(f'In buy(): Saving stoves = {stoves}')
  try: 
    with open(STOVES_FILE, 'w') as fp: 
      json.dump(stoves, fp) 
  except FileNotFoundError: 
    print(f'In pigs(): File {STOVES_FILE} not found! Not sure what to do here!') 

  print(f'In buy(): Saving uncooked chickens = {uncooked_chickens}')
  try: 
    with open(UNCOOKED_CHICKENS_FILE, 'w') as fp: 
      json.dump(uncooked_chickens, fp) 
  except FileNotFoundError: 
    print(f'In pigs(): File {UNCOOKED_CHICKENS_FILE} not found! Not sure what to do here!') 

  print(f'In buy(): Saving sheeps = {pc}')
  try: 
    with open(PC_FILE, 'w') as fp: 
      json.dump(pc, fp) 
  except FileNotFoundError: 
    print(f'In buy(): File {PC_FILE} not found! Not sure what to do here!') 

  print(f'In buy(): Saving sheeps = {bowls}')
  try: 
    with open(BOWLS_FILE, 'w') as fp: 
      json.dump(bowls, fp) 
  except FileNotFoundError: 
    print(f'In buy(): File {BOWLS_FILE} not found! Not sure what to do here!') 




@bot.command()
async def health(ctx):
  global healths, HEALTH_FILE
  user = str(ctx.message.author.id)

  #-------------------------------------
  try:
    with open(HEALTH_FILE, 'r') as fp: 
      healths = json.load(fp) 
  except FileNotFoundError:
    print(f'In on_ready(): File {HEALTH_FILE} not found. Starting off with an empty balances dictionary.') 
    health = {} 
  #-------------------------------------
  
  print(f'In health(): Author Id = {ctx.message.author.id}, Author Name = {user}')
  if user in healths:
    embed = discord.Embed(title = f"{ctx.message.author}'s health :heartpulse:", description = "Your health is deprived everytime you harvest.\nTo regenerate, go to `le pharmacy` to buy meds.\nDose them to regenerate health.", color = random.choice(random_colors))
    embed.add_field(name = "Your health", value = f'{healths[user]}/100')
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





@bot.command(name = 'plead')
@commands.cooldown(1, 60, commands.BucketType.user)
async def plead(ctx):
  global balances, START_BAL 
  INCREMENT = random.randint(20, 70)
  user = str(ctx.message.author.id) 
  print(f'In plead(): Author Id = {ctx.message.author.id}, Author Name = {user}')

  #-------------------------------------
  try:
    with open(BALANCES_FILE, 'r') as fp: 
      balances = json.load(fp) 
  except FileNotFoundError:
    print(f'In on_ready(): File {BALANCES_FILE} not found. Starting off with an empty balances dictionary.') 
    balances = {} 
  #-------------------------------------

  if user in balances: 
    # print(f'In plead(): Found record for {user}. Incrementing balance by {random.randint(20,70)}')
    responses = [
      f"**Detective Dank** donated {INCREMENT} coins to {ctx.message.author.mention}!",
      f"**David Dobrik** donated {INCREMENT} coins to {ctx.message.author.mention}!",
      f"**Pewdiepie** donated {INCREMENT} coins to {ctx.message.author.mention}!",
      f"**Kylie Jenner** donated {INCREMENT} coins to {ctx.message.author.mention}!",
      f"**Ur Mom** donated {INCREMENT} coins to {ctx.message.author.mention}!",
      f"**Kanye West** donated {INCREMENT} coins to {ctx.message.author.mention}!",
      f"**Markiplier** donated {INCREMENT} coins to {ctx.message.author.mention}!",
      f"**Mojang** donated {INCREMENT} coins to {ctx.message.author.mention}!",
      f"**Jesus** donated {INCREMENT} coins to {ctx.message.author.mention}!"
    ]
    await ctx.send(random.choice(responses))
    balances[user] += INCREMENT
  else: 
    print(f'In plead(): No record for {user} found. Creating a new record with a starting balance of {START_BAL}') 
    balances[user] = START_BAL 
    await ctx.send(f'hey you don\'t have a bank account yet. I just created one for you and started you off with le {START_BAL}') 

  print(f'In plead(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In beg(): File {BALANCES_FILE} not found! Not sure what to do here!') 


  





@bot.command(name = 'bal', aliases = ['balance', 'coins', 'money'])
async def bal(ctx, member: discord.Member): 
  global balances, START_BAL 
  user = str(ctx.message.author.id)
  member2 = str(member.id)

  #-------------------------------------
  try:
    with open(BALANCES_FILE, 'r') as fp: 
      balances = json.load(fp) 
  except FileNotFoundError:
    print(f'In on_ready(): File {BALANCES_FILE} not found. Starting off with an empty balances dictionary.') 
    balances = {} 
  #-------------------------------------
  
  if member2 in balances:
    embed = discord.Embed(title=f":moneybag: {member.name}'s balance", description=f"**Bank Account**: {balances[member2]:,d}/ꝏ", color = random.choice(random_colors))

    await ctx.send(embed=embed)
  else:
    await ctx.send('that user does not have a bank account')



#===============
#===============
# ERRORS
#===============
#===============






@rice.error
async def rice_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    m, s = divmod(error.retry_after, 60)
    await ctx.send(f'wait **{round(m)} minutes and {round(s)} seconds** to get more goods  ')

@stew.error
async def stew_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    m, s = divmod(error.retry_after, 60)
    await ctx.send(f'wait **{round(m)} minutes and {round(s)} seconds** to get more stew  ')
  elif isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Proper Usage: `le stew [ex: mooshroom]`')

@give.error
async def give_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Proper Usage: `le give [amount] [user]`')

@youtube.error
async def youtube_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Proper Usage: `le youtube [search query]`')

@use.error
async def use_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Proper Usage: `le use [item]`')


@setmembermessage.error
async def setmembermessage_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Proper Usage: `le setmembermessage [message]`')
  elif isinstance(error, commands.MissingPermissions):
    await ctx.send('You don\'t have the perm: `Manage Server`!')
    
@reactionmessage.error
async def reactionmessage_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send('You don\'t have the perm: `Manage Server`!')
  
@membermessage.error
async def membermessage_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send('You don\'t have the perm: `Manage Server`!')

@setchannelid.error
async def setchannelid_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send('You don\'t have the perm: `Manage Server`!') 
  elif isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Proper Usage: `le setchannelid [channel id]`')

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

@sheep.error
async def sheep_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    m, s = divmod(error.retry_after, 60)
    await ctx.send(f'wait **{round(m)} minutes and {round(s)} seconds** to get more goods  ')


@health.error
async def health_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    m, s = divmod(error.retry_after, 60)
    h, m = divmod(m, 60)
    await ctx.send(f'wait **{round(h)} hours and {round(m)} minutes** to get more revenue  ')

@pig.error
async def pig_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    m, s = divmod(error.retry_after, 60)
    await ctx.send(f'wait **{round(m)} minutes and {round(s)} seconds** to get more goods  ')





@fly.error
async def fly_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Proper Usage: `le fly [morris/douglas]`')


@automemez.error
async def am_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    global autoMeme
    autoMeme = True
    while autoMeme == True:
      await meme(ctx)
      await asyncio.sleep(5)

@purchase.error
async def purchase_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Proper Usage: `le purchase [ex: mooshroom] [amount]`')

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

@bal.error
async def bal_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    user = str(ctx.message.author.id)
    if user in balances:
      embed = discord.Embed(title=f":moneybag: {ctx.message.author.name}'s balance", description=f"**Bank Account**: {balances[user]:,d}/ꝏ", color = random.choice(random_colors))

      await ctx.send(embed=embed)
    else:
      balances[user] = 100
      await ctx.send('You didnt have an account so i made you one with a start of 100 coins')

@setprefix.error
async def setprefix_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Proper Usage: `le setprefix [prefix]`')










@sell.error
async def sell_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Proper Usage: `le sell [item] [amount]`')





@get.error
async def get_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Proper Usage: `le get [morris/douglas]`')




@buy.error
async def buy_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Proper Usage: `le buy [item] [amount]`')



@combine.error
async def combine_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Proper Usage: `le combine [chicken] [rice]` See `le notebook` for amounts of the recipe')





@requirements.error
async def requirements_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Proper Usage: `le requirements [medium city/advanced city]`')
    



@buffalo.error
async def buffalo_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    m, s = divmod(error.retry_after, 60)
    await ctx.send(f'wait **{round(m)} minutes and {round(s)} seconds** to get more goods ')





@daily.error
async def daily_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    m, s = divmod(error.retry_after, 60 )
    h, m = divmod(m, 60)
    await ctx.send(f'wait **{round(h)} hours and {round(m)} minutes** to get ur daily coins ')
    return





@grab.error
async def grab_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    m, s = divmod(error.retry_after, 60)
    await ctx.send(f'wait **{round(m)} minutes and {round(s)} seconds** to grab another airdrop ')
    return





@cook.error
async def cook_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    m, s = divmod(error.retry_after, 60)
    await ctx.send(f'wait **{round(m)} minutes and {round(s)} seconds** to cook again ')
    return  
  elif isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Proper Usage: `le cook [chicken]`')





@plead.error
async def plead_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    m, s = divmod(error.retry_after, 60)
    await ctx.send(f'wait **{round(m)} minutes and {round(s)} seconds** to plead again ')
    return





@twitch.error
async def stream_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    m, s = divmod(error.retry_after, 60)
    await ctx.send(f'wait **{round(m)} minutes and {round(s)} seconds** to stream again ')
    return




@work.error
async def work_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    m, s = divmod(error.retry_after, 60)
    await ctx.send(f'wait **{round(m)} minutes and {round(s)} seconds** to work again ')
    return


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
          await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load()
    await bot.start('x')
            
asyncio.run(main())
