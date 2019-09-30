import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from models import *


class WordList(SQLAlchemyObjectType):

    class Meta:
        model = WordModel
        interfaces = (graphene.relay.Node, )


class Query(graphene.ObjectType):

    node = graphene.relay.Node.Field()
    word = graphene.Field(WordList, uuid=graphene.Int())

    def resolve_word(self, args, context, info):
        query = WordList.get_query(info.context)
        uuid = args.get('uuid')
        return query.get(uuid)


schema = graphene.Schema(query=Query, types=[WordList])
