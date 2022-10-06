import torch.nn as nn
import torch.nn.functional as F
import torch



class MLP(nn.Module):
# Multilayer Perceptron for regression.

	def __init__(self):
		super().__init__()
		self.layers = nn.Sequential(
			nn.Linear(5, 64),
			nn.ReLU(),
			nn.Linear(64, 64),
			nn.ReLU(),
			nn.Linear(64, 1)
			)


	def forward(self, x):
	
	  return self.layers(x)