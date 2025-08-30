import discord
from util import buttons, functions
from util.functions import get_teamsize



class GoeMenu(discord.ui.View):
    labels_to_disable = ["Base", "DPS"]
    def __init__(self, client, boss):
            super().__init__(timeout=None)
            self.new_time = None
            self.client = client
            self.is_completed = False
            self.boss = boss
            self.add_item(buttons.CommentButton())
            self.add_item(buttons.PingButton())
            self.add_item(buttons.SetTime())
            self.add_item(buttons.CompleteButton())
            self.add_item(buttons.CloseButton())


#region dps button
    @discord.ui.button(label=f"DPS", style=discord.ButtonStyle.blurple, emoji="⚔️", custom_id="goedps")
    async def dpsbutton(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            user_mention = f"<@{interaction.user.id}> ({interaction.user.name})"
            embed = interaction.message.embeds[0]
            embed_dict = embed.to_dict()
            teamsize = get_teamsize(embed)
            dps_field = embed_dict['fields'][2]['value'].split(", ")

            if len(teamsize) == 10 and user_mention not in teamsize:
                await interaction.response.send_message(f"Looks like the team may be full!", ephemeral=True)
                return
            if user_mention in dps_field:
                functions.team_removeuser(dps_field, user_mention)
                new_field = ", ".join(dps_field)
                embed.set_field_at(2, name="⚔️ DPS", value=new_field, inline=True)
                embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(get_teamsize(embed))}/10")
                await interaction.response.edit_message(embed=embed)
                return
            elif all(field != "`Empty`" for field in dps_field):
                await interaction.response.send_message("There is no more room for ⚔️ DPS", ephemeral=True)
                return

            functions.team_adduser(dps_field, user_mention)
            new_field = ", ".join(dps_field)
            embed.set_field_at(2, name="⚔️ DPS", value=new_field, inline=True)
            embed.set_footer(text=f"Message ID: {interaction.message.id}  •  Team size {len(get_teamsize(embed))}/10")
            await interaction.response.edit_message(embed=embed)
        except Exception as e:
            print(f"dpsbutton error(GoeMenu): {e}")
#endregion
