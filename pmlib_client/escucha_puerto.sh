
#r=$(lsof -c $1 -i@$2:$3)
lsof -c $1 -i@$2:$3 > /tmp/kk
nl=$(cat /tmp/kk| wc -l)

while [ $nl -ge 2 ] 
do
   lsof -c $1 -i@$2:$3 > /tmp/kk1
   if ! diff /tmp/kk1 /tmp/kk > /dev/null
      

   cat /tmp/kk
   sleep 2
#  r=$(lsof -c $1 -i@$2:$3)
   lsof -c $1 -i@$2:$3 > /tmp/kk
   nl=$(cat /tmp/kk| wc -l)
done
