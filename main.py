import json
import vk
from flask import Flask

app = Flask(__name__)
confirmation_token = '6d75c23e'
token = 'bddeddc0f08b56addc83768d464cea4246ecb5e1b2c9b5df894900aeb84dcec396cc77eae7a5b6062bd6f'
_wait_for_sender = []
sender_vkid = 0
app_id = 6630979

# @app.route('/', methods=['POST'])
# def processing():
#     #Распаковываем json из пришедшего POST-запроса
#     data = json.loads(request.data)
#     #Вконтакте в своих запросах всегда отправляет поле типа
#     if 'type' not in data.keys():
#         return 'not vk'
#     if data['type'] == 'confirmation':
#         return confirmation_token
#     elif data['type'] == 'message_new':

#         session = vk.Session()
#         api = vk.API(session, v=5.0)
#         user_id = data['object']['user_id']
#         message = data['object']['title']

#         if message == 'ok':
#             sender_vkid = user_id
#         elif message == 'send me':
#             api.send_message(sender_vkid, token, 'lol')
#         else:
#             response = 'Я на отправил запрос к {0}. Необходимо зайти на эту страницу и подтвердить добавление.'.format(message)

#             auth_link = '''https://oauth.vk.com/authorize?client_id={app_id}
#                                &scope=photos,audio,video,docs,notes,pages,status,
#                                offers,questions,wall,groups,messages,email,
#                                notifications,stats,ads,offline,docs,pages,stats,
#                                notifications&response_type=token '''.format(app_id=app_id) # TODO INSERT CORRECT TOKEN

#             api.send_message(message, token,
#                                'Вашу страницу добавляют для рассылки, '
#                                'для подтверждения этого надо пройти по этой ссылке {0}, '
#                                'скопировать ссылку из адресной строки и отправить мне обратно.'
#                                .format(auth_link))

#             _wait_for_sender.append(message)

#         return 'ok'

@app.route('/', methods=['POST'])
def processing():
    return 'lol'
    session = vk.Session()
    api = vk.API(session, v=5.0)
    api.send_message(481116745, token, 'Это я')
    return 'ok'
    
    
    user_id = data['object']['user_id']
    message = data['object']['title']
        
        #Распаковываем json из пришедшего POST-запроса
    data = json.loads(request.data)
    #Вконтакте в своих запросах всегда отправляет поле типа
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        session = vk.Session()
        api = vk.API(session, v=5.0)
        user_id = data['object']['user_id']
        api.messages.send(access_token=token, user_id=str(user_id), message='Привет, я новый бот!')
        # Сообщение о том, что обработка прошла успешно
        return 'ok'

@app.route('/')
def LOL():
    return 'hello'

app.run(debug=True)
