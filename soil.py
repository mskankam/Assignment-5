import numpy as np
import matplotlib.pyplot as plt

seiveSize = np.array([4.75,2,0.85,0.425,0.25,0.15,0.075]) #seive sizes used for experiment
percentPassed= np.array([100,95.2,84.2,61.4,41.6,20.4,6.9]) #percentage of soil particles that passed each seive
plt.figure(figsize=(8.5,6))
plt.semilogx(seiveSize, percentPassed)
plt.xlim(5,0.08)
plt.title('Percent Size Distribution Curve for Soil Sample')
plt.xlabel('seive size(mm)')
plt.ylabel('percentage passing (X)')
plt.tight_layout() #Automatically adjust th plot size in figure
plt.show()

