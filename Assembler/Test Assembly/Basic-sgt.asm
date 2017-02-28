# Author: Aidan Pieper
#
# NOTE: if your instruction word does not support immediates as large as 7, 
# you will need to REWRITE this code in order to work with your processor 
#
# results: 
#	$3 = 0
#	$4 = 0
#	$5 = 1

addi $1 $0 -1
addi $2 $0 6
sgt  $3 $1 $2
sgt  $4 $1 $1
sgt  $5 $2 $1
