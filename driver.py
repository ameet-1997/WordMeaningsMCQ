import argparse
import numpy as np
from sklearn.metrics import f1_score
import pandas as pd
from gensim_vectors import Meanings

def argparser():
    Argparser = argparse.ArgumentParser()
    Argparser.add_argument('--load', type=str, default='/media/ameet/8AD2C89ED2C88FBD/Books and Documents/Academics/IIT/IIT Material/Sem 6/NLP/Programming_Assignment/Word_Similarity/NLP_wordsim/Data/google/GoogleNews-vectors-negative300.bin', help='Path to binary file of vectors')
    Argparser.add_argument('--mode', type=int, default=1, help='2 for interactive shell and 1 for reading words from the file')


    args = Argparser.parse_args()
    return args


# Get the training data
args = argparser() 

# Create instance of object
meanings = Meanings(args)
meanings.calculate_score()