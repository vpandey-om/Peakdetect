## load required library
from glob import glob
from peakonly.ms_peakonly import PeakOnly
import pandas as pd 
import matplotlib.pyplot as plt

mzfolder='/Users/vpandey/projects/gitlabs/peakDetection/raw/*.mzML' # this is for the mZFiles paths (I got tow raw files form Rajiv)
mzFiles=glob(mzfolder)
modelPath='/Users/vpandey/projects/gitlabs/peakDetection/models' # her we have download recnet models so every time you don't have to dwonload from web.
po = PeakOnly(model_dir=modelPath)
# mint.ms_files=mzFiles
table_peakonly = po.process(mzFiles) 
## I had  to modifid code in  run_utils.py files
# because some of the reasons we are getting rtdiff for some speciific mzFile
#   try:
#         frequency = scandiff / rtdiff
#     except:
#         frequency=1e10
table_peakonly.to_csv('/Users/vpandey/projects/gitlabs/peakDetection/PeakCombined/results/peak_only_rajiv.csv',sep='\t',index=None)
