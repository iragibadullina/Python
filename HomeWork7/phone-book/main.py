from os.path import exists
from csv_format import create
from file import writing_scv
from file import writing_txt


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    create()

writing_scv()
writing_txt()