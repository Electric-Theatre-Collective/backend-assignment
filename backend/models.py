from mongoengine import Document
from mongoengine.fields import (
    StringField,
    IntField,
    ListField,
    ReferenceField,
)


# =======================================================================


class User(Document):
    meta = {'collection': 'user'}

    username = StringField(required=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)


# =======================================================================


class AssetVersion(Document):
    meta = {'collection': 'asset'}

    name = StringField(required=True)
    asset_type = StringField(required=True, choices=['model', 'rig', 'look', 'animation', 'render'])
    version = IntField(required=True)
    disk_path = StringField(required=True)
    author = ReferenceField("User", required=True)
