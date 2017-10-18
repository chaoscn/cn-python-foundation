"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
from collections import defaultdict

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""

telephoneList= []
for t in texts:
    if t[0] not in telephoneList:
        telephoneList.append(t[0])
    if t[1] not in telephoneList:
        telephoneList.append(t[1])

for c in calls:
    if c[0] not in telephoneList:
        telephoneList.append(c[0])
    if c[1] not in telephoneList:
        telephoneList.append(c[1])

print ('There are %s different telephone numbers in the records.'% (telephoneList.__len__()))  # len(telephoneList)