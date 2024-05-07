

from google.colab import files
uploaded = files.upload()


t = []
with open('/content/groceries.csv') as file:
    temporary = [i.strip() for i in file.readlines()]
    for j in temporary:
        t.append(j.split(','))

import pandas as p
import numpy as n
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

ding = TransactionEncoder()
hot = encoder.fit_transform(t)
dataFrame = p.DataFrame(hot, columns=encoder.columns_)

item = apriori(dataFrame, min_support = 0.02, use_colnames = True)
item.sample(10, random_state=45)

association = association_rules(items, metric='lift', min_threshold=1)
association.sample(10)

association.sort_values('confidence', ascending = False)[0:20]
