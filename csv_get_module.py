""" cvs_get_module.py
This module displays the summary of the tabular data contained in a CSV file 
"""
import pandas as pd

print("cvs_get_module is loaded")

def display_file_location(path, filename):
    print("File Location: {}".format(path+filename))

class CSVGetInfo:
    """ This class displays the summary of the tabular data contained in a CSV file """

    def __init__(self, path, file_name):
        self.path = path
        self.file_name = file_name

    def display_summary(self):
        data = pd.read_csv(self.path + self.file_name)
        print(self.file_name)
        print(data.info())

if __name__ == '__main__':

    data_by_artists = CSVGetInfo("/Users/erdemisbilen/Lessons/", "data_by_artists.csv")
    data_by_genres = CSVGetInfo("/Users/erdemisbilen/Lessons/", "data_by_genres.csv")

    data_by_artists.display_summary()
    data_by_genres.display_summary()
