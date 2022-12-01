#Read the list of classes that you want in your ImageNet Subset
TARGET_GROUPS_FILE='/tkadapt/canimesh/Supervised_Contrastive_Loss/IN100.txt'
GROUP_TO_LABELS_MAPPING_LOCATION = '/tkadapt/canimesh/Supervised_Contrastive_Loss/'
GROUP_TO_LABELS_MAPPING_FILE='mapping.csv'

#Defining the constants for the val Set

VAL_SET_FILE_FORMAT=".JPEG"
VAL_SET_ANNOTATION_FORMAT=".xml"
VAL_SET_ANNOTATION_LOCATION = '/tkadapt/dataset/ILSVRC/Annotations/CLS-LOC/val/'
VAL_SET_SOURCE= '/tkadapt/dataset/ILSVRC/Data/CLS-LOC/val/'
VAL_SET_DESTINATION = '/tkadapt/canimesh/data/cifar100_comp/imnet_mini/val/'
VAL_SET_LABELS_FILE = '/tkadapt/canimesh/data/cifar100_comp/imnet_mini/valLabels.csv'

#Defining the constants for the train Set

TRAIN_SET_FILE_FORMAT=".JPEG"
TRAIN_SET_SOURCE= '/tkadapt/dataset/ILSVRC/Data/CLS-LOC/train/'
TRAIN_SET_DESTINATION = '/tkadapt/canimesh/data/cifar100_comp/imnet_mini/train/'
TRAIN_SET_LABELS_FILE = '/tkadapt/canimesh/data/cifar100_comp/imnet_mini/trainLabels.csv'
EXAMPLES_PER_CLASS=100

DELIMITER='/'