import logging
import sys
import os

logs_dir = os.path.join(os.path.dirname(__name__), 'logs')
logs_path = os.path.join(os.path.dirname(__name__), 'logs', 'my_logs.log')
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

date_fmt = '%d.%m.%Y %H:%M:%S'
error_fmt = logging.Formatter('%(asctime)s %(name)s: %(message)s', datefmt=date_fmt)

# stdout logger
print_logger = logging.getLogger('printer')
print_logger.setLevel(logging.INFO)
print_handler = logging.StreamHandler(stream=sys.stdout)
print_handler.setLevel(logging.INFO)
print_logger.addHandler(print_handler)

# progress checker
progress_logger = logging.getLogger('*Progress*')
progress_logger.setLevel(logging.INFO)
progress_file_handler = logging.FileHandler(logs_path)
progress_file_handler.setLevel(logging.INFO)
progress_file_handler.setFormatter(error_fmt)
progress_logger.addHandler(progress_file_handler)

error_logger = logging.getLogger('*ERROR*')
error_logger.setLevel(logging.INFO)
error_file_handler = logging.FileHandler(logs_path)
error_file_handler.setLevel(logging.ERROR)
error_file_handler.setFormatter(error_fmt)
error_console_handler = logging.StreamHandler(stream=sys.stdout)
error_console_handler.setLevel(logging.INFO)
error_console_handler.setFormatter(error_fmt)
error_logger.addHandler(error_file_handler)
error_logger.addHandler(error_console_handler)
