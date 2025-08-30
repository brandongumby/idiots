import discord
import copy
from datetime import datetime

message_sets = {}

#region  Team embed
teamembed = discord.Embed(description=(f"# Welcome to Idiots Teamforming Channel"), color=discord.Color.random())
teamembed.set_thumbnail(url=("https://i.imgur.com/mJXeo9U.png"))
teamembed.add_field(name="How to host?", value=f"Hosting an event has never been easier!", inline=False)
teamembed.add_field(name="Step 1", value=f"* Select a boss from the drop down menu below this post.\nAfter making the selection a sign up sheet will be formed.", inline=False)
teamembed.add_field(name="Step 2", value=f"* Click the '⏰ Set Time' button to then enter a date and time for your event.\n* Enter the time you want and the Timezone, it will display local time for everyone else.\n* This will ping the boss role automatically", inline=False)
teamembed.add_field(name="Step 3", value=f"* Make sure you add in any additional comments by clicking the '💬 Add Comment' button.\n* Include any rules that may differ or any other information you think is important that the team should know before signing up!", inline=False)  
teamembed.add_field(name="Step 4", value=f"* Sign up to your desired role and wait for the team to fill", inline=False) 
teamembed.add_field(name="Step 5", value=f"* Lastly when the team is full, click the '✅ Complete' button and ping the team shortly before the start!", inline=False) 
teamembed.add_field(name="Add/remove", value=f"* After selecting a boss, as the host you can add/remove players who may need it.\n* Use the **/add_user** or **/remove_user** commands.\n*You can find the message ID on the bottom left of the sign up sheet!*", inline=False)

oteam_dict = teamembed.to_dict()
team_dict1 = copy.deepcopy(oteam_dict)
#endregion

#region  Vorago embeds
voriginal_values = [f"`Empty`", f"`Empty`"]
vdescription_values = ["# Vorago", " ", "**[Basic Vorago Guide](https://pvme.github.io/pvme-guides/basic-guides/vorago-basic/vorago-basic/)**"]
vcombined_discription = "\n".join(vdescription_values)
vcombined_value = ", ".join(voriginal_values)

voragoembed = discord.Embed(description=(vcombined_discription), color=discord.Color.random(), timestamp=datetime.now())
voragoembed.set_thumbnail(url=("https://runescape.wiki/images/thumb/Vorago.png/800px-Vorago.png?925d8"))
voragoembed.add_field(name="⏰ Start Time", value=f"Click '⏰ Set Time' to set a start time", inline=False)
voragoembed.add_field(name="💬 Comments:", value=f"Click '💬 Add Comment' to add any additional comments", inline=False)
voragoembed.add_field(name="🛡️ Base Tank", value=f"`Empty`", inline=True)
voragoembed.add_field(name="💣 Bomb Tank", value=f"`Empty`", inline=True)
voragoembed.add_field(name="5️⃣ TL5", value=f"`Empty`", inline=True)  
voragoembed.add_field(name="⚔️ DPS", value=vcombined_value, inline=True) 
voragoembed.add_field(name="**RULES:**", value=f"<#1271568914538827807>\n**Seismic weapons & energies are SPLIT** *(unless stated otherwise and agreed upon)*", inline=False)

ovorago_dict = voragoembed.to_dict()
vorago_dict = copy.deepcopy(ovorago_dict)
voragovalues = copy.deepcopy(voriginal_values)

voragorules = discord.Embed(description=(f"# Vorago Rules"), color=discord.Color.random())
voragorules.set_thumbnail(url=("https://runescape.wiki/images/thumb/Vorago.png/800px-Vorago.png?925d8"))
voragorules.add_field(name=" ", value=f"* Seismic weapons & energies are __**SPLIT**__ (unless stated otherwise).", inline=False)
voragorules.add_field(name=" ", value=f"* Being on voice chat is **__HIGLY ADVISED IF LEARNING/NEW TO THE BOSS__**", inline=False)
voragorules.add_field(name=" ", value=f"* If you are newer to Vorago we recommend checking out a **[Basic Vorago Guide](https://pvme.github.io/pvme-guides/basic-guides/vorago-basic/vorago-basic/)**", inline=False)

ovrules_dict = voragorules.to_dict()
vrules_dict = copy.deepcopy(ovrules_dict)
#endregion

#region  HM Vorago embeds
hmvoriginal_values = ["`Empty`", "`Empty`", "`Empty`", "`Empty`", "`Empty`"]
hmvbomb_values = ["`Empty`", "`Empty`"]
hmvdescription_values = ["# Hardmode Vorago", " ", "**[Hardmode Vorago Guide](https://pvme.io/pvme-guides/rs3-full-boss-guides/vorago/hard-mode-overview/)**"]
hmvcombined_discription = "\n".join(hmvdescription_values)
hmvcombined_value = ", ".join(hmvoriginal_values)
hmvbombcombined_value = "\n".join(hmvbomb_values)

hmvoragoembed = discord.Embed(description=(hmvcombined_discription), color=discord.Color.random(), timestamp=datetime.now())
hmvoragoembed.set_thumbnail(url=("https://runescape.wiki/images/Bombi_%28red%29_pet.png?73ada"))
hmvoragoembed.add_field(name="⏰ Start Time", value=f"Click '⏰ Set Time' to set a start time", inline=False)
hmvoragoembed.add_field(name="💬 Comments:", value=f"Click '💬 Add Comment' to add any additional comments", inline=False)
hmvoragoembed.add_field(name="🛡️ Base Tank", value=f"`Empty`", inline=True)
hmvoragoembed.add_field(name="💣 Bomb Tanks", value=hmvbombcombined_value, inline=True)
hmvoragoembed.add_field(name="5️⃣ TL5", value=f"`Empty`", inline=True)  
hmvoragoembed.add_field(name="⚔️ DPS", value=hmvcombined_value, inline=True) 
hmvoragoembed.add_field(name="**RULES:**", value=f"<#1271568914538827807>\n**Seismic weapons are SPLIT & energies/commons are KEEPS** *(unless stated otherwise and agreed upon)*", inline=False)

ohmvorago_dict = hmvoragoembed.to_dict()
hmvorago_dict = copy.deepcopy(ohmvorago_dict)
hmvoragovalues = copy.deepcopy(hmvoriginal_values)


hmvoragorules = discord.Embed(description=(f"# Hardmode Vorago Rules"), color=discord.Color.random())
hmvoragorules.set_thumbnail(url=("https://runescape.wiki/images/Bombi_%28red%29_pet.png?73ada"))
hmvoragorules.add_field(name=" ", value=f"* Seismic weapons are __**SPLIT**__ (unless stated otherwise).", inline=False)
hmvoragorules.add_field(name=" ", value=f"* energies and all commons are  __**KEEPS**__ (unless stated otherwise).", inline=False)
hmvoragorules.add_field(name=" ", value=f"* Being on voice chat is **__HIGLY ADVISED IF LEARNING/NEW TO THE BOSS__**", inline=False)
hmvoragorules.add_field(name=" ", value=f"* If you are newer to Hardmode Vorago we recommend checking out a **[Hardmode Vorago Guide](https://pvme.io/pvme-guides/rs3-full-boss-guides/vorago/hard-mode-overview/)**", inline=False)

ohmvrules_dict = hmvoragorules.to_dict()
hmvrules_dict = copy.deepcopy(ohmvrules_dict)
#endregion

#region  raids embeds
raidsoriginal_values = ["`Empty`", "`Empty`", "`Empty`", "`Empty`", "`Empty`"]
st5_values = ["`Empty`", "`Empty`"]
raidsdescription_values = ["# Full Raids", " ", "**[Yakamaru Guide](https://pvme.io/pvme-guides/rs3-full-boss-guides/yakamaru/)**"]
raidscombined_discription = "\n".join(raidsdescription_values)
raidsdps_value = ", ".join(raidsoriginal_values)
st5combined_value = "\n".join(st5_values)

raidsembed = discord.Embed(description=(raidscombined_discription), color=discord.Color.random(), timestamp=datetime.now())
raidsembed.set_thumbnail(url=("https://runescape.wiki/images/Yakamaru.png?18623"))
raidsembed.add_field(name="⏰ Start Time", value=f"Click '⏰ Set Time' to set a start time", inline=False)
raidsembed.add_field(name="💬 Comments:", value=f"Click '💬 Add Comment' to add any additional comments", inline=False)
raidsembed.add_field(name="🛡️ Base Tank", value=f"`Empty`", inline=True)
raidsembed.add_field(name="🅱️ Backup SC", value=f"`Empty`", inline=True)
raidsembed.add_field(name="1️⃣ Pet Tank 1/3", value=f"`Empty`", inline=True)
raidsembed.add_field(name="2️⃣ Pet Tank 2", value=f"`Empty`", inline=True)
raidsembed.add_field(name="🐶 North Chargers", value=f"`Empty`", inline=True)
raidsembed.add_field(name="💥 Main Stun", value=f"`Empty`", inline=True)
raidsembed.add_field(name="⚡ Backup Stun", value=f"`Empty`", inline=True)
raidsembed.add_field(name="🐍 North Tank", value=f"`Empty`", inline=True)
raidsembed.add_field(name="🤢 Poison Tank", value=f"`Empty`", inline=True)
raidsembed.add_field(name="❤️ CPR", value=f"`Empty`", inline=True)
raidsembed.add_field(name="🇩 Double", value=f"`Empty`", inline=True)
raidsembed.add_field(name="🪼 Jelly Wrangler", value=f"`Empty`", inline=True)
raidsembed.add_field(name="🦈 Shark 10", value=f"`Empty`", inline=True)
raidsembed.add_field(name="0️⃣ Stun 0", value=f"`Empty`", inline=True)
raidsembed.add_field(name="5️⃣ Stun 5", value=st5combined_value, inline=True)  
raidsembed.add_field(name="⚔️ DPS", value=raidsdps_value, inline=False)
raidsembed.add_field(name="**RULES:**", value=f"<#1271568914538827807>\n**ALL drops are KEEPS**", inline=False)


oraids_dict = raidsembed.to_dict()
raids_dict = copy.deepcopy(oraids_dict)
raidsvalues = copy.deepcopy(raidsoriginal_values)


raidsrules = discord.Embed(description=(f"# Raids Rules"), color=discord.Color.random())
raidsrules.set_thumbnail(url=("https://runescape.wiki/images/Yakamaru.png?18623"))
raidsrules.add_field(name=" ", value=f"* All drops are  __**KEEPS**__.", inline=False)
raidsrules.add_field(name=" ", value=f"* Being on voice chat is **__HIGLY ADVISED IF LEARNING/NEW TO THE BOSS__**", inline=False)
raidsrules.add_field(name=" ", value=f"* If you are newer to Raids we recommend checking out a **[Yakamaru Guide](https://pvme.io/pvme-guides/rs3-full-boss-guides/yakamaru/)**", inline=False)

oraidsrules_dict = raidsrules.to_dict()
raidsrules_dict = copy.deepcopy(oraidsrules_dict)
#endregion

#region  aod embeds
#normal 7 man
aoddescription_values = ["# Nex: Angel of Death", " ", "**[Nex: Angel of Death Guide](https://pvme.io/pvme-guides/rs3-full-boss-guides/angel-of-death-7s/mechanics/)**"]
aodcombined_discription = "\n".join(aoddescription_values)

aodembed = discord.Embed(description=(aodcombined_discription), color=discord.Color.random(), timestamp=datetime.now())
aodembed.set_thumbnail(url=("https://runescape.wiki/images/Nex_%28Angel_of_Death%29.png?16149"))
aodembed.add_field(name="⏰ Start Time", value=f"Click '⏰ Set Time' to set a start time", inline=False)
aodembed.add_field(name="💬 Comments:", value=f"Click '💬 Add Comment' to add any additional comments", inline=False)
aodembed.add_field(name="🛡️ Base Tank", value=f"`Empty`", inline=True)
aodembed.add_field(name="🇺 Umbra", value=f"`Empty`", inline=True)
aodembed.add_field(name="🇬 Glacies", value=f"`Empty`", inline=True)
aodembed.add_field(name="🇨 Cruor", value=f"`Empty`", inline=True)  
aodembed.add_field(name="🇫 Fumus", value=f"`Empty`", inline=True)  
aodembed.add_field(name="🔨 Hammer", value=f"`Empty`", inline=True)    
aodembed.add_field(name="☁️ Smoke Cloud", value=f"`Empty`", inline=True) 
aodembed.add_field(name="**RULES:**", value=f"<#1271568914538827807>\n**Codex are SPLIT and weapons/chests are KEEPS** *(unless stated otherwise and agreed upon)*", inline=False)

oaod_dict = aodembed.to_dict()
aod_dict = copy.deepcopy(oaod_dict)

#rules
aodrules = discord.Embed(description=(f"# Nex: Angel of Death Rules"), color=discord.Color.random())
aodrules.set_thumbnail(url=("https://runescape.wiki/images/Nex_%28Angel_of_Death%29.png?16149"))
aodrules.add_field(name=" ", value=f"* Codex are __**SPLIT**__ (unless stated otherwise).", inline=False)
aodrules.add_field(name=" ", value=f"* Chests and weapons are __**KEEPS**__ (unless stated otherwise).", inline=False)
aodrules.add_field(name=" ", value=f"* Absolutely no toxicity is allowed - you will be warned (we recognise people get grumpy when things don't go well!)", inline=False)
aodrules.add_field(name=" ", value=f"* After a 10 minute grace period your spot is subject to be filled, if no fill is found by 15 minutes after start time the hour is subject to disband.", inline=False)
aodrules.add_field(name=" ", value=f"* Being on voice chat is **__HIGLY ADVISED IF LEARNING/NEW TO THE BOSS__**", inline=False)
aodrules.add_field(name=" ", value=f"* If you are newer to Nex: Angel of Death we recommend checking out a **[Nex: Angel of Death Guide](https://pvme.io/pvme-guides/rs3-full-boss-guides/angel-of-death-7s/mechanics/)**", inline=False)
aodrules.add_field(name="Additional Information: ", value=f"[click here for additional info](https://discord.com/channels/889687198323048518/1060285450541092975/1262923086404128843)", inline=False)

oaodrules_dict = aodrules.to_dict()
aodrules_dict = copy.deepcopy(oaodrules_dict)

#8+ man
aod8original_values = ["`Empty`", "`Empty`", "`Empty`", "`Empty`"]
aod8dps_value = ", ".join(aod8original_values)

aod8description_values = ["# Nex: Angel of Death (8+)", " ", "**[Nex: Angel of Death Guide](https://pvme.io/pvme-guides/rs3-full-boss-guides/angel-of-death-7s/mechanics/)**"]
aod8combined_discription = "\n".join(aod8description_values)

aod8embed = discord.Embed(description=(aod8combined_discription), color=discord.Color.random(), timestamp=datetime.now())
aod8embed.set_thumbnail(url=("https://runescape.wiki/images/Nex_%28Angel_of_Death%29.png?16149"))
aod8embed.add_field(name="⏰ Start Time", value=f"Click '⏰ Set Time' to set a start time", inline=False)
aod8embed.add_field(name="💬 Comments:", value=f"Click '💬 Add Comment' to add any additional comments", inline=False)
aod8embed.add_field(name="🛡️ Base Tank", value=f"`Empty`", inline=True)
aod8embed.add_field(name="🇺 Umbra", value=f"`Empty`", inline=True)
aod8embed.add_field(name="🇬 Glacies", value=f"`Empty`", inline=True)
aod8embed.add_field(name="🇨 Cruor", value=f"`Empty`", inline=True)  
aod8embed.add_field(name="🇫 Fumus", value=f"`Empty`", inline=True)  
aod8embed.add_field(name="🔨 Hammer", value=f"`Empty`", inline=True)    
aod8embed.add_field(name="☁️ Smoke Cloud", value=f"`Empty`", inline=True)
aod8embed.add_field(name="⚔️ DPS", value=aod8dps_value, inline=False) 
aod8embed.add_field(name="**RULES:**", value=f"<#1271568914538827807>\n**Codex are SPLIT and weapons/chests are KEEPS** *(unless stated otherwise and agreed upon)*", inline=False)

oaod8_dict = aod8embed.to_dict()
aod8_dict = copy.deepcopy(oaod8_dict)

#5 man
aod5description_values = ["# Nex: Angel of Death (5 man)", " ", "**[Nex: Angel of Death Guide](https://pvme.io/pvme-guides/rs3-full-boss-guides/angel-of-death-7s/mechanics/)**"]
aod5combined_discription = "\n".join(aod5description_values)

aod5embed = discord.Embed(description=(aod5combined_discription), color=discord.Color.random(), timestamp=datetime.now())
aod5embed.set_thumbnail(url=("https://runescape.wiki/images/Nex_%28Angel_of_Death%29.png?16149"))
aod5embed.add_field(name="⏰ Start Time", value=f"Click '⏰ Set Time' to set a start time", inline=False)
aod5embed.add_field(name="💬 Comments:", value=f"Click '💬 Add Comment' to add any additional comments", inline=False)
aod5embed.add_field(name="🛡️ Base Tank", value=f"`Empty`", inline=True)
aod5embed.add_field(name="🇺 Umbra/Glacies", value=f"`Empty`", inline=True)
aod5embed.add_field(name="🇨 Cruor/Fumus", value=f"`Empty`", inline=True)
aod5embed.add_field(name="🔨 Hammer", value=f"`Empty`", inline=True)    
aod5embed.add_field(name="☁️ Smoke Cloud", value=f"`Empty`", inline=True)
aod5embed.add_field(name="**RULES:**", value=f"<#1271568914538827807>\n**Codex are SPLIT and weapons/chests are KEEPS** *(unless stated otherwise and agreed upon)*", inline=False) 

oaod5_dict = aod5embed.to_dict()
aod5_dict = copy.deepcopy(oaod5_dict)
#endregion

#region  vorkath embeds
vorkoriginal_values = ["`Empty`", "`Empty`", "`Empty`", "`Empty`", "`Empty`", "`Empty`", "`Empty`", "`Empty`"]
vorkdps_value = ", ".join(vorkoriginal_values)

vorkdescription_values = ["# Vorkath", " ", "**[Vorkath Guide](https://pvme.io/pvme-guides/rs3-full-boss-guides/vorkath/necro-vorkath/)**"]
vorkcombined_discription = "\n".join(vorkdescription_values)

vorkembed = discord.Embed(description=(vorkcombined_discription), color=discord.Color.random(), timestamp=datetime.now())
vorkembed.set_thumbnail(url=("https://runescape.wiki/images/archive/20240528223235%21Vorkath.png?a7f11"))
vorkembed.add_field(name="⏰ Start Time", value=f"Click '⏰ Set Time' to set a start time", inline=False)
vorkembed.add_field(name="💬 Comments:", value=f"Click '💬 Add Comment' to add any additional comments", inline=False)
vorkembed.add_field(name="🛡️ Zemo Tank", value=f"`Empty`", inline=True)
vorkembed.add_field(name="🐲 Vorky Tank", value=f"`Empty`", inline=True)
vorkembed.add_field(name="⚔️ DPS", value=vorkdps_value, inline=False)
vorkembed.add_field(name="**RULES:**", value=f"<#1271568914538827807>\n**All drops are KEEPS** *(unless stated otherwise and agreed upon)*", inline=False)

ovork_dict = vorkembed.to_dict()
vork_dict = copy.deepcopy(ovork_dict)


vorkrules = discord.Embed(description=(f"# Vorkath Rules"), color=discord.Color.random())
vorkrules.set_thumbnail(url=("https://runescape.wiki/images/archive/20240528223235%21Vorkath.png?a7f11"))
vorkrules.add_field(name=" ", value=f"* All drops are __**KEEPS**__ (unless stated otherwise).", inline=False)
vorkrules.add_field(name=" ", value=f"* Being on voice chat is **__HIGLY ADVISED IF LEARNING/NEW TO THE BOSS__**", inline=False)
vorkrules.add_field(name=" ", value=f"* If you are newer to Vorkath we recommend checking out a **[Vorkath Guide](https://pvme.io/pvme-guides/rs3-full-boss-guides/angel-of-death-7s/mechanics/https://pvme.io/pvme-guides/rs3-full-boss-guides/vorkath/necro-vorkath/)**", inline=False)


ovorkrules_dict = vorkrules.to_dict()
vorkrules_dict = copy.deepcopy(ovorkrules_dict)
#endregion

#region  rots embeds
rotsdescription_values = ["# Barrows: Rise of the Six", " ", "**[Basic RotS Guide](https://pvme.io/pvme-guides/basic-guides/rise-of-the-six-basic/)**"]
rotscombined_discription = "\n".join(rotsdescription_values)

rotsembed = discord.Embed(description=(rotscombined_discription), color=discord.Color.random(), timestamp=datetime.now())
rotsembed.set_thumbnail(url=("https://runescape.wiki/images/Karil_the_Tainted_%28Shadow%29.png?d9426"))
rotsembed.add_field(name="⏰ Start Time", value=f"Click '⏰ Set Time' to set a start time", inline=False)
rotsembed.add_field(name="💬 Comments:", value=f"Click '💬 Add Comment' to add any additional comments", inline=False)
rotsembed.add_field(name="↖️ Incite West", value=f"`Empty`", inline=True)
rotsembed.add_field(name="↙️ DPS West", value=f"`Empty`", inline=True)
rotsembed.add_field(name="↗️ Incite East", value=f"`Empty`", inline=True)  
rotsembed.add_field(name="↘️ DPS East", value=f"`Empty`", inline=True) 
rotsembed.add_field(name="**RULES:**", value=f"<#1271568914538827807>\n**ALL drops are KEEPS** *(unless stated otherwise and agreed upon)*", inline=False)

orots_dict = rotsembed.to_dict()
rots_dict = copy.deepcopy(orots_dict)


rotsrules = discord.Embed(description=(f"# Barrows: Rise of the Six Rules"), color=discord.Color.random())
rotsrules.set_thumbnail(url=("https://runescape.wiki/images/Karil_the_Tainted_%28Shadow%29.png?d9426"))
rotsrules.add_field(name=" ", value=f"* All drops are __**KEEPS**__ (unless stated otherwise).", inline=False)
rotsrules.add_field(name=" ", value=f"* Being on voice chat is **__HIGLY ADVISED IF LEARNING/NEW TO THE BOSS__**", inline=False)
rotsrules.add_field(name=" ", value=f"* If you are newer to Rise of the Six we recommend checking out a **[Basic RotS Guide](https://pvme.io/pvme-guides/basic-guides/rise-of-the-six-basic/)**", inline=False)

orotsrules_dict = rotsrules.to_dict()
rotsrules_dict = copy.deepcopy(orotsrules_dict)
#endregion

#region  kerapac embeds

keradescription_values = ["# Kerapac", " ", "**[Basic Kerapac Guide](https://pvme.io/pvme-guides/basic-guides/kerapac-hm-basic/)**"]
keracombined_discription = "\n".join(keradescription_values)

keraembed = discord.Embed(description=(keracombined_discription), color=discord.Color.random(), timestamp=datetime.now())
keraembed.set_thumbnail(url=("https://runescape.wiki/images/thumb/Kerapac%2C_the_bound.png/1280px-Kerapac%2C_the_bound.png?593e2"))
keraembed.add_field(name="⏰ Start Time", value=f"Click '⏰ Set Time' to set a start time", inline=False)
keraembed.add_field(name="💬 Comments:", value=f"Click '💬 Add Comment' to add any additional comments", inline=False)
keraembed.add_field(name="⬆️ North Echo", value=f"`Empty`", inline=True)
keraembed.add_field(name="⬅️ West Echo", value=f"`Empty`", inline=True)
keraembed.add_field(name="⬇️ South Echo", value=f"`Empty`", inline=True)  
keraembed.add_field(name="**RULES:**", value=f"<#1271568914538827807>\n**Staff pieces are SPLIT & all other drops are KEEPS** *(unless stated otherwise and agreed upon)*", inline=False)

okera_dict = keraembed.to_dict()
kera_dict = copy.deepcopy(okera_dict)


kerarules = discord.Embed(description=(f"# Kerapac Rules"), color=discord.Color.random())
kerarules.set_thumbnail(url=("https://runescape.wiki/images/thumb/Kerapac%2C_the_bound.png/1280px-Kerapac%2C_the_bound.png?593e2"))
kerarules.add_field(name=" ", value=f"* All staff pieces are __**SPLIT**__ (unless stated otherwise).", inline=False)
kerarules.add_field(name=" ", value=f"* All other drops are __**KEEPS**__ (unless stated otherwise).", inline=False)
kerarules.add_field(name=" ", value=f"* Being on voice chat is **__HIGLY ADVISED IF LEARNING/NEW TO THE BOSS__**", inline=False)
kerarules.add_field(name=" ", value=f"* If you are newer to Kerapac we recommend checking out a **[Basic Kerapac Guide](https://pvme.io/pvme-guides/basic-guides/kerapac-hm-basic/)**", inline=False)

okerarules_dict = kerarules.to_dict()
kerarules_dict = copy.deepcopy(okerarules_dict)


#endregion

#region  solak embeds
solakoriginal_values = [f"`Empty`", f"`Empty`"]
solaknw_values = [f"`Empty`", f"`Empty`"]
solakne_values = [f"`Empty`", f"`Empty`"]
solaksw_values = [f"`Empty`", f"`Empty`"]
solakse_values = [f"`Empty`", f"`Empty`"]
solakdescription_values = ["# Solak", " ", "**[Basic Solak Guide](https://pvme.io/pvme-guides/basic-guides/solak-basic/)**"]
solakcombined_discription = "\n".join(solakdescription_values)
solakcombined_value = "\n".join(solakoriginal_values)
nwcombined_value = "\n".join(solaknw_values)
necombined_value = "\n".join(solakne_values)
swcombined_value = "\n".join(solaksw_values)
secombined_value = "\n".join(solakse_values)

solakembed = discord.Embed(description=(solakcombined_discription), color=discord.Color.random(), timestamp=datetime.now())
solakembed.set_thumbnail(url=("https://runescape.wiki/images/Solak.png?3239c"))
solakembed.add_field(name="⏰ Start Time", value=f"Click '⏰ Set Time' to set a start time", inline=False)
solakembed.add_field(name="💬 Comments:", value=f"Click '💬 Add Comment' to add any additional comments", inline=False)
solakembed.add_field(name="🛡️ Base", value=f"`Empty`", inline=True)
solakembed.add_field(name="↖️ North West", value=nwcombined_value, inline=True)
solakembed.add_field(name="↙️ South West", value=necombined_value, inline=True)  
solakembed.add_field(name="↗️ North East", value=swcombined_value, inline=True)
solakembed.add_field(name="↘️ South East", value=secombined_value, inline=True)
solakembed.add_field(name="🧝‍♀️ Elf", value=solakcombined_value, inline=True)  
solakembed.add_field(name="**RULES:**", value=f"<#1271568914538827807>\n**Bows and grims are SPLIT everything else is KEEPS** *(unless stated otherwise and agreed upon)*", inline=False)

osolak_dict = solakembed.to_dict()
solak_dict = copy.deepcopy(osolak_dict)


solakrules = discord.Embed(description=(f"# Solak Rules"), color=discord.Color.random())
solakrules.set_thumbnail(url=("https://runescape.wiki/images/Solak.png?3239c"))
solakrules.add_field(name=" ", value=f"* Bows and Grimoires are __**SPLIT**__ (unless stated otherwise).", inline=False)
solakrules.add_field(name=" ", value=f"* Clusters and everything else are __**KEEPS**__ (unless stated otherwise).", inline=False)
solakrules.add_field(name=" ", value=f"* Being on voice chat is **__HIGLY ADVISED IF LEARNING/NEW TO THE BOSS__**", inline=False)
solakrules.add_field(name=" ", value=f"* If you are newer to Solak we recommend checking out a **[Basic Solak Guide](https://pvme.io/pvme-guides/basic-guides/solak-basic/)**", inline=False)

osolakrules_dict = solakrules.to_dict()
solakrules_dict = copy.deepcopy(osolakrules_dict)


#endregion

#region  Croesus embeds

croedescription_values = ["# Croesus", " ", "**[Basic Croesus Guide](https://pvme.io/pvme-guides/rs3-full-boss-guides/croesus/croesus/)**"]
croecombined_discription = "\n".join(croedescription_values)

croeembed = discord.Embed(description=(croecombined_discription), color=discord.Color.random(), timestamp=datetime.now())
croeembed.set_thumbnail(url=("https://runescape.wiki/images/thumb/Croesus.png/1024px-Croesus.png?b260c"))
croeembed.add_field(name="⏰ Start Time", value=f"Click '⏰ Set Time' to set a start time", inline=False)
croeembed.add_field(name="💬 Comments:", value=f"Click '💬 Add Comment' to add any additional comments", inline=False)
croeembed.add_field(name="🦋 Hunter", value=f"`Empty`", inline=True)
croeembed.add_field(name="🪓 Woodcutting", value=f"`Empty`", inline=True)
croeembed.add_field(name="⛏️ Mining", value=f"`Empty`", inline=True) 
croeembed.add_field(name="🎣 Fishing", value=f"`Empty`", inline=True) 
croeembed.add_field(name="**RULES:**", value=f"<#1271568914538827807>\n**All drops are KEEPS** *(unless stated otherwise and agreed upon)*", inline=False) 

ocroe_dict = croeembed.to_dict()
croe_dict = copy.deepcopy(ocroe_dict)


croerules = discord.Embed(description=(f"# Croesus Rules"), color=discord.Color.random())
croerules.set_thumbnail(url=("https://runescape.wiki/images/thumb/Croesus.png/1024px-Croesus.png?b260c"))
croerules.add_field(name=" ", value=f"* All drops are __**KEEPS**__ (unless stated otherwise).", inline=False)
croerules.add_field(name=" ", value=f"* Being on voice chat is **__HIGLY ADVISED IF LEARNING/NEW TO THE BOSS__**", inline=False)
croerules.add_field(name=" ", value=f"* If you are newer to Croesus we recommend checking out a **[Basic Croesus Guide](https://pvme.io/pvme-guides/rs3-full-boss-guides/croesus/croesus/)**", inline=False)

ocroerules_dict = croerules.to_dict()
croerules_dict = copy.deepcopy(ocroerules_dict)

#endregion

#region  Zammy embeds

zammyoriginal_values = [f"`Empty`", f"`Empty`", f"`Empty`"]
zammydescription_values = ["# Zamorak", " ", "**[Basic Zamorak Guide](https://pvme.io/pvme-guides/basic-guides/zamorak-basic/)**"]
zammycombined_discription = "\n".join(zammydescription_values)
zammycombined_value = ", ".join(zammyoriginal_values)

zammyembed = discord.Embed(description=(zammycombined_discription), color=discord.Color.random(), timestamp=datetime.now())
zammyembed.set_thumbnail(url=("https://runescape.wiki/images/Zamorak%2C_Lord_of_Chaos.png?c087a"))
zammyembed.add_field(name="⏰ Start Time", value=f"Click '⏰ Set Time' to set a start time", inline=False)
zammyembed.add_field(name="💬 Comments:", value=f"Click '💬 Add Comment' to add any additional comments", inline=False)
zammyembed.add_field(name="🛡️ Base", value=f"`Empty`", inline=True)
zammyembed.add_field(name="🧙‍♀️ Witch", value=f"`Empty`", inline=True)
zammyembed.add_field(name="⭕ Pads", value=f"`Empty`", inline=True) 
zammyembed.add_field(name="⚔️ DPS", value=zammycombined_value, inline=True)  
zammyembed.add_field(name="**RULES:**", value=f"<#1271568914538827807>\n**All drops are KEEPS** *(unless stated otherwise and agreed upon)*", inline=False)

ozammy_dict = zammyembed.to_dict()
zammy_dict = copy.deepcopy(ozammy_dict)


zammyrules = discord.Embed(description=(f"# Zamorak Rules"), color=discord.Color.random())
zammyrules.set_thumbnail(url=("https://runescape.wiki/images/Zamorak%2C_Lord_of_Chaos.png?c087a"))
zammyrules.add_field(name=" ", value=f"* All drops are __**KEEPS**__ (unless stated otherwise).", inline=False)
zammyrules.add_field(name=" ", value=f"* Being on voice chat is **__HIGLY ADVISED IF LEARNING/NEW TO THE BOSS__**", inline=False)
zammyrules.add_field(name=" ", value=f"* If you are newer to Zamorak we recommend checking out a **[Basic Zamorak Guide](https://pvme.io/pvme-guides/basic-guides/zamorak-basic/)**", inline=False)

ozammyrules_dict = zammyrules.to_dict()
zammyrules_dict = copy.deepcopy(ozammyrules_dict)

#endregion

#region  sanctum of rebirth

sororiginal_values = [f"`Empty`", f"`Empty`", f"`Empty`"]
sordescription_values = ["# Sanctum of Rebirth", " ", "**[Sanctum of Rebirth HM Guide](https://pvme.io/pvme-guides/rs3-full-boss-guides/sanctum/sanctum-hm-mechanics-overview/)**"]
sorcombined_discription = "\n".join(sordescription_values)
sorcombined_value = ", ".join(sororiginal_values)

sorembed = discord.Embed(description=(sorcombined_discription), color=discord.Color.random(), timestamp=datetime.now())
sorembed.set_thumbnail(url=("https://cdn.runescape.com/assets/img/external/news/2024/07/sanctumheader.jpg"))
sorembed.add_field(name="⏰ Start Time", value=f"Click '⏰ Set Time' to set a start time", inline=False)
sorembed.add_field(name="💬 Comments:", value=f"Click '💬 Add Comment' to add any additional comments", inline=False)
sorembed.add_field(name="🛡️ Base", value=f"`Empty`", inline=True)
sorembed.add_field(name="⚔️ DPS", value=sorcombined_value, inline=True) 
sorembed.add_field(name="**RULES:**", value=f"<#1271568914538827807>\n**All drops are KEEPS** *(unless stated otherwise and agreed upon)*", inline=False)


osor_dict = sorembed.to_dict()
sor_dict = copy.deepcopy(osor_dict)


sorrules = discord.Embed(description=(f"# Sanctum of Rebirth Rules"), color=discord.Color.random())
sorrules.set_thumbnail(url=("https://cdn.runescape.com/assets/img/external/news/2024/07/sanctumheader.jpg"))
sorrules.add_field(name="WORK IN PROGRESS", value=f"*These rules and the sign-up sheet are subject to change as we learn more*", inline=False)
sorrules.add_field(name=" ", value=f"* All drops are __**KEEPS**__ (unless stated otherwise).", inline=False)
sorrules.add_field(name=" ", value=f"* Being on voice chat is **__HIGLY ADVISED IF LEARNING/NEW TO THE BOSS__**", inline=False)
sorrules.add_field(name=" ", value=f"* If you are newer to Sanctum of Rebirth we recommend checking out a **[Sanctum of Rebirth HM Guide](https://pvme.io/pvme-guides/rs3-full-boss-guides/sanctum/sanctum-hm-mechanics-overview/)**", inline=False)

osorrules_dict = sorrules.to_dict()
sorrules_dict = copy.deepcopy(osorrules_dict)
#endregion

#region  gate of elidinis
goeoriginal_values = [f"`Empty`", f"`Empty`", f"`Empty`", f"`Empty`", f"`Empty`", f"`Empty`", f"`Empty`", f"`Empty`", f"`Empty`", f"`Empty`"]
goedescription_values = ["# Gate of Elidinis", " ", "**Guide coming soon tm**"]
goecombined_discription = "\n".join(goedescription_values)
goecombined_value = ", ".join(goeoriginal_values)

goeembed = discord.Embed(description=(goecombined_discription), color=discord.Color.random(), timestamp=datetime.now())
goeembed.set_thumbnail(url=("https://runescape.wiki/images/The_Gate_of_Elidinis.png?a7cbb"))
goeembed.add_field(name="⏰ Start Time", value=f"Click '⏰ Set Time' to set a start time", inline=False)
goeembed.add_field(name="💬 Comments:", value=f"Click '💬 Add Comment' to add any additional comments", inline=False)
goeembed.add_field(name="⚔️ DPS", value=goecombined_value, inline=True) 
goeembed.add_field(name="**RULES:**", value=f"<#1271568914538827807>\n**All drops are KEEPS** *(unless stated otherwise and agreed upon)*", inline=False)


ogoe_dict = goeembed.to_dict()
goe_dict = copy.deepcopy(ogoe_dict)


goerules = discord.Embed(description=(f"# Gate of Elidinis Rules"), color=discord.Color.random())
goerules.set_thumbnail(url=("https://runescape.wiki/images/The_Gate_of_Elidinis.png?a7cbb"))
goerules.add_field(name="WORK IN PROGRESS", value=f"*These rules and the sign-up sheet are subject to change as we learn more*", inline=False)
goerules.add_field(name=" ", value=f"* All drops are __**KEEPS**__ (unless stated otherwise).", inline=False)
goerules.add_field(name=" ", value=f"* Being on voice chat is **__HIGLY ADVISED IF LEARNING/NEW TO THE BOSS__**", inline=False)
goerules.add_field(name=" ", value=f"* If you are newer to Gate of Elidinis we recommend checking out a **Guide coming soon tm**", inline=False)

ogoerules_dict = goerules.to_dict()
goerules_dict = copy.deepcopy(ogoerules_dict)
#endregion

#region  elite dungeons
edsoriginal_values = [f"`Empty`", f"`Empty`", f"`Empty`"]
edsdescription_values = ["# Elite Dungeons", " ", ""]
edscombined_discription = "\n".join(edsdescription_values)
edscombined_value = ", ".join(edsoriginal_values)

edsembed = discord.Embed(description=(edscombined_discription), color=discord.Color.random(), timestamp=datetime.now())
edsembed.set_thumbnail(url=("https://runescape.wiki/images/Seiryu_the_Azure_Serpent.png?932ac"))
edsembed.add_field(name="⏰ Start Time", value=f"Click '⏰ Set Time' to set a start time", inline=False)
edsembed.add_field(name="💬 Comments:", value=f"Click '💬 Add Comment' to add any additional comments", inline=False)
edsembed.add_field(name="⚔️ DPS", value=edscombined_value, inline=True) 
edsembed.add_field(name="**RULES:**", value=f"<#1271568914538827807>\n**All drops are KEEPS** *(unless stated otherwise and agreed upon)*", inline=False)


oeds_dict = edsembed.to_dict()
eds_dict = copy.deepcopy(oeds_dict)


edsrules = discord.Embed(description=(f"# Elite Dungeon Rules"), color=discord.Color.random())
edsrules.set_thumbnail(url=("https://runescape.wiki/images/Seiryu_the_Azure_Serpent.png?932ac"))
edsrules.add_field(name="WORK IN PROGRESS", value=f"*These rules and the sign-up sheet are subject to change as we learn more*", inline=False)
edsrules.add_field(name=" ", value=f"* All drops are __**KEEPS**__ (unless stated otherwise).", inline=False)
edsrules.add_field(name=" ", value=f"* Being on voice chat is **__HIGLY ADVISED IF LEARNING/NEW TO THE BOSS__**", inline=False)
edsrules.add_field(name=" ", value=f"* If you are newer to Gate of Elidinis we recommend checking out a **Guide coming soon tm**", inline=False)

oedsrules_dict = edsrules.to_dict()
edsrules_dict = copy.deepcopy(oedsrules_dict)
#endregion

#region  amascut (normal mode)
amaiginal_values = [f"`Empty`", f"`Empty`"]
amasdescription_values = ["# Amascut, the Devourer (NM)", " ", "**Guide currently unavailable**"]
amascombined_discription = "\n".join(amasdescription_values)
amascombined_value = ", ".join(amaiginal_values)

amasembed = discord.Embed(description=(amascombined_discription), color=discord.Color.random(), timestamp=datetime.now())
amasembed.set_thumbnail(url=("https://runescape.wiki/images/Amascut%2C_the_Devourer.png?8c814"))
amasembed.add_field(name="⏰ Start Time", value=f"Click '⏰ Set Time' to set a start time", inline=False)
amasembed.add_field(name="💬 Comments:", value=f"Click '💬 Add Comment' to add any additional comments", inline=False)
amasembed.add_field(name="🛡️ Base", value=f"`Empty`", inline=True)
amasembed.add_field(name="↖️ West Scarabs", value=f"`Empty`", inline=True) 
amasembed.add_field(name="↙️ West Chains", value=f"`Empty`", inline=True) 
amasembed.add_field(name="↗️ East Scarabs", value=f"`Empty`", inline=True) 
amasembed.add_field(name="↘️ East Chains", value=f"`Empty`", inline=True)
amasembed.add_field(name="🟩 Green Lines", value=amascombined_value, inline=True)
amasembed.add_field(name="**RULES:**", value=f"<#1271568914538827807>\n**All drops are SPLITS *(for now)*** *(unless stated otherwise and agreed upon)*", inline=False)


oamas_dict = amasembed.to_dict()
amas_dict = copy.deepcopy(oamas_dict)


amasrules = discord.Embed(description=(f"# Amascut, the Devourer Rules"), color=discord.Color.random())
amasrules.set_thumbnail(url=("https://runescape.wiki/images/Amascut%2C_the_Devourer.png?8c814"))
amasrules.add_field(name="WORK IN PROGRESS", value=f"*These rules and the sign-up sheet are subject to change as we learn more*", inline=False)
amasrules.add_field(name=" ", value=f"* All drops are __**SPLITS**__ (unless stated otherwise).", inline=False)
amasrules.add_field(name=" ", value=f"* Being on voice chat is **__HIGLY ADVISED IF LEARNING/NEW TO THE BOSS__**", inline=False)
amasrules.add_field(name=" ", value=f"* If you are newer to Amascut we recommend checking out a **Guide currently unavailable**", inline=False)

oamasrules_dict = amasrules.to_dict()
amasrules_dict = copy.deepcopy(oamasrules_dict)
#endregion

#region  amascut (enraged mode)
hmamaiginal_values = [f"`Empty`", f"`Empty`"]
hmamasdescription_values = ["# Amascut, the Devourer (Enraged)", " ", "**Guide currently unavailable**"]
hmamascombined_discription = "\n".join(hmamasdescription_values)
hmamascombined_value = ", ".join(hmamaiginal_values)

hmamasembed = discord.Embed(description=(hmamascombined_discription), color=discord.Color.random(), timestamp=datetime.now())
hmamasembed.set_thumbnail(url=("https://runescape.wiki/images/Amascut%2C_the_Devourer.png?8c814"))
hmamasembed.add_field(name="⏰ Start Time", value=f"Click '⏰ Set Time' to set a start time", inline=False)
hmamasembed.add_field(name="💬 Comments:", value=f"Click '💬 Add Comment' to add any additional comments", inline=False)
hmamasembed.add_field(name="🛡️ Base", value=f"`Empty`", inline=True)
hmamasembed.add_field(name="↖️ West Scarabs", value="`Empty`", inline=True) 
hmamasembed.add_field(name="↙️ West Chains", value="`Empty`", inline=True) 
hmamasembed.add_field(name="↗️ East Scarabs", value="`Empty`", inline=True) 
hmamasembed.add_field(name="↘️ East Chains", value="`Empty`", inline=True) 
hmamasembed.add_field(name="🟩 Green Lines", value=amascombined_value, inline=True) 
hmamasembed.add_field(name="⤴️ Platformer (sub 2k)", value="`Empty`", inline=True) 
hmamasembed.add_field(name="🔣 Heiroglyphs", value="`Empty`", inline=True) 
hmamasembed.add_field(name="**RULES:**", value=f"<#1271568914538827807>\n**All drops are SPLITS *(for now)*** *(unless stated otherwise and agreed upon)*", inline=False)


hmoamas_dict = hmamasembed.to_dict()
hmamas_dict = copy.deepcopy(hmoamas_dict)
#endregion

