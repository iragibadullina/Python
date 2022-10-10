import telebot, datetime, time, math, re
from telebot import types

BOT_TOKEN = '5571877343:AAGxVVBv9JHOBweac1Cq-HkI-iQKq6SpkD4' 
BOT_NAME = 'calc_bot34' 
bot = telebot.TeleBot(BOT_TOKEN)

START_MESSAGE = """(Введите выражение)"""
# Сообщение поддержки
HELP_MESSAGE = """Мной пользоваться очень просто. Вы мне отправляете выражение, а я вам возвращаю его результат.
***Операторы***:
    + - сложение;
    - - вычитание;
    \* - умножение;
    / - деление;
    \*\* - возведение в степнь.
    
***Функции***:
    cos(x) - косинус x;
    sin(x) - синус x;
    tg(x) - тангенс x;
    fact(x) - факториал x;
    sqrt(x) - квадратный корень х;
    sqr(x) - х в квадрате."""

 
def fact(float_):
    return math.factorial(float_)

def cos(float_):
    return math.cos(float_)

def sin(float_):
    return math.sin(float_)

def tg(float_):
    return math.tan(float_)
    
def tan(float_):
    return math.tan(float_)

def send_start(message):
    print('%s (%s): %s' %(message.chat.first_name, message.chat.username, message.text))
    msg = None

    if message.text.lower() == '/start':
        msg = bot.send_message(message.chat.id, START_MESSAGE, parse_mode='markdown')

    elif message.text.lower() == '/help':
        msg = bot.send_message(message.chat.id, HELP_MESSAGE, parse_mode='markdown')
        
    if (msg):
        print('Бот: %s'%msg.text)

def answer_to_user(message):
    print('%s (%s): %s' %(message.chat.first_name, message.chat.username, message.text))
    msg = None

    user_message = message.text.lower()

    if BOT_NAME:
        regex = re.compile(BOT_NAME.lower())
        print(regex.search(user_message))
        if regex.search(user_message) == None:
            return

        regex = re.compile('%s[^a-z]'%(BOT_NAME.lower()))
        user_message = regex.sub("", user_message)

    user_message = user_message.lstrip()
    user_message = user_message.rstrip()
    
    print(user_message)

    if user_message == 'привет':
        msg = bot.send_message(message.chat.id, '*Привет, %s*'%(message.chat.first_name), parse_mode='markdown')

    elif user_message == 'помощь':
        msg = bot.send_message(message.chat.id, HELP_MESSAGE, parse_mode='markdown')

    if (msg):
        print('Бот: %s'%msg.text)

def inline_answer_to_user(inline_query):
    answer = 0
    answer_list = []
    try:
        answer = str(eval(inline_query.query.lower().replace(' ', '')))
        answer_to_send = answer.replace('*', '\*')
        query_to_send = inline_query.query.replace('*', '\*').lower().replace(' ', '')

        answer_list.append(types.InlineQueryResultArticle
        (
            id = 0,
            title = 'Отправить с выражением'
            description='%s = %s' % (inline_query.query, answer),
            input_message_content = types.InputTextMessageContent(
                message_text = '%s = *%s*' % (query_to_send, answer_to_send),
                parse_mode = 'markdown')         
        ))

        answer_list.append(types.InlineQueryResultArticle
        (
            id = 1,
            title = 'Отправить без выражения',
            description='%s' % (answer),
            input_message_content = types.InputTextMessageContent(
                message_text = '*%s*' % (answer_to_send),
                parse_mode = 'markdown'),
        ))
            
    except SyntaxError: answer = False
    except NameError: answer = False
    except TypeError: answer = False
    except ZeroDivisionError: answer = False

    if (not answer):    
        answer_list = []
        answer_list.append(types.InlineQueryResultArticle
        (
            id = 0,
            title = 'Калькулятор',
            description='start, \nhelp\n'
            input_message_content = types.InputTextMessageContent(message_text = 'начни заново')
        ))
    
    bot.answer_inline_query(inline_query.id, answer_list)


if (__name__ == '__main__'):
       bot.polling()
        