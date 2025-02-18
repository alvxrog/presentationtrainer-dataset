#!/bin/bash

# Download directories vars
root_dl="pt-v1"
root_dl_targz="pt-v1_targz"

# Make root directories
[ ! -d $root_dl ] && mkdir $root_dl
[ ! -d $root_dl_targz ] && mkdir $root_dl_targz

# Download train tars, will resume
curr_dl=${root_dl_targz}/train
[ ! -d $curr_dl ] && mkdir -p $curr_dl
wget -c -i https://github.com/alvxrog/presentationtrainer-dataset/train/pt_v1_train_path.txt -P $curr_dl

# Downloads complete
echo -e "\nDownloads complete! Now run extractor, k700_2020_extractor.sh"