import json
import os
import uuid
from datetime import datetime


COMMENTS_FILE = "database/comments.json"



def load_comments():

    if not os.path.exists(COMMENTS_FILE):
        return []

    with open(COMMENTS_FILE, "r") as file:
        return json.load(file)



def save_comments(comments):

    with open(COMMENTS_FILE, "w") as file:
        json.dump(
            comments,
            file,
            indent=4
        )



def create_comment(story_id, user_id, text):

    comments = load_comments()

    comment = {
        "id": str(uuid.uuid4()),
        "story_id": story_id,
        "user_id": user_id,
        "text": text,
        "date": str(datetime.now()),
        "status": "pending"
    }


    comments.append(comment)

    save_comments(comments)

    return comment
