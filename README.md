# Rice Analysis Project

## Overview
This project analyzes two rice varieties, `Cammeo` and `Osmancik`, using various statistical methods and visualizations to identify distinguishing features.

## Conclusions
The analysis of the Cammeo and Osmancik rice varieties reveals several key differences between the two. The Cammeo variety generally has larger grains, as indicated by the greater area and longer major and minor axes, compared to the Osmancik variety. This is evident from the box plot, which shows a broader distribution of area sizes for Cammeo, and the histogram, where Cammeo grains demonstrate a higher average area.

The pair plot further illustrates distinct clustering patterns between the two varieties, with attributes like Area, Major Axis Length, and Minor Axis Length serving as strong indicators for differentiating the two classes. The scatter plot of Major Axis Length versus Minor Axis Length also supports this, showing that Cammeo grains are generally longer and larger than those of Osmancik. Additionally, the correlation heatmap reveals strong relationships between size-related attributes, such as Area and Convex Area, and Major Axis Length and Perimeter, suggesting that the physical dimensions of the grains are interconnected.

Overall, these findings suggest that the Cammeo variety is characterized by larger, more elongated grains, and that the measured attributes could be effectively used to classify the two rice varieties. This information could be valuable for developing automated systems for rice classification and quality control.

## Visualizations

### Box Plot of Area by Rice Class
![Box Plot](https://raw.githubusercontent.com/hamid-ananda/RiceBreeedAnalysis/main/BoxPlotofAreabyRiceClass.png)

### Histogram of Area by Rice Class
![Histogram](https://raw.githubusercontent.com/hamid-ananda/RiceBreeedAnalysis/main/HistogramofAreabyRiceClass.png)

### Pair Plot of Rice Attributes
![Pair Plot](https://raw.githubusercontent.com/hamid-ananda/RiceBreeedAnalysis/main/PairPlotofRiceAttributes.png)

### Scatter Plot of Major vs. Minor Axis Length
![Scatter Plot](https://raw.githubusercontent.com/hamid-ananda/RiceBreeedAnalysis/main/ScatterPlotofMajorvsMinorAxisLength.png)

### Correlation Heatmap of Rice Attributes
![Correlation Heatmap](https://raw.githubusercontent.com/hamid-ananda/RiceBreeedAnalysis/main/CorrelationHeatmapofRiceAttributes.png)
