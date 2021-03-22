import json
from pathlib import Path

THIS_DIR = Path(__file__).parent.resolve()
RESOURCE_DIR = THIS_DIR.joinpath("resources")

creds_path = RESOURCE_DIR.joinpath("connstr.json")
with open(creds_path) as fh:
    odbc_connstr = json.load(fh).get("connstr")