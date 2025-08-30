import discord
import io
import textwrap
import traceback
from contextlib import redirect_stdout
from util import config, functions, myviews, modals

class CodeModal(discord.ui.Modal, title="Execute Code"):
    code = discord.ui.TextInput(
        label="Python Code",
        style=discord.TextStyle.paragraph,
        placeholder="print('hello world')",
        required=True,
        max_length=2000,
    )

    async def on_submit(self, interaction: discord.Interaction):
        try:
            if interaction.user.id != config.OWNER:
                await interaction.response.send_message("⛔ You cannot use this.", ephemeral=True)
                return

            user = await functions.load_user(interaction.client, interaction.user.id, interaction.guild_id)
            async with interaction.client.db.cursor() as cursor:
                code = str(self.code)

                env = {
                    "cursor": cursor,
                    "default": user,
                    "client": interaction.client,
                    "guild_id": interaction.guild_id,
                    "channel": interaction.channel,
                    "discord": discord,
                    "interaction": interaction,
                    "functions": functions,
                    "myviews": myviews,
                    "modals": modals
                }

                body = "async def _func():\n" + textwrap.indent(code, "    ")

                stdout = io.StringIO()
                try:
                    exec(body, env)
                    func = env["_func"]

                    with redirect_stdout(stdout):
                        result = await func()
                except Exception:
                    error = traceback.format_exc()
                    return await interaction.response.send_message(f"Error: ```\n{error}\n```", ephemeral=True)

                output = stdout.getvalue()
                if result is not None:
                    output += f"\nReturn: {result}"

                if not output.strip():
                    output = "✅ Code executed successfully (no output)."

                # truncate if too long
                if len(output) > 1900:
                    output = output[:1900] + "... [truncated]"

                await interaction.response.send_message(f"```py\n{output}\n```", ephemeral=True)
        except Exception as e:
            print(f"CodeModal error: {e}")