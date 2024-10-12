import shopify
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

token = os.getenv('TOKEN')
merchant = os.getenv('MERCHANT')
version = os.getenv('API_VERSION')

def shopify_client():
    api_session = shopify.Session(merchant, version, token)
    shopify.ShopifyResource.activate_session(api_session)
    client = shopify.GraphQL()
    return client