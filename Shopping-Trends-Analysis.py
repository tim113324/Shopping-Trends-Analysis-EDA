import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.rc('font', family = 'Microsoft JhengHei') #------讓圖表文字能和微軟正黑體相容


# 檢查資料
df = pd.read_csv('shopping_trends_updated.csv')
# 查看資料資訊
df.info()                 
# 檢查資料是否有Null值(無)
pd.set_option('display.max_columns', None)
# 檢查是否有重複資料(無)
print(df.duplicated())
# 查看資料的敘述性統計
print(df.describe())
for data in df.columns:
    print(data)
    print(df[data].unique())
    print("=======================================================")




# 一、對象調查（顧客基本資料（性別比例、年齡分布、地區分布(前十)）） 
labels = []
gender_counts = df['Gender'].value_counts()
count_M = gender_counts.get('Male', 0)
count_F = gender_counts.get('Female', 0)
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
plt.subplots_adjust(wspace = 0.5)
axes[0].pie([count_M, count_F],
        autopct = '%1.1f%%',
        colors = ['lightblue', 'pink'],
        labels = ('男', '女')
)
axes[0].set_title('性別比例')
axes[0].set_ylabel('')

age_gender = df.groupby(['Age', 'Gender'])['Age'].size().unstack()
axes[1].scatter(age_gender.index, age_gender['Male'], color = 'lightblue', label = 'Male')
axes[1].scatter(age_gender.index, age_gender['Female'], color = 'pink', label = 'Female')
axes[1].legend()
axes[1].set_title('年齡依男女的人數分布')
axes[1].set_ylabel('人數')
axes[1].set_xlabel('年齡')

location = df.groupby(['Location'])['Location'].size().nlargest(10)
location.plot(kind = 'barh', color = '#C48888', ax = axes[2])
axes[2].set_title('地區分布（前十）')
axes[2].set_xlabel('')
axes[2].set_ylabel('')
plt.show()




# 二、探討問題（顧客在購買上的表現）
# 1. 性別對購買金額影響
gender_buy = df.groupby(['Gender'])['Purchase Amount (USD)'].sum()
bars = gender_buy.plot(kind = 'bar', color = ['pink', 'lightblue'], figsize = (10, 6))
for bar in bars.containers:
    bars.bar_label(bar, label_type = 'edge')
plt.xlabel('')
plt.ylabel('')
plt.title('男女的個別銷售額')
plt.xticks(rotation = 0)
plt.show()


# 2. 各年齡層對購買金額影響
bins = [10, 20, 30, 40, 50, 60, 70]
labels = ['10-20', '21-30', '31-40', '41-50', '51-60', '61-70']
df['Age Range'] = pd.cut(df['Age'], bins=bins, labels=labels)
ageprice = df.groupby(['Age Range'])['Purchase Amount (USD)'].sum()
bars = ageprice.plot(kind = 'bar', color = '#FFAF60', figsize = (10, 6))
for bar in bars.containers:
    bars.bar_label(bar, label_type = 'edge')
plt.xlabel('')
plt.ylabel('')
plt.title('各年齡層的銷售額')
plt.xticks(rotation = 0)
plt.show()


# 3. 銷售額前十商品 vs 銷量前十商品
fig, axes = plt.subplots(1, 2, figsize = (15, 7))
product = df.groupby(['Item Purchased'])['Purchase Amount (USD)'].sum().nlargest(10)
bars1 = product.plot(kind = 'bar', color = '#FFAF60', ax = axes[0])
for i, bar1 in enumerate(bars1.patches):
    height = bar1.get_height()
    axes[0].text(bar1.get_x() + bar1.get_width() / 2, height, height, ha = 'center', va = 'bottom')
axes[0].set_xlabel('')
axes[0].set_ylabel('')
axes[0].set_title('銷售額前十商品')
axes[0].tick_params(axis = 'x', rotation = 45)
product_sum = df.groupby(['Item Purchased'])['Purchase Amount (USD)'].sum()
product_ten = df.groupby(['Item Purchased']).size().nlargest(10)
product = product_sum.loc[product_ten.index]
bars2 = product.plot(kind = 'bar', color = '#7AFEC6', ax = axes[1])
for x, bar2 in enumerate(bars2.patches):
    height = bar2.get_height()
    axes[1].text(bar2.get_x() + bar2.get_width() / 2, height, height, ha = 'center', va = 'bottom')
axes[1].set_xlabel('')
axes[1].set_ylabel('')
axes[1].set_title('銷量前十商品')
axes[1].tick_params(axis = 'x', rotation = 45)
plt.show()


# 4. 哪些種類、尺寸、類別、顏色（前十）比較多人買
category = df.groupby(['Category'])['Category'].size()
fig, axes = plt.subplots(1, 3, figsize = (16, 5))
category.plot(kind = 'pie', autopct = '%1.1f%%', colors = sns.color_palette('deep'), ax = axes[0])
axes[0].set_title('類別購買比例')
axes[0].set_ylabel('')
size = df.groupby(['Size'])['Size'].size()
size.plot(kind = 'pie', autopct = '%1.1f%%', colors = sns.color_palette('deep'), ax = axes[1])
axes[1].set_title('尺寸購買比例')
axes[1].set_ylabel('')
color = df.groupby(['Color'])['Color'].size().nlargest(10).sort_values(ascending = True)
colors = []
row = 0
while row <= 9:
    colors.append(color.index[row])
    row += 1
color.plot(kind = 'barh', color = colors, ax = axes[2])
axes[2].set_title('前十熱門顏色')
axes[2].set_ylabel('')
plt.subplots_adjust(wspace = 0.5)
plt.show()


# 5. 性別在各類別上的銷量影響
category_age = df.groupby(['Category', 'Gender']).size().unstack()
category_age.plot(kind = 'bar', color = ['pink', 'lightblue'], figsize = (10, 6), stacked = True)
plt.title('男女在各類別上的銷量')
plt.xlabel('')
plt.xticks(rotation = 0)
for i in range(len(category_age)):
    female_value = category_age.iloc[i, 0]
    male_value = category_age.iloc[i, 1]
    total = female_value + male_value
    plt.text(i, female_value / 2, female_value, ha = 'center', va = 'center', color = 'white')
    plt.text(i, female_value + male_value / 2, male_value, ha = 'center', va = 'center', color = 'white')
    plt.text(i, total, total, ha = 'center', va = 'bottom')
plt.show()


# 6. 銷售額前十地區
location = df.groupby(['Location'])['Purchase Amount (USD)'].sum().nlargest(10)
barhs = location.plot(kind = 'barh', color = '#C48888', figsize = (10, 6))
for barh in barhs.containers:
    barhs.bar_label(barh, label_type = 'edge')
plt.title('銷售額前十地區')
plt.xlabel('')
plt.ylabel('')
plt.show()


# 7. 哪些運送方案，支付方式較多人使用
deliver = df.groupby(['Shipping Type'])['Shipping Type'].size()
fig, axes = plt.subplots(1, 2, figsize = (10, 5))
deliver.plot(kind = 'pie', autopct = '%1.1f%%', colors = sns.color_palette('pastel'), ax = axes[0])
axes[0].set_title('運送方案')
axes[0].set_ylabel('')
pay = df.groupby(['Payment Method'])['Payment Method'].size()
deliver.plot(kind = 'pie', autopct = '%1.1f%%', colors = sns.color_palette('pastel'), ax = axes[1])
axes[1].set_title('支付方式')
axes[1].set_ylabel('')
plt.subplots_adjust(wspace = 0.7)
plt.show()


# 8. 訂閱狀態在購買頻率次數上的影響
frequency = df.groupby(['Frequency of Purchases', 'Subscription Status'])['Frequency of Purchases'].size().unstack()
bars = frequency.plot(kind = 'bar', color = sns.color_palette('pastel'), figsize = (10, 8))
for bar in bars.containers:
    bars.bar_label(bar, label_type = 'edge')
plt.title('訂閱狀態在購買頻率次數上的表現')
plt.ylabel('')
plt.xlabel('')
plt.xticks(rotation = 45)
plt.show()


# 9. 各季的銷售額成長曲線
season_order = ['Spring', 'Summer', 'Fall', 'Winter']
df['Season'] = pd.Categorical(df['Season'], categories = season_order, ordered = True)
seasonsales = df.groupby(['Season'])['Purchase Amount (USD)'].sum()
bars = seasonsales.plot(kind='bar', color='#66B3FF', figsize = (10, 6))
lines = seasonsales.plot(kind = 'line', color = '#EAC100', marker='o', ax = bars)
for i, value in enumerate(seasonsales):
    lines.text(i, value + 0.02 * max(seasonsales), value, ha='center', color='#EAC100')
plt.title('各季的銷量成長曲線')
plt.ylabel('')
plt.xlabel('')
plt.show()


# 10. 前十熱門商品的顏色選擇及銷量為何
ten_size = []
color = []
for item in product_ten.index:
    product_color = df[df['Item Purchased'] == item].groupby(['Color']).size()
    max_color = product_color.idxmax()
    max_count = product_color.max()
    color.append(max_color)
    ten_size.append(int(max_count))
plt.figure(figsize = (15, 6))
bars = plt.bar(product_ten.index, ten_size, color = '#C48888')
plt.title('前十熱門商品的顏色選擇及銷量')
plt.xlabel('')
plt.ylabel('')
plt.xticks(rotation = 45)
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height / 2, color[i], ha = 'center', va = 'center', color = 'white')
    plt.text(bar.get_x() + bar.get_width() / 2, height, height, ha = 'center', va = 'bottom')
plt.show()


# 11. 前十熱門商品的類別選擇及銷量為何
ten_size = []
category = []
for item in product_ten.index:
    product_cat = df[df['Item Purchased'] == item].groupby(['Category']).size()
    max_cat = product_cat.idxmax()
    max_count = product_cat.max()
    category.append(max_cat)
    ten_size.append(int(max_count))
plt.figure(figsize = (15, 6))
bars = plt.bar(product_ten.index, ten_size, color = '#C48888')
plt.xlabel('')
plt.ylabel('')
plt.title('前十熱門商品的類別選擇及銷量')
plt.xticks(rotation = 45)
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height / 2, category[i], ha = 'center', va = 'center', color = 'white')
    plt.text(bar.get_x() + bar.get_width() / 2, height, height, ha = 'center', va = 'bottom')
plt.show()


# 12. 前十熱門商品的購買頻率次數為何
product_max_fres = []
max_freq_types = []
for item in product_ten.index:
    freq_counts = df[df['Item Purchased'] == item].groupby('Frequency of Purchases').size()
    max_freq = freq_counts.idxmax()
    max_count = freq_counts.max() 
    product_max_fres.append(max_count)
    max_freq_types.append(max_freq)
plt.figure(figsize = (18, 6))
bars = plt.bar(product_ten.index, product_max_fres, color = '#C48888')
plt.title('前十熱門商品的購買頻率次數')
plt.xlabel('')
plt.ylabel('')
plt.xticks(rotation = 45)
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height / 2, max_freq_types[i], ha = 'center', va = 'center', color = 'white')
    plt.text(bar.get_x() + bar.get_width() / 2, height, height, ha = 'center', va = 'bottom')
plt.show()


# 13. 前十熱門商品在各季的銷量表現
product_season = df.groupby(['Item Purchased', 'Season']).size().unstack()
product = product_season.loc[product_ten.index]
product.plot(kind = 'bar', color = sns.color_palette('pastel'), figsize=(18, 6), stacked = True)
for i in range(len(product)):
    fall = product.iloc[i, 0]
    spring = product.iloc[i, 1]
    summer = product.iloc[i, 2]
    winter = product.iloc[i, 3]
    total = fall + spring + summer + winter
    plt.text(i, fall / 2, int(fall), ha = 'center', va = 'center', color = 'white')
    plt.text(i, fall + spring / 2, int(spring), ha = 'center', va = 'center', color = 'white')
    plt.text(i, fall + spring + summer / 2, int(summer), ha = 'center', va = 'center', color = 'white')
    plt.text(i, fall + spring + summer + winter / 2, int(winter), ha = 'center', va = 'center', color = 'white')
    plt.text(i, total, total, ha = 'center', va = 'bottom', color = 'black')
plt.title('前十熱門商品在各季的銷量表現')
plt.xticks(rotation = 45)
plt.show()


# 14. 前十平均評價最好的商品 vs 前十熱門商品的平均評價
review_ten = df.groupby(['Item Purchased'])['Review Rating'].mean().round(1).nlargest(10)
fig, axes = plt.subplots(1, 2, figsize = (15, 6))
bars1 = review_ten.plot(kind = 'bar', color = '#A6A6D2', ax = axes[0])
for i, bar1 in enumerate(bars1.patches):
    height = bar1.get_height()
    axes[0].text(bar1.get_x() + bar1.get_width() / 2, height, height, ha = 'center', va = 'bottom')
axes[0].set_title('前十平均評價最好的商品')
axes[0].set_xlabel('')
axes[0].set_ylabel('')
axes[0].tick_params(axis='x', rotation=45)
product_review = df.groupby(['Item Purchased', ])['Review Rating'].mean().round(1)
product_ten_review = product_review.loc[product_ten.index]
bars2 = product_ten_review.plot(kind = 'bar', color = '#6FB7B7', ax = axes[1])
for x, bar2 in enumerate(bars2.patches):
    height = bar2.get_height()
    axes[1].text(bar2.get_x() + bar2.get_width() / 2, height, height, ha = 'center', va = 'bottom')
axes[1].set_title('前十熱門商品的平均評價')
axes[1].set_xlabel('')
axes[1].set_ylabel('')
axes[1].tick_params(axis = 'x', rotation = 45)
plt.show()


# 15. 年齡層及性別在評價上的影響
gen_age_review = df.groupby(['Age Range', 'Gender'])['Review Rating'].mean().round(1).unstack()
bars = gen_age_review.plot(kind = 'bar', color = ['pink', 'lightblue'], figsize = (12, 6))
plt.title('男女在各年齡層的平均評價')
for bar in bars.containers:
    bars.bar_label(bar, label_type = 'edge')
plt.xlabel('')
plt.ylabel('')
plt.xticks(rotation = 0)
plt.show()


# 16. 有折扣是否會影響購買金額
discount = df.groupby([ 'Gender','Discount Applied'])['Purchase Amount (USD)'].sum().unstack()
discount.plot(kind = 'bar', color = ['#C48888', '#613030'], figsize = (10, 6), stacked = True)
plt.title('男女有折扣時的購買金額')
plt.xlabel('')
plt.ylabel('')
plt.xticks(rotation = 0)
for i in range(len(discount)):
    no_value = discount.iloc[i, 0]
    yes_value = discount.iloc[i, 1]
    total = no_value + yes_value
    plt.text(i, no_value / 2, no_value, ha = 'center', va = 'center', color = 'white')
    plt.text(i, no_value + yes_value / 2, yes_value, ha = 'center', va = 'center', color = 'white')
    plt.text(i, total, total, ha = 'center', va = 'bottom')
plt.show()


# 17. 皮爾遜相關係數熱力圖（數值型資料）
numeric = df.select_dtypes(include = ['number'])
correlation = numeric.corr()
plt.figure(figsize = (14, 8))
sns.heatmap(correlation, annot = True, cmap = 'coolwarm', linewidths = 0.5)
plt.title('皮爾遜熱力圖關聯性')
plt.show()


