import pandas as pd
from scipy.io import arff
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

data, meta = arff.loadarff('D:\dataAnalysisRice-main\dataAnalysisRice-main\Rice_Cammeo_Osmancik.arff')
df = pd.DataFrame(data)
df['Class'] = df['Class'].str.decode('utf-8')

grouped = df.groupby('Class').agg(['mean', 'median', 'std'])
print(grouped.T)

plt.figure(figsize=(10, 6))
sns.boxplot(x='Class', y='Area', data=df)
plt.title('Box Plot of Area by Rice Class')
plt.savefig('BoxPlotofAreabyRiceClass.png')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Area', hue='Class', kde=True, bins=30)
plt.title('Histogram of Area by Rice Class')
plt.savefig("HistogramofAreabyRiceClass.png")
plt.show()

sns.pairplot(df, hue='Class', markers=["o", "s"], diag_kind='kde')
plt.suptitle('Pair Plot of Rice Attributes', y=1.02)
plt.savefig("PairPlotofRiceAttributes.png")
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Major_Axis_Length', y='Minor_Axis_Length', hue='Class', data=df)
plt.title('Scatter Plot of Major vs. Minor Axis Length')
plt.savefig("ScatterPlotofMajorvsMinorAxisLength.png")
plt.show()

plt.figure(figsize=(12, 8))
corr = df.drop('Class', axis=1).corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap of Rice Attributes')
plt.savefig("CorrelationHeatmapofRiceAttributes.png")
plt.show()
 
FinalConclusion = """
The analysis of the Cammeo and Osmancik rice varieties reveals several key differences between the two. 
The Cammeo variety generally has larger grains, as indicated by the greater area and longer major and minor 
axes, compared to the Osmancik variety. This is evident from the box plot, which shows a broader distribution 
of area sizes for Cammeo, and the histogram, where Cammeo grains demonstrate a higher average area.

The pair plot further illustrates distinct clustering patterns between the two varieties, with attributes like 
Area, Major Axis Length, and Minor Axis Length serving as strong indicators for differentiating the two classes. 
The scatter plot of Major Axis Length versus Minor Axis Length also supports this, showing that Cammeo grains 
are generally longer and larger than those of Osmancik. Additionally, the correlation heatmap reveals strong 
relationships between size-related attributes, such as Area and Convex Area, and Major Axis Length and Perimeter, 
suggesting that the physical dimensions of the grains are interconnected.

Overall, these findings suggest that the Cammeo variety is characterized by larger, more elongated grains, and that 
the measured attributes could be effectively used to classify the two rice varieties. This information could be 
valuable for developing automated systems for rice classification and quality control.
"""

print(FinalConclusion)
