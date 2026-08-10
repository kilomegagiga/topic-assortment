import os
import csv

class WeightedNouns:

    def __init__(self):
        self.part_of_speech = 'noun';
        self.source_filename = 'ucrel.lancs.ac.uk-bncfreq-lists-5_1_all_rank_noun.txt'

    def get_source_file_path(self):
        data_file_name = self.source_filename

        file_path = os.path.realpath(__file__)
        data_path = file_path
        data_path = os.path.abspath(os.path.join(data_path, os.pardir))
        data_path = os.path.join(data_path, 'rsrc')
        data_path = os.path.join(data_path, data_file_name)
        return data_path

    def load_from_path(self, data_path):
        result = []
        with open(data_path, newline='') as file:
            reader = csv.reader(file, delimiter='\t')
            for row in reader:
                result.append([float(row[2]), row[1]])
        return result

    def get_weighted_list(self):
        return self.load_from_path(self.get_source_file_path())
