from graphql import graphql_sync
from flask import Flask, request, jsonify
from schema import schema
import json

app = Flask(__name__)

@app.route('/graphql', methods=['POST'])
def graphql_request():
    data = request.get_json()
    query = data['query']
    result = graphql_sync(schema, query)
    return json.dumps(result.data)

if __name__ == '__main__':
    app.run(debug=True)