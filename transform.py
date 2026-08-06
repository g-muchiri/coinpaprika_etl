def transform_coin_data(extracted_output):
    import pandas as pd

    coins_df = pd.json_normalize(extracted_output)

    coins_df.drop(columns=['first_data_at','quotes.USD.percent_change_1h', 'quotes.USD.percent_change_30m', 'quotes.USD.percent_change_6h', 
                       'quotes.USD.percent_change_12h'], inplace= True)

    coins_df.drop(columns=['quotes.USD.percent_change_7d',
                       'quotes.USD.percent_change_1y',
                       'quotes.USD.percent_change_24h',
                       'quotes.USD.percent_change_30d',
                       'quotes.USD.percent_change_15m'], inplace = True)

    coins_df.rename(columns={'quotes.USD.price':'price_USD', 
                         'quotes.USD.volume_24h':'volume_in_24h',
                         'quotes.USD.volume_24h_change_24h':'volume_change_in_24h',
                         'quotes.USD.market_cap':'mkt_cap',
                         'quotes.USD.market_cap_change_24h':'mkt_cap_change',
                         'quotes.USD.ath_price':'ath_price', 
                         'quotes.USD.ath_date':'ath_date',
                         'quotes.USD.percent_from_price_ath':'%_from_price_ath'
                        }, inplace=True
                )

    ## Changing a string to a timestamp

    coins_df['last_updated'] = pd.to_datetime(coins_df['last_updated'])

    coins_df['time_last_updated'] = coins_df['last_updated'].dt.time

    return coins_df

