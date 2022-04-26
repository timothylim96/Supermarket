import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn
import seaborn as sns
import matplotlib.pyplot as plt

sales=pd.read_csv(r'C:\Users\timot\Desktop\Kagglicious\Supermarket\supermarket_sales - Sheet1.csv')
print(sales.head())
print(sales.info())
sales['date'] = pd.to_datetime(sales['Date'])
print(sales.info())
sales['date'].dtype
sales['date'] = pd.to_datetime(sales['date'])
sales['day'] = (sales['date']).dt.day
print(sales['day']) # which  day regardless of month/year sales were done
sales['month'] = (sales['date']).dt.month
print(sales['month'])# which  month regardless of year sales were done
sales['year'] = (sales['date']).dt.year
print(sales['year'])# which  year  sales were done
sales['Time'] = pd.to_datetime(sales['Time'])
sales['Hour'] = (sales['Time']).dt.hour
print(sales['Hour'].nunique()) #  11 unique hours sales were done
print(sales['Hour'].unique())
print(sales.describe())

categorical_columns = [cname for cname in sales.columns if sales[cname].dtype == "object"]
print(categorical_columns)
print("# unique values in Branch: {0}".format(len(sales['Branch'].unique().tolist())))
print("# unique values in City: {0}".format(len(sales['City'].unique().tolist())))
print("# unique values in Customer Type: {0}".format(len(sales['Customer type'].unique().tolist())))
print("# unique values in Gender: {0}".format(len(sales['Gender'].unique().tolist())))
print("# unique values in Product Line: {0}".format(len(sales['Product line'].unique().tolist())))
print("# unique values in Payment: {0}".format(len(sales['Payment'].unique().tolist())))

sns.set(style="darkgrid")      #gridplot
genderCount  = sns.countplot(x="Gender", data =sales).set_title("Gender_Count")
plt.show() # equal number of sales from males and females

sns.boxplot(x="Branch", y="Rating", data=sales).set_title("Ratings by Branch")
plt.show() # branch b has the lowest mean and percentile ratings as compared to branch A and C

genderCount  = sns.lineplot(x="Hour",  y = 'Quantity',data =sales).set_title("Product Sales per Hour")
plt.show() # most of the sales were done at 14:00 local time

genderCount  = sns.relplot(x="Hour",  y = 'Quantity', col= 'month' , row= 'Branch',
                           kind="line", hue="Gender", style="Gender", data =sales, markers=True,
                           height=1.5 )
plt.show()# see the hourly branch sales in a monthly fashion

genderCount  = sns.relplot(x="Hour",  y = 'Total', col= 'month' , row= 'Branch',
                           estimator = None, kind="line", data =sales,height=1.5)
plt.show()# total hourly sales in a monthly fashion

ax=sns.boxplot(y = 'Product line', x = 'Quantity', data=sales )
ax.tick_params(labelsize=6)
plt.show()

ax=sns.countplot(y = 'Product line', data=sales, order = sales['Product line'].value_counts().index )
ax.tick_params(labelsize=6)
plt.show()# Fashion Accessories is the highest while Health and beauty is the lowest

ax=sns.boxplot(y = 'Product line', x = 'Total', data=sales )
ax.tick_params(labelsize=6)
plt.show()

ax=sns.stripplot(y = 'Product line', x = 'Total', hue = 'Gender', data=sales )
ax.tick_params(labelsize=6)
plt.legend(bbox_to_anchor=(1, 1), loc=2)
plt.show()# distribution of how much each gender spends on the products

sns.relplot(y = 'Product line', x = 'gross income', data=sales )
plt.show()# distribution of gross income within each line of product

ax=sns.boxenplot(y = 'Product line', x = 'Rating', data=sales )
ax.tick_params(labelsize=6)
plt.show()#IQR distribution of ratings for each line of products. Food and Beverages have the highest average rating
# while sports and travel the lowest

sns.countplot(x="Payment", data=sales).set_title("Payment Channel")
plt.show()# most customers pay through Ewallet and cash payment

sns.countplot(x="Payment", hue = "Branch", data =sales).set_title("Payment Channel by Branch")
plt.show()# breaking down payment channels by branch

sales['Customer type'].nunique()
sns.countplot(x="Customer type", data=sales).set_title("Customer Type")
plt.show()#50% split btwn member and non member

sns.countplot(x="Customer type", hue="Branch", data=sales).set_title("Customer Type by Branch")
plt.show()# distribution of member type by branch

sales.groupby(['Customer type']).agg({'Total': 'sum'})
sns.barplot(x="Customer type", y="Total", estimator = sum, data=sales)
plt.show()# customer type and the amount of sales they do, member did more sales

sns.swarmplot(x="Customer type",  y = "Rating",  hue = "City", data =sales).set_title("Customer Type")
plt.show()# distribution of member type by cities and ratings


