import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22],
    'Score': [85, 90, 95]
}

df  = pd.DataFrame(data)
# print("DataFrame:\n", df)

# print("Names:", df['Age'])
print(df[df['Score'] >= 90])

