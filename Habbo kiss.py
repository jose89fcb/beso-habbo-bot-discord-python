import urllib
import json
import requests
import discord
from discord.ext import commands
import datetime
import io
 
from urllib import parse, request
from PIL import Image, ImageDraw, ImageFont, ImageFile
import time


with open("configuracion.json") as f:
    config = json.load(f)

bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help

@bot.command()
async def beso(ctx,  keko1, keko2, lugar):
    await ctx.message.delete()
    await ctx.send("Generando beso💕...", delete_after=0)
    time.sleep(3)
    
    response = requests.get(f"https://www.habbo.es/api/public/users?name={keko1}")
    response1 = requests.get(f"https://www.habbo.es/api/public/users?name={keko2}")
    
    habbo = response.json()['figureString']
    habbo1 = response1.json()['figureString']

   
    

    
    
   
    
    url = "https://www.habbo.com/habbo-imaging/avatarimage?size=l&figure="+ habbo +"&direction=1&head_direction=1&gesture=eyb&size=l"
    img1 = Image.open(io.BytesIO(requests.get(url).content))
    img1 = img1.resize((64,110), Image.Resampling.LANCZOS)#tamaño del keko 1
    
    url1 = "https://www.habbo.com/habbo-imaging/avatarimage?size=l&figure="+ habbo1 +"&direction=5&head_direction=6&gesture=eyb&size=l"
    habbol = Image.open(io.BytesIO(requests.get(url1).content))
    habbol = habbol.resize((64,110), Image.Resampling.LANCZOS)#tamaño del keko 2


    
    


    

   

    

    
    
    



    img2 = img1.copy()
    
    
    
    img1 = Image.open(r"imagenes/" + lugar + ".png").convert("RGBA") #imagen  -> arenaplaya barco carretera desierto futbol hierba
    img1.paste(img2,(20,0), mask = img2) #Posicion del keko 1
    
    ###
    

    img1.paste(habbol,(44,0), mask = habbol) #Posicion del keko 2
    
  
 
    
    

 
    
    

    




    

    
    
    
   
    
   
       


      
    
       
      

      
    
       
            
        
        
        
       
        
    with io.BytesIO() as image_binary:
        img1.save(image_binary, 'PNG')
        image_binary.seek(0)

        await ctx.send(file=discord.File(fp=image_binary, filename='keko.png'))
         
        
        
        
        


@bot.event
async def on_ready():
    print("BOT listo!")
    
bot.run(config["tokendiscord"])   