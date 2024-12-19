from setuptools import find_packages, setup

setup(
    name="bluesky_posts",
    packages=find_packages(exclude=["bluesky_posts_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
