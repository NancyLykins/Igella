import discord
import Commands.status.statusButtons
from Commands.status.statusEmbeds.infosEmbed import infosEmbed
from Commands.status.statusEmbeds.inventaryEmbed import inventaryEmbed
from Commands.status.useMenu import useMenu
from Commands.status.equipMenu import equipMenu

async def showInventaryEmbed(interaction: discord.Interaction):
    playerId = interaction.user.id
    view = discord.ui.View(timeout=1800)
    embed, has = await inventaryEmbed(playerId)
    async def menuStatisticas(interaction: discord.Interaction):
        embed = await infosEmbed(interaction.user.id)
        await interaction.response.edit_message(embed=embed, view=Commands.status.statusButtons.infosButtons())
    
    statusButton = discord.ui.Button(label="Status", style=discord.ButtonStyle.success)
    statusButton.callback = menuStatisticas
    view.add_item(statusButton)
    
    for element in has:
        if(element == 'equipable' and has[element] == True):
            button = discord.ui.Button(label="Equipar", style=discord.ButtonStyle.primary)
            button.callback = equipMenu
            view.add_item(button)
            
        if(element == 'usable' and has[element] == True):
            button = discord.ui.Button(label="Usar", style=discord.ButtonStyle.red)
            button.callback = useMenu
            view.add_item(button)
    
    await interaction.response.edit_message(embed=embed, view=view)
