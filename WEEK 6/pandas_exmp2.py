import pandas as pd

cars = {
    "Name": ["Toyota", "Honda", "Ford"],
    "Model": ["Corolla", "Civic", "Mustang"],
    "Year": [2020, 2019, 2021],
}

df = pd.DataFrame(cars)
print(df)