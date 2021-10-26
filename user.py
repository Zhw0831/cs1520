from flask_login import UserMixin
from datastore_entity import DatastoreEntity, EntityValue
import datetime

class User(DatastoreEntity, UserMixin):
    username = EntityValue(None)
    email = EntityValue(None)