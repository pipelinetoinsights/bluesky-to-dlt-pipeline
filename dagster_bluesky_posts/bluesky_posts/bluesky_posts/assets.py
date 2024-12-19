from dagster import AssetExecutionContext
from dagster_embedded_elt.dlt import DagsterDltResource, dlt_assets
from dlt import pipeline
from .bluesky_posts_dagster_pipeline import blusky_source

@dlt_assets(
    dlt_source=blusky_source(),
    dlt_pipeline=pipeline(
        pipeline_name="bluesky_posts_v2",
        dataset_name="bluesky_data",
        destination="filesystem",
        progress="log",
    ),
    name="bluesky",
    group_name="bluesky",
)
def dagster_github_assets(context: AssetExecutionContext, dlt: DagsterDltResource):
    yield from dlt.run(context=context)

