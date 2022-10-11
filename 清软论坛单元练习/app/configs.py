# -*- coding: utf-8 -*-
"""
Flask 配置文件
"""
import os
from app.utils import config


class Config(object):
    """
    通用配置
    """
    # Flask config
    SECRET_KEY = config.get_yaml('app.SECRET', '')
    # SERVER_NAME = '{}:{}'.format(
    #     config.get_yaml('app.HOST', '127.0.0.1'),
    #     config.get_yaml('app.PORT', 5000)
    # )
    ENV = config.get_yaml('app.ENV', 'dev')
    SALT = config.get_yaml('app.SALT', '')

    # SQLALCHEMY config
    SQLALCHEMY_DATABASE_URI = config.get_yaml('db.MYSQL', '')
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # JWT config
    JWT_SECRET = config.get_yaml('jwt.SECRET', 'flask-project')
    JWT_EXPIRE_HOURS = config.get_yaml('jwt.EXPIRE_HOURS', 24)


class DevelopmentConfig(Config):
    """
    开发模式配置
    """
    TYPE = 'dev'
    DEBUG = True


class ProductionConfig(Config):
    """
    生产模式配置
    """
    TYPE = 'prod'

    DEBUG = False
    ENV = 'production'


class TestConfig(Config):
    """
    测试模式配置
    """
    TYPE = 'test'

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"


configs = {
    "default": DevelopmentConfig,
    "dev": DevelopmentConfig,
    "prod": ProductionConfig,
    "test": TestConfig
}
