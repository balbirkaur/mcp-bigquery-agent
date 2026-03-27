from google import genai
from app.tools_bigquery import get_location_data

client = genai.Client(
    vertexai=True,
    project="empirical-realm-491209-s7",
    location="us-central1"
)

def generate_response(query: str):
    location_data = get_location_data()

    prompt = f"""
    User Query: {query}

    Location Data:
    {location_data}

    Suggest the best location based on:
    - footfall
    - rent
    Give a clear recommendation.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.replace("**", "").replace("\n", " ")