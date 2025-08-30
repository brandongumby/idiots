import discord
from util import embeds, config, myviews, achievements
from bosses.vorago import vmenu, hmvmenu
from bosses.raids import raidsmenu
from bosses.aod import aodmenu, aod8menu, aod5menu
from bosses.vorkath import vorkmenu
from bosses.rots import rotsmenu
from bosses.kerapac import keramenu
from bosses.solak import solakmenu
from bosses.croesus import cromenu
from bosses.zammy import zammymenu
from bosses.sanctum import sormenu
from bosses.gate import goemenu
from bosses.eds import edsmenu
from bosses.amascut import amascutmenu, hmamascutmenu
from discord.ui import View
import copy



#region  POFDropdown
class POFDropdown(discord.ui.Select):
        def __init__(self, client):
            self.client = client
            options=[
                discord.SelectOption(label="Rabbit"),
                discord.SelectOption(label="Chicken"),
                discord.SelectOption(label="Sheep"),
                discord.SelectOption(label="Cow"),
                discord.SelectOption(label="Chinchompa"),
                discord.SelectOption(label="Spider"),
                discord.SelectOption(label="Yak"),
                discord.SelectOption(label="Zygomite"),
                discord.SelectOption(label="Dragon"),
                discord.SelectOption(label="Frog"),
                discord.SelectOption(label="Jadinko"),
                discord.SelectOption(label="Salamander"),
                discord.SelectOption(label="Varanusaur"),
                discord.SelectOption(label="Arcane Apoterrasaur"),
                discord.SelectOption(label="Brutish Dinosaur"),
                discord.SelectOption(label="Scimitops"),
                discord.SelectOption(label="Bagrada Rex"),
                discord.SelectOption(label="Spicati Apoterrasaur"),
                discord.SelectOption(label="Asciatops"),
                discord.SelectOption(label="Corbicula Rex"),
                discord.SelectOption(label="Oculi Apoterrasaur"),
                discord.SelectOption(label="Malletops"),
                discord.SelectOption(label="Pavosaurus Rex"),

            ]

            super().__init__(placeholder="Select an animal to check the status of", options=options, min_values=1, max_values=1, custom_id="POF_dropdown")

        async def callback(self, interaction: discord.Interaction):

#region rabbit            
            if self.values[0] == "Rabbit": 
                async with self.client.db.cursor() as cursor:
                    await cursor.execute("SELECT breed1, traita1, traita2, traita3, breed2, traitb1, traitb2, traitb3, owner, lender FROM animals WHERE animal = ? AND guild = ?", ("rabbit", interaction.guild.id,))

                    animal_data = await cursor.fetchone()
                    if animal_data:
                        breed1, trait_a1, trait_a2, trait_a3, breed2, trait_b1, trait_b2, trait_b3, owner, lender = animal_data
                    
                        checkpofembed = discord.Embed(title=f"Rabbit Pair", description=f"")
                        checkpofembed.set_thumbnail(url="https://runescape.wiki/images/Jackalope.png?bc6dc")
                        checkpofembed.add_field(name=f"First Rabbit", value=f"Breed: **{breed1}**\nTrait 1: **{trait_a1}**\nTrait 2: **{trait_a2}**\nTrait 3: **{trait_a3}**", inline=True)
                        checkpofembed.add_field(name=f"Second Rabbit", value=f"Breed: **{breed2}**\nTrait 1: **{trait_b1}**\nTrait 2: **{trait_b2}**\nTrait 3: **{trait_b3}**", inline=True)
                        checkpofembed.add_field(name="", value=f"Original Owner: **{owner}** | Lender: **{lender}**", inline=False)
                        await interaction.response.send_message(embed=checkpofembed, ephemeral=True)

                    else:
                        await interaction.response.send_message("We currently don't have any Rabbits", ephemeral=True)
#endregion

#region chickens            
            if self.values[0] == "Chicken": 
                async with self.client.db.cursor() as cursor:
                    await cursor.execute("SELECT breed1, traita1, traita2, traita3, breed2, traitb1, traitb2, traitb3, owner, lender FROM animals WHERE animal = ? AND guild = ?", ("chicken", interaction.guild.id,))

                    animal_data = await cursor.fetchone()
                    if animal_data:
                        breed1, trait_a1, trait_a2, trait_a3, breed2, trait_b1, trait_b2, trait_b3, owner, lender = animal_data
                    
                        checkpofembed = discord.Embed(title=f"Chicken Pair", description=f"") #Original Owner: **{owner}**
                        checkpofembed.set_thumbnail(url="https://runescape.wiki/images/Lizard_chicken.png?122d5")
                        checkpofembed.add_field(name=f"First Chicken", value=f"Breed: **{breed1}**\nTrait 1: **{trait_a1}**\nTrait 2: **{trait_a2}**\nTrait 3: **{trait_a3}**", inline=True)
                        checkpofembed.add_field(name=f"Second Chicken", value=f"Breed: **{breed2}**\nTrait 1: **{trait_b1}**\nTrait 2: **{trait_b2}**\nTrait 3: **{trait_b3}**", inline=True)
                        checkpofembed.add_field(name="", value=f"Original Owner: **{owner}** | Lender: **{lender}**", inline=False)
                        await interaction.response.send_message(embed=checkpofembed, ephemeral=True)

                    else:
                        await interaction.response.send_message("We currently don't have any Chickens", ephemeral=True)
#endregion

#region sheep            
            if self.values[0] == "Sheep": 
                async with self.client.db.cursor() as cursor:
                    await cursor.execute("SELECT breed1, traita1, traita2, traita3, breed2, traitb1, traitb2, traitb3, owner, lender FROM animals WHERE animal = ? AND guild = ?", ("sheep", interaction.guild.id,))

                    animal_data = await cursor.fetchone()
                    if animal_data:
                        breed1, trait_a1, trait_a2, trait_a3, breed2, trait_b1, trait_b2, trait_b3, owner, lender = animal_data
                    
                        checkpofembed = discord.Embed(title=f"Sheep Pair", description=f"")
                        checkpofembed.set_thumbnail(url="https://runescape.wiki/images/thumb/Golden_ewe.png/800px-Golden_ewe.png?efcd1")
                        checkpofembed.add_field(name=f"First Sheep", value=f"Breed: **{breed1}**\nTrait 1: **{trait_a1}**\nTrait 2: **{trait_a2}**\nTrait 3: **{trait_a3}**", inline=True)
                        checkpofembed.add_field(name=f"Second Sheep", value=f"Breed: **{breed2}**\nTrait 1: **{trait_b1}**\nTrait 2: **{trait_b2}**\nTrait 3: **{trait_b3}**", inline=True)
                        checkpofembed.add_field(name="", value=f"Original Owner: **{owner}** | Lender: **{lender}**", inline=False)
                        await interaction.response.send_message(embed=checkpofembed, ephemeral=True)

                    else:
                        await interaction.response.send_message("We currently don't have any Sheep", ephemeral=True)
#endregion

#region cow           
            if self.values[0] == "Cow": 
                async with self.client.db.cursor() as cursor:
                    await cursor.execute("SELECT breed1, traita1, traita2, traita3, breed2, traitb1, traitb2, traitb3, owner, lender FROM animals WHERE animal = ? AND guild = ?", ("cow", interaction.guild.id,))

                    animal_data = await cursor.fetchone()
                    if animal_data:
                        breed1, trait_a1, trait_a2, trait_a3, breed2, trait_b1, trait_b2, trait_b3, owner, lender = animal_data
                    
                        checkpofembed = discord.Embed(title=f"Cow Pair", description=f"")
                        checkpofembed.set_thumbnail(url="https://runescape.wiki/images/Harlequin_cow.png?5b536")
                        checkpofembed.add_field(name=f"First Cow", value=f"Breed: **{breed1}**\nTrait 1: **{trait_a1}**\nTrait 2: **{trait_a2}**\nTrait 3: **{trait_a3}**", inline=True)
                        checkpofembed.add_field(name=f"Second Cow", value=f"Breed: **{breed2}**\nTrait 1: **{trait_b1}**\nTrait 2: **{trait_b2}**\nTrait 3: **{trait_b3}**", inline=True)
                        checkpofembed.add_field(name="", value=f"Original Owner: **{owner}** | Lender: **{lender}**", inline=False)
                        await interaction.response.send_message(embed=checkpofembed, ephemeral=True)

                    else:
                        await interaction.response.send_message("We currently don't have any Cows", ephemeral=True)
#endregion

#region chinchompas           
            if self.values[0] == "Chinchompa": 
                async with self.client.db.cursor() as cursor:
                    await cursor.execute("SELECT breed1, traita1, traita2, traita3, breed2, traitb1, traitb2, traitb3, owner, lender FROM animals WHERE animal = ? AND guild = ?", ("chinchompa", interaction.guild.id,))

                    animal_data = await cursor.fetchone()
                    if animal_data:
                        breed1, trait_a1, trait_a2, trait_a3, breed2, trait_b1, trait_b2, trait_b3, owner, lender = animal_data
                    
                        checkpofembed = discord.Embed(title=f"Chinchompa Pair", description=f"")
                        checkpofembed.set_thumbnail(url="https://runescape.wiki/images/Golden_chinchompa_%28NPC%29.png?33001")
                        checkpofembed.add_field(name=f"First Chinchompa", value=f"Breed: **{breed1}**\nTrait 1: **{trait_a1}**\nTrait 2: **{trait_a2}**\nTrait 3: **{trait_a3}**", inline=True)
                        checkpofembed.add_field(name=f"Second Chinchompa", value=f"Breed: **{breed2}**\nTrait 1: **{trait_b1}**\nTrait 2: **{trait_b2}**\nTrait 3: **{trait_b3}**", inline=True)
                        checkpofembed.add_field(name="", value=f"Original Owner: **{owner}** | Lender: **{lender}**", inline=False)
                        await interaction.response.send_message(embed=checkpofembed, ephemeral=True)

                    else:
                        await interaction.response.send_message("We currently don't have any Chinchompas", ephemeral=True)
#endregion

#region spiders           
            if self.values[0] == "Spider": 
                async with self.client.db.cursor() as cursor:
                    await cursor.execute("SELECT breed1, traita1, traita2, traita3, breed2, traitb1, traitb2, traitb3, owner, lender FROM animals WHERE animal = ? AND guild = ?", ("spider", interaction.guild.id,))

                    animal_data = await cursor.fetchone()
                    if animal_data:
                        breed1, trait_a1, trait_a2, trait_a3, breed2, trait_b1, trait_b2, trait_b3, owner, lender = animal_data
                    
                        checkpofembed = discord.Embed(title=f"Spider Pair", description=f"")
                        checkpofembed.set_thumbnail(url="https://runescape.wiki/images/Araxyte_spider_%28NPC%29.png?4877b")
                        checkpofembed.add_field(name=f"First Spider", value=f"Breed: **{breed1}**\nTrait 1: **{trait_a1}**\nTrait 2: **{trait_a2}**\nTrait 3: **{trait_a3}**", inline=True)
                        checkpofembed.add_field(name=f"Second Spider", value=f"Breed: **{breed2}**\nTrait 1: **{trait_b1}**\nTrait 2: **{trait_b2}**\nTrait 3: **{trait_b3}**", inline=True)
                        checkpofembed.add_field(name="", value=f"Original Owner: **{owner}** | Lender: **{lender}**", inline=False)
                        await interaction.response.send_message(embed=checkpofembed, ephemeral=True)

                    else:
                        await interaction.response.send_message("We currently don't have any Spiders", ephemeral=True)
#endregion

#region yak           
            if self.values[0] == "Yak": 
                async with self.client.db.cursor() as cursor:
                    await cursor.execute("SELECT breed1, traita1, traita2, traita3, breed2, traitb1, traitb2, traitb3, owner, lender FROM animals WHERE animal = ? AND guild = ?", ("yak", interaction.guild.id,))

                    animal_data = await cursor.fetchone()
                    if animal_data:
                        breed1, trait_a1, trait_a2, trait_a3, breed2, trait_b1, trait_b2, trait_b3, owner, lender = animal_data
                    
                        checkpofembed = discord.Embed(title=f"Yak Pair", description=f"")
                        checkpofembed.set_thumbnail(url="https://runescape.wiki/images/Sacred_yak.png?70ff2")
                        checkpofembed.add_field(name=f"First Yak", value=f"Breed: **{breed1}**\nTrait 1: **{trait_a1}**\nTrait 2: **{trait_a2}**\nTrait 3: **{trait_a3}**", inline=True)
                        checkpofembed.add_field(name=f"Second Yak", value=f"Breed: **{breed2}**\nTrait 1: **{trait_b1}**\nTrait 2: **{trait_b2}**\nTrait 3: **{trait_b3}**", inline=True)
                        checkpofembed.add_field(name="", value=f"Original Owner: **{owner}** | Lender: **{lender}**", inline=False)
                        await interaction.response.send_message(embed=checkpofembed, ephemeral=True)

                    else:
                        await interaction.response.send_message("We currently don't have any Yaks", ephemeral=True)
#endregion

#region zygomites           
            if self.values[0] == "Zygomite": 
                async with self.client.db.cursor() as cursor:
                    await cursor.execute("SELECT breed1, traita1, traita2, traita3, breed2, traitb1, traitb2, traitb3, owner, lender FROM animals WHERE animal = ? AND guild = ?", ("zygomite", interaction.guild.id,))

                    animal_data = await cursor.fetchone()
                    if animal_data:
                        breed1, trait_a1, trait_a2, trait_a3, breed2, trait_b1, trait_b2, trait_b3, owner, lender = animal_data
                    
                        checkpofembed = discord.Embed(title=f"Zygomite Pair", description=f"")
                        checkpofembed.set_thumbnail(url="https://runescape.wiki/images/Magical_zygomite_%28NPC%29.png?04b6b")
                        checkpofembed.add_field(name=f"First Zygomite", value=f"Breed: **{breed1}**\nTrait 1: **{trait_a1}**\nTrait 2: **{trait_a2}**\nTrait 3: **{trait_a3}**", inline=True)
                        checkpofembed.add_field(name=f"Second Zygomite", value=f"Breed: **{breed2}**\nTrait 1: **{trait_b1}**\nTrait 2: **{trait_b2}**\nTrait 3: **{trait_b3}**", inline=True)
                        checkpofembed.add_field(name="", value=f"Original Owner: **{owner}** | Lender: **{lender}**", inline=False)
                        await interaction.response.send_message(embed=checkpofembed, ephemeral=True)

                    else:
                        await interaction.response.send_message("We currently don't have any Zygomites", ephemeral=True)
#endregion

#region dragons           
            if self.values[0] == "Dragon": 
                async with self.client.db.cursor() as cursor:
                    await cursor.execute("SELECT breed1, traita1, traita2, traita3, breed2, traitb1, traitb2, traitb3, owner, lender FROM animals WHERE animal = ? AND guild = ?", ("dragon", interaction.guild.id,))

                    animal_data = await cursor.fetchone()
                    if animal_data:
                        breed1, trait_a1, trait_a2, trait_a3, breed2, trait_b1, trait_b2, trait_b3, owner, lender = animal_data
                    
                        checkpofembed = discord.Embed(title=f"Dragon Pair", description=f"")
                        checkpofembed.set_thumbnail(url="https://runescape.wiki/images/Royal_dragon_%28NPC%29.png?9f33a")
                        checkpofembed.add_field(name=f"First Dragon", value=f"Breed: **{breed1}**\nTrait 1: **{trait_a1}**\nTrait 2: **{trait_a2}**\nTrait 3: **{trait_a3}**", inline=True)
                        checkpofembed.add_field(name=f"Second Dragon", value=f"Breed: **{breed2}**\nTrait 1: **{trait_b1}**\nTrait 2: **{trait_b2}**\nTrait 3: **{trait_b3}**", inline=True)
                        checkpofembed.add_field(name="", value=f"Original Owner: **{owner}** | Lender: **{lender}**", inline=False)
                        await interaction.response.send_message(embed=checkpofembed, ephemeral=True)

                    else:
                        await interaction.response.send_message("We currently don't have any Dragons", ephemeral=True)
#endregion

#region frogs           
            if self.values[0] == "Frog": 
                async with self.client.db.cursor() as cursor:
                    await cursor.execute("SELECT breed1, traita1, traita2, traita3, breed2, traitb1, traitb2, traitb3, owner, lender FROM animals WHERE animal = ? AND guild = ?", ("frog", interaction.guild.id,))

                    animal_data = await cursor.fetchone()
                    if animal_data:
                        breed1, trait_a1, trait_a2, trait_a3, breed2, trait_b1, trait_b2, trait_b3, owner, lender = animal_data
                    
                        checkpofembed = discord.Embed(title=f"Frog Pair", description=f"")
                        checkpofembed.set_thumbnail(url="https://runescape.wiki/images/Cactoad_%28grown%29.png?7b611")
                        checkpofembed.add_field(name=f"First Frog", value=f"Breed: **{breed1}**\nTrait 1: **{trait_a1}**\nTrait 2: **{trait_a2}**\nTrait 3: **{trait_a3}**", inline=True)
                        checkpofembed.add_field(name=f"Second Frog", value=f"Breed: **{breed2}**\nTrait 1: **{trait_b1}**\nTrait 2: **{trait_b2}**\nTrait 3: **{trait_b3}**", inline=True)
                        checkpofembed.add_field(name="", value=f"Original Owner: **{owner}** | Lender: **{lender}**", inline=False)
                        await interaction.response.send_message(embed=checkpofembed, ephemeral=True)

                    else:
                        await interaction.response.send_message("We currently don't have any Frogs", ephemeral=True)
#endregion

#region jadinko           
            if self.values[0] == "Jadinko": 
                async with self.client.db.cursor() as cursor:
                    await cursor.execute("SELECT breed1, traita1, traita2, traita3, breed2, traitb1, traitb2, traitb3, owner, lender FROM animals WHERE animal = ? AND guild = ?", ("jadinko", interaction.guild.id,))

                    animal_data = await cursor.fetchone()
                    if animal_data:
                        breed1, trait_a1, trait_a2, trait_a3, breed2, trait_b1, trait_b2, trait_b3, owner, lender = animal_data
                    
                        checkpofembed = discord.Embed(title=f"Jadinko Pair", description=f"")
                        checkpofembed.set_thumbnail(url="https://runescape.wiki/images/Luminous_jadinko.png?569f9")
                        checkpofembed.add_field(name=f"First Jadinko", value=f"Breed: **{breed1}**\nTrait 1: **{trait_a1}**\nTrait 2: **{trait_a2}**\nTrait 3: **{trait_a3}**", inline=True)
                        checkpofembed.add_field(name=f"Second Jadinko", value=f"Breed: **{breed2}**\nTrait 1: **{trait_b1}**\nTrait 2: **{trait_b2}**\nTrait 3: **{trait_b3}**", inline=True)
                        checkpofembed.add_field(name="", value=f"Original Owner: **{owner}** | Lender: **{lender}**", inline=False)
                        await interaction.response.send_message(embed=checkpofembed, ephemeral=True)

                    else:
                        await interaction.response.send_message("We currently don't have any Jadinko", ephemeral=True)
#endregion

#region salamander           
            if self.values[0] == "Salamander": 
                async with self.client.db.cursor() as cursor:
                    await cursor.execute("SELECT breed1, traita1, traita2, traita3, breed2, traitb1, traitb2, traitb3, owner, lender FROM animals WHERE animal = ? AND guild = ?", ("salamander", interaction.guild.id,))

                    animal_data = await cursor.fetchone()
                    if animal_data:
                        breed1, trait_a1, trait_a2, trait_a3, breed2, trait_b1, trait_b2, trait_b3, owner, lender = animal_data
                    
                        checkpofembed = discord.Embed(title=f"Salamander Pair", description=f"")
                        checkpofembed.set_thumbnail(url="https://runescape.wiki/images/Wytchfire_salamander.png?d15a0")
                        checkpofembed.add_field(name=f"First Salamander", value=f"Breed: **{breed1}**\nTrait 1: **{trait_a1}**\nTrait 2: **{trait_a2}**\nTrait 3: **{trait_a3}**", inline=True)
                        checkpofembed.add_field(name=f"Second Salamander", value=f"Breed: **{breed2}**\nTrait 1: **{trait_b1}**\nTrait 2: **{trait_b2}**\nTrait 3: **{trait_b3}**", inline=True)
                        checkpofembed.add_field(name="", value=f"Original Owner: **{owner}** | Lender: **{lender}**", inline=False)
                        await interaction.response.send_message(embed=checkpofembed, ephemeral=True)

                    else:
                        await interaction.response.send_message("We currently don't have any Salamanders", ephemeral=True)
#endregion

#region varanusaur           
            if self.values[0] == "Varanusaur": 
                async with self.client.db.cursor() as cursor:
                    await cursor.execute("SELECT breed1, traita1, traita2, traita3, breed2, traitb1, traitb2, traitb3, owner, lender FROM animals WHERE animal = ? AND guild = ?", ("varanusaur", interaction.guild.id,))

                    animal_data = await cursor.fetchone()
                    if animal_data:
                        breed1, trait_a1, trait_a2, trait_a3, breed2, trait_b1, trait_b2, trait_b3, owner, lender = animal_data
                    
                        checkpofembed = discord.Embed(title=f"Varanusaur Pair", description=f"")
                        checkpofembed.set_thumbnail(url="https://runescape.wiki/images/Hypnotic_dinosaur_%28grown%29.png?e58e5")
                        checkpofembed.add_field(name=f"First Varanusaur", value=f"Breed: **{breed1}**\nTrait 1: **{trait_a1}**\nTrait 2: **{trait_a2}**\nTrait 3: **{trait_a3}**", inline=True)
                        checkpofembed.add_field(name=f"Second Varanusaur", value=f"Breed: **{breed2}**\nTrait 1: **{trait_b1}**\nTrait 2: **{trait_b2}**\nTrait 3: **{trait_b3}**", inline=True)
                        checkpofembed.add_field(name="", value=f"Original Owner: **{owner}** | Lender: **{lender}**", inline=False)
                        await interaction.response.send_message(embed=checkpofembed, ephemeral=True)

                    else:
                        await interaction.response.send_message("We currently don't have any Varanusaurs", ephemeral=True)
#endregion

#region Arcane apoterrasaurs          
            if self.values[0] == "Arcane Apoterrasaur": 
                async with self.client.db.cursor() as cursor:
                    await cursor.execute("SELECT breed1, traita1, traita2, traita3, breed2, traitb1, traitb2, traitb3, owner, lender FROM animals WHERE animal = ? AND guild = ?", ("arcane apoterrasaur", interaction.guild.id,))

                    animal_data = await cursor.fetchone()
                    if animal_data:
                        breed1, trait_a1, trait_a2, trait_a3, breed2, trait_b1, trait_b2, trait_b3, owner, lender = animal_data
                    
                        checkpofembed = discord.Embed(title=f"Arcane Apoterrasaur Pair", description=f"")
                        checkpofembed.set_thumbnail(url="https://runescape.wiki/images/Arcane_apoterrasaur_lucidum_%28grown%29.png?2d48c")
                        checkpofembed.add_field(name=f"First Arcane Apoterrasaur", value=f"Breed: **{breed1}**\nTrait 1: **{trait_a1}**\nTrait 2: **{trait_a2}**\nTrait 3: **{trait_a3}**", inline=True)
                        checkpofembed.add_field(name=f"Second Arcane Apoterrasaur", value=f"Breed: **{breed2}**\nTrait 1: **{trait_b1}**\nTrait 2: **{trait_b2}**\nTrait 3: **{trait_b3}**", inline=True)
                        checkpofembed.add_field(name="", value=f"Original Owner: **{owner}** | Lender: **{lender}**", inline=False)
                        await interaction.response.send_message(embed=checkpofembed, ephemeral=True)

                    else:
                        await interaction.response.send_message("We currently don't have any Arcane Apoterrasaurs", ephemeral=True)
#endregion

#region Brutish Dinosaur          
            if self.values[0] == "Brutish Dinosaur": 
                async with self.client.db.cursor() as cursor:
                    await cursor.execute("SELECT breed1, traita1, traita2, traita3, breed2, traitb1, traitb2, traitb3, owner, lender FROM animals WHERE animal = ? AND guild = ?", ("brutish dinosaur", interaction.guild.id,))

                    animal_data = await cursor.fetchone()
                    if animal_data:
                        breed1, trait_a1, trait_a2, trait_a3, breed2, trait_b1, trait_b2, trait_b3, owner, lender = animal_data
                    
                        checkpofembed = discord.Embed(title=f"Brutish Dinosaur Pair", description=f"")
                        checkpofembed.set_thumbnail(url="https://runescape.wiki/images/Magnificent_dinosaur.png?cedcf")
                        checkpofembed.add_field(name=f"First Brutish Dinosaur", value=f"Breed: **{breed1}**\nTrait 1: **{trait_a1}**\nTrait 2: **{trait_a2}**\nTrait 3: **{trait_a3}**", inline=True)
                        checkpofembed.add_field(name=f"Second Brutish Dinosaur", value=f"Breed: **{breed2}**\nTrait 1: **{trait_b1}**\nTrait 2: **{trait_b2}**\nTrait 3: **{trait_b3}**", inline=True)
                        checkpofembed.add_field(name="", value=f"Original Owner: **{owner}** | Lender: **{lender}**", inline=False)
                        await interaction.response.send_message(embed=checkpofembed, ephemeral=True)

                    else:
                        await interaction.response.send_message("We currently don't have any Brutish Dinosaurs", ephemeral=True)
#endregion

#region Scimitops         
            if self.values[0] == "Scimitops": 
                async with self.client.db.cursor() as cursor:
                    await cursor.execute("SELECT breed1, traita1, traita2, traita3, breed2, traitb1, traitb2, traitb3, owner, lender FROM animals WHERE animal = ? AND guild = ?", ("scimitops", interaction.guild.id,))

                    animal_data = await cursor.fetchone()
                    if animal_data:
                        breed1, trait_a1, trait_a2, trait_a3, breed2, trait_b1, trait_b2, trait_b3, owner, lender = animal_data
                    
                        checkpofembed = discord.Embed(title=f"Scimitops Pair", description=f"")
                        checkpofembed.set_thumbnail(url="https://runescape.wiki/images/Scimitops_lucidum_%28grown%29.png?3f540")
                        checkpofembed.add_field(name=f"First Scimitops", value=f"Breed: **{breed1}**\nTrait 1: **{trait_a1}**\nTrait 2: **{trait_a2}**\nTrait 3: **{trait_a3}**", inline=True)
                        checkpofembed.add_field(name=f"Second Scimitops", value=f"Breed: **{breed2}**\nTrait 1: **{trait_b1}**\nTrait 2: **{trait_b2}**\nTrait 3: **{trait_b3}**", inline=True)
                        checkpofembed.add_field(name="", value=f"Original Owner: **{owner}** | Lender: **{lender}**", inline=False)
                        await interaction.response.send_message(embed=checkpofembed, ephemeral=True)

                    else:
                        await interaction.response.send_message("We currently don't have any Scimitops", ephemeral=True)
#endregion

#region Bagrada Rex         
            if self.values[0] == "Bagrada Rex": 
                async with self.client.db.cursor() as cursor:
                    await cursor.execute("SELECT breed1, traita1, traita2, traita3, breed2, traitb1, traitb2, traitb3, owner, lender FROM animals WHERE animal = ? AND guild = ?", ("bagrada rex", interaction.guild.id,))

                    animal_data = await cursor.fetchone()
                    if animal_data:
                        breed1, trait_a1, trait_a2, trait_a3, breed2, trait_b1, trait_b2, trait_b3, owner, lender = animal_data
                    
                        checkpofembed = discord.Embed(title=f"Bagrada Rex Pair", description=f"")
                        checkpofembed.set_thumbnail(url="https://runescape.wiki/images/Bagrada_lucidum_%28grown%29.png?57409")
                        checkpofembed.add_field(name=f"First Bagrada Rex", value=f"Breed: **{breed1}**\nTrait 1: **{trait_a1}**\nTrait 2: **{trait_a2}**\nTrait 3: **{trait_a3}**", inline=True)
                        checkpofembed.add_field(name=f"Second Bagrada Rex", value=f"Breed: **{breed2}**\nTrait 1: **{trait_b1}**\nTrait 2: **{trait_b2}**\nTrait 3: **{trait_b3}**", inline=True)
                        checkpofembed.add_field(name="", value=f"Original Owner: **{owner}** | Lender: **{lender}**", inline=False)
                        await interaction.response.send_message(embed=checkpofembed, ephemeral=True)

                    else:
                        await interaction.response.send_message("We currently don't have any Bagrada Rex", ephemeral=True)
#endregion

#region Spicati Apoterrasaur        
            if self.values[0] == "Spicati Apoterrasaur": 
                async with self.client.db.cursor() as cursor:
                    await cursor.execute("SELECT breed1, traita1, traita2, traita3, breed2, traitb1, traitb2, traitb3, owner, lender FROM animals WHERE animal = ? AND guild = ?", ("spicati apoterrasaur", interaction.guild.id,))

                    animal_data = await cursor.fetchone()
                    if animal_data:
                        breed1, trait_a1, trait_a2, trait_a3, breed2, trait_b1, trait_b2, trait_b3, owner, lender = animal_data
                    
                        checkpofembed = discord.Embed(title=f"Spicati Apoterrasaur Pair", description=f"")
                        checkpofembed.set_thumbnail(url="https://runescape.wiki/images/thumb/Spicati_apoterrasaur_lucidum_%28grown%29.png/800px-Spicati_apoterrasaur_lucidum_%28grown%29.png?cb315")
                        checkpofembed.add_field(name=f"First Spicati Apoterrasaur", value=f"Breed: **{breed1}**\nTrait 1: **{trait_a1}**\nTrait 2: **{trait_a2}**\nTrait 3: **{trait_a3}**", inline=True)
                        checkpofembed.add_field(name=f"Second Spicati Apoterrasaur", value=f"Breed: **{breed2}**\nTrait 1: **{trait_b1}**\nTrait 2: **{trait_b2}**\nTrait 3: **{trait_b3}**", inline=True)
                        checkpofembed.add_field(name="", value=f"Original Owner: **{owner}** | Lender: **{lender}**", inline=False)
                        await interaction.response.send_message(embed=checkpofembed, ephemeral=True)

                    else:
                        await interaction.response.send_message("We currently don't have any Spicati Apoterrasaurs", ephemeral=True)
#endregion

#region Asciatops        
            if self.values[0] == "Asciatops": 
                async with self.client.db.cursor() as cursor:
                    await cursor.execute("SELECT breed1, traita1, traita2, traita3, breed2, traitb1, traitb2, traitb3, owner, lender FROM animals WHERE animal = ? AND guild = ?", ("asciatops", interaction.guild.id,))

                    animal_data = await cursor.fetchone()
                    if animal_data:
                        breed1, trait_a1, trait_a2, trait_a3, breed2, trait_b1, trait_b2, trait_b3, owner, lender = animal_data
                    
                        checkpofembed = discord.Embed(title=f"Asciatops Pair", description=f"")
                        checkpofembed.set_thumbnail(url="https://runescape.wiki/images/Asciatops_lucidum.png?63326")
                        checkpofembed.add_field(name=f"First Asciatops", value=f"Breed: **{breed1}**\nTrait 1: **{trait_a1}**\nTrait 2: **{trait_a2}**\nTrait 3: **{trait_a3}**", inline=True)
                        checkpofembed.add_field(name=f"Second Asciatops", value=f"Breed: **{breed2}**\nTrait 1: **{trait_b1}**\nTrait 2: **{trait_b2}**\nTrait 3: **{trait_b3}**", inline=True)
                        checkpofembed.add_field(name="", value=f"Original Owner: **{owner}** | Lender: **{lender}**", inline=False)
                        await interaction.response.send_message(embed=checkpofembed, ephemeral=True)

                    else:
                        await interaction.response.send_message("We currently don't have any Asciatops", ephemeral=True)
#endregion

#region Corbicula Rex        
            if self.values[0] == "Corbicula Rex": 
                async with self.client.db.cursor() as cursor:
                    await cursor.execute("SELECT breed1, traita1, traita2, traita3, breed2, traitb1, traitb2, traitb3, owner, lender FROM animals WHERE animal = ? AND guild = ?", ("corbicula rex", interaction.guild.id,))

                    animal_data = await cursor.fetchone()
                    if animal_data:
                        breed1, trait_a1, trait_a2, trait_a3, breed2, trait_b1, trait_b2, trait_b3, owner, lender = animal_data
                    
                        checkpofembed = discord.Embed(title=f"Corbicula Rex Pair", description=f"")
                        checkpofembed.set_thumbnail(url="https://runescape.wiki/images/Corbicula_lucidum_%28grown%29.png?d318b")
                        checkpofembed.add_field(name=f"First Corbicula Rex", value=f"Breed: **{breed1}**\nTrait 1: **{trait_a1}**\nTrait 2: **{trait_a2}**\nTrait 3: **{trait_a3}**", inline=True)
                        checkpofembed.add_field(name=f"Second Corbicula Rex", value=f"Breed: **{breed2}**\nTrait 1: **{trait_b1}**\nTrait 2: **{trait_b2}**\nTrait 3: **{trait_b3}**", inline=True)
                        checkpofembed.add_field(name="", value=f"Original Owner: **{owner}** | Lender: **{lender}**", inline=False)
                        await interaction.response.send_message(embed=checkpofembed, ephemeral=True)

                    else:
                        await interaction.response.send_message("We currently don't have any Corbicula Rex", ephemeral=True)
#endregion

#region Oculi Apoterrasaur        
            if self.values[0] == "Oculi Apoterrasaur": 
                async with self.client.db.cursor() as cursor:
                    await cursor.execute("SELECT breed1, traita1, traita2, traita3, breed2, traitb1, traitb2, traitb3, owner, lender FROM animals WHERE animal = ? AND guild = ?", ("oculi apoterrasaur", interaction.guild.id,))

                    animal_data = await cursor.fetchone()
                    if animal_data:
                        breed1, trait_a1, trait_a2, trait_a3, breed2, trait_b1, trait_b2, trait_b3, owner, lender = animal_data
                    
                        checkpofembed = discord.Embed(title=f"Oculi Apoterrasaur Pair", description=f"")
                        checkpofembed.set_thumbnail(url="https://runescape.wiki/images/thumb/Oculi_apoterrasaur_lucidum_%28grown%29.png/800px-Oculi_apoterrasaur_lucidum_%28grown%29.png?55625")
                        checkpofembed.add_field(name=f"First Oculi Apoterrasaur", value=f"Breed: **{breed1}**\nTrait 1: **{trait_a1}**\nTrait 2: **{trait_a2}**\nTrait 3: **{trait_a3}**", inline=True)
                        checkpofembed.add_field(name=f"Second Oculi Apoterrasaur", value=f"Breed: **{breed2}**\nTrait 1: **{trait_b1}**\nTrait 2: **{trait_b2}**\nTrait 3: **{trait_b3}**", inline=True)
                        checkpofembed.add_field(name="", value=f"Original Owner: **{owner}** | Lender: **{lender}**", inline=False)
                        await interaction.response.send_message(embed=checkpofembed, ephemeral=True)

                    else:
                        await interaction.response.send_message("We currently don't have any Oculi Apoterrasaurs", ephemeral=True)
#endregion

#region Malletops       
            if self.values[0] == "Malletops": 
                async with self.client.db.cursor() as cursor:
                    await cursor.execute("SELECT breed1, traita1, traita2, traita3, breed2, traitb1, traitb2, traitb3, owner, lender FROM animals WHERE animal = ? AND guild = ?", ("malletops", interaction.guild.id,))

                    animal_data = await cursor.fetchone()
                    if animal_data:
                        breed1, trait_a1, trait_a2, trait_a3, breed2, trait_b1, trait_b2, trait_b3, owner, lender = animal_data
                    
                        checkpofembed = discord.Embed(title=f"Malletops Pair", description=f"")
                        checkpofembed.set_thumbnail(url="https://runescape.wiki/images/Malletops_lucidum_%28grown%29.png?10aa0")
                        checkpofembed.add_field(name=f"First Malletops", value=f"Breed: **{breed1}**\nTrait 1: **{trait_a1}**\nTrait 2: **{trait_a2}**\nTrait 3: **{trait_a3}**", inline=True)
                        checkpofembed.add_field(name=f"Second Malletops", value=f"Breed: **{breed2}**\nTrait 1: **{trait_b1}**\nTrait 2: **{trait_b2}**\nTrait 3: **{trait_b3}**", inline=True)
                        checkpofembed.add_field(name="", value=f"Original Owner: **{owner}** | Lender: **{lender}**", inline=False)
                        await interaction.response.send_message(embed=checkpofembed, ephemeral=True)

                    else:
                        await interaction.response.send_message("We currently don't have any Malletops", ephemeral=True)
#endregion

#region Pavosaurus Rex     
            if self.values[0] == "Pavosaurus Rex": 
                async with self.client.db.cursor() as cursor:
                    await cursor.execute("SELECT breed1, traita1, traita2, traita3, breed2, traitb1, traitb2, traitb3, owner, lender FROM animals WHERE animal = ? AND guild = ?", ("pavosaurus rex", interaction.guild.id,))

                    animal_data = await cursor.fetchone()
                    if animal_data:
                        breed1, trait_a1, trait_a2, trait_a3, breed2, trait_b1, trait_b2, trait_b3, owner, lender = animal_data
                    
                        checkpofembed = discord.Embed(title=f"Pavosaurus Rex Pair", description=f"")
                        checkpofembed.set_thumbnail(url="https://runescape.wiki/images/Pavosaurus_lucidum_%28grown%29.png?f84ae")
                        checkpofembed.add_field(name=f"First Pavosaurus Rex", value=f"Breed: **{breed1}**\nTrait 1: **{trait_a1}**\nTrait 2: **{trait_a2}**\nTrait 3: **{trait_a3}**", inline=True)
                        checkpofembed.add_field(name=f"Second Pavosaurus Rex", value=f"Breed: **{breed2}**\nTrait 1: **{trait_b1}**\nTrait 2: **{trait_b2}**\nTrait 3: **{trait_b3}**", inline=True)
                        checkpofembed.add_field(name="", value=f"Original Owner: **{owner}** | Lender: **{lender}**", inline=False)
                        await interaction.response.send_message(embed=checkpofembed, ephemeral=True)

                    else:
                        await interaction.response.send_message("We currently don't have any Pavosaurus Rex", ephemeral=True)
#endregion

#endregion

#region  TeamformDropdown
class TeamformDropdown(discord.ui.Select):
        def __init__(self, client):
            options=[
                   discord.SelectOption(label="Nex: Angel Of Death"),
                   discord.SelectOption(label="Nex: Angel Of Death (5 man)"),
                   discord.SelectOption(label="(8+) Nex: Angel Of Death"),
                   discord.SelectOption(label="Croesus"),
                   discord.SelectOption(label="Kerapac"),
                   discord.SelectOption(label="Raids"),
                   discord.SelectOption(label="Rise of the Six"),
                   discord.SelectOption(label="Solak"),
                   discord.SelectOption(label="Vorago"),
                   discord.SelectOption(label="Hardmode Vorago"),
                   discord.SelectOption(label="Vorkath"),
                   discord.SelectOption(label="Zamorak"),
                   discord.SelectOption(label="Sanctum of Rebirth"),
                   discord.SelectOption(label="Gate of Elidinis"),
                   discord.SelectOption(label="Elite Dungeons"),
                   discord.SelectOption(label="Amascut, the Devourer (Normal)"),
                   discord.SelectOption(label="Amascut, the Devourer (Enraged)"),
            ]

            super().__init__(placeholder="Please select a boss to host", options=options, min_values=1, max_values=1, custom_id="teamform_dropdown")
            self.client = client

        async def callback(self, interaction: discord.Interaction):

#region  vorago
            if self.values[0] == "Vorago":
                try:        
                    boss = 1
                    embed = discord.Embed.from_dict(embeds.vorago_dict)
                    embed.set_author(name=f"Hosted by {interaction.user.name}", icon_url="https://cdn.discordapp.com/emojis/773261133192757328.gif")
                    await interaction.response.send_message(embed=embed, view=vmenu.VoragoMenu(self.client, boss))
                    message = await interaction.original_response()

                    embed.set_footer(text=f"Message ID: {message.id}  •  Team size 0/5")
                    await interaction.followup.edit_message(message_id=message.id, embed=embed, view=vmenu.VoragoMenu(self.client, boss))
                except Exception as e:
                    print(f"TeamformDropdown error(Vorago): {e}")
#endregion  
 
#region  aod     
            elif self.values[0] == "Nex: Angel Of Death":
                try:
                    boss = 2
                    embed = discord.Embed.from_dict(embeds.aod_dict)
                    embed.set_author(name=f"Hosted by {interaction.user.name}", icon_url="https://cdn.discordapp.com/emojis/773261133192757328.gif")
                    await interaction.response.send_message(embed=embed, view=aodmenu.AodMenu(self.client, boss))
                    message = await interaction.original_response()

                    embed.set_footer(text=f"Message ID: {message.id}  •  Team size 0/7")
                    await interaction.followup.edit_message(message_id=message.id, embed=embed, view=aodmenu.AodMenu(self.client, boss))  
                except Exception as e:
                    print(f"TeamformDropdown error(aod): {e}")            
#endregion

#region  aod 5 man
            elif self.values[0] == "Nex: Angel Of Death (5 man)":
                try:
                    boss = 2
                    embed = discord.Embed.from_dict(embeds.aod5_dict)
                    embed.set_author(name=f"Hosted by {interaction.user.name}", icon_url="https://cdn.discordapp.com/emojis/773261133192757328.gif")
                    await interaction.response.send_message(embed=embed, view=aod5menu.Aod5Menu(self.client, boss))
                    message = await interaction.original_response()

                    embed.set_footer(text=f"Message ID: {message.id}  •  Team size 0/5")
                    await interaction.followup.edit_message(message_id=message.id, embed=embed, view=aod5menu.Aod5Menu(self.client, boss))
                except Exception as e:
                    print(f"TeamformDropdown error(aod 5 man): {e}") 
#endregion

#region  aod 8 man
            elif self.values[0] == "(8+) Nex: Angel Of Death":
                try:
                    boss = 2
                    embed = discord.Embed.from_dict(embeds.aod8_dict)
                    embed.set_author(name=f"Hosted by {interaction.user.name}", icon_url="https://cdn.discordapp.com/emojis/773261133192757328.gif")
                    await interaction.response.send_message(embed=embed, view=aod8menu.Aod8Menu(self.client, boss))
                    message = await interaction.original_response()

                    await interaction.followup.edit_message(message_id=message.id, embed=embed, view=aod8menu.Aod8Menu(self.client, boss)) 
                except Exception as e:
                    print(f"TeamformDropdown error(aod 8 man): {e}")             
#endregion

#region  HM vorago  
            elif self.values[0] == "Hardmode Vorago":  
                try:         
                    boss = 3
                    embed = discord.Embed.from_dict(embeds.hmvorago_dict)
                    embed.set_author(name=f"Hosted by {interaction.user.name}", icon_url="https://cdn.discordapp.com/emojis/773261133192757328.gif")
                    await interaction.response.send_message(embed=embed, view=hmvmenu.HMVoragoMenu(self.client, boss)) 
                    message = await interaction.original_response()

                    embed.set_footer(text=f"Message ID: {message.id}  •  Team size 0/9")
                    await interaction.followup.edit_message(message_id=message.id, embed=embed, view=hmvmenu.HMVoragoMenu(self.client, boss))
                except Exception as e:
                    print(f"TeamformDropdown error(HM vorago): {e}")                 
#endregion

#region  croesus     
            elif self.values[0] == "Croesus":
                try:
                    boss = 4
                    embed = discord.Embed.from_dict(embeds.croe_dict)
                    embed.set_author(name=f"Hosted by {interaction.user.name}", icon_url="https://cdn.discordapp.com/emojis/773261133192757328.gif")
                    await interaction.response.send_message(embed=embed, view=cromenu.CroeMenu(self.client, boss))
                    message = await interaction.original_response()

                    embed.set_footer(text=f"Message ID: {message.id}  •  Team size 0/4")
                    await interaction.followup.edit_message(message_id=message.id, embed=embed, view=cromenu.CroeMenu(self.client, boss))
                except Exception as e:
                    print(f"TeamformDropdown error(croesus): {e}") 
#endregion

#region  kerapac     
            elif self.values[0] == "Kerapac":
                try:
                    boss = 5
                    embed = discord.Embed.from_dict(embeds.kera_dict)
                    embed.set_author(name=f"Hosted by {interaction.user.name}", icon_url="https://cdn.discordapp.com/emojis/773261133192757328.gif")
                    await interaction.response.send_message(embed=embed, view=keramenu.KeraMenu(self.client, boss))
                    message = await interaction.original_response()

                    embed.set_footer(text=f"Message ID: {message.id}  •  Team size 0/3")
                    await interaction.followup.edit_message(message_id=message.id, embed=embed, view=keramenu.KeraMenu(self.client, boss))
                except Exception as e:
                    print(f"TeamformDropdown error(Kerapac): {e}")
#endregion

#region  raids     
            elif self.values[0] == "Raids":
                try:
                    boss = 6
                    embed = discord.Embed.from_dict(embeds.raids_dict)
                    embed.set_author(name=f"Hosted by {interaction.user.name}", icon_url="https://cdn.discordapp.com/emojis/773261133192757328.gif")
                    await interaction.response.send_message(embed=embed, view=raidsmenu.RaidsMenu(self.client, boss)) 
                    message = await interaction.original_response()


                    embed.set_footer(text=f"Message ID: {message.id}  •  Team size 0/10")
                    await interaction.followup.edit_message(message_id=message.id, embed=embed, view=raidsmenu.RaidsMenu(self.client, boss)) 
                except Exception as e:
                    print(f"TeamformDropdown error(raids): {e}") 
#endregion

#region  rots    
            elif self.values[0] == "Rise of the Six":
                try:
                    boss = 7
                    embed = discord.Embed.from_dict(embeds.rots_dict)
                    embed.set_author(name=f"Hosted by {interaction.user.name}", icon_url="https://cdn.discordapp.com/emojis/773261133192757328.gif")
                    await interaction.response.send_message(embed=embed, view=rotsmenu.RotsMenu(self.client, boss))
                    message = await interaction.original_response()

                    embed.set_footer(text=f"Message ID: {message.id}  •  Team size 0/4")
                    await interaction.followup.edit_message(message_id=message.id, embed=embed, view=rotsmenu.RotsMenu(self.client, boss))
                except Exception as e:
                    print(f"TeamformDropdown error(rots): {e}")
#endregion

#region  solak     
            elif self.values[0] == "Solak":
                try:
                    boss = 8
                    embed = discord.Embed.from_dict(embeds.solak_dict)
                    embed.set_author(name=f"Hosted by {interaction.user.name}", icon_url="https://cdn.discordapp.com/emojis/773261133192757328.gif")
                    await interaction.response.send_message(embed=embed, view=solakmenu.SolakMenu(self.client))
                    message = await interaction.original_response()

                    embed.set_footer(text=f"Message ID: {message.id}  •  Team size 0/7")
                    await interaction.followup.edit_message(message_id=message.id, embed=embed, view=solakmenu.SolakMenu(self.client))
                except Exception as e:
                    print(f"TeamformDropdown error(solak): {e}")
#endregion

#region  vorkath    
            elif self.values[0] == "Vorkath":
                try:
                    boss = 9
                    embed = discord.Embed.from_dict(embeds.vork_dict)
                    embed.set_author(name=f"Hosted by {interaction.user.name}", icon_url="https://cdn.discordapp.com/emojis/773261133192757328.gif")
                    await interaction.response.send_message(embed=embed, view=vorkmenu.VorkMenu(self.client, boss))
                    message = await interaction.original_response()

                    embed.set_footer(text=f"Message ID: {message.id}  •  Team size 0/10")
                    await interaction.followup.edit_message(message_id=message.id, embed=embed, view=vorkmenu.VorkMenu(self.client, boss))
                except Exception as e:
                    print(f"TeamformDropdown error(vorkath): {e}")
#endregion

#region  zamorak     
            elif self.values[0] == "Zamorak":
                try:
                    boss = 10
                    embed = discord.Embed.from_dict(embeds.zammy_dict)
                    embed.set_author(name=f"Hosted by {interaction.user.name}", icon_url="https://cdn.discordapp.com/emojis/773261133192757328.gif")
                    await interaction.response.send_message(embed=embed, view=zammymenu.ZammyMenu(self.client, boss))
                    message = await interaction.original_response()

                    embed.set_footer(text=f"Message ID: {message.id}  •  Team size 0/5")
                    await interaction.followup.edit_message(message_id=message.id, embed=embed, view=zammymenu.ZammyMenu(self.client, boss))
                except Exception as e:
                    print(f"TeamformDropdown error(zamorak): {e}")
#endregion

#region  sanctum of rebirth    
            elif self.values[0] == "Sanctum of Rebirth":
                try:
                    boss = 11
                    embed = discord.Embed.from_dict(embeds.sor_dict)
                    embed.set_author(name=f"Hosted by {interaction.user.name}", icon_url="https://cdn.discordapp.com/emojis/773261133192757328.gif")
                    await interaction.response.send_message(embed=embed, view=sormenu.SorMenu(self.client, boss))
                    message = await interaction.original_response()

                    embed.set_footer(text=f"Message ID: {message.id}  •  Team size 0/4")
                    await interaction.followup.edit_message(message_id=message.id, embed=embed, view=sormenu.SorMenu(self.client, boss))
                except Exception as e:
                    print(f"TeamformDropdown error(sanctum of rebirth): {e}")
#endregion

#region  Gate of Elidinis    
            elif self.values[0] == "Gate of Elidinis":
                try:
                    boss = 12
                    embed = discord.Embed.from_dict(embeds.goe_dict)
                    embed.set_author(name=f"Hosted by {interaction.user.name}", icon_url="https://cdn.discordapp.com/emojis/773261133192757328.gif")
                    await interaction.response.send_message(embed=embed, view=goemenu.GoeMenu(self.client, boss))
                    message = await interaction.original_response()

                    embed.set_footer(text=f"Message ID: {message.id}  •  Team size 0/10")
                    await interaction.followup.edit_message(message_id=message.id, embed=embed, view=goemenu.GoeMenu(self.client, boss))
                except Exception as e:
                    print(f"TeamformDropdown error(Gate of Elidinis): {e}")
#endregion

#region  Elite dungeons
            elif self.values[0] == "Elite Dungeons":
                try:
                    boss = 13
                    embed = discord.Embed.from_dict(embeds.eds_dict)
                    embed.set_author(name=f"Hosted by {interaction.user.name}", icon_url="https://cdn.discordapp.com/emojis/773261133192757328.gif")
                    await interaction.response.send_message(embed=embed, view=edsmenu.EdsMenu(self.client, boss))
                    message = await interaction.original_response()

                    embed.set_footer(text=f"Message ID: {message.id}  •  Team size 0/3")
                    await interaction.followup.edit_message(message_id=message.id, embed=embed, view=edsmenu.EdsMenu(self.client, boss))
                except Exception as e:
                    print(f"TeamformDropdown error(Elite dungeons): {e}")
#endregion

#region  Amascut, the Devourer (Normal)
            elif self.values[0] == "Amascut, the Devourer (Normal)":
                try:
                    boss = 14
                    embed = discord.Embed.from_dict(embeds.amas_dict)
                    embed.set_author(name=f"Hosted by {interaction.user.name}", icon_url="https://cdn.discordapp.com/emojis/773261133192757328.gif")
                    await interaction.response.send_message(embed=embed, view=amascutmenu.AmasMenu(self.client, boss))
                    message = await interaction.original_response()

                    embed.set_footer(text=f"Message ID: {message.id}  •  Team size 0/5")
                    await interaction.followup.edit_message(message_id=message.id, embed=embed, view=amascutmenu.AmasMenu(self.client, boss))
                except Exception as e:
                    print(f"TeamformDropdown error(Amascut (Normal)): {e}")
#endregion

#region  Amascut, the Devourer (Enraged)
            elif self.values[0] == "Amascut, the Devourer (Enraged)":
                try:
                    boss = 14
                    embed = discord.Embed.from_dict(embeds.hmamas_dict)
                    embed.set_author(name=f"Hosted by {interaction.user.name}", icon_url="https://cdn.discordapp.com/emojis/773261133192757328.gif")
                    await interaction.response.send_message(embed=embed, view=hmamascutmenu.HMAmasMenu(self.client, boss))
                    message = await interaction.original_response()

                    embed.set_footer(text=f"Message ID: {message.id}  •  Team size 0/5")
                    await interaction.followup.edit_message(message_id=message.id, embed=embed, view=hmamascutmenu.HMAmasMenu(self.client, boss))
                except Exception as e:
                    print(f"TeamformDropdown error(Amascut (Enraged)): {e}")
#endregion

#RESETS DROPDOWN BACK TO PLACEHOLDER
            new_dropdown = TeamformDropdown(self.client)
            new_view = View(timeout=None)
            new_view.add_item(new_dropdown)
            await interaction.message.edit(view=new_view)
#endregion

#region
class AchievementDropdown(discord.ui.Select):
        def __init__(self, client, uncompleted_list, target_user):
            options = [discord.SelectOption(label=name) for name in uncompleted_list]

            super().__init__(placeholder="Please select an Achievement to give", options=options, min_values=1, max_values=1, custom_id="achievement_dropdown")
            self.client = client
            self.target_user = target_user

        async def callback(self, interaction: discord.Interaction):
            try:
                selected = self.values[0]
                selected_dict = next((d for d in achievements.achievements if d["name"] == selected), None)

                if selected_dict is not None:
                    selected_cat = selected_dict["cat"]
                    cat_attr = getattr(self.target_user.achievements, selected_cat)
                    cat_attr.points += selected_dict["points"]
                    cat_attr.tasks += selected_dict["tasks"]
                    self.target_user.achievements.completed.append(selected)
                    await self.target_user.save()
                    await interaction.response.send_message(f"You have successfully added the achievement: `{selected}`", ephemeral=True)
            except Exception as e:
                print(f"AchievementDropdown error: {e}")
#endregion  

#region multipage achievement dropdown
class AchievementDropdownMulti(discord.ui.Select):
        def __init__(self, client, lists_dict, target_user):
            options = [discord.SelectOption(label=a["name"]) for a in lists_dict]

            super().__init__(placeholder="Please select a list of achievements", options=options, min_values=1, max_values=1, custom_id="achievement_dropdown_multi")
            self.client = client
            self.lists_dict = lists_dict
            self.target_user = target_user

        async def callback(self, interaction: discord.Interaction):
            try:
                selected = self.values[0]
                selected_dict = next((d for d in self.lists_dict if d["name"] == selected), None)

                if selected_dict is not None:
                    selected_list = selected_dict["list"]
     
                await interaction.response.send_message("Select an Achievement to give", ephemeral=True, view=myviews.AchievementView(self.client, selected_list, self.target_user))
            except Exception as e:
                print(f"AchievementDropdownMulti error: {e}")
#endregion

