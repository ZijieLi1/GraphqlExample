from graphql import (
    GraphQLObjectType,
    GraphQLSchema,
    GraphQLString,
    GraphQLInt,
    GraphQLNonNull,
    GraphQLField,
    GraphQLArgument,
    GraphQLList
)


Info_type = GraphQLObjectType(
    name='Info',
    fields={
        'case': GraphQLField(GraphQLInt),
        'link': GraphQLField(GraphQLString),
    }
)

# Define a GraphQL object type for Event
Event_type = GraphQLObjectType(
    name='Event',
    fields={
        'source': GraphQLField(GraphQLString),
        'date': GraphQLField(GraphQLInt),
        'detail': GraphQLField(Info_type)
    }
)

# Define a root query type
root_query = GraphQLObjectType(
    name='Query',
    fields={
        'getEvents': GraphQLField(
            GraphQLList(Event_type),
            resolve=lambda _, info: [
                {
                    'source': 'WHO',
                    'date': 25,
                    'detail': {'case':300, 'link':'WHO.com'}
                },
                {
                    'source': 'CDC',
                    'date': 25,
                    'detail': {'case':999, 'link':'CDC.com'}
                },
                {
                    'source': 'WHO',
                    'date': 26,
                    'detail': {'case':300, 'link':'WHO2.com'}
                },
            ]
        ),
    },
)


# Define a GraphQL schema with the root query type
schema = GraphQLSchema(query=root_query)