# Discord.py-GIF-search
A Discord.py cog to allow quick searches utilising Giphy and Tenor

**Setup**
1. Have a Discord.py bot (Quickstart available at https://discordpy.readthedocs.io/en/stable/quickstart.html)
2. Assuming you're using the minimal quickstart bot, place the cog in the same directory as your bot. 
3. Add a folder named "keys" into the same directory as your bot.
4. Add a file named "giphy" into the folder named "keys" and add your Giphy API key to that file (Giphy setup: https://developers.giphy.com/docs/api#quick-start-guide)
5. Add a file named "tenor" into the folder named "keys" and add your Tenor API key to that file (Tenor setup: https://tenor.com/gifapi/documentation#quickstart-setup)
6. Add    ```client.load_extension('COG_GIF_search')``` somewhere in the code of your bot.
7. Run the minimal bot.

**Commands**
* ```!cat``` - Posts an embed of a random cat using either Giphy or Tenor
* ```!dog``` - Posts an embed of a random dog using either Giphy or Tenor
* ```!owl``` - Posts an embed of a random owl using either Giphy or Tenor
* ```!frog``` - Posts an embed of a random frog using either Giphy or Tenor
* ```!eyebleach``` - Posts 3 embedded images of, hopefully, cute things
* ```!cookies``` - Posts an embed of, hopefully, some random pastry using either Giphy or Tenor
* ```!tenor [search terms]``` - Posts an embed of a random gif related to the search terms using Tenor
* ```!giphy [search terms]``` - Posts an embed of a random gif related to the search terms using Giphy

