import requests
from .syllabus_urls import UPSC_SYLLABUS_URLS

def fetch_url(exam_part: str):
    url = UPSC_SYLLABUS_URLS.get(exam_part)

    if not url:
        raise ValueError("Invalid exam part")

    response = requests.get(url)
    response.raise_for_status()

    return response.text