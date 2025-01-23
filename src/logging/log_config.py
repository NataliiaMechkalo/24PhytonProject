import logging

def setup_logging():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filename='test_log.log',
                        filemode='w')
    return logging.getLogger(__name__)