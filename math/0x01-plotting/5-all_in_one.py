#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)
#----------------------------------------
fig = plt.figure()
fig.suptitle("All in One")
ax0 = fig.add_subplot(3, 2, 1)
ax1 = fig.add_subplot(3, 2, 2)
ax2 = fig.add_subplot(3, 2, 3)
ax3 = fig.add_subplot(3, 2, 4)
ax4 = fig.add_subplot(3, 2, (5,6))

#plot1
ax0.plot( np.arange(0,11,1), y0, 'r-')
#plot2
ax1.set_xlabel('Height (in)',fontsize=8)
ax1.set_ylabel('Weight (lbs)',fontsize=8)
ax1.set_title("Men's Height vs Weight",fontsize=8)
ax1.scatter(x1, y1, c='m')
#plot3
ax2.set_xlabel('Time (years)',fontsize=8)
ax2.set_ylabel('Fraction Remaining',fontsize=8)
ax2.set_title("Exponential Decay of C-14",fontsize=8)
ax2.axis(xmin=0,xmax=28650)
ax2.plot(x2, y2)
ax2.set_yscale('log')
#plot4
ax3.set_xlabel('Time (years)',fontsize=8)
ax3.set_ylabel('Fraction Remaining',fontsize=8)
ax3.set_title('Exponential Decay of Radioactive Elements',fontsize=8)
ax3.set(xlim=(0, 20000), ylim=(0,1))
line_labels=["C-14","Ra-226"]
ax3.plot(x3, y31, 'r--')
ax3.plot(x3, y32, 'g-')
ax3.legend(   
           labels=line_labels,
           loc="upper right"   
           )
#plot5
ax4.set_xlabel('Grades',fontsize=8)
ax4.set_ylabel('Number of Students',fontsize=8)
ax4.set_title('Project A',fontsize=8)
ax4.axis([0,100,0,30])
ax4.hist(student_grades,bins=range(40,101,10),edgecolor='k')

fig.tight_layout()
plt.show()
