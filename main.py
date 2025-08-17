from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from schema import schema

def main():
    op = Operation(schema.query_type)
    schema.query_type
    cube = op.cube
    cube.events()
    endpoint = HTTPEndpoint("http://localhost:4000/cubejs-api/graphql")
    data = endpoint(op)

    print(data)



if __name__ == "__main__":
    main()
