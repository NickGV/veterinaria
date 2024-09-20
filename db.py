from pymongo import MongoClient
from django.conf import settings

client = MongoClient(settings.MONGODB_URI)
db = client.get_default_database()