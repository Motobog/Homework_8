from ui import list_p_ui
import pandas as pd

def list_all(db_in,db_in_1):
    return pd.merge(db_in,db_in_1, how='left').iloc[:,[1,7]]

def list_unw(db_in,db_in_1):
    db_r=pd.merge(db_in,db_in_1, how='left')
    return  db_r[db_r['дата увольнения'].notna()].iloc[:,[1,7]]

def list_w(db_in,db_in_1):
    db_r=pd.merge(db_in,db_in_1, how='left')
    return  db_r[db_r['дата увольнения'].isnull()].iloc[:,[1,7]]

def list_p(db_in, db_in_1):
    num = list_p_ui(db_in)
    db_res = pd.merge(db_in,db_in_1, how='left')
    return db_res.iloc[num,[1,2,4,5,6,7]],db_res.iloc[num,1]

def list_z(db_in, db_in_1):
    num = list_p_ui(db_in)
    db_r=pd.merge(db_in,db_in_1, how='left')
    search_res=db_in.iloc[num,1]
    return search_res,db_r.loc[db_r.ФИО==search_res].iloc[:,[8,7]].to_string(index=False)
   