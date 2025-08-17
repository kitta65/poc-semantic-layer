import asyncio
from graphql_client import Client
from graphql_client.custom_fields import (
    EventsMembersFields,
    ResultFields,
)
from graphql_client.custom_queries import Query

CLIENT = Client(url="http://localhost:4000/cubejs-api/graphql")

async def main():
    query = Query.cube().fields(
        ResultFields.events().fields(
            EventsMembersFields.count
        )
    )
    response = await CLIENT.query(query, operation_name="my_first_query")
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
