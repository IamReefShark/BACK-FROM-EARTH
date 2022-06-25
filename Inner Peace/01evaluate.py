import math
import heapq
import multiprocessing
import numpy as np
from time import time

_model = None
_testRatings = None
_testNegatives = None
_K = None

def evaluate_model(model, testRatings, testNegatives, K, num_thread):
	global _model
	global _testRatings
	global _testNegatives
	global _K
	_model = model
	_testRatings = testRatings
	_testNegatives = testNegatives
	_K = K

	hits, ndcgs = [],[]
	if(num_thread > 1):
		pool = multiprocessing.Pool(processes = num_thread)
		res = pool.map(eval_one_rating, range(len(_testRatings)))
		pool.close()
		pool.join()
		hits = [r[0] for r in res]
		ndcgs =