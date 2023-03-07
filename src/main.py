import pandas as pd
import src.Analysis as wis
import glob
import os


def main(raw_csv_folder, product_excel):
    """
    This function is the main function of the program. It takes in the folder
    path of the raw text files and the path of the product excel file. It
    calls the functions in the Analysis.py file to create the excel file.
    """

    os.chdir('/Users/maxwell/Coding/PolyU/wisconson_analysis')

    os.chdir(raw_csv_folder)
    filename_list = glob.glob('*.csv')
    os.chdir('/Users/maxwell/Coding/PolyU/wisconson_analysis')

    pre_df = pd.DataFrame()
    impo_df = pd.DataFrame()
    one_mth_df = pd.DataFrame()
    six_mth_df = pd.DataFrame()

    for file in filename_list:
        d = wis.summary_WCST(file)
        tem_df = pd.DataFrame(data=d)
        session = int(tem_df.session)
        if session == 1:
            pre_df = pd.concat([pre_df, tem_df], ignore_index=True)

        elif session == 2:
            impo_df = pd.concat([impo_df, tem_df], ignore_index=True)

        elif session == 3:
            one_mth_df = pd.concat([one_mth_df, tem_df], ignore_index=True)

        elif session == 4:
            six_mth_df = pd.concat([six_mth_df, tem_df], ignore_index=True)
        wis.write_excel(pre_df, impo_df, one_mth_df, six_mth_df)


main('revised_excel_files', 'WSCT Output.xlsx')
