from google.cloud import bigquery

def get_location_data():
    client = bigquery.Client()

    query = """
    SELECT area, footfall, rent
    FROM `empirical-realm-491209-s7.mcp_dataset.location_data`
    ORDER BY footfall DESC
    LIMIT 3
    """

    query_job = client.query(query)
    results = query_job.result()

    data = []
    for row in results:
        data.append({
            "area": row.area,
            "footfall": row.footfall,
            "rent": row.rent
        })

    return data