from ariadne import QueryType, gql, make_executable_schema
from ariadne.asgi import GraphQL
from ariadne.contrib.federation import make_federated_schema

type_defs = gql("""
    type Query {
        hello: String!
    }
""")

query = QueryType()

@query.field("hello")
def resolve_hello(_, info):
    return "Hello fabien !"

schema = make_federated_schema(type_defs, query)
app = GraphQL(schema)