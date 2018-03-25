#Finding optimum number of epochs.
from sklearn.random_projection import sparse_random_matrix
import numpy as np
import surprise
import pandas as pd
import matplotlib.pyplot as plt
from surprise.model_selection import GridSearchCV
from surprise import SVD
import time
import os
import psutil




# run 'pip install scikit-surprise' to install surprise
class MatrixFacto(surprise.AlgoBase):
    '''A basic rating prediction algorithm based on matrix factorization.'''

    def __init__(self, learning_rate, n_epochs, n_factors):

        self.lr = learning_rate  # learning rate for SGD
        self.n_epochs = n_epochs  # number of iterations of SGD
        self.n_factors = n_factors  # number of factors

    def train(self, trainset):
        '''Learn the vectors p_u and q_i with SGD'''

        print('Fitting data with SGD...')

        # Randomly initialize the user and item factors.
        p = np.random.normal(0, .1, (trainset.n_users, self.n_factors))
        q = np.random.normal(0, .1, (trainset.n_items, self.n_factors))

        # SGD procedure
        for _ in range(self.n_epochs):
            for u, i, r_ui in trainset.all_ratings():
                err = r_ui - np.dot(p[u], q[i])
                # Update vectors p_u and q_i
                p[u] += self.lr * err * q[i]
                q[i] += self.lr * err * p[u]
                # Note: in the update of q_i, we should actually use the previous (non-updated) value of p_u.
                # In practice it makes almost no difference.

        self.p, self.q = p, q
        self.trainset = trainset

    def estimate(self, u, i):
        '''Return the estmimated rating of user u for item i.'''

        # return scalar product between p_u and q_i if user and item are known,
        # else return the average of all ratings
        if self.trainset.knows_user(u) and self.trainset.knows_item(i):
            return np.dot(self.p[u], self.q[i])
        else:
            return self.trainset.global_mean







y = []
y_plot = []
counter = 0
x_plot = []
time_plot = []
mem_plot = []

for i in range(1, 10):


    reader = surprise.Reader(name=None, line_format='user item rating', sep=',', skip_lines=1)
    data = surprise.Dataset.load_from_file('/Users/keyadesai/Desktop/Recommendation Engine/ratings_woheader.csv',
                                           reader=reader)
    # data.split(5)

    algo = surprise.KNNBasic()
    param_grid = {'n_epochs': [i], 'lr_all': [0.005],
                  'reg_all': [0.02]}
    
    gs = GridSearchCV(SVD, param_grid, measures=['rmse', 'mae'], cv=3)
    gs.fit(data)
    results_df = pd.DataFrame.from_dict(gs.cv_results)

    y.append(results_df.mean_test_rmse)
    y_plot.append(y[counter][0])
    x_plot.append(i)



print(y_plot)
plt.plot(x_plot, y_plot, 'ro')
plt.xlabel('Number of epochs')
plt.ylabel(('Mean RMSE'))
plt.show()
