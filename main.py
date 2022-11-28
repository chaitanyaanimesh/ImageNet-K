from generator import Generator
import argparse
import util

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", default="val", type=str,
                        help="Specify which part of dataset needs to be generated. Choices = ['val','train']")
    args = parser.parse_args()
    return args

if __name__=="__main__":

    #Parse the arguments
    args = parseArgs()

    #Sanity check before proceeding forward
    util.sanityCheck()

    #Create Gennerator object
    generatorObj = Generator()

    #Call the specifief task
    if args.task == 'val':
        generatorObj.generateValSet()
    elif args.task == 'train':
        generatorObj.generateTrainSet()
    else:
        raise ValueError('Invalid task supplied. Please select either \'val\' or \'train\'')


















