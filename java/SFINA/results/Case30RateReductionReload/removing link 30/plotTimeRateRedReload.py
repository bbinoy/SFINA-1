# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from loadData import *

mAcData = np.array(loadData('totalTime.txt',[0,2]))
mDcData = np.array(loadData('totalTime.txt',[2,4]))
iAcData = np.array(loadData('totalTime.txt',[4,6]))
iDcData = np.array(loadData('totalTime.txt',[6,8]))

iterData = np.array(loadData('iterations.txt',[0,8]))

mAcDataAvg = np.average(mAcData,axis=0)
mDcDataAvg = np.average(mDcData,axis=0)
iAcDataAvg = np.average(iAcData,axis=0)
iDcDataAvg = np.average(iDcData,axis=0)

iterDataAvg = np.average(iterData,axis=0)

times = np.linspace(0,29,30)
redFactor = np.linspace(0,50,30)
print(redFactor)
print(mAcDataAvg.shape)
print(redFactor.shape)

fig = plt.figure(figsize=(7.5, 7))
ax = fig.add_subplot(111)
plt.rcParams.update({'font.size': 16})

plt.plot(redFactor,mAcDataAvg, color='0', linewidth=3, linestyle='-', label='Matpower AC')
plt.plot(redFactor,iAcDataAvg, color='0', linewidth=3, linestyle='-', marker='o',label='InterPSS AC')
plt.plot(redFactor,mDcDataAvg, color='0.5', linewidth=3, linestyle='-', label='Matpower DC')
plt.plot(redFactor,iDcDataAvg, color='0.5', linewidth=3, linestyle='-',marker='o', label='InterPSS DC')

ax2 = ax.twinx()
ax2.bar(redFactor,iterDataAvg,color='0.8', label='Iterations')
ax2.set_ylabel('Iterations')
ax2.set_ylim(0,20)
#ax2.set_yticklabels(['0','6',' ',' ',' '])
ax2.legend(fontsize=16, loc=4)

ax.legend(loc=1, fontsize=16, labelspacing=0.15, borderpad=0.3, handletextpad=0.15, title='Simulation Time')
ax.tick_params(axis='both',length=8, width=1)
ax.set_ylabel('Simulation Time [ms]')
ax.set_xlabel('Capacity Reduction [%]')
plt.xlim(1,50)

x0, x1 = ax.get_xlim()
y0, y1 = ax.get_ylim()
#ax.set_aspect((x1-x0)/(y1-y0))

#fig.subplots_adjust(left=0.17)

plt.savefig('case30RateReductionSimuTimeSquare.pdf')
#plt.show()
#
#fig2 = plt.figure()
#ax = fig2.add_subplot(111)
#for line in mAcData:
#    plot(times,line)
#plt.title('MAT,AC') 
#    
#fig3 = plt.figure()
#ax = fig3.add_subplot(111)
#for line in mDcData:
#    plot(times,line)
#plt.title('MAT,DC')    
#    
#fig4 = plt.figure()
#ax = fig4.add_subplot(111)
#for line in iAcData:
#    plot(times,line)
#plt.title('IPSS,AC')    
#    
#fig5 = plt.figure()
#ax = fig5.add_subplot(111)
#for line in iDcData:
#    plot(times,line)
#plt.title('IPSS,DC')
    
plt.show()