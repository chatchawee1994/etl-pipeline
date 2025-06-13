import pandas as pd
from datetime import datetime

dfInput = pd.read_csv('sample_products.csv')
dfOutput = pd.read_csv('output/cleaned_products.csv')

with open('output/test_result.txt', 'a') as f:
    f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')

    if dfOutput.dtypes['unit_price'] == 'int64':
        f.write('Test 1: unit_price is of type int64 - Passed\n')
    else:
        f.write('Test 1: unit_price is of type int64 - Failed\n')

    