import csv
import logging

logging.basicConfig(level=logging.INFO)


async def load_data(raw_csv_data):
    """_summary_

    Args:
        row_data (csv): row csv file coming from https://www.sti.nasa.gov/nasa-thesaurus/
    """
    clean_csv = []
    with open(raw_csv_data, newline="\n", encoding="utf-8") as raw_csv:
        f = csv.reader(raw_csv)
        for row in f:
            logging.info(clean_row(row))
            clean_csv.append(clean_row(row))
    return clean_csv


def write_data(clean_csv, file_name):
    """write data to csv file

    Args:
        clean_csv (list): csv row list
        file_name (string): output filename
    """
    with open(file_name, "w", encoding="utf-8") as yaml_f:
        for row in clean_csv:
            print(row, file=yaml_f)


def clean_row(r):
    """Strip out unwanted chars."""
    for index in r:
        return index.replace('"', "")
