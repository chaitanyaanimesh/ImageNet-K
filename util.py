import os
import constants

def sanityCheck():
    if not os.path.exists(constants.TARGET_GROUPS_FILE):
        raise FileNotFoundError("Target Group File Not found. Please specify the correct path for it.")
    elif not os.path.exists(constants.GROUP_TO_LABELS_MAPPING_LOCATION):
        raise FileNotFoundError("Path specified in GROUP_TO_LABELS_MAPPING_LOCATION doesn't exist.")
    else:
        pass