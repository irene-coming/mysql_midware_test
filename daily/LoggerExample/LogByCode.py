# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 PM6:02
# @Author  : zhaohongjie@actionsky.com

import logging
import sys

logger = logging.getLogger('simple_test')
logger.setLevel(logging.INFO)

handler= logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)

formatter = logging.Formatter("(%asctime)s - %(name)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.debug("debug msg" )
logger.info("info msg")
logger.warning("warn msg")
logger.error("error msg")
logger.critical("critical msg")