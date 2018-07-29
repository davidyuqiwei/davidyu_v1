#!/usr/bin/sh
#grep -r -o -P '.{0,10}目标价.{0,10}' /cygdrive/g/stock/data/news_report/shanghai/600004 > price_target.txt 
grep -r -o -P -h '.{0,10}目标价.{0,10}' /cygdrive/g/stock/data/news_report/shanghai/600004 > price_target.txt
