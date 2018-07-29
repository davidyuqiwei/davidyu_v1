# encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import jieba
import jieba.posseg as pseg
import jieba.analyse

#data_file=r'G:\stock\data\news_report\shanghai\600004\600004_2015-12-16_33.txt'
data_file='price_target.txt'
f = open(data_file)
a1=f.read()
#print a1
seg_list = jieba.cut(a1, cut_all=False)
#print("Full Mode: " + "/ ".join(seg_list))  # 全模式
words = pseg.cut(a1)

word1=[]
flag1=[]
for word,flag in words:
    word1.append(word)
    flag1.append(flag)
#print word1
    #print('%s %s' % (word,flag))
#for word, flag in words:
#    print('%s %s' % (word, flag))
i=-1
for word in word1:
    i+=1
    if word=='目标价' and flag1[i+1]=='m':
        print('%s %s  ' % (word1[i],word1[i+1]))
    elif word=='目标价' and flag1[i+1]=='p':
        print('%s %s %s ' % (word1[i],word1[i+1],word1[i+2]))
    elif word=='目标价' and flag1[i+1]=='n':
        print('%s %s %s ' % (word1[i],word1[i+1],word1[i+2]))
    elif word=='目标价' and flag1[i-1]=='m':
        print('%s %s %s ' % (word1[i-2],word1[i-1],word1[i]))


        #print word1[i+1]
        #1+1

text1='调整盈利预测,下调目标价,维持“中性”评级'
words = pseg.cut(text1)
for word, flag in words:
    print('%s %s' % (word, flag))

topK=20
tags = jieba.analyse.extract_tags(a1, topK=topK)
print(",".join(tags))
