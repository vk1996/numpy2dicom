# numpy2dicom
A utility for numpy array-dicom interoperability

Credits: https://stackoverflow.com/a/59786233/10449294

Usage

```
from array2dcm import convert2dcm
from glob import glob
from tqdm import tqdm 

files=sorted(glob('mydicomfolder/*.jpeg'))
for file in tqdm(files):
    convert2dcm(imgpath=file,check=True)
 
 ```
