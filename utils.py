"""This module contains utility functions."""

import pandas as pd
import csv
from datetime import datetime
import logging
import sys


def read_csv(file):
    data = pd.read_csv(file)
    return data


def write_csv(file, data):
    with open(file, mode='w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(data)


def log_error(error):
    logging.error(error)


def log_info(info):
    logging.info(info)


def log_debug(debug):
    logging.debug(debug)


def log_warning(warning):
    logging.warning(warning)


def log_critical(critical):
    logging.critical(critical)


def current_time():
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    return current_time