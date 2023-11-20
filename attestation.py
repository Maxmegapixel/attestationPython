import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
print(data)

print(pd.get_dummies(data)) # метод get_dummies

unique_values = data['whoAmI'].unique()    
one_hot_data = pd.DataFrame()
for value in unique_values:
    one_hot_data[value] = (data['whoAmI'] == value).astype(int)     # для уникального значения создается столбец и заполняется
print(one_hot_data)