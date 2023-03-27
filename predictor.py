import pickle
import pandas as pd
import numpy as np


# load the model from disk


def predict(file):
	
	df = pd.read_csv(file)
	ip = list()
	for rowval in df:
		ip.append(rowval)
	
	A = np.array(ip)
	B = np.reshape(A, (1, 178))
	B = B.astype(np.float64)
	with open('model_gnb.pkl','rb') as f:
	    mp=pickle.load(f)

	pred=mp.predict(B)

	res = pred[0]

	return res
	