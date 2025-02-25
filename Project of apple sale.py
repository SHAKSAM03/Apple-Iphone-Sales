#-------------------------------------------------------------------------------
# Name:        Project iphone sales
# Purpose:
#
# Author:      Shaksam
#
# Created:     24/02/2025
# Copyright:   (c) Shaksam 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
# we are using the apple_products dataset
data = pd.read_csv(r"C:\Users\Hp\Downloads\apple_products.csv")
print(data)
print(data.isnull().sum())
print(data.describe())

#Apple sales analysis in India
highest_rated=data.sort_values(by=["Star Rating"],ascending =False)
highest_rated=highest_rated.head(10)
print(highest_rated['Product Name'])

# HIGHEST  rated iphone on flipkart
iphones=highest_rated["Product Name"].value_counts()
labels= iphones.index
counts=highest_rated["Number Of Ratings"]
figure= px.bar(highest_rated,x=labels,y=counts)
figure.show()
print(iphones)


reviews=highest_rated["Number Of Reviews"]
figure= px.bar(highest_rated,x=labels,y=reviews)
figure.show()
print(iphones)

figure = px.scatter(data_frame =data, x="Number Of Ratings",y="Sale Price",size="Discount Percentage",trendline="ols",title="Relationship between sale price and number of rating")
figure.show()

figure = px.scatter(data_frame =data, x="Number Of Ratings",y="Discount Percentage",size="Sale Price",trendline="ols",title="Relationship between Discount Percentage and number of rating")
figure.show()


