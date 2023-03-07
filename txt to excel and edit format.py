#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 13:20:58 2022

@author: maxwelllaw
"""

import pandas as pd
import os

# load analysis file, standard columns
# df_an = pd.read_excel('WCST_Raw Data _ Analysis.xlsx')
heading = ['ExperimentName', 'Subject', 'Session', 'Clock.Information',
           'DataFile.Basename', 'Display.RefreshRate', 'ExperimentVersion',
           'Group', 'RandomSeed', 'RuntimeVersion', 'RuntimeVersionExpected',
           'SessionDate', 'SessionStartDateTimeUtc', 'SessionTime',
           'StudioVersion', 'Block', 'List1', 'List1.Cycle', 'List1.Sample',
           'List3', 'List3.Cycle', 'List3.Sample', 'Procedure[Block]',
           'Running[Block]', 'Trial', 'CardIMG1[Trial]', 'CardIMG2[Trial]',
           'CardIMG3[Trial]', 'CardIMG4[Trial]', 'CardStim[Trial]', 'Category',
           'CorrectAnswer[Trial]', 'FeedbackDisplay2.ACC',
           'FeedbackDisplay2.CRESP', 'FeedbackDisplay2.DurationError',
           'FeedbackDisplay2.OnsetDelay', 'FeedbackDisplay2.OnsetTime',
           'FeedbackDisplay2.OnsetToOnsetTime', 'FeedbackDisplay2.RESP',
           'FeedbackDisplay2.RT', 'FeedbackDisplay2.RTTime', 'List2',
           'List2.Cycle', 'List2.Sample', 'List4', 'List4.Cycle', 'List4.Sample',
           'PracticeList', 'PracticeList.Cycle', 'PracticeList.Sample',
           'Procedure[Trial]', 'Running[Trial]', 'Slide5.ACC', 'Slide5.CRESP',
           'Slide5.DurationError', 'Slide5.OnsetDelay', 'Slide5.OnsetTime',
           'Slide5.OnsetToOnsetTime', 'Slide5.RESP', 'Slide5.RT', 'SubTrial',
           'CardIMG1[SubTrial]', 'CardIMG2[SubTrial]', 'CardIMG3[SubTrial]',
           'CardIMG4[SubTrial]', 'CardStim[SubTrial]', 'ColorList',
           'ColorList.Cycle', 'ColorList.Sample', 'ColorList2', 'ColorList2.Cycle',
           'ColorList2.Sample', 'CorrectAnswer[SubTrial]', 'NonPerseverativeError',
           'NumberList', 'NumberList.Cycle', 'NumberList.Sample', 'NumberList1',
           'NumberList1.Cycle', 'NumberList1.Sample', 'PerseverativeError',
           'Procedure[SubTrial]', 'Running[SubTrial]', 'ShapeList',
           'ShapeList.Cycle', 'ShapeList.Sample', 'ShapeList1', 'ShapeList1.Cycle',
           'ShapeList1.Sample', 'Stimulus.ACC', 'Stimulus.CRESP',
           'Stimulus.DurationError', 'Stimulus.OnsetDelay', 'Stimulus.OnsetTime',
           'Stimulus.OnsetToOnsetTime', 'Stimulus.RESP', 'Stimulus.RT',
           'TrialType']


# acess file containing txt files
txt_data_path = './txt_files'

# check the eprime version
# filename = 'Wisconsin-1174-3.txt'  # v3
# filename = 'Wisconsin-1171-1.txt'  # v2


def checkver():
    return df['StudioVersion'][0][0]


# remove first line in each txt file
for filename in os.listdir(txt_data_path):  # iteration every txt file
    if filename.endswith(".txt"):
        with open('./txt_files/'+filename, 'r', encoding="utf-16-le") as f:
            lines = f.readlines()
        with open('./txt_files/edited_txt/'+filename, 'w') as f:
            f.writelines(lines[1:])


for filename in os.listdir(txt_data_path+'/edited_txt'):  # iteration every txt file
    #filename = os.listdir(txt_data_path+'/edited_txt')[0]
    if filename.endswith(".txt"):
        df = pd.read_csv(txt_data_path+'/edited_txt/' +
                         filename, sep='\t', index_col=False)
        #df = pd.read_csv(os.listdir(txt_data_path)[0],sep = '\t', encoding="utf-16")

        if checkver() == '2':
            df = df.loc[:, heading]
            output_file_path = './revised_excel_files/'
            df.to_csv(output_file_path+filename.split(".")
                      [0] + ".csv", index=False)

        else:
            heading_new = []
            [heading_new.append(col_title.replace("Slide5", "FeedbackDisplay2"))
             if "Slide5" in col_title else heading_new.append(col_title) for col_title in heading]
            for col in df.columns:
                if "Slide4" in col:
                    new_title = col.replace("Slide4", "FeedbackDisplay2")
                    df = df.rename({col: new_title}, axis=1)
                if "NumberList2" in col:
                    new_title = col.replace("NumberList2", "NumberList1")
                    df = df.rename({col: new_title}, axis=1)
                if "ShapeList2" in col:
                    new_title = col.replace("ShapeList2", "ShapeList1")
                    df = df.rename({col: new_title}, axis=1)
                if "Slide5" in col:
                    new_title = col.replace("Slide5", "Stimulus")
                    df = df.rename({col: new_title}, axis=1)
            df = df.loc[:, heading_new]
            output_file_path = './revised_excel_files/'
            df.to_csv(output_file_path+filename.split(".")
                      [0] + ".csv", index=False)
        print('Finsihed ' + filename)
