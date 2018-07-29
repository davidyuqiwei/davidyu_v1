#!/usr/bin/sh
text='hk_cen'
tr1='_dr.csv'
file1=$text$tr1
python decrease.py > $file1
#iconv -f GB2312 -t utf-8 zhongyang_dr.txt > zhongyang_dr_win.txt
