import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from flask import current_app as app
from app.database_logic.models import db, Cereal # <-- current app?

class Cereal(SQLAlchemyObjectType):
    class Meta:
        model = Cereal
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_cereals = SQLAlchemyConnectionField(Cereal.connection)

schema = graphene.Schema(query=Query)