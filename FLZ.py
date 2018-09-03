import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands

Client = discord.Client()
bot_prefix = '/'
bot = commands.Bot(command_prefix=bot_prefix)
token = ("NDg1NTE2MTAxMzg0NTM2MDc0.DmxsmA.fg0pEFFJSNV1NLv-hSCltHaeV7U")

@bot.event
async def on_ready():
    print('Logged in as')
    print('Name: {}'.format(bot.user.name) + "#" + bot.user.discriminator)
    print('ID: {}'.format(bot.user.id))
    print('------')

@bot.command(pass_context=True, description="Invite me!")
async def invite(ctx):

    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='----FaTaLz Support Bot----')
    embed.add_field(name='Do you like this bot? Invite me to your server :D', value='- https://discordapp.com/oauth2/authorize?client_id=485516101384536074&scope=bot&permissions=8')
    await bot.send_message(author, embed=embed)



@bot.command(pass_context=True, description="Find the User's profile")
async def user(ctx):
    user = ctx.message.mentions[0]
    userjoinedat = str(user.joined_at).split('.', 1)[0]
    usercreatedat = str(user.created_at).split('.', 1)[0]

    userembed = discord.Embed(
        title="Username:",
        description=user.name,
        color=ctx.message.author.color
    )
    userembed.set_author(
        name="User Info"
    )
    userembed.add_field(
        name="Joined the server at: ",
        value=userjoinedat
    )
    userembed.add_field(
        name="User Created at:",
        value=usercreatedat
    )
    userembed.add_field(
        name="Discriminator:",
        value=user.discriminator
    )
    userembed.add_field(
        name="User ID:",
        value=user.id
    )
    userembed.add_field(
        name="Status:",
        value=user.status
    )
    userembed.add_field(
        name="Top Role:",
        value=user.top_role
    )

    if user.avatar_url:
        userembed.set_author(name=user.name, url=user.avatar_url)
        userembed.set_thumbnail(url=user.avatar_url)
        userembed.set_footer(text="Requested by {}".format(ctx.message.author.name) + "#{}".format(ctx.message.author.discriminator), icon_url='{}'.format(ctx.message.author.avatar_url))

    else:
        user.set_author(name=name)
    await bot.send_message(ctx.message.channel, embed=userembed)

@bot.command(pass_context=True, description="Check your server's info")
async def serverinfo(ctx):

    author  = ctx.message.author
    channel = ctx.message.channel

    isAdmin = author.permissions_in(channel).administrator

    if isAdmin:

        # Next, we get the server data and run that into our command!

        embed = discord.Embed(title="{}'s Info".format(ctx.message.server.name), description="A brief information about this server", color=ctx.message.author.color)
        embed.add_field(name="Name", value=ctx.message.server.name)
        embed.add_field(name="Server ID", value="`{}`".format(ctx.message.server.id))
        embed.add_field(name="Members", value="{}".format(len(ctx.message.server.members)))
        embed.add_field(name="Roles", value='{}'.format(len(ctx.message.server.roles)))
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        embed.set_footer(text="Requested by {}".format(ctx.message.author.name) + "#{}".format(ctx.message.author.discriminator), icon_url='{}'.format(ctx.message.author.avatar_url))

        # And finally, we send the message after the command is used!

        await bot.say(embed=embed)
    else:
        await bot.say("I can't let you view the server's information :( Sorry")

bot.run(token)
