import marimo

__generated_with = "0.14.17"
app = marimo.App(width="medium")


@app.cell
def _():
    import polars as pl

    # graphql
    from graphql_client import Client
    from graphql_client.custom_fields import (
        EventsMembersFields,
        ResultFields,
    )
    from graphql_client.input_types import EventsOrderByInput
    from graphql_client.custom_queries import Query
    return (
        Client,
        EventsMembersFields,
        EventsOrderByInput,
        Query,
        ResultFields,
        pl,
    )


@app.cell
def _(Client):
    client = Client(url="http://localhost:4000/cubejs-api/graphql")
    return (client,)


@app.cell
async def _(
    EventsMembersFields,
    EventsOrderByInput,
    Query,
    ResultFields,
    client,
    pl,
):
    _query = Query.cube().fields(
        ResultFields.events(order_by=EventsOrderByInput(count="desc")).fields(
            EventsMembersFields.count,
            EventsMembersFields.city,
        )
    )
    data = await client.query(_query, operation_name="my_first_query")
    data = map(lambda row: row["events"], data["cube"])
    pl.from_dicts(data)
    return


if __name__ == "__main__":
    app.run()
