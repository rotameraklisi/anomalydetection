#!/usr/bin/env python
# coding: utf-8

# In[94]:


#data preprocessing

#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the dataset
path=r"C:\Users\Asus\Desktop\kddcup.data_10_percent_corrected"
names = ['duration','protocol_type','service','flag','src_bytes',
        'dst_bytes','land','wrong_fragment',
        'urgent','hot','num_failed_logins','logged_in','num_compromised',
        'root_shell','su_attempted','num_root','num_file_creations','num_shells',
        'num_access_files','num_outbound_cmds','is_host_login','is_guest_login',
        'count','srv_count','serror_rate','srv_serror_rate','rerror_rate','srv_rerror_rate'
        ,'some_srv_rate','diff_srv_rate','srv_diff_host_rate','dst_host_count','dst_host_srv_count',
        'dst_host_some_srv_rate','dst_host_diff_srv_rate','dst_host_some_src_port_rate',
         'dst_host_srv_diff_host_rate','dst_host_serror_rate','dst_host_srv_serror_rate',
         'dst_host_rerror_rate','dst_host_srv_rerror_rate','label']
dataset = pd.read_csv(path,names=names)


x_train = dataset.iloc[:,0:41].values
y_train = dataset.iloc[:, 41].values


# In[95]:


print(dataset.shape)


# In[96]:


print(dataset.iloc[:, 41].values)


# In[97]:


print(x_train.shape)


# In[98]:


print(dataset['flag'].value_counts())


# In[99]:


print(dataset['service'].value_counts())


# In[100]:


print(dataset['protocol_type'].value_counts())


# In[101]:


dataset.columns


# In[75]:


from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [1])
x_train = onehotencoder.fit_transform(x_train).toarray()


# In[102]:


print(dataset.tail(10))


# In[108]:


from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
x_train[:,1] = labelencoder.fit_transform(x_train[:,1])
x_train[:,2] = labelencoder.fit_transform(x_train[:,2])
x_train[:,3] = labelencoder.fit_transform(x_train[:,3])


# In[109]:


print(x_train)


# In[110]:


print(dataset.describe())


# In[111]:


print(dataset.keys())


# In[112]:


dtype_dt=dataset.dtypes.reset_index()
print(dtype_dt)
#veri tiplerine bakıldı


# In[113]:


dataset.count()
#eksik veriye bakıldı
#eksik veri yok


# In[115]:


dataset.info()


# In[51]:


print(dataset.isnull().sum())


# In[117]:





# In[123]:


from sklearn.model_selection import train_test_split

train_X, test_X, train_y, test_y = train_test_split(X_scaled, y_train, 
                                                    train_size=0.7,
                                                    test_size=0.3,
                                                    random_state=120)
 


# In[ ]:


#feature scaling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
train_X = sc_x.fit_transform(train_X)
test_X = sc_x.transform(test_X)


# In[ ]:


#data preprocessing

#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the dataset
dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

#taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
imputer = imputer.fit(x[:, 1:])
x[:, 1:] = imputer.transform(x[:, 1:])

#encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x = LabelEncoder()
x[:, 0] = labelencoder_x.fit_transform(x[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
x = onehotencoder.fit_transform(x).toarray()
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

#splitting the dataset into the training set and test set
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)




# In[ ]:




