import random
import numpy as np

X_train = []
y_train = []
X_test = []
colors = ['red', 'blue', 'green', 'orange', 'yellow', 'black', 'white', 'grey', 'purple', 'pink']

for _ in range(100):
    x, y, z = random.randint(1,10),random.randint(1,10),random.randint(1,10)
    if [x,y,z] not in X_train:
        X_train.append([x,y,z])

for _ in range(len(X_train)):
    y_train.append(colors[random.randint(0,len(colors)-1)])

for _ in range(20):
    x, y, z = random.random()*10.0,random.random()*10.0,random.random()*10.0
    if [x,y,z] not in X_test:
        X_test.append([x,y,z])
        
def nearest(X_train, y_train, X_test_value):
    small=10000000000
    x_final=[]
    for x in X_train:
        if np.linalg.norm(np.asarray(x)-np.asarray(X_test_value))<small:
            small=np.linalg.norm(np.asarray(x)-np.asarray(X_test_value))
            x_final=X_train[X_train.index(x)]
    return y_train[X_train.index(x_final)]

def nearestWookies(X_train, y_train, X_test):
    wookie_colors = []
    for x in X_test:
        color = nearest(X_train, y_train, x)
        wookie_colors.append(color)
        
    return wookie_colors