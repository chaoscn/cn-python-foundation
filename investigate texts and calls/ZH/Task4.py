"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字母顺序输出。
"""
suspiciousList = set()
inCallList= set()

for c in calls:
    suspiciousList.add(c[0])
    inCallList.add(c[1])

textList= set()
for t in texts:
    textList.add(t[0])
    textList.add(t[1])

for s in suspiciousList.copy():
    if s in inCallList:
        suspiciousList.remove(s)
        continue
    if s in textList:
        suspiciousList.remove(s)

print('These numbers could be telemarketers: ')
for s in sorted(suspiciousList):
    print(s)