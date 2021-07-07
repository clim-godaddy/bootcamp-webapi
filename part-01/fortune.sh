# nu
n=$(ls quotes | wc -l)
r=$(($RANDOM % $n + 1))
q=$(printf %02d $r)
cat quotes/$q
