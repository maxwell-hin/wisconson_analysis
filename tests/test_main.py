import pytest
import pandas as pd
import src.main as main


@pytest.fixture()
def input_folder_output_excel(tmpdir):
    raw_txt_folder = '/Users/maxwell/Coding/PolyU/wisconsin/revised_excel_files'
    product_excel = tmpdir.join('WSCT Output.xlsx')
    yield raw_txt_folder, product_excel


def no_null_col(input_folder_output_excel):
    raw_txt_folder, product_excel = input_folder_output_excel
    main(raw_txt_folder, product_excel)
    with pd.read_excel(product_excel) as df:
        test = df.isnull().any()
    assert test == True
