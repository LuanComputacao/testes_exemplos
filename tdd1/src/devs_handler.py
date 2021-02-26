import csv


def read_devs_data(devs_data_file):
    with open(devs_data_file) as f:
        return [dev for dev in csv.DictReader(f)]
