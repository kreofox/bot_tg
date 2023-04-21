import telebot
import webbrowser


from telebot import types 

bot = telebot.TeleBot("TOKEN_BOT")

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Go to the site " ,)
    markup.row(btn1)
    btn2 = types.KeyboardButton("Delete photo" ,)
    btn3 = types.KeyboardButton("Change the text " ,)
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, "Hello", reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

@bot.message_handler(commands=["photos"]) #sends a photo
def photo(message):
    file = open("./bot_tg/photo/ari.jpg", "rd")
    bot.send_photo(message.chat.id, file, )

@bot.message_handler(commands=["video"]) #sends a video
def audio(message):
    file = open("./bot_tg/audi/audio.mp4", "rd")
    bot.send_video(message.chat.id, file )

@bot.message_handler(commands=["Music"]) #send a musc
def music(message):
    file = open("./bot_tg/musc/musc.mp3")
    bot.send_audio(message.chat.id, file)

def on_click(message):
    if message.text == "Go to the site":
        webbrowser.open("http//")
    elif message.text == "Delete photo ":
        bot.send_message(message.chat.id, "Delet photo")
    elif message.text == "Change the text ":
        bot.send_message(message.chat.id, "Change the text ")
    

@bot.message_handler(content_types=["photo"])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Go to the site" , url="https://")
    markup.row(btn1)
    btn2 =types.InlineKeyboardButton("Delet photo", callback_data="delete")
    btn3 =types.InlineKeyboardButton("Change the text ", callback_data="edit")
    markup.row(btn2, btn3) 
    bot.reply_to(message, "What a beautiful picture!", reply_markup = markup)


@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    if callback.data == "delete":
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == "edit":
        bot.edit_message_text("Edit text", callback.message.chat.id, callback.message.message_id)



#-1 - removes before communication 
#row - button design
#callback_data - performs the values 
#InlineKeyboardMarkup - adds markup  
#InlineKeyButton - adds a button 
bot.polling(none_stop = True)