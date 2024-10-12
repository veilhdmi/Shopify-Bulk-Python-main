line_items="""
    lineItems{
        edges {
            node {
                id
                quantity
                title
                product {
                    id
                    description
                    handle
                }
                originalUnitPriceSet {
                    shopMoney {
                        amount
                    }
                }
            }
        }
    }
"""