from crm.schema import Query as CRMQuery, Mutation as CRMMutation
import graphene
from crm.schema import Mutation as CrmMutation, CustomerType, ProductType, OrderType


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello, GraphQL!")


class Mutation(CrmMutation, graphene.ObjectType):
    pass


class Query(CRMQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
