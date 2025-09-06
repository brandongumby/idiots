#region  imports
# Standard library
from datetime import datetime, timezone

# Third-party libraries
import discord
from discord.ui import Button

# custom modules
from util import myviews, config, functions, modals

#endregion


#region CommentButton
class CommentButton(discord.ui.Button):
    def __init__(self):
        label = f"💬 Add Comment"
        super().__init__(label=label, style=discord.ButtonStyle.gray, custom_id="add_comment")

    async def callback(self, interaction: discord.Interaction):
        try:
            author_name = f"Hosted by {interaction.user.name}"
            embed = interaction.message.embeds[0]
            
            if embed.author.name == f"Hosted by {interaction.user.name}" or interaction.user.guild_permissions.manage_messages:
                await interaction.response.send_modal(modals.CommentInputModal(author_name))
            else:
                await interaction.response.send_message("You are not the author of this embed or you don't have permission to set the time.", ephemeral=True)
        except Exception as e:
            print(f"CommentButton error(button): {e}")
#endregion

#region PingButton
class PingButton(discord.ui.Button):
    def __init__(self):
        label = f"❗ Ping Team"
        super().__init__(label=label, style=discord.ButtonStyle.gray, custom_id="pingbutton")

    async def callback(self, interaction: discord.Interaction):
        try:
            embed = interaction.message.embeds[0]
            mention_string = " ".join(functions.remove_parentheses(item) for item in functions.get_teamsize(embed))

            pingembed = discord.Embed(title="PVM Hour Starting!")
            pingembed.add_field(name="Get Ready!", value=f"We are starting the hour soon!")
            pingembed.set_thumbnail(url=embed.thumbnail.url)

            if embed.author.name == f"Hosted by {interaction.user.name}" or interaction.user.guild_permissions.manage_messages:
                if len(functions.get_teamsize(embed)) != 0:
                    self.disabled = True
                    self.style = discord.ButtonStyle.secondary

                    await interaction.response.edit_message(embed=embed, view=self.view)
                    if interaction.guild_id == config.GUILD_ID:
                        target_channel = interaction.guild.get_channel(config.DISCUSSION_CHANNEL)
                    else:
                        target_channel = interaction.channel
                    await target_channel.send(f"{mention_string}", embed=pingembed)
                else:
                    await interaction.response.send_message("You can't ping a team with no one on it.", ephemeral=True)
            else:
                await interaction.response.send_message("You are not the author of this embed or you don't have permissions to ping the team.", ephemeral=True) 
        except Exception as e:
            print(f"PingButton error(button): {e}")
#endregion

#region SetTime
class SetTime(discord.ui.Button):
    def __init__(self):
        label = f"⏰ Set Time"
        super().__init__(label=label, style=discord.ButtonStyle.gray, custom_id="set_time")

    async def callback(self, interaction: discord.Interaction):
        try:
            author_name = f"Hosted by {interaction.user.name}"
            embed = interaction.message.embeds[0]
            
            if embed.author.name == f"Hosted by {interaction.user.name}" or interaction.user.guild_permissions.manage_messages:
                modal = modals.TimeInputModal(author_name, interaction.client, self.view.boss)
                await interaction.response.send_modal(modal)
                await modal.wait()
                self.new_time = modal.result
            else:
                await interaction.response.send_message("You are not the author of this embed or you don't have permission to set the time.", ephemeral=True)
        except Exception as e:
            print(f"SetTime error(button): {e}")
#endregion

#region CompleteButton
class CompleteButton(discord.ui.Button):
    def __init__(self):
        label = f"✅ Complete"
        super().__init__(label=label, style=discord.ButtonStyle.green, custom_id="complete_button")

    async def callback(self, interaction: discord.Interaction):
        try:
            embed = interaction.message.embeds[0]
            if embed.author.name == f"Hosted by {interaction.user.name}" or interaction.user.guild_permissions.manage_messages:
                if not self.view.is_completed:
                    for item in self.view.children:
                        if isinstance(item, Button) and item.label in self.view.labels_to_disable:
                            item.disabled = True
                    self.view.is_completed = True
                    self.label = " Re-open"
                    self.style = discord.ButtonStyle.green
                    self.emoji = "🔓"
                else:
                    for item in self.view.children:
                        if isinstance(item, Button) and item.label in self.view.labels_to_disable:
                            item.disabled = False
                    self.view.is_completed = False
                    self.label = " Complete"
                    self.style = discord.ButtonStyle.green
                    self.emoji = "✅"
                await interaction.response.edit_message(embed=embed, view=self.view)
            else:
                await interaction.response.send_message("You are not the author of this embed or you don't have permission to complete this.", ephemeral=True)
        except Exception as e:
            print(f"CompleteButton error(button): {e}")
#endregion

#region CloseButton
class CloseButton(discord.ui.Button):
    def __init__(self):
        label = f"⛔ Close"
        super().__init__(label=label, style=discord.ButtonStyle.red, custom_id="close_button")

    async def callback(self, interaction: discord.Interaction):
        try:
            confirmation_view = myviews.ConfirmationView(interaction)
            now_unix = int(datetime.now(timezone.utc).timestamp())
            created_at = int(interaction.message.created_at.timestamp())
            if self.view.new_time is None:
                self.view.new_time = created_at + 86400
            embed = interaction.message.embeds[0]
            finished_time = self.view.new_time + 86400
            if now_unix > finished_time:
                await interaction.response.send_message("Are you sure you want to delete this message?", view=confirmation_view, delete_after=3)
            elif embed.author.name == f"Hosted by {interaction.user.name}" or interaction.user.guild_permissions.manage_messages:
                await interaction.response.send_message("Are you sure you want to delete this message?", view=confirmation_view, delete_after=3)
            else:
                await interaction.response.send_message("You are not the author of this embed or you don't have permission to close this.", ephemeral=True)
        except Exception as e:
            print(f"CloseButton error(button): {e}")
#endregion


