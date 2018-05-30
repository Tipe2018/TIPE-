import simdkalman
import numpy as np 
import csv 
#define model
kf=simdkalman.KalmanFilter(
    state_transition=[[1,1],[0,1]],
    process_noise=np.diag([0.1,0.01]),
    observation_model=np.array([[1,0]]),
    observation_noise=1.0)

##generate some fake data
#import numpy.random as random
##100 independent time series
#data=random.normal(size=(100,200))
## with 10% of NaNs denoting missing values
#data[random.uniform(size=data.shape) < 0.1] = np.nan

file=open('valeurs.csv','r')
file.readline() #lis la 1e ligne( celle des textes)
fichier=csv.reader(file, delimiter=';')
Lx=[]
for ligne in fichier:
    Lx.append(eval(ligne[1]))


#Smooth all data
smoothed = kf.smooth(Lx,initial_value = [1,0],initial_covariance = np.eye(2) * 0.5)

# second timeseries, third time step, hidden state x
print('mean')
print(smoothed.states.mean[0,:])

print('covariance')
print(smoothed.states.cov[0,:])
#Predict new data for a single series
predicted = kf.predict(Lx[1,2,:], 12)

# predicted observation y, third new time step
pred_mean = predicted.observations.mean[2]
pred_stdev = np.sqrt(predicted.observations.cov[2])

print('%g +- %g' % (pred_mean, pred_stdev))


