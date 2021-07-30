from ..db_config import base_db

class BaseRepository:
    """ """
    collection = None
    conn = [collection]
    @classmethod
    def create_one(cls, data_user):
        """ .... """
        del data_user['_id'] #123
        base_db[cls.collection].insert_one(data_user)
        ...

    @classmethod
    def get_one(cls, data_user):
        """ .... """
        data = base_db[cls.collection].find_one({'_id':data_user.id})

        data['id'] = data.pop('_id')

        ...

