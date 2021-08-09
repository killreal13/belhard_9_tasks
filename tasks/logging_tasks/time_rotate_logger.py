"""
Настроить логгирование с модулем logging.

Настроить формат вывода.
Настроить, чтобы вывод шел в файл и в консоль.
Настроить ротацию файла лога по времени (полночь).
"""
import logging
from logging.handlers import TimedRotatingFileHandler


logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler_1 = TimedRotatingFileHandler(filename='loggs.txt',
                                     when='midnight',
                                     interval=1,
                                     backupCount=30,
                                     encoding=None,
                                     delay=True,
                                     utc=False,
                                     atTime=None,
                                     errors=None)
handler.setLevel(logging.WARNING)
handler_1.setLevel(logging.ERROR)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
formatter_1 = logging.Formatter("%(asctime)s %(filename)s:%(lineno)d: %(levelname)s:%(message)s")
handler.setFormatter(formatter)
handler_1.setFormatter(formatter_1)
logger.addHandler(handler)
logger.addHandler(handler_1)
