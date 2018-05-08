import logging

def get_logger(level=logging.DEBUG, name='Expressome'):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.hasHandlers():
    	ch = logging.StreamHandler()
    	formatter = logging.Formatter('%(asctime)s: %(levelname)s  %(name)s] %(message)s', datefmt='%Y-%m-%d %I:%M:%S')
    	ch.setFormatter(formatter)
    	logger.addHandler(ch)
    return logger
