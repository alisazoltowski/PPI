### This script extracts the timecourse of the subject space ROI
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

for feat in feat_files:
    # get subj number
    subj_run = feat.split("/")[7]
    subj = subj_run.split("_")[0]

    # grab subject space roi for region you want
    roi_subject = baseDir + "ROIs/subject_space/" + subj + "/ifg_ptri_func_space.nii.gz"

    # grab filtered functional data
    filtered_func = feat + "/filtered_func_data.nii.gz"
    print filtered_func

    #set up directory for time course information to be extracted to:
    subj_time_dir = baseDir + "Timecourse/" + subj_run
    if not os.path.exists(subj_time_dir):
        os.makedirs(subj_time_dir)
    #next, define timecourse output file (change name for region)
    subj_timecourse = subj_time_dir + "/ifg_ptri_tc.txt"
    print subj_timecourse
    #run fsl command on operarting system:
    os.system("fslmeants -i " + filtered_func + " -o " + subj_timecourse + " -m " + roi_subject)