
import pandas as pd

raw_data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
            'age': [20, 19, 22, 21],
            'favorite_color': ['blue', 'red', 'yellow', "green"],
            'grade': [88, 92, 95, 70]}
df = pd.DataFrame(raw_data)
names = df.to_dict()["name"]
issn = {y:x for x,y in names.items()}

print(issn)