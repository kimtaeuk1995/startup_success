import os

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import DateTime, Integer, String, Text
from sqlalchemy_utils import create_database, database_exists

engine = create_engine("postgres+psycopg2://moong@localhost:5432/crunchbase")
if not database_exists(engine.url):
    create_database(engine.url)

acquisitions_df = pd.read_csv("acquisitions.csv")
table_name = "acquisitions"
acquisitions_df.to_sql(
    table_name,
    engine,
    if_exists="replace",
    index=False,
    chunksize=500,
    dtype={
        "company_permalink": Text,
        "company_name": Text,
        "company_category_list": Text,
        "company_country_code": Text,
        "company_state_code": Text,
        "company_region": Text,
        "company_city": Text,
        "acquirer_permalink": Text,
        "acquirer_name": Text,
        "acquirer_category_list": Text,
        "acquirer_country_code": Text,
        "acquirer_state_code": Text,
        "acquirer_region": Text,
        "acquirer_city": Text,
        "acquired_at": Text,
        "acquired_month": Text,
        "price_amount": Text,
        "price_currency_code": Text,
    },
)
acquisitions = pd.read_sql_table(table_name, con=engine)

companies_df = pd.read_csv("companies.csv")
table_name2 = "companies"
companies_df.to_sql(
    table_name2,
    engine,
    if_exists="replace",
    index=False,
    chunksize=500,
    dtype={
        "permalink": Text,
        "name": Text,
        "homepage_url": Text,
        "category_list": Text,
        "funding_total_usd": Text,
        "status": Text,
        "country_code": Text,
        "state_code": Text,
        "region": Text,
        "city": Text,
        "funding_rounds": Text,
        "founded_at": Text,
        "first_funding_at": Text,
        "last_funding_at": Text,
    },
)
companies = pd.read_sql_table(table_name2, con=engine)

investments_df = pd.read_csv("investments.csv")
table_name3 = "investments"
investments_df.to_sql(
    table_name3,
    engine,
    if_exists="replace",
    index=False,
    chunksize=500,
    dtype={
        "company_permalink": Text,
        "company_name": Text,
        "company_category_list": Text,
        "company_country_code": Text,
        "company_state_code": Text,
        "company_region": Text,
        "company_city": Text,
        "investor_permalink": Text,
        "investor_name": Text,
        "investor_country_code": Text,
        "investor_state_code": Text,
        "investor_region": Text,
        "investor_city": Text,
        "funding_round_permalink": Text,
        "funding_round_type": Text,
        "funding_round_code": Text,
        "funded_at": Text,
        "raised_amount_usd": Text,
    },
)
investments = pd.read_sql_table(table_name3, con=engine)
investments.head()

rounds_df = pd.read_csv("rounds.csv")
table_name4 = "rounds"
rounds_df.to_sql(
    table_name4,
    engine,
    if_exists="replace",
    index=False,
    chunksize=500,
    dtype={
        "company_permalink": Text,
        "company_name": Text,
        "company_category_list": Text,
        "company_country_code": Text,
        "company_state_code": Text,
        "company_region": Text,
        "company_city": Text,
        "funding_round_permalink": Text,
        "funding_round_type": Text,
        "funding_round_code": Text,
        "funded_at": Text,
        "raised_amount_usd": Text,
    },
)
rounds = pd.read_sql_table(table_name4, con=engine)
rounds.head()
