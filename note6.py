import matplotlib . pyplot as plt
import numpy as np
import pandas as pd
import datetime
from scipy . optimize import curve_fit
covid = pd . read_csv ('https://raw.githubusercontent.com/AndreSlash/cases/main/owid-covid-data.csv')
covid . tail ()
covid_hk = covid [ covid ['location']. str. contains ('Bulgaria')]
covid_hk = covid_hk [[ 'date', 'total_cases']]
Y = covid_hk [[ 'total_cases']]
X = covid_hk [[ 'date']]
t = np . linspace (1 , len (X) , len (X))
fig , ax = plt . subplots ()
ax . plot (t ,Y )
plt . show () 
covid_hk = covid_hk [[ 'date', 'total_cases']]

Y1 = Y. head (200)
X1 = X. head (200)
t1 = np . linspace (0 , 1 , len ( X1 ))
fig , ax = plt . subplots ()
ax . plot (t1 , Y1 )
plt . show ()
def logistic (t , r , N0 , k):
  return r * N0 * np . exp ( r * t) * (1 - (( N0 * np . exp (r * t)) / k))
Y1_2=[]
for s in range ( len ( Y1 )):
  Y1_2.append ( Y1.values [s][0])
l = np . linspace (0 , 1, 200)

popt , pcov = curve_fit ( logistic , l , Y1_2 , p0 =[1 ,0 ,1] , maxfev =10000)
q ,w , e = popt
plt . plot (l , Y1 )
ly = logistic (l , q , w , e)
plt.plot (l , ly )
plt.show ()
