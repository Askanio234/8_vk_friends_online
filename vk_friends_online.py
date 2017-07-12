import vk
import os
import getpass


APP_ID = os.getenv("APP_ID")
if not APP_ID:
    raise Exception("APP_ID should be specified as env variable")


def get_user_login():
    return input("Введите ваш логин: ")


def get_user_password():
    return getpass.getpass(prompt="Введите пароль: ")
    

def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope = "friends"
    )
    api = vk.API(session)
    return api.users.get(user_ids=api.friends.getOnline(), fields="first_name, last_name")


def output_friends_to_console(friends_online):
    for num, friend in enumerate(friends_online, start=1):
        print("{}. {} {}".format(num, friend["first_name"], friend["last_name"]))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
