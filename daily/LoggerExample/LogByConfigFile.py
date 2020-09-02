# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 PM4:00
# @Author  : zhaohongjie@actionsky.com

import logging
import logging.config

logging.basicConfig()
logging.config.fileConfig('ConfigFileAssets/logging.conf')

# 使用配置中的日志器
simple_logger=logging.getLogger("simpleExample")
simple_logger.debug("simpleExample debug msg" )
simple_logger.info("simpleExample info msg")
simple_logger.warning("simpleExample warn msg")
simple_logger.error("simpleExample error msg")
simple_logger.critical("simpleExample critical msg")

# 使用root日志器，只有匹配配置中>=error级别的日志会输出
root_logger=logging.getLogger()
root_logger.debug("root debug msg" )
root_logger.info("root info msg")
root_logger.warning("root warn msg")
root_logger.error("root error msg")
root_logger.critical("root critical msg")

# 用一个没有在配置文件中定义的logger名称来创建一个日志器logger
logger = logging.getLogger('unconfiged')
logger.debug('unconfiged debug message')
logger.info('unconfiged info message')
logger.warning('unconfiged warn message')
logger.error('unconfiged error message')
logger.critical('unconfiged critical message')