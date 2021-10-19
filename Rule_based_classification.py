#region Rule Based Classification
#region Import Data & Library
import pandas as pd
dff=pd.read_csv(r"C:\Users\king\Desktop\DSMLBC1\datasets\hafta_2\persona.csv")
dff.columns=[col.lower() for col in df.columns]
df=dff.copy()
df
#endregion
#region Function for Rule Based Classification
def classification(df):
    df = df.groupby(["country", "source", "sex", "age"]).agg({"price": "sum"})
    df.sort_values(by="price", ascending=False, inplace=True)
    df.reset_index(inplace=True)
    bins = [0, 18, 23, 30, 40, df["age"].max()]
    my_labels = ["0_18", "19_23", "24_30", "31_40", "41_" + str(df["age"].max())]
    df["age_cat"] = pd.cut(df["age"], bins, labels=my_labels)
    df["customers_level_based"] = [row[0] + "_" + row[1] + "_" + row[2] + "_" + row[5] + "_" for row in df.values]
    df = df.groupby("customers_level_based").agg({"price": "mean"})
    df.reset_index(inplace=True)
    df["segment"] = pd.qcut(df["price"], 4, labels=["D", "C", "B", "A"])
    return df
classification(df)
#endregion
#endregion