#!/usr/bin/sh
text='xinjiapo'
file1=$text.csv
win1='_win.csv'
file2=$text$win1
echo $file2
python t1.py > $file1
iconv -f GB2312 -t utf-8 $file1 > $file2
