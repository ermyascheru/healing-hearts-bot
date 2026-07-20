import json
import os
import uuid
from datetime import datetime


STORIES_FILE = "database/stories.json"



def load_stories():

    if not os.path.exists(STORIES_FILE):
        return []

    with open(STORIES_FILE, "r") as file:
        return json.load(file)



def save_stories(stories):

    with open(STORIES_FILE, "w") as file:
        json.dump(
            stories,
            file,
            indent=4
        )



def create_story(user_id, text, anonymous_name):

    stories = load_stories()
    story = {

    "id": str(uuid.uuid4()),

    "user_id": user_id,

    "anonymous_name": anonymous_name,

    "text": text,

    "date": str(datetime.now()),

    "status": "pending"
}

    stories.append(story)

    save_stories(stories)


    return story
def get_story_by_id(story_id):

    stories = load_stories()

    for story in stories:
        if story["id"] == story_id:
            return story

    return None
