import pandas as pd
import numpy as np
import pickle

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.impute import KNNImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score
from sklearn.ensemble import VotingClassifier

kd= pd.read_csv("kidney_disease.csv")

kd.drop('id',axis=1,inplace=True)

kd[['rbc','pc']] = kd[['rbc','pc']].replace(to_replace={'abnormal':1,'normal':0})
kd[['pcc','ba']] = kd[['pcc','ba']].replace(to_replace={'present':1,'notpresent':0})
kd[['htn','dm','cad','pe','ane']]= kd[['htn','dm','cad','pe','ane']].replace(to_replace={'yes':1,'no':0})
kd[['appet']]= kd[['appet']].replace(to_replace={'good':0,'poor':1})

kd[['classification']]= kd[['classification']].replace(to_replace={'ckd':1,'ckd\t':1,'notckd':0})
kd[['cad','dm']]= kd[['cad','dm']].replace(to_replace={'\tyes':1,' yes':1,'\tno':0})
kd[['pcv','wc','rc']]= kd[['pcv','wc','rc']].replace(to_replace={'\t?':np.nan})
kd[['pcv','wc']]= kd[['pcv','wc']].replace(to_replace={'\t43':'43','\t6200':'6200','\t8400':'8400'})

kd['age'].fillna(method='bfill',inplace=True)
kd['bp'].fillna(method='bfill',inplace=True)
kd['sg'].fillna(method='bfill',inplace=True)
kd['al'].fillna(method='bfill',inplace=True)
kd['su'].fillna(method='bfill',inplace=True)
kd['bgr'].fillna(method='bfill',inplace=True)
kd['bu'].fillna(method='bfill',inplace=True)
kd['sc'].fillna(method='bfill',inplace=True)
kd['sod'].fillna(method='bfill',inplace=True)
kd['pot'].fillna(method='bfill',inplace=True)
kd['hemo'].fillna(method='bfill',inplace=True)
kd['pcv'].fillna(method='bfill',inplace=True)
kd['wc'].fillna(method='bfill',inplace=True)
kd['rc'].fillna(method='bfill',inplace=True)

k_imp = KNNImputer(n_neighbors = 7)
kd1=pd.DataFrame(k_imp.fit_transform(kd))
kd1.columns=kd.columns

x= kd1.drop('classification',axis=1)
y= kd1['classification']

sc = StandardScaler()
x = sc.fit_transform(x)

x_tr,x_tt,y_tr,y_tt= train_test_split(x,y,train_size=0.84,random_state=255)

logr= LogisticRegression(penalty='elasticnet',random_state=620,solver='saga',class_weight={0.0:0.85,1.0:0.15},l1_ratio=0.7)
logr.fit(x_tr,y_tr)

rof= RandomForestClassifier(n_estimators=125,criterion='entropy',random_state=552,class_weight={0.0:0.87,1.0:0.1},max_samples=75,ccp_alpha=0.12)
rof.fit(x_tr,y_tr)

model_list= [('log_reg',logr),('rf',rof)]

ensemble_mdl= VotingClassifier(model_list,voting="soft")

model = ensemble_mdl.fit(x_tr,y_tr)

pickle.dump(model,open('ckd.pkl','wb'))
