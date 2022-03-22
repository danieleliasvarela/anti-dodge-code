import pyautogui as bot

bot.PAUSE = 2

bot.hotkey("alt", "tab")
bot.click("encontrarpartida.png")

# enquanto nao encontrar a imagem do botao de aceitar a partida
# o console devolve "PROCURANDO PARTIDA"
while bot.locateOnScreen('aceitar.png') == None:
    print('PROCURANDO PARTIDA')

# se o botao de aceitar partida aparecer, o bot aceita automaticamente
if bot.locateOnScreen('aceitar.png'):
    bot.click('aceitar.png')

# PARA CLIENT VERSAO 12.5