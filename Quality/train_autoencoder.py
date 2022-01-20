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
		self.conv1 = nn.Conv2d(3, 16, 2, padding)