import os
import numpy as np
from constants import *
import xml.etree.ElementTree as ET
import csv
import shutil as shu

class Generator:

    def __init__(self):
        self.labels = {}

        txt_data = open(TARGET_GROUPS_FILE, 'r')
        for ids, txt in enumerate(txt_data):
            s = str(txt.split('\n')[0])
            self.labels[s] = ids

        # Making a persistent copy of labels dictionary on disk
        with open(GROUP_TO_LABELS_MAPPING_LOCATION+GROUP_TO_LABELS_MAPPING_FILE, 'w') as mappingFile:
            csvWriter = csv.writer(mappingFile)
            for group, label in self.labels.items():
                csvWriter.writerow([group, label])

        # Reading back the persistent copy of labels
        self.labels = {}
        with open(GROUP_TO_LABELS_MAPPING_LOCATION+GROUP_TO_LABELS_MAPPING_FILE, 'r') as mappingFile:
            mappingFileReader = csv.reader(mappingFile)
            for row in mappingFileReader:
                self.labels[row[0]] = int(row[1])


    def generateValSet(self):

        if not os.path.exists(VAL_SET_DESTINATION):
            os.makedirs(VAL_SET_DESTINATION)

        valSetLabelsFileObj = open(VAL_SET_LABELS_FILE, 'w')
        valSetLabelsWriter = csv.writer(valSetLabelsFileObj)
        for valFile in os.listdir(VAL_SET_SOURCE):
            ValAnnotationFile = valFile[:-len(VAL_SET_FILE_FORMAT)] + VAL_SET_ANNOTATION_FORMAT
            tree = ET.parse(VAL_SET_ANNOTATION_LOCATION + ValAnnotationFile)
            root = tree.getroot()
            group = root.find('object').find('name').text
            if group in self.labels.keys():
                valSetLabelsWriter.writerow([valFile, self.labels[group]])
                shu.copyfile(VAL_SET_SOURCE + valFile, VAL_SET_DESTINATION + valFile)

        valSetLabelsFileObj.close()


    def generateTrainSet(self):

        if not os.path.exists(TRAIN_SET_DESTINATION):
            os.makedirs(TRAIN_SET_DESTINATION)

        trainSetLabelsFileObj = open(TRAIN_SET_LABELS_FILE, 'w')
        trainSetLabelsWriter = csv.writer(trainSetLabelsFileObj)
        for group, label in self.labels.items():
            trainFiles = os.listdir(TRAIN_SET_SOURCE + group)
            trainFiles = np.random.choice(trainFiles, size=100, replace=False)
            for trainFile in trainFiles:
                trainSetLabelsWriter.writerow([trainFile, label])
                shu.copyfile(TRAIN_SET_SOURCE + group + DELIMITER + trainFile, TRAIN_SET_DESTINATION + trainFile)
                break
            break

        trainSetLabelsFileObj.close()