from setuptools import find_packages, setup

setup(
    name="dagster_university",
    packages=find_packages(exclude=["dagster_university_tests"]),
    install_requires=[
        "dagster==1.3.*",
        "dagster-cloud",
        "dagster-dbt",
        "dagster-gcp",
        "beautifulsoup4",
        "dbt-duckdb",
        "geopandas",
        "kaleido",
        "pandas",
        "plotly",
        "psycopg2-binary",
        "requests",
        "shapely"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
