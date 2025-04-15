import pandas as pd


jsMammies = {
    "Name": ["Annie", "Everline", "Grace"],
    "age": [25, 45, 28],
    "height": [5.4, 5.6, 5.5],
}

girlfriends_table = pd.DataFrame(jsMammies)
print(girlfriends_table)