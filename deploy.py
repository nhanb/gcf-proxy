#!/usr/bin/env python3
import sys
from subprocess import run

"""
USAGE: ./deploy.py [region]
    [region] being one of the regions below or "all"
"""

regions = (
    "asia-east2",
    "asia-northeast1",
    "europe-west1",
    "europe-west2",
    "us-central1",
    "us-east1",
    "us-east4",
)


def deploy(region):
    run(
        [
            "gcloud",
            "functions",
            "deploy",
            "nhansproxy",
            "--quiet",
            "--allow-unauthenticated",
            "--runtime=python37",
            "--trigger-http",
            "--env-vars-file=.env.yaml",
            f"--region={region}",
        ]
    )


if len(sys.argv) < 2:
    print("* Must specify region to deploy:\n" + "\n".join(regions))
    exit(1)

region = sys.argv[1]

if region in regions:
    deploy(region)
elif region == "all":
    print("Deploying ALL")
    for r in regions:
        print(">", r)
        deploy(r)
else:
    print("Invalid region")
    exit(1)
