from os import getcwd
from openpyxl import load_workbook
import re

def get_key(val):
    for key,value in month_dict.items():
        if val == value:
            return key

current_working_dir = getcwd()
utilization_tracker_xl = 'D:/Embedded_NA_UtilizationTracker__Jan-20.xlsx'
utilization_wb = load_workbook(utilization_tracker_xl)
utilization_sheets = utilization_wb.sheetnames

# print(utilization_sheets)

calendar_xl = 'D:/Calendar.xlsx'
calendar_wb = load_workbook(calendar_xl)
calendar_sheets = calendar_wb.sheetnames
# print(calendar_sheets)

calendar_Sheet1 = calendar_wb['Sheet1']

# Task : Retrieving the month from the Utilization filename 

splitwise_name = re.split(r'\W+|_',utilization_tracker_xl)
# list of all substrings: D, Embedded , NA, UtilizationTracker, Jan, 20

# Exception Testing code written below
# Replacing Jan with September or any Dictionary Value mentioned in below dict
#if 'Jan' in splitwise_name:
#    splitwise_name.remove('Jan')
#    splitwise_name.append('September')

month_dict = {1:['01','Jan','January'], 2:['02','Feb','February'], 3:['03','Mar','March'], 4:['04','Apr','April'], 5:['05','May','May'], 6:['06','Jun','June'],
              7:['07','Jul','July'],8:['08','Aug','August'], 9:['09','Sep','Sept','September'], 10:['10','Oct','October'], 11:['11','Nov','November'], 12:['12','Dec','December']}

month_name = ''
for key in month_dict.keys():
    for month_data in month_dict[key]:  # Will parse entire list 
        if month_data in splitwise_name:
            month_name = month_data # Returns Jan
           
print(month_name)


