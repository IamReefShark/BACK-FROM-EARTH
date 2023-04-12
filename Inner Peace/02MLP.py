import numpy as np

import theano
import theano.tensor as T
import keras
from keras import backend as K
from keras import initializations
from keras.regularizers import l2, activity_l2
from keras.models import Sequential, Graph, Model
from keras.layers.core import Dense, Lambda, Activation
from keras.layers import Embedding, Input, Dense, merge, Reshape, Merge, Flatten, Dropout
from keras.constraints import maxnorm
from keras.optimizers import Adagrad, Adam, SGD, RMSprop
from evaluate import evaluate_model
from Dataset import Dataset
from time import time
import sys
import argparse
import multiprocessing as mp


def parse_args():
	parser = argparse.ArgumentParser(description = "Run MLP.")
	parser.add_argument('--path', nargs = '?', default = 'Data/', help = 'Input data path.')
	parser.add_argument('--dataset', nargs = '?', default = 'ml-1m', help = 'Choose a dataset.')
	parser.add_argument('--epochs', type = int, default = 100, help = 'Number of epochs.')
	parser.add_argument('--batch_size', type = int, default = 256, help = 'Batch size.')
	parser.add_argument('--layers', nargs = '?', default = '[64, 32, 16, 8]', help = "Size of each layer. Note that the concatenation of user and item embedding. So layers[0]/2 is the embedding size.")
	parser.add_argument('--reg_layers', nargs = '?', default = '[0,0,0,0]', help = "Regularization for each layer")
	parser.add_argument('--num_neg', type = int, default = 4, help = 'Number of negatives instances to pair with a positive instances.)
	parser.add_argument('--lr', type = float, default = 0.001, help = 'Learning rate.')
	parser.add_argument('--learner', nargs = '?', default = 'adam', help = 'Specify an optimizer: adagrad, adam, rmsprop, sgd')
	parser.add_argument('--verbose', type = int, default = 1, help = 'Show performance per')




























