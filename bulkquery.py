import json

def bulk_operation(query):
    q = """
        mutation {{
          bulkOperationRunQuery(
        query:\"""{query}\"""  
          ) {{
            bulkOperation {{
              id
              status
            }}
            userErrors {{
              field
              message
            }}
          }}
        }}
        """.format(query=query)
    return q

q_bulk_status="""
query bulkStatus($id: ID!){
  node(id: $id){
    ... on BulkOperation {
      id
      status
      errorCode
      createdAt
      completedAt
      objectCount
      fileSize
      url
      partialDataUrl
    }
  }
}
"""

def bulk_status(client,bulk):
    bulk_id=json.loads(bulk)['data']['bulkOperationRunQuery']['bulkOperation']['id']
    status=json.loads(client.execute(q_bulk_status,{'id':bulk_id}))
    return status