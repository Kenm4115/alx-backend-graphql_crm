import graphene
from crm.schema import Mutation as CrmMutation, CustomerType, ProductType, OrderType

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello, GraphQL!")

class Mutation(CrmMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
