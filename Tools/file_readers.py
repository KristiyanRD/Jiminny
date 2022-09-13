import os
import yaml


class FileReader:

    @staticmethod
    def yaml_reader(relative_path=''):
        with open(os.path.realpath(relative_path), "r") as cfg:
            try:
                data = yaml.safe_load(cfg)
                return data
            except yaml.YAMLError as exc:
                return print(exc)

    @staticmethod
    def text_reader(relative_path=''):
        with open(os.path.realpath(relative_path), 'r') as f:
            list_of_data = list(map(str.strip, f.readlines()))
            return list_of_data
