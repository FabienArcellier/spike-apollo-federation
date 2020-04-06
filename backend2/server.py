from ariadne import QueryType, gql, make_executable_schema
from ariadne.asgi import GraphQL
from ariadne.contrib.federation import make_federated_schema

type_defs = gql("""
    type Query {
        hello2: String!
    }
""")

query = QueryType()

@query.field("hello2")
def resolve_hello2(_, info):
    return "Hello2 fabien !"

schema = make_federated_schema(type_defs, query)
app = GraphQL(schema)