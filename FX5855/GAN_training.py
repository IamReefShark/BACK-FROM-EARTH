import torch , torchvision
import numpy as np
from torch import nn as nn
import torch.nn.functional as F
import argparse
from Dataloader import get_train_valid_loader
import torchvision.utils as vutils
import matplotlib.pyplot as plt
from train_autoencoder import ConvAutoencoder
from train_ffn import CombineLatent

def Adversarial_training(Alice, Eve, Bob, FFN, train_data_loader, batch_size, FFN_o)