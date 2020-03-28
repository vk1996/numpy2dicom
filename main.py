from array2dcm import convert2dcm
from glob import glob
from tqdm import tqdm 

files=sorted(glob('mydicomfolder/*.jpeg'))
for file in tqdm(files):
    convert2dcm(imgpath=file,check=True)
