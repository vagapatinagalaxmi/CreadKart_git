import logging
class logGenerater:
     @staticmethod
     def loggen():
         logger=logging.getLogger()
         logfile = logging.FileHandler("C:\\python fixture\\credKart\\Logs\\automation.log")
         format=logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(levelno)s - %(message)s-%(funcName)s")
         logfile.setFormatter(format)
         logger.addHandler(logfile)
         logger.setLevel(logging.INFO)
         return logger




#warning
#info
#Debug
#Error
#Critical