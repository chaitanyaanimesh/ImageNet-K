# ImageNet-K
A simple and convenient repo for generating ImageNet-K (K classes). Can be used for generating ImageNet-100 or any smaller/larger subset
of ImageNet.

Default values in constant files assumes the following structure of ImageNet directory (Please consider changing the locations in constants.py
if it differs):
```
/dataset/ILSVRC/
            |--Annotations/CLS-LOC/
            |                  |--train
            |                  |--val
            |                  |--test
            |--Data/CLS-LOC/
                       |--train
                       |--val
                       |--test
```