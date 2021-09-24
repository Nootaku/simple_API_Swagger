import os


class Config(object):
    TESTING = False
    SECRET_KEY = os.urandom(16)
    UPLOAD_FOLDER = os.path.join(os.getcwd(), "cdn")


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
