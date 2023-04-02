import pandas as pd

class FileHasTooManyRows(Exception):

    def __init__(self,numberofrows):
        self.numberofrows = numberofrows
        self.message = f"CSV File has too many rows, amx row count is 1000 and current number of rows are {self.numberofrows}"



try:
    file_path = "annual-enterprise-survey-2021-financial-year-provisional-csv.csv"
    csv_data = pd.read_csv(filepath_or_buffer=file_path,encoding="unicode_escape",nrows=1100)
    number_of_rows = len(csv_data)
    if number_of_rows>1000:
        raise FileHasTooManyRows(number_of_rows)
except Exception as exception:
    print(exception.message)