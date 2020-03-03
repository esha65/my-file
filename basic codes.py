pd.options.display.float_format="{:.2f}".format
pd.set_option("display.max_columns",500)
sns.set(rc={"figure.figsize":(12,8)})

## pip install xgboost

##outlier=[]
def detect_outlier(data):
    mean=np.mean(data)
    std=np.mean(data)
    for i in data:
        z=(i-mean)/std
        if z>3:
            outlier.append(i)
    return outlier

