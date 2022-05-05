import random
from faker import Faker
import vk_api

token = "cca857c898cddf36df64b23b6cb96ee9cfd86b19aaa976c065a3bd969db24738f4b6ecae6dc9802d120eb"

fake = Faker("ru_RU")
vk = vk_api.VkApi(token=token)
vk._auth_token()

while True:
    messages = vk.method("messages.getConversations", {"offset":0, "count":20, "filter":"unanswered"})
    if messages["count"] > 1:
        text = messages['items'][0]["last_message"]["text"]
        user_id = messages['items'][0]["last_message"]["from_id"]
        print(text)
        if text.lower() == "привет":
            vk.method("messages.send", {"user_id": user_id, "message": "Хай",
                                        "random_id": random.randint(1, 1000)})
        elif text.lower() == "хочу поболтать" or text.lower() == "ответь":
            answerFromMe = input()
            vk.method("messages.send", {"user_id":user_id, "message":answerFromMe,
                                    "random_id":random.randint(1, 1000)})
        elif text.lower() == "рандом":
            vk.method("messages.send", {"user_id": user_id, "message": random.randint(1, 1000),
                                        "random_id": random.randint(1, 1000)})
        elif text.lower() == "😳":
            vk.method("messages.send", {"user_id": user_id, "message": "софа не удивляйся) это очевидно)"
                                                                       " ты предсказуема)",
                                        "random_id": random.randint(1, 1000)})
        elif text.lower() == "рандом фио":
            fake_name = fake.name()
            vk.method("messages.send", {"user_id": user_id, "message": fake_name,
                                        "random_id": random.randint(1, 1000)})
        elif text.lower() == "вика":
            vk.method("messages.send", {"user_id": user_id, "message": "Затролил🗿. Ты хорни?",
                                        "random_id": random.randint(1, 1000)})
        elif text.lower() == "помощь":
            fake_name = fake.name()
            vk.method("messages.send", {"user_id": user_id, "message": "Команды в боте: \n"
                                                                       "1) рандом ---> генерация рандомного числа\n"
                                                                       "2) рандом фио---> фейковое имя, "
                                                                       "фамилия, отчество\n"
                                                                       "3) хочу поболтать(ответь) ---> "
                                                                       "Диалог с разработчиком\n"
                                                                       "4)фото ---> Фотография",
                                        "random_id": random.randint(1, 1000)})
        elif text.lower() == "фото":
            uploader = vk_api.upload.VkUpload(vk)
            img = uploader.photo_messages("clickbeat.jpg")
            media_id = str(img[0]["id"])
            owner_id = str(img[0]["owner_id"])
            vk.method("messages.send", {"user_id":user_id, "attachment":"photo" + owner_id + "_" + media_id,
                                    "random_id":random.randint(1, 1000)})
        else:
            vk.method("messages.send", {"user_id":user_id, "message":"Капец я Арсений, я хз что вы мне пишете."
                                                                     " Но я все равно это прочитал))"
                                                                     " 'Помощь' ---> выводит список команд",
                                    "random_id":random.randint(1, 1000)})

