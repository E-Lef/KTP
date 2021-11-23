import discord
import json
from discord.ext import commands 
import datetime
client = discord.Client()
bot = commands.Bot(command_prefix='!', owner_id=)
now = datetime.datetime.today()
d = now.isoweekday()
if d==1:
    c=id channel day 
if d==2:
    c=""
if d==3:
    c=""
if d==4:
    c=""
if d==5:
    c=""
if d==6:
    c=""

with open(r'json path') as file:
    data = json.load(file)
    k=[]
    v=[]
    for i in data.keys():
        k.append(i)
    for n in data.values():
        v.append(n)

print(k[0],v[0])
@client.event
async def on_ready():
    a=[]
    print("confirmation in progress")
    if ""in v[0]:
        a.append('<@iduser>')
        a.append("")
    if   ""in v[0]:
        a.append('<@iduser>')
        a.append("")

    elif "" not in v[0] and ""not in v[0]:
        a.append('<@iduser>')
        a.append(' : {} {} '.format(k[0],v[0]))
    i=0
    while i < len(a):
        await client.get_channel(id=c).send(a[i])
        i +=1
    print("confirmation sent")
    await client.close()
client.run("Token")
