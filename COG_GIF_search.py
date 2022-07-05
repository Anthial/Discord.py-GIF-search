import discord
from discord.ext import commands
import random
import giphy_client
from giphy_client.rest import ApiException 
import requests
import json


##assuming API keys are in a folder called keys and in files named based on which API key is being loaded. 
try:
    with open("keys/giphy", 'r') as key_g:
        giphy_api_key = key_g.readline()
    with open("keys/tenor", 'r') as key_t:
        tenor_api_key = key_t.readline()
except IOError:
    print('Something went wrong, please restart this bot instance.')
api_inst = giphy_client.DefaultApi()


class owlbot_gifs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Send 3 cute animal gifs
    @commands.command()
    async def eyebleach(self, ctx):
        await ctx.message.delete(delay=5)
        eyebleach = random.choice(['cute animals', 'eyebleach'])
        amount = 3
        counter = 1
        r_int = random.choice([1, 2, 3]),
        while counter <= r_int[0] :
            await random.choice([self.cat, self.dog, self.owl, self.frog])(ctx)
            counter += 1
        await self.random_gif_search(ctx, eyebleach, amount-r_int[0])

    #Send 1 cat gif
    @commands.command(aliases=["cats"])
    async def cat(self, ctx):
        cat = random.choice(['cat', 'kitten', 'cute cats', 'catto', 'funny cat', 'sad cat', 'funny kitten', 'funny kittens'])
        await self.random_gif_search(ctx, cat, 1)

    #Send 1 dog gif
    @commands.command(aliases=["dogs"])
    async def dog(self, ctx):
        dog = random.choice(['dog', 'doggo', 'cute dogs', 'puppy', 'cute puppy', 'funny dogs', 'funny dog', 'funny puppy'])
        await self.random_gif_search(ctx, dog, 1)

    #Send 1 cookie-related gif
    @commands.command(aliases=['cookie'])
    async def cookies(self, ctx):
        cookie = random.choice(['cookie', 'cookies', 'cake', 'baking'])
        await self.random_gif_search(ctx, cookie, 1)  

    @commands.command(aliases=['owls'])
    async def owl(self, ctx):
        owl = random.choice(['owl animal', 'cute owl animal', 'funny owl animal'])
        await self.random_gif_search(ctx, owl, 1) 

    @commands.command(aliases=['frogs'])
    async def frog(self, ctx):
        owl = random.choice(['frog animal', 'cute frog animal', 'funny frog animal', 'cute small frog', 'cute frog', 'cute small frogs', 'cute frogs'])
        await self.random_gif_search(ctx, owl, 1)   

    async def send_embed_gif(self, ctx, gif, text):
        await ctx.message.delete(delay=5)
        embed_var = discord.Embed()
        embed_var.set_footer(text=text)
        embed_var.set_image(url=gif)
        await ctx.send(embed=embed_var)
        

    async def tenor_search(self, message, amount):
        t_res = requests.get('https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s' % (message, tenor_api_key, 20))
        if t_res.status_code == 200:
            t_json = json.loads(t_res.content)
            gif = random.choices(t_json['results'], k= amount)
            return gif
        return False

    @commands.command()
    async def tenor(self, ctx, *, message):
        t_gif = await self.tenor_search(message, 1)
        if t_gif:
            t_gif = t_gif[0]['media'][0]['gif']['url']
            await self.send_embed_gif(ctx, t_gif, "Via Tenor")
        else:
            await ctx.send("No results found.")
    
    async def giphy_search(self, message, amount):
        try:
            g_res = api_inst.gifs_search_get(giphy_api_key, message, limit=20, rating='g')
            gif = random.choices(list(g_res.data), k = amount)
            return gif  
        except ApiException:
            return False

        
            
    @commands.command()
    async def giphy(self, ctx, *, message):
        g_gif = await self.giphy_search(message, 1)
        if g_gif:
            g_gif = g_gif[0].images.original.url
            await self.send_embed_gif(ctx, g_gif, "Powered By GIPHY")
        else:
            await ctx.send("No results found.")
    

    #Search Tenor or GIPHY for 20 gifs containing the search 'term' and embed and post 'amount' of randomly chosen gifs in the channel where the command that led into this function was posted.
    async def random_gif_search(self, ctx, term, amount):
        tenor = False
        if random.randint(0,1) == 1:
            tenor = True
        if tenor:    
            gif = await self.tenor_search(term, amount)
            if not gif:
                #attempt to make sure GIFs are posted even if Tenor API fails. 
                tenor = False
        #GIPHY search
        if not tenor:
            gif = await self.giphy_search(term, amount)
        for a in gif:
            if not tenor:
                a = a.images.original.url
                text = "Powered By GIPHY"
            else:
                a = a['media'][0]['gif']['url']
                text = "Via Tenor"
            await self.send_embed_gif(ctx, a, text)
        
def setup(bot):
    bot.add_cog(owlbot_gifs(bot))
