import os

class Config:
    """
    General configuration class
    """
    SECRET_KEY = 'leA6Y0wfVb7KIoblYzyl7Q'
    
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    # Email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


class ProdConfig(Config):
    """
    Production configuration class
    """
    SQLALCHEMY_DATABASE_URI = 'postgres://gubechukwawatr:eb353c3409ff3ba2ae1cfb3d392293ea718489760f40a543efaa8c8366c0503d@ec2-44-199-83-229.compute-1.amazonaws.com:5432/dfblrv4b6i69lk'


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/pitches_test'



class DevConfig(Config):
    """
    Development configuration class
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/pitches'
    DEBUG = True
    



config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
