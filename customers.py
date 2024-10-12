from orders import orders

customers="""
query {{
    customers{{
        edges {{
            node {{
                id
                firstName
                lastName
                {orders}
            }}
        }}
    }}
}}
""".format(orders=orders)

print(customers)