import os
import mongoengine


def init_db():
    host = os.getenv('MONGODB_HOSTNAME')
    port = int(os.getenv('MONGODB_PORT'))
    mongoengine.connect(db='dev', host=host, port=port)
