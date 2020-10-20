import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
import os

bot = commands.Bot(command_prefix = '.linkedin ')
bot.remove_command("help")

@bot.event
async def on_ready():
	print('online')
	await bot.change_presence(activity = discord.Game(name = ".linkedin help"))

@bot.command(aliases = ['profile', 'connect'])
async def share(ctx, link, *, arg = None):
	user = ctx.message.author
	profile_link = link
	profile_name = arg
	guild = ctx.message.guild
	if arg != None:
		if profile_link.startswith('https://linkedin.com/in/') or profile_link.startswith('https://www.linkedin.com/in/'):
			embed = discord.Embed(
				title = 'Connect with ' + profile_name,
				description = profile_name + " is looking for connections on LinkedIn! [View their profile.](" + profile_link + ")",
				color = 0x32b3e2
			)
			embed.set_author(
				name = "LinkedIn Profile",
				url = profile_link,
				icon_url = "http://assets.stickpng.com/images/58e91afdeb97430e81906504.png"
			)
			if guild.icon_url == None:
				icon_url = 'http://assets.stickpng.com/images/58e91afdeb97430e81906504.png'
			else:
				icon_url = guild.icon_url
			embed.set_footer(text = 'Shared by ' + str(user) + ' in \'' + guild.name + '\'', icon_url = icon_url)
			embed.set_thumbnail(url = user.avatar_url)
			await ctx.send(embed = embed)

			await ctx.message.delete()
		else:
			await ctx.send(user.mention + ' Profile url must start with https://linkedin.com/in/. Example: .linkedin share https://linkedin.com/in/john-doe-1698165272/ John Doe')
	else:
		await ctx.send(user.mention + ' Please include profile name')


linkedinchannels = [731321297497227327, 731829355675648050, 730655769363742750]
@bot.command()
async def broadcast(ctx, link, *, arg = None):
	user = ctx.message.author
	profile_link = link
	profile_name = arg
	guild = ctx.message.guild
	if arg != None:
		if profile_link.startswith('https://linkedin.com/in/') or profile_link.startswith('https://www.linkedin.com/in/'):
			embed = discord.Embed(
				title = 'Connect with ' + profile_name,
				description = profile_name + " is looking for connections on LinkedIn! [View their profile.](" + profile_link + ")",
				color = 0x32b3e2
			)
			embed.set_author(
				name = "LinkedIn Profile",
				url = "https://www.linkedin.com/in/linus-kay/",
				icon_url = "https://techmarketingbuffalo.com/wp-content/uploads/2013/11/linkedin-logo-high-res-1254-1024x1024.jpg"
			)
			if guild.icon_url == None:
				icon_url = 'https://libus.xyz/i/6a952652591d013cadd6b11f623c6339/upload.jpg'
			else:
				icon_url = guild.icon_url
			embed.set_footer(text = 'Shared by ' + str(user) + ' in \'' + guild.name + '\'', icon_url = icon_url)
			embed.set_thumbnail(url = user.avatar_url)
			await ctx.send(embed = embed)

			for channelid in linkedinchannels:
				#ensure message isnt sent again in same channel
				if channelid != ctx.channel.id:
					embed = discord.Embed(
						title = 'Connect with ' + profile_name,
						description = profile_name + " is looking for connections on LinkedIn! [View their profile.](" + profile_link + ")",
						color = 0x32b3e2
					)
					embed.set_author(
						name = "LinkedIn Broadcast",
						url = "https://www.linkedin.com/in/linus-kay/",
						icon_url = "https://techmarketingbuffalo.com/wp-content/uploads/2013/11/linkedin-logo-high-res-1254-1024x1024.jpg"
					)
					if guild.icon_url == None:
						icon_url = 'https://libus.xyz/i/6a952652591d013cadd6b11f623c6339/upload.jpg'
					else:
						icon_url = guild.icon_url
					embed.set_footer(text = 'Shared by ' + str(user) + ' in \'' + guild.name + '\'', icon_url = icon_url)
					embed.set_thumbnail(url = user.avatar_url)
					channel = bot.get_channel(channelid)
					await channel.send(embed = embed)
			await ctx.message.delete()
		else:
			await ctx.send(user.mention + ' Profile url must start with https://linkedin.com/in/')
	else:
		await ctx.send(user.mention + ' Please include profile name')

@bot.command()
async def help(ctx):
	embed = discord.Embed(
		title = 'LinkedIn Bot Help',
		description = "**.linkedin share <profile url> <profile name>**\nShare your LinkedIn profile to this server. Profile URL must be a valid https://linkedin.com/in/ link. Example: .linkedin share https://linkedin.com/in/john-doe-1698165272/ John Doe\n\n**.linkedin broadcast <profile url> <profile name>**\nShare your LinkedIn profile to connected servers. \n- RMIT InfoTech\n- RISC",
		color = 0x32b3e2
	)
	await ctx.send(embed = embed)

load_dotenv('.env')
bot.run(os.getenv('BOT_TOKEN'))