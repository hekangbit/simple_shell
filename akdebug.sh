#!/bin/bash

infile=$1
outfile=$2

export outfile

echo "Start echo reg data!\n"

#tmpbuf=$(cat $infile | awk '$1=="{"{print $2 "\t" $3}' $infile
#awk '$1=="{"{echo $2 " " $3 > "'$outfile'"}' $infile
#awk '$1=="{"{system("echo $2 "\t" $3 > "'$outfile'"")}' $infile
#awk '$1=="{"{print $2 " " substr($3,2); system("echo hello_nennnn")}' $infile

#awk '$1=="{"{print $2 " " substr($3,2) > ENVIRON["outfile"]}' $infile
awk '$1=="{"{reg=$2; val=substr($3,2); ofile=ENVIRON["outfile"];system("echo"" "reg" "val" > "ofile)}' $infile

echo "Done!\n"

