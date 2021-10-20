for FILE in `ls ./output/ | sort -g`; 
do
    printf "\033c"
    cat './output/'$FILE
    sleep .05s
done