import scipy.sparse as sp
import numpy as np

class Dataset(object):

	def __init__(self, path):

		self.trainMatrix = self.load_rating_file_as_matrix(path + ".train.rating")
		self.testRatings = self.load_rating_file_as_list(path + ".test.rating")
		self.testNegatives = self.load_negative_file(path + ".test.negative")
		assert len(self.testRatings) == len(self.testNegatives)

		self.num_users, self.num_items = self.trainMatrix.shape

	def load_rating_file_as_list(self, filename):
		ratingList = []
		with open(filename, "r") as f:
			line = f.readline()
			while line != None and line != "":
				arr = line.split("\t")
				user, item = int(arr[0]),