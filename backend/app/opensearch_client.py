from opensearchpy import OpenSearch

# Initialize the OpenSearch client
client = OpenSearch(
    hosts=[{'host': 'localhost', 'port': 9200}],
    http_auth=('admin', 'admin'),  # Replace with your OpenSearch credentials
    use_ssl=False,
    verify_certs=False
)

INDEX_NAME = 'epirecipes'

def search_recipes(keyword, filters, page, limit):
    query = {
        "size": limit,
        "from": (page - 1) * limit,
        "query": {
            "bool": {
                "must": [
                    {"multi_match": {"query": keyword, "fields": ["title", "description"]}}
                ],
                "filter": []
            }
        }
    }

    if filters["cuisine"]:
        query["query"]["bool"]["filter"].append({"term": {"cuisine.keyword": filters["cuisine"]}})
    if filters["ingredients"]:
        query["query"]["bool"]["filter"].append({"term": {"ingredients.keyword": filters["ingredients"]}})
    if filters["prep_time"]:
        query["query"]["bool"]["filter"].append({"range": {"prep_time": {"lte": filters["prep_time"]}}})

    response = client.search(index=INDEX_NAME, body=query)
    return response['hits']['hits']
