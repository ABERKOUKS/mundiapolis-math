#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.suptitle('Project A')
plt.axis([0,100,0,30])
plt.hist(student_grades,bins=range(40,101,10),edgecolor='k')
plt.show()