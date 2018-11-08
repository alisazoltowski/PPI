### This script transform atlas ROI into subject space for functional connectivity
### Alisa Zoltowski edited from Michelle Failla
### Created 10-24-18

# import what is needed for the operating system

import os
# import glob which in this case helps match files in directories
import glob

# set up base directory and base subject directory
baseDir = "/Volumes/Data/alisazoltowski/PIEC/RestingState/"
basefeatDir = baseDir + "1stLevel"

# get list of subject files (all files in subject directory)
feat_files = glob.glob(basefeatDir + "*/*")

# define atlas ROI to transform
roi_atlas = baseDir + "ROIs/ifg_par_tri_roi.nii.gz"

for feat in feat_files:
    #get subj number
    subj_run = feat.split("/")[7]
    subj = subj_run.split("_")[0]

    # set up where subject space roi should go, make it a directory if it doesn't already exist
    roi_subject = baseDir + "ROIs/subject_space/" + subj + "/ifg_ptri_func_space.nii.gz"
    if not os.path.exists(baseDir + "/ROIs/subject_space/" + subj):
        os.makedirs(baseDir + "/ROIs/subject_space/" + subj)
    # name the transformation matrix and brain mask
    # NOTE this is for fsl registrations and may need to change for spm
    transformation_matrix = feat + "/reg/standard2example_func.mat"
    brain_mask = feat + "/reg/example_func.nii.gz"

    print transformation_matrix
    print brain_mask
    print roi_subject

    # create graded mask
    os.system("flirt -in " + roi_atlas + " -applyxfm -init " + transformation_matrix + " -out " + roi_subject + " -paddingsize 0.0 -interp trilinear -ref " + brain_mask)

    # create binary mask
    roi_subject_bin = baseDir + "ROIs/subject_space/" + subj + "/ifg_subject_func_space_bin.nii.gz"
    print roi_subject_bin
    os.system("fslmaths " + roi_subject + " -bin " + roi_subject_bin)
