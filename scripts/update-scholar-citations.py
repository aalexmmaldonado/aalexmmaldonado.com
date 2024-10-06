#!/usr/bin/env python3

import glob
import os

from dotenv import load_dotenv
from serpapi import GoogleSearch

os.chdir(os.path.dirname(os.path.abspath(__file__)))

load_dotenv("../.env")
SERPAPI_API_KEY = os.environ["SERPAPI_API_KEY"]


def get_citation_data(author_id, citation_id):
    search = GoogleSearch(
        {
            "api_key": SERPAPI_API_KEY,
            "engine": "google_scholar_author",
            "hl": "en",
            "author_id": author_id,
            "citation_id": citation_id,
            "view_op": "view_citation",
        }
    )
    return search.get_dict()


for pub_file in glob.glob("../content/outputs/pub*.md"):
    pub_info: dict[str, str] = {}
    with open(pub_file, "r", encoding="utf-8") as f:
        pub_lines = f.readlines()
    for i, line in enumerate(pub_lines):
        if "gscholar_author_id" in line:
            pub_info["author_id"] = line.split(":")[-1].strip().replace('"', "")
        if "gscholar_citation_id" in line:
            pub_info["citation_id"] = (
                ":".join(line.split(":")[1:]).strip().replace('"', "")
            )
        if "---" in line and i > 1:
            break
    citation_info = get_citation_data(**pub_info)
    if "total_citations" in citation_info["citation"].keys():
        total_citations = citation_info["citation"]["total_citations"]["cited_by"]["total"]
    else:
        total_citations = 0
    for i, line in enumerate(pub_lines):
        if "gscholar_citation_num" in line:
            pub_lines[i] = f'gscholar_citation_num: "{total_citations}"\n'
            break
        if "---" in line and i > 1:
            break
    with open(pub_file, "w", encoding="utf-8") as f:
        f.writelines(pub_lines)
