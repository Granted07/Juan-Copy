import discord
from discord.ext import commands
from run247 import keep_alive
import helpd
import os




bot = commands.Bot(command_prefix="j!")
s = False

#login
@bot.event
async def on_ready():
   
    activity=discord.Activity(type=discord.ActivityType.listening, name="j!guide")
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
@bot.command()
async def guide(ctx):
  helpmsg = discord.Embed(
    title="**Guide:**",
    description= helpd.helpdes,
    colour = discord.Colour.blue()
  )
  helpmsg.set_thumbnail(url="https://i.imgur.com/6vMsukK.png")

  helpmsg.set_author(name="VRTX", url="https://github.com/Sohxn", icon_url="https://avatars.githubusercontent.com/u/85051820?s=96&v=4")
  #fields
  

  helpmsg.add_field(name="Basic commands:",
  value= helpd.f1 , inline=False),

  

  helpmsg.add_field(name="Admin:",
  value= helpd.f2 , inline=False)

  
  
  helpmsg.add_field(name="utility:", 
  value = helpd.f3 , inline = False)
  
  
  
  await ctx.send(embed = helpmsg)







#admin commands~
@bot.command() #ban
async def ban(ctx , member:discord.Member , *, reason=None):
    await member.ban()
    
    
    banned = discord.Embed(
          title = ":rofl:",
          colour = discord.Colour.red()
        )
    banned.add_field(name = 
    str(member) + " was banned" , value = reason , inline = False )
    banned.set_image(url="https://tuesdayshorse.files.wordpress.com/2016/07/the-world_s-top-10-best-images-of-laughing-horses-7.jpg?w=1088")

    await ctx.send(embed = banned)
    #we do a little trolling
    lolmsg = discord.Embed(
        colour = discord.Colour.red()
       )
    lolmsg.set_image(url="https://tuesdayshorse.files.wordpress.com/2016/07/the-world_s-top-10-best-images-of-laughing-horses-7.jpg?w=1088")

    await member.send(embed =lolmsg)
    
#test snippet
@bot.command()
async def servers(ctx):
  for i in bot.guilds:
    await ctx.send(i)

@bot.command() #unban
async def unban(ctx , * , member):
    bannedmfs = await ctx.guild.bans()
    bname , btag = member.split("#")
    for reentry in bannedmfs:
      user = reentry.user
      if (user.name , user.discriminator) == (bname , btag):
        await ctx.guild.unban(user)



@bot.command() #kick
async def kick(ctx , member:discord.Member , *, reason=None):
    await member.kick()
    
    
    kicked = discord.Embed(
          title = "LOL LODU NIKAL GAYA :rofl:",
          colour = discord.Colour.red()
        )
    kicked.add_field(name = 
    str(member) + " was kicked" , value = reason , inline = False )
    kicked.set_image(url="https://c.tenor.com/P3ISPtq4tyMAAAAM/horse-animals.gif")

    await ctx.send(embed = kicked)
    #we do a little more trolling
    kickmsg = discord.Embed(
        colour = discord.Colour.red()
       )
    kickmsg.set_image(url="https://tuesdayshorse.files.wordpress.com/2016/07/the-world_s-top-10-best-images-of-laughing-horses-7.jpg?w=1088")

    await member.send(embed =kickmsg)

 




###utility:

@bot.command()
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
  await ctx.send(embed = run)



@bot.command()
async def jointime(ctx, *, member: discord.Member):
    await ctx.send('{0} joined this server on {0.joined_at}'.format(member))





@bot.command()
async def stopspam(ctx):
     global loop
     loop = False
  
@bot.command()
async def pingspam(ctx , member: discord.Member , *, n=0):
    if n>=25 :
      beshispam = discord.Embed(
        colour = discord.Colour.red()
       )
      beshispam.set_image(url="https://c.tenor.com/liyOQm1y4J0AAAAC/horse-slap.gif")
      await ctx.send(embed = beshispam)
                            
    else:
      loop = True
      for i in range(n):
        print(loop)
        if loop ==  True:
            await ctx.send(member.mention)
        elif loop == False:
            continue

      
         
#@bot.command()
#async def banword(ctx ,*, member: discord.Member):

  


#fun


#runs~
keep_alive()
tok = os.environ['token']
bot.run(tok)
