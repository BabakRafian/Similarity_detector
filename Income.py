'''
@Author: Babak Rafian
This program finds and reports the k number of closest neighbour for each data point in Income.csv
'''

import pandas as pd
import sys

data = pd.read_csv('data/Income.csv')
k = 5

def ageSim(p,q):
    if q.age <= p.age + 5 and q.age >= p.age-5:
        return 1
    else:
        return 0

def workclassSim(p,q):
    if p.workclass == q.workclass:
        return 1
    else:
        return 0

def eduSim(p,q):
    if p.education == q.education:
        return 1
    else:
        return 0

def maritalSim(p,q):
    if p.marital_status == q.marital_status:
        return 1
    else:
        return 0

def occuSim(p,q):
    if p.occupation == q.occupation:
        return 1
    else:
        return 0

def relationSim(p,q):
    if p.relationship == q.relationship:
        return 1
    else:
        return 0

def raceSim(p,q):
    if p.race == q.race:
        return 1
    else:
        return 0

def genderSim(p,q):
    if p.gender == q.gender:
        return 1
    else:
        return 0

def capitalSim(p,q):
    pCapital = p.capital_gain - p.capital_loss
    qCapital = q.capital_gain - q.capital_loss
    if (pCapital< 0 and qCapital <0) or (pCapital>0 and qCapital>0) or (pCapital==0 and qCapital==0):
        return 1
    else:
        return 0

def workHourSim(p,q):
    if (p.hour_per_week < 40 and q.hour_per_week <40) or (p.hour_per_week >= 40 and q.hour_per_week >= 40):
        return 1
    else:
        return 0

def countrySim(p,q):
    if p.native_country == q.native_country:
        return 1
    else:
        return 0

def sim(p,q):
    w = 0.09
    similarity = w*(ageSim(p,q))+ w*(workclassSim(p,q))+ w*(eduSim(p,q))+w*(maritalSim(p,q))+ w*(occuSim(p,q))+ w*(relationSim(p,q))+ w*(raceSim(p,q))+ w*(genderSim(p,q))+ w*(capitalSim(p,q))+ w*(workHourSim(p,q))+ w*(countrySim(p,q))
    return similarity

sys.stdout.write("Transaction ID  1st ID  1st Prox")
sys.stdout.write("\t\t\t2nd ID  2nd Prox")
sys.stdout.write("\t\t\t3rd ID  3rd Prox")
for i in range(4,k+1):
    sys.stdout.write("\t\t\t{0}th ID  {0}th Prox".format(i))


print
#print('Transaction ID   1st ID  1st Prox  \t\t\t2nd ID  2nd Prox   \t\t\t3rd ID  3rd Prox   \t\t\t4th ID  4th Prox   \t\t\t5th ID  5th Prox')
for i in range(data.__len__()):
    p = data.iloc[i]
    list = []
    for j in range(data.__len__()):
        q= data.iloc[j]
        if q.ID != p.ID:
            similarity = sim(p,q)
            #print(similarity)
            tupl = (q, similarity)
            if len(list) <= k:
                list.append(tupl)
            else:
                for x in range(k):
                    if similarity > list[x][1]:
                        del list[x]
                        list.append(tupl)
                        break
    for y in range(k):
        sys.stdout.write("{0}".format(i+1))
        sys.stdout.write("\t\t\t\t {0}".format(list[y][0].ID))
        sys.stdout.write("\t{0}".format(list[y][1]))
    print

