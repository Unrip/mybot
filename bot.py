from telegram.ext import Updater, CommandHandler


def greet_user(update, context):
	print('Вызван /start')
	update.message.reply_text('Hello, {user_name}!')

def main():
	mybot = Updater('1110531499:AAGz523yCnbjBdfKxclekS57er24dx8LaB4', use_context=True)
	
	dp = mybot.dispatcher
	dp.add_handler(CommandHandler("start", greet_user))
	
	mybot.start_polling()
	mybot.idle()
	
	
if __name__ == "__main__":
	main()
	