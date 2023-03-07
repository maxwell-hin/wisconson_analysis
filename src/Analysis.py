#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 12:10:58 2022

@author: maxwell_law
"""

import os
import pandas as pd
import numpy as np
# import xlsxwriter

excel_path = './revised_excel_files/'


def summary_WCST(file):
    df = pd.read_csv(excel_path+file)
    #filename = os.listdir()[3]
    df.drop([0, 1, 2, 3, 4, 5], inplace=True)
    df = df.reset_index(drop=True)

    # ==============================================================================
    # =============================Variables========================================

    SubjectID = 'Yt2_'+file[11:14]
    Cantabcode = file[10:14]
    Session = df['Session'][0]
    # ==============================================================================
    Consecutive = df['TrialType'][29] == df['TrialType'][30]
    if Consecutive:
        RepeatB3B4 = 1
    else:
        RepeatB3B4 = 0
    # ==============================================================================
    total_Error = len(df['Stimulus.ACC']) - \
        sum(df['Stimulus.ACC'])  # TotalError
    total_ACC = sum(df['Stimulus.ACC'])  # TotalACC
    total_ACC_per = 100*(total_ACC/len(df['Stimulus.ACC']))
    # ==============================================================================
    if Consecutive:
        switching_rng = list(range(6, 14))+list(range(16, 24))\
            + list(range(36, 44))+list(range(46, 54))
    else:
        switching_rng = list(range(6, 14))+list(range(16, 24))+list(range(26, 34))\
            + list(range(36, 44))+list(range(46, 54))

    switching_block = df.loc[switching_rng]
    SError = len(switching_block)-sum(switching_block['Stimulus.ACC'])
    SACC = sum(switching_block['Stimulus.ACC'])
    # SCorrectRate
    SACC_per = 100*(sum(switching_block['Stimulus.ACC'])/len(switching_block))
    del switching_block
    # ==============================================================================
    if Consecutive:
        NS_rng = list(range(2, 10))+list(range(12, 20))+list(range(22, 40))\
            + list(range(42, 50))+list(range(52, 60))
    else:
        NS_rng = list(range(2, 10))+list(range(12, 20))+list(range(22, 30))\
            + list(range(32, 40))+list(range(42, 50))+list(range(52, 60))

    NS_block = df.loc[NS_rng]
    NSError = len(NS_block)-sum(NS_block['Stimulus.ACC'])
    NSACC = sum(NS_block['Stimulus.ACC'])
    NSACC_per = sum(NS_block['Stimulus.ACC'])/len(NS_block)  # NSCorrectRate
    del NS_block
    # ==============================================================================
    MeanRT = df['Stimulus.RT'].mean()  # MeanRT
    # ==============================================================================
    MeanSRT = df.loc[switching_rng]['Stimulus.RT'].mean()  # MeanSRT
    # ==============================================================================
    MeanNSRT = df.loc[NS_rng]['Stimulus.RT'].mean()  # MeanSRT
    # ==============================================================================
    Correct_MeanRT = df[df['Stimulus.ACC'] ==
                        1]['Stimulus.RT'].mean()  # Correct_MeanRT
    # ==============================================================================
    Correct_SRT = df.loc[switching_rng]['Stimulus.RT'].mean()  # Correct_SRT
    # ==============================================================================
    Correct_NSRT = df.loc[NS_rng]['Stimulus.RT'].mean()  # Correct_NSRT
    del NS_rng, switching_rng
    # ==============================================================================
    Set_rng = list(range(2, 10))+list(range(12, 20))+list(range(22, 30))\
        + list(range(32, 40))+list(range(42, 50))+list(range(52, 60))
    SetError = len(Set_rng)-sum(df.loc[Set_rng]['Stimulus.ACC'])
    del Set_rng
    # ==============================================================================
    rng_1 = list(range(10))
    rng_2 = list(range(10, 20))
    rng_3 = list(range(20, 30))
    rng_4 = list(range(30, 40))
    rng_5 = list(range(40, 50))
    rng_6 = list(range(50, 60))

    PerError = 0
    for l in range(1, 7):
        rng_list = eval('rng_'+str(l))
        for i in df.loc[rng_list]["Stimulus.ACC"][2:].index:
            if df.loc[rng_list]["Stimulus.ACC"][i] == 0:
                if df.loc[rng_list]["Stimulus.ACC"][i-1] == 0:
                    PerError += 1  # PerError
    del rng_1, rng_2, rng_3, rng_4, rng_5, rng_6

    # ==============================================================================
    L1_ACC = df.loc[list(range(5))]['Stimulus.ACC'].sum()
    L1_RT = df.loc[list(range(5))]['Stimulus.RT'].mean()
    A1_ACC = df.loc[list(range(5, 10))]['Stimulus.ACC'].sum()
    A1_RT = df.loc[list(range(5, 10))]['Stimulus.RT'].mean()

    L2_ACC = df.loc[list(range(10, 15))]['Stimulus.ACC'].sum()
    L2_RT = df.loc[list(range(10, 15))]['Stimulus.RT'].mean()
    A2_ACC = df.loc[list(range(15, 20))]['Stimulus.ACC'].sum()
    A2_RT = df.loc[list(range(15, 20))]['Stimulus.RT'].mean()

    L3_ACC = df.loc[list(range(20, 25))]['Stimulus.ACC'].sum()
    L3_RT = df.loc[list(range(20, 25))]['Stimulus.RT'].mean()
    A3_ACC = df.loc[list(range(25, 30))]['Stimulus.ACC'].sum()
    A3_RT = df.loc[list(range(25, 30))]['Stimulus.RT'].mean()

    L4_ACC = df.loc[list(range(30, 35))]['Stimulus.ACC'].sum()
    L4_RT = df.loc[list(range(30, 35))]['Stimulus.RT'].mean()
    A4_ACC = df.loc[list(range(35, 40))]['Stimulus.ACC'].sum()
    A4_RT = df.loc[list(range(35, 40))]['Stimulus.RT'].mean()

    L5_ACC = df.loc[list(range(40, 45))]['Stimulus.ACC'].sum()
    L5_RT = df.loc[list(range(40, 45))]['Stimulus.RT'].mean()
    A5_ACC = df.loc[list(range(45, 50))]['Stimulus.ACC'].sum()
    A5_RT = df.loc[list(range(45, 50))]['Stimulus.RT'].mean()

    L6_ACC = df.loc[list(range(50, 55))]['Stimulus.ACC'].sum()
    L6_RT = df.loc[list(range(50, 55))]['Stimulus.RT'].mean()
    A6_ACC = df.loc[list(range(55, 60))]['Stimulus.ACC'].sum()
    A6_RT = df.loc[list(range(55, 60))]['Stimulus.RT'].mean()
    # ==============================================================================
    L_TotalACC = L1_ACC+L2_ACC+L3_ACC+L4_ACC+L5_ACC+L6_ACC
    L_TotalACC_per = 100*(L_TotalACC/30)
    L_RT = sum(np.array([L1_RT, L2_RT, L3_RT, L4_RT, L5_RT, L6_RT]))/6

    A_TotalACC = A1_ACC+A2_ACC+A3_ACC+A4_ACC+A5_ACC+A6_ACC
    A_TotalACC_per = 100*(A_TotalACC/30)
    A_RT = sum(np.array([A1_RT, A2_RT, A3_RT, A4_RT, A5_RT, A6_RT]))/6
    # ==============================================================================
    color_list = df[df['TrialType'].str.contains(
        'color', na=False, case=False)]
    color_list = color_list.reset_index(drop=True)

    Color_L_ACC = color_list.loc[list(
        range(0, 5))+list(range(10, 15))]['Stimulus.ACC'].sum()
    Color_L_ACC_per = Color_L_ACC*10
    Color_L_RT = color_list.loc[list(
        range(0, 5))+list(range(10, 15))]['Stimulus.RT'].mean()
    Color_A_ACC = color_list.loc[list(
        range(5, 10))+list(range(15, 20))]['Stimulus.ACC'].sum()
    Color_A_ACC_per = Color_A_ACC*10
    Color_A_RT = color_list.loc[list(
        range(5, 10))+list(range(15, 20))]['Stimulus.RT'].mean()
    Color_ACC = color_list['Stimulus.ACC'].sum()
    Color_ACC_per = 100*(Color_ACC/len(color_list))
    Color_RT = color_list['Stimulus.RT'].mean()
    del color_list

    shape_list = df[df['TrialType'].str.contains('Shape', na=False)]
    shape_list = shape_list.reset_index(drop=True)

    Shape_L_ACC = shape_list.loc[list(
        range(0, 5))+list(range(10, 15))]['Stimulus.ACC'].sum()
    Shape_L_ACC_per = Shape_L_ACC*10
    Shape_L_RT = shape_list.loc[list(
        range(0, 5))+list(range(10, 15))]['Stimulus.RT'].mean()
    Shape_A_ACC = shape_list.loc[list(
        range(5, 10))+list(range(15, 20))]['Stimulus.ACC'].sum()
    Shape_A_ACC_per = Shape_A_ACC*10
    Shape_A_RT = shape_list.loc[list(
        range(5, 10))+list(range(15, 20))]['Stimulus.RT'].mean()
    Shape_ACC = shape_list['Stimulus.ACC'].sum()
    Shape_ACC_per = 100*(Shape_ACC/len(shape_list))
    Shape_RT = shape_list['Stimulus.RT'].mean()
    del shape_list

    num_list = df[df['TrialType'].str.contains('number', na=False)]
    num_list = num_list.reset_index(drop=True)

    Num_L_ACC = num_list.loc[list(range(0, 5)) +
                             list(range(10, 15))]['Stimulus.ACC'].sum()
    Num_L_ACC_per = Num_L_ACC*10
    Num_L_RT = num_list.loc[list(range(0, 5)) +
                            list(range(10, 15))]['Stimulus.RT'].mean()
    Num_A_ACC = num_list.loc[list(
        range(5, 10))+list(range(15, 20))]['Stimulus.ACC'].sum()
    Num_A_ACC_per = Num_A_ACC*10
    Num_A_RT = num_list.loc[list(range(5, 10)) +
                            list(range(15, 20))]['Stimulus.RT'].mean()
    Num_ACC = num_list['Stimulus.ACC'].sum()
    Num_ACC_per = 100*(Num_ACC/len(num_list))
    Num_RT = num_list['Stimulus.RT'].mean()
    del num_list

    # ==============================================================================
    # ===========================To SPSS============================================
    d = {'subid': [SubjectID],
         'cantabcode': [Cantabcode],
         'session': [Session],
         'repeat': [RepeatB3B4],
         'tt_error': [total_Error],
         'tt_acc': [total_ACC],
         'tt_acc_per': [total_ACC_per],
         'serror': [SError],
         'sacc': [SACC],
         'sacc_per': [SACC_per],
         'nserror': [NSError],
         'nsacc': [NSACC],
         'nsacc_per': [NSACC_per],
         'mRT': [MeanRT],
         'mSRT': [MeanSRT],
         'mNSRT': [MeanSRT],
         'corr_mRT': [Correct_MeanRT],
         'corr_SRT': [Correct_SRT],
         'corr_NSRT': [Correct_NSRT],
         'seterror': [SetError],
         'pererror': [PerError],
         'l1_acc': [L1_ACC],
         'l1_rt': [L1_RT],
         'a1_acc': [A1_ACC],
         'a1_rt': [A1_RT],
         'l2_acc': [L2_ACC],
         'l2_rt': [L2_RT],
         'a2_acc': [A2_ACC],
         'a2_rt': [A2_RT],
         'l3_acc': [L3_ACC],
         'l3_rt': [L3_RT],
         'a3_acc': [A3_ACC],
         'a3_rt': [A3_RT],
         'l4_acc': [L4_ACC],
         'l4_rt': [L4_RT],
         'a4_acc': [A4_ACC],
         'a4_rt': [A4_RT],
         'l5_acc': [L5_ACC],
         'l5_rt': [L5_RT],
         'a5_acc': [A5_ACC],
         'a5_rt': [A5_RT],
         'l6_acc': [L6_ACC],
         'l6_rt': [L6_RT],
         'a6_acc': [A6_ACC],
         'a6_rt': [A6_RT],
         'ltt_acc': [L_TotalACC],
         'ltt_acc_per': [L_TotalACC_per],
         'ltt_rt': [L_RT],
         'att_acc': [A_TotalACC],
         'att_acc_per': [A_TotalACC_per],
         'att_rt': [A_RT],
         'color_l_acc': [Color_L_ACC],
         'color_l_acc_per': [Color_L_ACC_per],
         'color_l_rt': [Color_L_RT],
         'color_a_acc': [Color_A_ACC],
         'color_a_acc_per': [Color_A_ACC_per],
         'color_a_rt': [Color_A_RT],
         'color_acc': [Color_ACC],
         'color_acc_per': [Color_ACC_per],
         'color_rt': [Color_RT],
         'shape_l_acc': [Shape_L_ACC],
         'shape_l_acc_per': [Shape_L_ACC_per],
         'shape_l_rt': [Shape_L_RT],
         'shape_a_acc': [Shape_A_ACC],
         'shape_a_acc_per': [Shape_A_ACC_per],
         'shape_a_rt': [Shape_A_RT],
         'shape_acc': [Shape_ACC],
         'shape_acc_per': [Shape_ACC_per],
         'shape_rt': [Shape_RT],
         'num_l_acc': [Num_L_ACC],
         'num_l_acc_per': [Num_L_ACC_per],
         'num_l_rt': [Num_L_RT],
         'num_a_acc': [Num_A_ACC],
         'num_a_acc_per': [Num_A_ACC_per],
         'num_a_rt': [Num_A_RT],
         'num_acc': [Num_ACC],
         'num_acc_per': [Num_ACC_per],
         'num_rt': [Num_RT],
         }
    return d


# ===========================To Excel============================================
def reset_index(df):
    df.set_index('subid', inplace=True)
    df.sort_index(inplace=True)
    return df


def write_excel(pre_df, impo_df, one_mth_df, six_mth_df, product_excel='WSCT Output.xlsx'):
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(product_excel, engine='xlsxwriter')
    pre_df = reset_index(pre_df)
    impo_df = reset_index(impo_df)
    one_mth_df = reset_index(one_mth_df)
    six_mth_df = reset_index(six_mth_df)

    pre_df.to_excel(writer, sheet_name='Pre', index=False)
    impo_df.to_excel(writer, sheet_name='Impo', index=False)
    one_mth_df.to_excel(writer, sheet_name='1mth', index=False)
    six_mth_df.to_excel(writer, sheet_name='6mth', index=False)
    writer.save()
