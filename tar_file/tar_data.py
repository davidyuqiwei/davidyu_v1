## this script tar the code directory
#from package_path_define.path_define import *
#path_data_backup1
import os
import tarfile
from datetime import datetime
import time
##-- find date now
time1=datetime.now().date().isoformat()
print time1
tar_file1="code_file_"+time1
tar_file=tar_file1+".tar.gz"
print tar_file

dir="G:\\stock\\code"
tar = tarfile.open(tar_file,"w:gz")
for root,dir,files in os.walk(dir):
    for file in files:
        print file
        fullpath = os.path.join(root,file)
        tar.add(fullpath)
tar.close()

#----------------------------------
# ---- last tar 2017-11-7
#os.system('mv '+tar_file+' '+path_databackup_save)
