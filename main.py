import vk_api
from random import choice, randrange
from vk_api.longpoll import VkLongPoll, VkEventType
TOKEN = 'vk1.a.I7elr2wQctj_2n1XxGL2_LQf1UrIryjGg-gwxBa6zNReQmDS_C9_0Bpprluez3jDy3PVPc66tBSZ1CJ5jTSBXngFAaEYyWRt4zzfvkY4vUbPtu95R3DGzB6xonWFQguD0-orpaFZSd1K5BMug1CZ9GboqulxbXHb40DeNEdLffxLH22aG03rI2NdVaAnM6bqnU-WJ1uE0NzeufY7WXksUw'
vk_session = vk_api.VkApi(token=TOKEN)
longpool = VkLongPoll(vk_session)
vk = vk_session.get_api()
vars = ['камень', 'ножн', 'бумага']
for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.text and event.to_me and event.text.lower() in vars:
        if event.from_user:
            vk.messages.send(user_id=event.user_id, message=choice(vars), random_id=randrange(1, 100000))
