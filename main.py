import discord
import os
from discord.ext import commands
import helpd
import os
from dotenv import load_dotenv


bot = commands.Bot(command_prefix="j!")
s = False

#login
@bot.event
async def on_ready():
   
    activity=discord.Activity(type=discord.ActivityType.listening, name="/guide")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Juan is online")

    #specials
    '''wish = discord.Embed(
      title = "**MERRY CHRISTMAS !**",
      description = "Santa's third most preferred mode of transport after Rudolph and Harley Davidson",
      colour = discord.Colour.red()
    )
    wish.set_image(url="https://c.tenor.com/7rbwjUolqgIAAAAC/christmas-horse.gif")
    
    for guild in bot.guilds:
      await guild.text_channels[0].send(embed = wish)'''

#bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))




#help
@bot.slash_command(name="guide", description="show a guide")
async def guide(ctx):
  helpmsg = discord.Embed(
    title="**Guide:**",
    description= helpd.helpdes,
    colour = discord.Colour.blue()
  )
  helpmsg.set_thumbnail(url="https://i.imgur.com/6vMsukK.png")
  helpmsg.set_author(name="Granted", url="https://github.com/Granted07", icon_url="https://avatars.githubusercontent.com/u/69675853?s=96&v=4")
  #fields
  helpmsg.add_field(name="Basic commands:",
  value= helpd.f1 , inline=False),
  # helpmsg.add_field(name="Admin:",
  # value= helpd.f2 , inline=False)
  helpmsg.add_field(name="utility:", 
  value = helpd.f3 , inline = False)
  await ctx.respond(embed = helpmsg)


#admin commands~
# @bot.slash_command() #ban
# async def ban(ctx , member:discord.Member , *, reason=None):
#     await member.ban()
#     banned = discord.Embed(
#           title = ":rofl:",
#           colour = discord.Colour.red()
#         )
#     banned.add_field(name = 
#     str(member) + " was banned" , value = reason , inline = False )
#     banned.set_image(url="https://tuesdayshorse.files.wordpress.com/2016/07/the-world_s-top-10-best-images-of-laughing-horses-7.jpg?w=1088")

#     await ctx.respond(embed = banned)
#     #we do a little trolling
#     lolmsg = discord.Embed(
#         colour = discord.Colour.red()
#        )
#     lolmsg.set_image(url="https://tuesdayshorse.files.wordpress.com/2016/07/the-world_s-top-10-best-images-of-laughing-horses-7.jpg?w=1088")

#     await member.send(embed =lolmsg)
    
#test snippet
@bot.slash_command()
async def servers(ctx):
  for i in bot.guilds:
    await ctx.respond(i)

# @bot.slash_command(name="unban", description="unban a member") #unban
# async def unban(ctx , member):
#     bannedmfs = await ctx.guild.bans()
#     bname , btag = member.split("#")
#     for reentry in bannedmfs:
#       user = reentry.user
#       if (user.name , user.discriminator) == (bname , btag):
#         await ctx.guild.unban(user)



# @bot.slash_command(name="kick", description="kick a member") #kick
# async def kick(ctx , member:discord.Member , reason):
#     await member.kick()
    
    
#     kicked = discord.Embed(
#           title = "LOL LODU NIKAL GAYA :rofl:",
#           colour = discord.Colour.red()
#         )
#     kicked.add_field(name = 
#     str(member) + " was kicked" , value = reason , inline = False )
#     kicked.set_image(url="https://c.tenor.com/P3ISPtq4tyMAAAAM/horse-animals.gif")

#     await ctx.respond(embed = kicked)
#     #we do a little more trolling
#     kickmsg = discord.Embed(
#         colour = discord.Colour.red()
#        )
#     kickmsg.set_image(url="https://tuesdayshorse.files.wordpress.com/2016/07/the-world_s-top-10-best-images-of-laughing-horses-7.jpg?w=1088")

#     await member.send(embed =kickmsg)

###utility:

@bot.slash_command(name="ping", description="shows your latency in ms")
async def ping(ctx):
  p = f'{round(bot.latency * 1000)} ms'
  l = round(bot.latency *1000)
  if l <= 100:
    status = "  :green_circle:"
  elif l > 100 and l < 200:
    status = "  :yellow_circle:"
  elif l > 200 and l < 350:
    status = "  :orange_circle:"
  else:
    status = "  :red_circle:"
  

  run = discord.Embed( 
    colour = discord.Colour.blurple(),
    title = "**CONNECTION STATUS** \n",
    description = "ping: "+p+ status
    )

  run.set_image(url="https://i.imgur.com/MJ0oDhO.gif")
  await ctx.respond(embed = run)

@bot.slash_command(name="jointime", description="displays with absolute precision the exact time whent the person joined this server")
async def jointime(ctx, *, member: discord.Member):
    await ctx.respond('{0} joined this server on {0.joined_at}'.format(member))

# @bot.slash_command(name="stopspam", description="stop a pingspam that you did by mistake")
# async def stopspam():
#      global loop
#      loop = False
  
@bot.slash_command(name="pingspam", description="spam and annoy the fuck out of them")
async def pingspam(ctx , member: discord.Member , number):
    if int(number)>=25 :
      beshispam = discord.Embed(
        colour = discord.Colour.red()
       )
      beshispam.set_image(url="https://c.tenor.com/liyOQm1y4J0AAAAC/horse-slap.gif")
      await ctx.respond(embed = beshispam)
                            
    else:
      loop = True
      for i in range(int(number)):
        print(loop)
        if loop ==  True:
            await ctx.respond(member.mention)
        elif loop == False:
            continue
        
load_dotenv()
tok = os.getenv('TOKEN')
bot.run(tok)
