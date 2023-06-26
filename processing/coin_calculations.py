import pandas as pd


# group data into pandas dataframe and calculate standard deviation
def process_dispersion(data: dict):
    prepared_data = prepare_data(data)

    df = pd.DataFrame.from_dict(prepared_data, orient='index')
    print(df.describe())

def prepare_data(data: dict) -> dict:
    prepared_data = {}
    for coin in data:
        coin_price = data[coin]["price"]["price"]
        prepared_data[coin] = coin_price
    return prepared_data

coin_data = {
    '01coin': {'price': {'price': 0.00036246, 'currency': 'usd'}},
    '0chain': {'price': {'price': 0.128576, 'currency': 'usd'}},
    '0x': {'price': {'price': 0.205179, 'currency': 'usd'}},
    '0x0-ai-ai-smart-contract': {'price': {'price': 0.056774, 'currency': 'usd'}},
    '0xauto-io-contract-auto-deployer': {'price': {'price': 0.00012253, 'currency': 'usd'}},
    '0xdao': {'price': {'price': 0.00059552, 'currency': 'usd'}},
    '0xdao-v2': {'price': {'price': 0.00525573, 'currency': 'usd'}},
    '0xmonero': {'price': {'price': 0.130834, 'currency': 'usd'}},
    '0xshield': {'price': {'price': 0.04271735, 'currency': 'usd'}},
    '12ships': {'price': {'price': 4.847e-05, 'currency': 'usd'}},
    '1337': {'price': {'price': 1.083e-05, 'currency': 'usd'}},
    '14066-santa-rosa': {'price': {'price': 62.33, 'currency': 'usd'}},
    '1617-s-avers': {'price': {'price': 54.32, 'currency': 'usd'}},
    '1art': {'price': {'price': 0.00880486, 'currency': 'usd'}}}
process_dispersion(coin_data)
