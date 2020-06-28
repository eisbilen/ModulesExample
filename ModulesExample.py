import csv_get_module as cg

data_by_genres = cg.CSVGetInfo("/Users/erdemisbilen/Lessons/", "data_by_genres.csv")
cg.display_file_location(data_by_genres.path, data_by_genres.file_name)
data_by_genres.display_summary()

from csv_get_module import display_file_location as dfl

dfl("/User/Python/","ModulesExample.py")