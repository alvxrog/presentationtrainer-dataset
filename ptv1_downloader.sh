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
wget -c -i https://raw.githubusercontent.com/alvxrog/presentationtrainer-dataset/refs/heads/main/train/pt_v1_train_path.txt -P $curr_dl

# Download validation tars, will resume
curr_dl=${root_dl_targz}/val
[ ! -d $curr_dl ] && mkdir -p $curr_dl
wget -c -i https://raw.githubusercontent.com/alvxrog/presentationtrainer-dataset/refs/heads/main/val/pt_v1_val_path.txt -P $curr_dl

# We don't download test tars, as we will use the validation set as our test set 
# (we won't do cross-validation)

# Download k700-2020 annotations targz file from deep mind
curr_dl=${root_dl_targz}/annotations/deepmind 
[ ! -d $curr_dl ] && mkdir -p $curr_dl
wget -c https://storage.googleapis.com/deepmind-media/Datasets/kinetics700_2020.tar.gz -P $curr_dl

# Download k700-2020 annotations targz file from deep mind
curr_dl=${root_dl_targz}/annotations/deepmind_top-up
[ ! -d $curr_dl ] && mkdir -p $curr_dl
wget -c https://storage.googleapis.com/deepmind-media/Datasets/kinetics700_2020_delta.tar.gz -P $curr_dl

# Download AVA Kinetics
curr_dl=${root_dl_targz}/annotations/AVA-Kinetics
[ ! -d $curr_dl ] && mkdir -p $curr_dl
wget -c https://s3.amazonaws.com/kinetics/700_2020/annotations/ava_kinetics_v1_0.tar.gz -P $curr_dl
wget -c https://s3.amazonaws.com/kinetics/700_2020/annotations/countix.tar.gz -P $curr_dl

# Download annotations csv files
curr_dl=${root_dl}/annotations
[ ! -d $curr_dl ] && mkdir -p $curr_dl
wget -c https://s3.amazonaws.com/kinetics/700_2020/annotations/train.csv -P $curr_dl
wget -c https://s3.amazonaws.com/kinetics/700_2020/annotations/val.csv -P $curr_dl

# Downloads complete
echo -e "\nDownloads complete! Now run extractor, ptv1_extractor.sh"