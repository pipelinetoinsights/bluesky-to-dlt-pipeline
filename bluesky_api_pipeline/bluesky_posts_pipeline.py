from datetime import datetime, timedelta
import dlt
from dlt.sources.rest_api import RESTAPIConfig, rest_api_resources

# Function to calculate yesterday's date range
def get_yesterday_date_range():
    """
    Calculates the ISO 8601 date range (since, until) for yesterday.
    Returns:
        tuple: since (start of yesterday), until (end of yesterday)
    """
    yesterday = datetime.utcnow() - timedelta(days=1)
    since = yesterday.replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + "Z"
    until = yesterday.replace(hour=23, minute=59, second=59, microsecond=999999).isoformat() + "Z"
    return since, until

# Define the Bluesky posts resource
@dlt.source
def blusky_source():
    # Get the date range for yesterday
    since, until = get_yesterday_date_range()

    # Define RESTAPIConfig for Bluesky API
    config: RESTAPIConfig = {
        "client": {
            "base_url": "https://public.api.bsky.app/xrpc/",
        },
        "resources": [
            {
                "name": "posts",
                "endpoint": {
                    "path": "app.bsky.feed.searchPosts",
                    "params": {
                        "q": "data engineer",  # Search term
                        "sort": "latest",
                        "since": since,
                        "until": until,
                        "tag": ["dataBS", "datasky"],
                        "limit": 50,
                    },
                },
            },
        ],
    }

    # Generate resources using RESTAPIConfig
    yield from rest_api_resources(config)

# Create and configure the pipeline
pipeline = dlt.pipeline(
        pipeline_name="bluesky_api2",
        destination="filesystem",
        dataset_name="bluesky_data",
    )

# Run the pipeline
load_info = pipeline.run(blusky_source())
print(load_info)