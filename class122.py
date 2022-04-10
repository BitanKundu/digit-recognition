import cv2
import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
X,y=fetch_openml("mnist_784",verison=1,return_X_y=True)
classes=["0","1","2","3","4","5","6","7","8","9'"]