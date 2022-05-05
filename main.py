import random
import time

from faker import Faker
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

token = "cca857c898cddf36df64b23b6cb96ee9cfd86b19aaa976c065a3bd969db24738f4b6ecae6dc9802d120eb"

fake = Faker("ru_RU")
vk = vk_api.VkApi(token=token)
vk._auth_token()

arrayOfPhotos = ["2V3bS4ANsX30c9F2XXJV2a-46nArfOHcx_Bm7MM2hgCPkJzHGkHgvW1hnP7zGB55nLHC4v80zwv2c97EIE0sMD-g.jpg",
                 "7jRwiMDBnQBimPZPeLWH1lncoYG1bxX58F6hgqJ2-DaeYWCO6odyrBKthosLmppj9vZFbKc-w6L8ZfQ3gAlfrfmd.jpg",
                 "ATkWy2A-ZI3KJ1kuI3GhoZa8sPUcGTnsDbeZJj9n6gD4bpPNAouyHQc7iEmKJNzFfMzngufDaiBVBDj7nENGJTLP.jpg",
                 "clickbeat.jpg",
                 "fKLYIoPwoAs9ZC0t47tDXyhJ-_ec6MFtcBIH6DxNLUkpi6Ho3qFRXLKi5nFKVzEGxLPIju_ch-PTHSbrNBWc6Sgr.jpg",
                 "Gpq0hsNyhLzcSgN73a-ZIqw4FYvXpxa6jTD5iHtFh7oCNIu_z-iv4Y8FbTit2Lhtx5DQAq7UvRrZuFwUApEXXhKk.jpg",
                 "KyEl9PUKOzJTVm59HNDsMgUgJZwga_R1s4dNgX1-B1iWIMB6pM_qTz9kapqBTuh-KzXnO4bUGosrqBJtHenRGhtX.jpg",
                 "nek3cZUUsC6TF7QLn5m_y7YDZB4AJXbG7HQnFJ5RpEhf7yQw34NQ-ULGMr8lQmLHZhVDyX9KrQjmrStdqLNKUkgm.jpg",
                 "Pv-yKS_l68k7OJxez2Jv5BO9H40RsfDt5CjIzInU1-pj5WjHPdrS8sAZm1QAz-fvx696jAEBNy6fD3FXHxHCW77K.jpg",
                 "rEMZyyMWBolJLO31zwK5z5IA_Tig_m8c6O1zhrRtJ1-CPUA7TtmQuP6jmojKY5WTVW-k-dTBhz-JSLaDfCHw1pFv.jpg",
                 "Uv1Y6TPdGg2ZuEECNdNdc3lzS8fc4y_yPcTwnR8LAM43SPmesuDtGF4dFSZRNAubkDixistGZsuvaPmwhdaSbI4y.jpg"]


def send_message(message, user_id, keyboard=None):
    post = {"user_id": user_id, "message": message,
                                "random_id": random.randint(1, 1000)}
    if keyboard!=None:
        post["keyboard"] = keyboard.get_keyboard()
    else:
        post=post
    vk.method("messages.send", post)


while True:
    messages = vk.method("messages.getConversations", {"offset":0, "count":20, "filter":"unanswered"})
    if messages["count"] > 1:
        text = messages['items'][0]["last_message"]["text"]
        user_id = messages['items'][0]["last_message"]["from_id"]
        print(text)
        if text.lower() == "привет":
            send_message("Хай!", user_id)
        elif text.lower() == "хочу поболтать" or text.lower() == "ответь":
            answerFromMe = input()
            send_message(answerFromMe, user_id)
        elif text.lower() == "рандом":
            send_message(random.randint(1, 1000), user_id)
        elif text.lower() == "😳":
            send_message("софа не удивляйся) это очевидно)ты предсказуема", user_id)
        elif text.lower() == "рандом фио":
            fake_name = fake.name()
            send_message(fake_name, user_id)
        elif text.lower() == "вика":
            send_message("Затролил🗿. Ты хорни?", user_id)
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
            send_message("Команды в боте: \n"
                                                                       "1) рандом ---> генерация рандомного числа\n"
                                                                       "2) рандом фио---> фейковое имя, "
                                                                       "фамилия, отчество\n"
                                                                       "3) хочу поболтать(ответь) ---> "
                                                                       "Диалог с разработчиком\n"
                                                                       "4)фото ---> Фотография", user_id)

        elif text.lower() == "фото":
            time.sleep(1)
            uploader = vk_api.upload.VkUpload(vk)
            img = uploader.photo_messages(arrayOfPhotos[random.randint(0, 10)])
            media_id = str(img[0]["id"])
            owner_id = str(img[0]["owner_id"])
            vk.method("messages.send", {"user_id":user_id, "attachment":"photo" + owner_id + "_" + media_id,
                                    "random_id":random.randint(1, 1000)})
        elif text.lower() == "start":
            keyboard = VkKeyboard(one_time=True)
            iButton = "button"
            keyboard.add_button(label=iButton, color=VkKeyboardColor.PRIMARY)
            send_message("Первая кнопка", user_id)

        else:
            time.sleep(5)
            send_message("Капец я Арсений, я хз что вы мне пишете."
                            " Но я все равно это прочитал))"
                            " 'Помощь' ---> выводит список команд", user_id)

