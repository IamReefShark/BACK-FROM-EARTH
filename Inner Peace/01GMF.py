import numpy as np
import theano.tensor as T
import keras
from keras import backend as K
from keras import initializations
from keras.models import Sequential, Model, load_model, save_model
from keras.layers.core import Dense, Lambda, Activation
from keras.layers import Embedding, Input, Dense, merge, Reshape, Merge, Flatten
from keras.optimizers import Adagrad, Adam, SGD, RMSprop
from keras.regularizers import l2
from Dataset import Dataset
from evaluate import evaluate_model
from time import time
import multiprocessing as mp
import sys
import math
import argparse


def parse_args():
	parser = argparse.ArgumentParser(description = "Run GMF.")
	parser.add_argument('--path', nargs = '?', default = 'Data/', help = 'Input data path.')
	parser.add_argument('--dataset', nargs = '?', default = 'ml-1m', help = 'Choose a dataset.')
	parser.add_argument('--epochs', type = int, default = 100, help = 'Number of epochs.')
	parser.add_argument('--batch_size', type = int, default = 256, help = 'Batch size.')
	parser.add_argument('--num_factors', type = int, default = 8, help = 'Embedding size.')
	parser.add_argument('--regs', nargs = '?', default = '[0,0]', help = "Regularization for user and item embeddings.")
	parser.add_argument('--num_neg', type = int, default = 4, help = 'Number of negative instances to pair with a positive instance.')
	parser.add_argument('--lr', type = float, default = 0.001, help = 'Learning rate.')
	parser.add_argument('--learner', nargs = '?', default = 'adam', help = 'Specify an optimizer: adagrad, adam, rmsprop, sgd')
	parser.add_argument('--verbose', type = int, default = 1, help = 'Show performance per X iterations')
	parser.add_argument('--out', type = int, default = 1, help = 'Whether to save the trained model.')
	return parser.parse_args()

def init_normal(shape, name = None):
	return initializations.normal(shape, scale = 0.1, name = n)















