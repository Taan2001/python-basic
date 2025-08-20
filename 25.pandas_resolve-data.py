"""
    Pandas - read and write data
"""
import pandas as pd

# # load data from csv file
# data = pd.read_csv("data.csv")

# print(f"data: {data}")
# print(f"type: {type(data)}")
# print(data.head()) # By default, the first 5 lines will be printed.
# print(data.head(7)) # the first 7 lines will be printed.
# print(data.tail()) # By default, the last 5 lines will be printed.

# # save csv file
# data.to_csv("data_new.csv", index=False)

# # inspect data
# print(data.info())

# # statistical
# print(data.describe())
# print(data.columns)
# print(data.index)

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
})

# # iloc - follow index of row and column (start from 0)
# # loc - follow labels of row and column - row and column name

# print(df)
# print(df.columns)
# print(df.index)

# # loc
# # get first row
# print(df.loc[0])

# # get rows
# print(df.loc[[0, 2]]) 

# # get rows with columns
# print(df.loc[:, ["Name", "City"]])
# print(df.loc[:0, ["Name", "City"]])

# # iloc
# print(df.iloc[0]) 
# print(df.iloc[[0, 2]]) 
# print(df.iloc[:, [0, 2]])

# new_df = df.set_index("Name")
# print(new_df)
# print(new_df.loc[["Alice"]])

"""
    Selecting and Filtering data
"""
# print(df["Name"])
# print(df[["Name", "City"]])

# filtered = df[df["Age"] >= 30]
# print(filtered)
# print(type(filtered))

# # add column in data frame
# df["new_column"] = ["A", "B", "XYZ"]
# print(df)

# # delete column => axis=1
# new_df = df.drop("City", axis=1)
# print(new_df)

# # delete row => axis=0
# new_df = df.drop(:0, axis=0)
# print(new_df)

# # change cell in data frame
# print(f"before change cell: \n{df}")
# df.loc[0, "Name"] = "Minh Anh"
# print(f"after change cell: \n{df}")

""" 
    Handle NaN
"""
df["Salary"] = [50000, None, 40000]
# print(df)
# print(df.info())

# # replace value
# df["Salary"] = df["Salary"].fillna(0) # assign 0 for NaN value
# print(df)

# remove it
new_df = df.dropna()
print(new_df)