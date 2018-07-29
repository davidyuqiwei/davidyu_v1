#!/usr/bin/sh
unset GREP_OPTIONS
foo=('000725' '000089' '600033' '600282' '600401' '600526' '600573' '600783' '600795'\
  '000778' '000917' '000979' '002333' )
#echo $foo
bar=$(printf "\|%s" "${foo[@]}")
bar1=${bar:2}
echo $bar1
grep -r $bar1 --color=always /home/qyu/hq185/qyu/data_all/extract_data/stock/report/ |sort -t , -k 5

#grep -r '000725\|000089' /home/qyu/hq185/qyu/data_all/extract_data/stock/report/

#c2=join , $stock1 $stock2
#echo $c2
