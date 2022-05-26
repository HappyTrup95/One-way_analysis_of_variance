import pandas as pd
import scipy.stats as stats
import csv


data = pd.read_csv('', sep=',')
samples=[list(frame) for group,frame in data.groupby('Therapy')['expr']]
print(stats.f_oneway(*samples))
