from os import environ
import subprocess

import pynecone as pc


ip_address = "localhost"

if environ.get("PORTFOLIO_ENV") == "COMPUTE":
    ip_address = subprocess.Popen(
        [
            'gcloud compute instances list --format json | jq -r ".[].networkInterfaces[0].accessConfigs[0].natIP"'
        ]
    )

config = pc.Config(
    app_name="portfolio",
    api_url=f"http://{ip_address}:8000",
    bun_path="$HOME/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
)
