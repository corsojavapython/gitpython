from telegram import Bot

# Inserisci il token del tuo bot Telegram
bot_token = 'CORSO PYTHON'

# Inizializza il bot
bot = Bot(token=bot_token)

# ID dell'utente a cui inviare il messaggio (puoi ottenere questo ID tramite il bot @userinfobot)
#user_id = 'USER_ID'

# Invia un messaggio privato all'utente
message_text = 'Questo è un messaggio privato da parte del tuo bot!'
#bot.send_message(chat_id=user_id, text=message_text)
bot.send_message(text=message_text)
print("Messaggio inviato con successo!")
