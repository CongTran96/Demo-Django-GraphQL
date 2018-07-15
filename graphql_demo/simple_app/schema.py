# file simple_app/schema.py
# import some modules of graphql library
import graphene
from graphene import Node
from graphene_django.types import DjangoObjectType
from graphene_django.filter.fields import DjangoFilterConnectionField
from . import models

# get the models from django and convert to graphql models
# filter_fields: specify the fields which can be filtered
# interfaces: use with filter_fields, don't care about that, 
class MessageType(DjangoObjectType):
    class Meta:
        model = models.Message
        filter_fields = {
            'message': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (Node, )

# Query format
# all_message is the filed will get from query
# resolve return the list we will query
class Query(graphene.ObjectType):
    message = Node.Field(MessageType)
    all_messages = DjangoFilterConnectionField(MessageType)