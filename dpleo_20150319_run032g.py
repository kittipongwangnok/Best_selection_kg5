#PhD reseach 2020
#Kittipong Wangnok, D6010218
#School of Physics, Institute of Science, Suranaree University of Technology

#Import all module
import sys
import os
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
from statistics import stdev
from statistics import mean
np.seterr(divide='ignore', invalid='ignore')

#Latex font
import matplotlib as mpl
from matplotlib import rc
plt.rc('text', usetex=True)
plt.rc('font', family='serif',size=16)

'''
1. Input file
'''
#################################################################################
#Please change the input file
DP_Leo = open("dpleo_20150318_run031kg5.log",'r').readlines()
N_dpleo = len(DP_Leo)

MJD_time = []
Exp_time =[]
counts_1 = []
countse_1 = []
counts_2 = []
countse_2 = []
counts_3 = []
countse_3 = []
counts_4 = []
countse_4 = []
counts_5 = []
countse_5 = []

'''
2. Read file
'''

for line in open("dpleo_20150318_run031kg5.log"):
#for line in open("dpleo_20150319g.log"):
    li=line.strip()
    if not li.startswith("#"):
        MJD_time.append(float(li.split(" ")[2]))
        Exp_time.append(float(li.split(" ")[4]))
        counts_1.append(float(li.split(" ")[15]))
        countse_1.append(float(li.split(" ")[16]))
        counts_2.append(float(li.split(" ")[31]))
        countse_2.append(float(li.split(" ")[32]))
        counts_3.append(float(li.split(" ")[47]))
        countse_3.append(float(li.split(" ")[48]))
        counts_4.append(float(li.split(" ")[63]))
        countse_4.append(float(li.split(" ")[64]))
        counts_5.append(float(li.split(" ")[79]))
        countse_5.append(float(li.split(" ")[80]))
#################################################################################
#Number of dpleo data
#print ('Number of data: I:', N_dpleo)

#Input data
x = MJD_time
ex = Exp_time
tar = counts_1
tar_err = countse_1
ref = counts_2
ref_err = countse_2
chk1 = counts_3
chk1_err = countse_3
chk2 = counts_4
chk2_err = countse_4
chk3 = counts_5
chk3_err = countse_5


data_demo = []
for i in range(len(x)):
        ex_day = ex[i]/(24*60*60)
        Flux_12 = tar[i]/ref[i]
        Flux_err_12 = (tar[i]/ref[i])*np.sqrt((tar_err[i]/tar[i])**2 + (ref_err[i]/ref[i])**2)
        weight_factor = 1
        subdivision = 2
        data_demo.append('%0.6f %0.6f %0.6f %0.6f %0.0f %0.0f' %(x[i], ex_day, Flux_12, Flux_err_12, weight_factor, subdivision))

'''
3. Save file
'''
extraction_method = data_demo
f = open("dpleo_20150318_run031kg5.dat", 'w')
for i in range(len(extraction_method)):
    f.write(str(extraction_method[i])+ '\n')
f.close()
