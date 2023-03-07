import pytest
import pandas as pd
import src.main as main
import src.Analysis as wis
import numpy as np

test_file = 'Wisconsin-1139-4.csv'


def test_no_null_data():
    d = wis.summary_WCST(test_file)
    d = list(d.values())
    d = [item[0] for item in d]
    for item in d[2:]:
        assert item == item


# @pytest.fixture
# def input_folder_output_excel(tmpdir):
#     raw_csv_folder = 'revised_excel_files'
#     product_excel = tmpdir.join('WSCT Output.xlsx')
#     yield raw_csv_folder, product_excel


# def test_no_null_col(input_folder_output_excel):
#     raw_csv_folder, product_excel = input_folder_output_excel
#     main(raw_csv_folder, product_excel)
#     df = pd.read_excel(product_excel)
#     test = df.isnull().sum().sum()
#     assert test == 0
