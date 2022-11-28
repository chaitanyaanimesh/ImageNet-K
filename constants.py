#Read the list of classes that you want in your ImageNet Subset
TARGET_GROUPS_FILE='IN100.txt'
GROUP_TO_LABELS_MAPPING_LOCATION = '/datset/'
GROUP_TO_LABELS_MAPPING_FILE='mapping.csv'

#Defining the constants for the val Set

VAL_SET_FILE_FORMAT=".JPEG"
VAL_SET_ANNOTATION_FORMAT=".xml"
VAL_SET_ANNOTATION_LOCATION = '/dataset/ILSVRC/Annotations/CLS-LOC/val/'
VAL_SET_SOURCE= '/dataset/ILSVRC/Data/CLS-LOC/val/'
VAL_SET_DESTINATION = '/dataset/imnet_mini/val/'
VAL_SET_LABELS_FILE = '/dataset/imnet_mini/valLabels.csv'

#Defining the constants for the train Set

TRAIN_SET_FILE_FORMAT=".JPEG"
TRAIN_SET_SOURCE= '/dataset/ILSVRC/Data/CLS-LOC/train/'
TRAIN_SET_DESTINATION = '/dataset/imnet_mini/train/'
TRAIN_SET_LABELS_FILE = '/dataset/imnet_mini/trainLabels.csv'


DELIMITER='/'