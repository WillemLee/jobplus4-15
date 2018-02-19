# -*- coding: utf-8 -*-
"""config.py
定义项目配置文件
"""

class BaseConfig(object):
    SECRET_KEY = 'very secret key'
    INDEX_PER_PAGE = 9
    ADMIN_PER_PAGE = 15


class DevelopmentConfig(BaseConfig):
    """
    开发环境配置
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/jobplus?charset=utf8'


class TestingConfig(BaseConfig):
    """
    测试环境配置
    """
    pass


class ProductionConfig(BaseConfig):
    """
    生产环境配置
    """
    pass


configs = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}