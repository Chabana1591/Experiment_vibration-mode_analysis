# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 13:05:46 2018

@author: Kohei Hayakawa
"""
import openpyxl
wb = openpyxl.load_workbook('matome.xlsx')
sheet = wb.get_sheet_by_name('アンバランス1005rpm')

tuple(sheet['c58':'c59']) #波形の取得'c58':'c50057'


