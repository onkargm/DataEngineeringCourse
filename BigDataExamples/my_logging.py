import logging
import re
import pandas as pd

data_csv_path = "annual-enterprise-survey-2021-financial-year-provisional-csv.csv"

data_csv_file_data = pd.read_csv(data_csv_path,encoding="unicode_escape",nrows=1000)

logging.basicConfig(
    filename="reading_csvs.log", level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s- %(message)s"

)

def is_pattern_match(string):
    logging.debug(f"Checking if {string} matches")
    digit_only = re.compile("\d")
    if digit_only.match(string):
        logging.info(f"{string} matches")
    else:
        logging.info(f"{string} does not match")

codes = data_csv_file_data["Industry_code_NZSIOC"].to_list()

for code in codes:
    is_pattern_match(code)

