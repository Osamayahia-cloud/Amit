import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def read_file(path:str):
    try:
        return pd.read_csv(path)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def Drop_unnecessary_features(df,col_to_drop:list[str]):
    return df.drop(col_to_drop,axis=1,inplace=True)

def Check_data_type(df):
    y = []
    for x in df.columns:
        if df[x].nunique()<=3:
            y.append("like categorical")
        else:
            y.append("not like categorical")
    Uni_col = df.nunique()
    dtype = df.dtypes
    infoo = pd.DataFrame({"num_uni": Uni_col,"types":dtype,"stat":y}).T
    return infoo     

def handle_Null(df):
    
    rat = Ratio(df)

    for i in rat.index:
        
        if rat["Ratio"][i] > 50:
            df.drop(i, axis=1, inplace=True)
        elif rat["Ratio"][i]<5:
            df.dropna(subset=[i],inplace=True)
        else:
            df.fillna(df[i].median(),inplace=True)



def Ratio(df):
    null= df.isnull().sum()
    ratio = null / df.shape[0] *100
    return pd.DataFrame({"Null_sum":null,"Ratio":ratio})



def handle_data_type(df):
    for x in df.columns:
            if df[x].nunique()<=3 or df[x].dtype=="str":
                df[x] = df[x].astype("category")



def handle_outliers(df):
    col_name = df.select_dtypes("number").columns
    for col in col_name:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        # print(IQR)
        Lower_Fence = Q1 - 1.5*IQR
        Upper_Fence = Q3 + 1.5*IQR
        
        Lower_Outliers = df[df[col]< Lower_Fence][col].values
        Upper_Outliers = df[df[col] > Upper_Fence][col].values
        df[col].replace(Lower_Outliers, Lower_Fence, inplace= True)
        df[col].replace(Upper_Outliers, Upper_Fence, inplace= True)




def check_outliers(df):
    num_cols = df.select_dtypes('number').columns
    plt.figure(figsize=(8,1))
    for i , col in enumerate(num_cols):
        plt.subplot(1,1,i+1)
        sns.boxplot(df[col], orient="h")
        plt.title(f"{col} Boxplot")