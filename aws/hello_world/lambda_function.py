from __future__ import print_function

import json
from dataclasses import dataclass
from typing import List

import pandas as pd
@dataclass
class awsEvent:
    Records: List[object]

def lambda_handler(event, context):
    record = event['Records'][0]
    payload = record['body']
    parsed_payload = json.loads(payload)
    user = parsed_payload["user"]
    print(f'--> user is {user}')

    my_data = {'first_name': ['David', 'John', 'Jane'], 'last_name': ['Smith', 'Doe', 'Doe']}

    df = pd.DataFrame(my_data, columns=['first_name', 'last_name'])

    print(f'--> {df.head()}')

if __name__ == "__main__":
    event: object = {'Records':[{'body': '{"user": "david"}'}]}
    context: object = {}
    lambda_handler(event, context)