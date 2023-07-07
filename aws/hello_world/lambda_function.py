from __future__ import print_function

import json
import pandas as pd


def lambda_handler(event, context):
    my_data = {'first_name': ['David', 'John', 'Jane'], 'last_name': ['Smith', 'Doe', 'Doe']}

    df = pd.DataFrame(my_data, columns=['first_name', 'last_name'])

    print(f'--> {df.head()}')

if __name__ == "__main__":
    event = []
    context = []
    lambda_handler(event, context)