#!/usr/bin/env python
# coding: utf-8

# ## Countries - Cluster Analysis

# Clustering of Clustering
# Types of Clustering:
# 1. Flat - i.e. K-Means
# 2. Hierarchical - the firt type of clustering
#                   (i.e. taxonomy of the animal kingdom)
#                 - Types: 
#                     1. Agglomerative (Bottom-Up) - easier to solve 
#                                                  - start with each cluster being its own, repetitive (n, n-1, n-2)
#                     2. Divisive (Top-Down) - i.e. dinosaurs, used in Elbow Method
# Dendogram - Agglomerative type of clustering
#    PROS: 
#        1. Hiearchical clustering shows all the possible linkages between clusters
#        2. We understand the data much, much better
#        3. No need to preset the number of clusters (like with k-means)
#        4. Many methods to perform hiearchical clustering (Ward!)
#   CONS:
#        1. Scalibility; hard to examine large group of observations, also expensive


# ### Import the Relevant Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set() #set style to seaborn


# ### Load the Data

# 'pd.read_csv(*.csv, index_col)' loads a given CSV file as a data frame
# 'index_col' is an argument which can specify a given column from the CSV as index of the data frame 
data = pd.read_csv('Country clusters standardized.csv', index_col='Country')


x_scaled = data.copy()
x_scaled = x_scaled.drop(['Language'], axis=1) # remove 'Language' column
x_scaled


# ### Plot the Data
sns.clustermap(x_scaled, cmap='mako')


# on the left side: dendogram
# on the top: a dendogram uniting the two features
# on the bottom: features
# on the right: observations

# note that Australia is a complete different color due to it being the only country in the southern hemisphere
