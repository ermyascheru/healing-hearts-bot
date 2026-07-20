import json
import os


REACTION_FILE = "database/reactions.json"



def load_reactions():

    if not os.path.exists(REACTION_FILE):
        return []

    with open(REACTION_FILE, "r") as file:
        return json.load(file)



def save_reactions(data):

    with open(REACTION_FILE, "w") as file:
        json.dump(
            data,
            file,
            indent=4
        )



def add_reaction(story_id, user_id):

    reactions = load_reactions()


    for reaction in reactions:

        if (
            reaction["story_id"] == story_id
            and reaction["user_id"] == user_id
        ):
            return False


    reactions.append({
        "story_id": story_id,
        "user_id": user_id
    })


    save_reactions(reactions)

    return True



def count_reactions(story_id):

    reactions = load_reactions()

    count = 0

    for reaction in reactions:

        if reaction["story_id"] == story_id:
            count += 1

    return count
