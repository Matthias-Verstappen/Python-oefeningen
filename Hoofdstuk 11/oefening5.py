# oefening 5

import numpy as np
import matplotlib.pyplot as plt

# functies

def convert(import_file):
    data = np.loadtxt(import_file, delimiter=';', dtype=float) #2d array
    data[:,1] = (data[:,1]-32)*5/9 # 2de kolom
    return data


# hoofdprogramma

converted_data = (convert('Files/degrees_fahrenheit.txt'))
plt.plot(converted_data[:,0], converted_data[:,1]) # x-as 1ste kolom, y-as 2de kolom
plt.title('Degrees Celsius')
plt.xlabel('Datapoints')
plt.ylabel('Temperatures')
plt.xticks(rotation=90)
plt.show()
