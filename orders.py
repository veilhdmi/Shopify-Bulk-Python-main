from lineitems import line_items
from journey import customer_journey
from address import billing_address

orders="""
    orders{{
        edges {{
            node {{
                id
                createdAt
                currentSubtotalLineItemsQuantity
                {customerJourney}
                {lineItems} 
                {billingAddress}
            }}
        }}
    }}
""".format(lineItems=line_items, customerJourney=customer_journey, billingAddress=billing_address)
print(orders)