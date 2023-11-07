import telebot
import os
from dotenv import load_dotenv
import model

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)
bot.set_webhook()

@bot.message_handler(commands=['start'])
def start(message):
    """
    Bot will introduce itself upon /start command, and prompt user for his request
    """
    try:
        # Start bot introduction
        disclaimer= "Disclaimer: \n\n This chatbot provides information and mental wellness support for migrant workers in Singapore. Your data will be collected for the purposes of this chatbot and in accordance with OpenAi’s privacy policy. Do exercise discretion. We do not provide professional advice and our information may not be accurate, it is recommended to still consult experts or local resources. Healthserve will not be liable for any losses or damage incurred as a result of the information provided or collected.\n Your use of this chatbot signifies your agreement with these terms."
        bot.send_message(message.chat.id, disclaimer)

        disclaimer_ben = "দাবিত্যাগ: \n\n এই চ্যাটবটটি সিঙ্গাপুরে অভিবাসী কর্মীদের জন্য তথ্য এবং মানসিক সুস্থতা সহায়তা প্রদান করে। আপনার ডেটা এই চ্যাটবটের উদ্দেশ্যে এবং OpenAI-র গোপনীয়তা নীতি অনুসারে সংগ্রহ করা হবে। দয়া করে সতর্ক থাকুন। আমরা পেশাদার পরামর্শ প্রদান করি না এবং আমাদের তথ্য সঠিক না হতে পারে, এটি এখনও বিশেষজ্ঞ বা স্থানীয় সম্পদের সাথে পরামর্শ করার সুপারিশ করা হয়। প্রদত্ত বা সংগ্রহ করা তথ্যের ফলে যে কোন ক্ষতি বা ক্ষতির জন্য Healthserve দায়ী থাকবে না।\nএই চ্যাটবট ব্যবহার করার মাধ্যমে আপনি এই শর্তাবলী সাথে আপনার সম্মতি প্রকাশ করতে বলে।"
        bot.send_message(message.chat.id, disclaimer_ben)

        start_message = "Hello! I am HealthBuddy. I am here to answer your questions about healthcare coverage of migrant workers. Ask away!"
        bot.send_message(message.chat.id, start_message)

        start_message_ben = "হ্যালো! আমি হেলথবাডি। আমি পরবাসী শ্রমিকদের স্বাস্থ্যসেবা সংকলন সম্পর্কে আপনার প্রশ্নে উত্তর দিতে এখানে আছি! প্রশ্ন করুন!"
        bot.send_message(message.chat.id, start_message_ben)

    except Exception as e:
        bot.send_message(
            message.chat.id, 'Sorry, something seems to gone wrong! Please try again later!\nদুঃখিত, কিছু ভুল হয়েছে বলে মনে হচ্ছে! অনুগ্রহ করে একটু পরে আবার চেষ্টা করুন!')


@bot.message_handler(content_types=['text'])
def send_text(message):
    response = model.getResponse(message.text)
    bot.send_message(message.chat.id, response)

def main():
    """Runs the Telegram Bot"""
    print('Loading configuration...') # Perhaps an idea on what you may want to change (optional)
    print('Successfully loaded! Starting bot...')
    bot.infinity_polling()


if __name__ == '__main__':
    main()