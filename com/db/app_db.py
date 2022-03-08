import logging
import os
from pymongo import MongoClient


class AppDB:
    logger = logging.getLogger('root')
    mongo_db = None

    def initialize(self, host, port, username, password, auth_source):
        mongo_client = MongoClient(host=host,
                                   port=port,
                                   username=username,
                                   password=password)

        self.mongo_db = mongo_client[os.environ["db.database"]]
        self.populate_properties()
