import numpy as np
import pandas as pd
from sklearn import *
import gc
import os
import random

# Load dataset files
train = pd.read_csv('train.new1.csv', header = 0)
test = pd.read_csv('test.new1.csv', header = 0)

train_dummies = get_dummies(train)

print(train_dummies)
