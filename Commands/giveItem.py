from Commands.sql.itens.select.takeItemId import takeItemId
from Commands.sql.itens.saveItenInInventary import saveItenInInventary
from Commands.sql.itens.select.takeItemQuant import takeItemQuant
from Commands.sql.itens.update.updateItensInInventary import updateItensInInventary

async def giveItem(ctx, player):
    msg = ctx.message.content
    _, item = msg.split(">")
    item = item.split(" ")
    itemList = [_ for _ in item if _ != '']
    item = itemList
    length = len(item)
    if (length <= 1):
        await ctx.send("Comando digitado incorretamente") 
        return
    
    amount = int(item[length-1])
    itemName = ""
    for _ in range(length-1):
        itemName += f"{item[_]} "
    itemName = itemName[:-1]
    try:
        itemId = takeItemId(itemName.lower())
        playerId = player.split("<@")[1][:-1]
        try:
            quant = int(takeItemQuant(playerId, itemId))
        except:
            quant = 0
        if(quant <= 0 or quant is None):
            saveItenInInventary(playerId, itemId, amount)
        else:
            updateItensInInventary(playerId, itemId, (amount + int(takeItemQuant(playerId, itemId))))
        await ctx.send("Item recebido com sucesso")

    except:
        await ctx.send(">>> Nenhum item encontrado")
    