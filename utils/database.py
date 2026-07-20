import json
import os
import random


USERS_FILE = "database/users.json"



def load_users():

    if not os.path.exists(USERS_FILE):
        return []

    with open(USERS_FILE, "r") as file:
        return json.load(file)



def save_users(users):

    with open(USERS_FILE, "w") as file:
        json.dump(
            users,
            file,
            indent=4
        )



def create_anonymous_name():

    number = random.randint(100, 999)

    return f"Healing Soul #{number}"



def add_user(user_id, username, first_name):

    users = load_users()


    for user in users:

        if user["id"] == user_id:
            return user


    new_user = {

        "id": user_id,

        "username": username,

        "first_name": first_name,

        "anonymous_name": create_anonymous_name(),

        "stories_shared": 0,

        "comments_sent": 0,

        "support_given": 0

    }


    users.append(new_user)

    save_users(users)


    return new_user



def get_anonymous_name(user_id):

    users = load_users()


    for user in users:

        if user["id"] == user_id:

            return user["anonymous_name"]


    return "Healing Soul"
