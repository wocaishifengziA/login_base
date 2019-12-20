# encoding: utf-8
import copy

import pymongo
from bson import ObjectId

from login.settings import settings


class MongoCore(object):

    def __init__(self):
        conf = settings["mongodb"]
        self.db = pymongo.MongoClient(conf["addr"])[conf["db"]]

    @property
    def user(self):
        return self.db.user


def mongo_id_to_str(mgo_obj):

    new_obj = copy.deepcopy(mgo_obj)
    i = new_obj.pop("_id", None)
    if i:
        new_obj["id"] = str(i)
    return new_obj


def str_id_to_mongo_id(str_obj):

    mgo_obj = copy.deepcopy(str_obj)
    i = mgo_obj.pop("id", None)
    if i:
        mgo_obj["_id"] = ObjectId(i)
    return mgo_obj


def resize_mongo_result(result, limit=None, offset=None):
    if limit:
        result = result.limit(limit)
    if offset:
        result = result.skip(offset)
    return result


mongodb = MongoCore()
