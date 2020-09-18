#!/usr/bin/env python

import re
import requests

SENSU = [
    "http://prod-sc-sensu-api-01.otsql.open-tabe.com:4567",
    "http://prod-ln-sensu-api-01.otsql.open-tabe.com:4567",
    "http://prod-usw2-sensu-api-01.otsql.open-tabe.com:4567",
    "http://prod-usw1-sensu-api-01.otsql.open-tabe.com:4567",
    "http://pp-sf-sensu-api-01.qasql.open-tabe.com:4567",
]

SHIT_WE_CARE_ABOUT = """
user dmoes {
uid 2015;
class super-user;
}
""".splitlines()

LINES = [line.strip() for line in SHIT_WE_CARE_ABOUT if line.strip()]

def fetch_events(sensu):
    url = f"{sensu}/events"
    return requests.get(url).json()

def extract_diff(event):
    if "ansible_vs_runtime" in event["check"]["name"]:
        output = event["check"]["output"]
        lines = output.splitlines()
        for line in lines:
            if line.strip().startswith("Details"):
                _detail, diffurl = line.split(":", 1)
                return diffurl.strip()

def ignore_line(line):
    return line.startswith("#") or re.match(r'^\[.+\]$', line) or line == "system { ... }"

def remove_irrelevant(diff):
    lines = diff.splitlines()
    simplified = []
    for line in lines:
        stripped = re.sub(r'^[-+\s]*', '', line.strip())
        if not ignore_line(stripped):
            simplified.append(stripped)
    return simplified

def main():
    for sensu in SENSU:
        events = fetch_events(sensu)
        for event in events:
            diffurl = extract_diff(event)
            if not diffurl:
                continue
            result = requests.get(diffurl)
            simplified = remove_irrelevant(result.text)
            # print(simplified)
            if simplified == LINES:
                # print("\n".join(simplified))
                print(event["client"]["name"])

if __name__ == "__main__":
    main()
