import logging
logging.basicConfig(filename="mylog.txt", level=logging.NOTSET)

logging.error("This is an error")
logging.critical("This is a problem in software design")
logging.warning("It is just a warning")
logging.info("Nothing to worry")
logging.debug("In line number 10 there is a systax error")