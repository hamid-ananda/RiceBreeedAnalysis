import pandas as pd
from scipy.io import arff
import numpy as np
import matplotlib.pyplot as plt 

data, meta = arff.loadarff('rice+cammeo+and+osmancik/Rice_Cammeo_Osmancik.arff')
df = pd.DataFrame(data)
df.columns = ["Area", "Perimeter", "Major Axis Length", "Minor Axis Length", "Eccentricity", "Convex Area", "Extent", "Class"]
df.to_csv('rice+cammeo+and+osmancik/Rice_Cammeo_Osmancik.csv', index=False)

#descriptive data analysis  
print(df.describe())