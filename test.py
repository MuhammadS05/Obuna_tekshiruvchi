import telebot


bot = telebot.TeleBot("BOT TOKEN")


channel_id = "KANAL ID'si"
channel_username = "KANAL username"

#obunachilar nomli dict ochib olinadi
obunachilar = {}

#obunani tekshiruvchi funksiya yoziladi (dekarator sifatida foydalanamiz)
def obuna_tekshiruvi(func):
    def obunalar(message):
        user_id = message.from_user.id
        if user_id in obunachilar:
            func(message)
        else:
            bot.reply_to(message, f"Siz kanalga obuna bo'lmagansiz!\nKanal: {channel_username}")
    return obunalar

#Foydalanuvchi botga start bosganda obunani tekshirib, mos javob qaytaradi
@bot.message_handler(commands=['start'])
@obuna_tekshiruvi
def start_xabari(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if obuna_bolgan(user_id):
        obunachilar[user_id] = True
        bot.send_message(chat_id, f"Assalomu alaykum {message.from_user.first_name}")
    else:
        bot.send_message(chat_id, f"Siz ushbu kanalga obuna bo'lmagansiz: {channel_username}")

#Foydalanuvchi obuna bo'lganini tasdiqlovchi/rad qiluvchi funksiya
def obuna_bolgan(user_id):
    try:
        obuna = bot.get_chat_member(channel_username, user_id)
        return obuna.status == 'member'
    except:
        return False


#Bunda ham istalgan matn yozilganda obunaga tekshiradi
@bot.message_handler(func=lambda message: True)
def istalgan_matn(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if obuna_bolgan(user_id):
        obunachilar[user_id] = True
        bot.send_message(chat_id, f"Botdan cheklovlarsiz foydalaning!")
    else:
        bot.send_message(chat_id, f"Siz ushbu kanalga obuna bo'lmagansiz: {channel_username}")

bot.polling()


#By M.M 
#Telegram Channel: @M_M_portfolio
