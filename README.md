# PPI

1) Use transform_roi.py to get a standard space ROI into native subject space per person 
*note, this uses fsl registration... I haven't checked if these files still work for spm registration*
2) Use timecourse_roi.py to get the timing file for each subject/run
3) Fsf template shows how to set up design when you have the timecourses extracted
