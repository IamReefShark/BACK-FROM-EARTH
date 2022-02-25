import torch, torchvision
import numpy as np
from torchvision import datasets
from torchvision import transforms
from torch.utils.data.sampler import SubsetRandomSampler
from torch import nn as nn
import torch.nn.functional as F
import argparse
from Dataloader import get_train_valid_loader

class ConvAutoencoder(nn.Module):
	def __init__(self):
		super(ConvAutoencoder, self).__init__()
		self.conv1 = nn.Conv2d(3, 16, 2, padding = 1)
		self.conv2 = nn.Conv2d(16, 4, 2, padding = 1)
		self.pool = nn.MaxPool2d(2, 2)
		self.t_conv1 = nn.ConvTranspose2d(4, 16, 2, stride = 2)
		self.t_conv2 = nn.ConvTranspose2d(16, 3, 2, stride = 2)
		
	def forward(self, x):
		x = F.relu(self.conv1(x))
		x = self.pool(x)
		x = F.relu(self.conv2(x))
		x = self.pool(x)
		x = F.relu(self.t_conv1(x))
		x = torch.tanh(self.t_conv2(x))
		return x

	def extract_latent(self, x):
		x = F.relu(self.conv1(x))
		x = self.pool(x)
		x = F.relu(self.conv2(x))
		x = self.pool(x)
		return x

	def distract_latent(self, x):
        x = F.relu(self.t_conv1(x))
        x = torch.tanh(self.t_conv2(x))
        return x



def train_autoencoder(Alice, train_data_loader, valid_data_loader, batch_size, c_optim, n_epoch, chkpt_file):
	min_train_loss = 100
	for j in range(n_epoch):
	  print("The Epoch is:", j)
	  Alice.train()
	  train_loss = 0
	  for i, train_data in enumerate(train_data_loader):
	  	c_optim.zero_grad()
	  	img = train_data[0]
	  	t_img = Alice(img)
	  	criterion = nn.MSELoss()
	  	loss = criterion(img, t_img)
	  	if i%10







