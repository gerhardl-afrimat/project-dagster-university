from dagster import AutoMaterializePolicy, Definitions, load_assets_from_modules

import os

from .assets import trips, metrics, requests, dbt_assets
from .resources import get_database_resource, dbt_resource
from .jobs import trip_update_job, weekly_update_job, adhoc_request_job
from .schedules import trip_update_schedule, weekly_update_schedule
from .sensors import adhoc_request_sensor

trip_assets = load_assets_from_modules(
    [trips],
    auto_materialize_policy=AutoMaterializePolicy.eager()
)
metric_assets = load_assets_from_modules(
    modules=[metrics],
    group_name="metrics",
    auto_materialize_policy=AutoMaterializePolicy.eager(),
)
requests_assets = load_assets_from_modules(
    modules=[requests],
    group_name="requests",
)


all_jobs = [trip_update_job, weekly_update_job, adhoc_request_job]
all_schedules = [trip_update_schedule, weekly_update_schedule]
all_sensors = [adhoc_request_sensor]

environment = os.getenv("DAGSTER_ENVIRONMENT", "local")
database_resource = get_database_resource(environment)

defs = Definitions(
    assets=[*trip_assets, *metric_assets, *requests_assets, dbt_assets.transformations],
    resources={
        "database": database_resource,
        "dbt": dbt_resource,
    },
    jobs=all_jobs,
    schedules=all_schedules,
    sensors=all_sensors,
)
