from bson.objectid import ObjectId
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import datetime
from app.exceptions.post_exceptions import IncorrectDataError, NotFoundId

load_dotenv()

client = MongoClient(os.getenv("DATABASE_URL"),
                     int(os.getenv("DATABASE_PORT")))
db = client.kenzie


class Post:
    def __init__(self, title: str, author: str, tags: list, content: str) -> None:
        self.id = db.post.count_documents({}) + 1
        self.created_at = {"data": datetime.datetime.utcnow()}
        self.update_at = {"data": datetime.datetime.utcnow()}
        self.title = title
        self.author = author
        self.tags = tags
        self.content = content

    def save_post(self):
        saved = db.post.insert_one(self.__dict__)

        if not saved:
            raise IncorrectDataError

        new_post = db.post.find_one({"id": self.id})
        del new_post["_id"]
        return new_post

    @staticmethod
    def all_posts():
        links = []

        posts_list = list(db.post.find())
        if len(posts_list) == 0:
            return {"msg": "Empty list"}

        for post in posts_list:
            links.append({
                "name": post["title"],
                "link": f"http://localhost:5000/posts/{post['id']}"
            })

        return links

    @staticmethod
    def post_by_id(id: int):
        post = db.post.find_one({"id": id})

        if not post:
            raise NotFoundId

        del post["_id"]
        return post

    @staticmethod
    def post_update(id: int, update: dict):
        post = db.post.find_one({"id": id})
        list_update = list(update.keys())

        for key in list_update:
            resp = post.get(key)
            if not resp:
                raise IncorrectDataError

        update["update_at"] = {"data": datetime.datetime.utcnow()}
        success_update = db.post.find_one_and_update({"id": id}, {"$set": update})
        post_update = db.post.find_one({"id": id})

        if not success_update:
            raise NotFoundId

        del post_update["_id"]
        return post_update

    @staticmethod
    def post_delete(id: int):
        post = db.post.find_one_and_delete({"id": id})

        if not post:
            raise NotFoundId

        del post["_id"]
        return post
