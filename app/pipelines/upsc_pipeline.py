from app.sources.upsc.fetch import fetch_url
from app.parsers.text_cleaner import clean_text
from app.extractors.syllabus_extractor import extract_topics
from app.builders.taxonomy_builder import build_taxonomy

from app.writers.db_writer import write_topics
from examverse_db.session import SessionLocal


def run_upsc_pipeline():
    print("🚀 Starting UPSC ingestion pipeline...")

    # 1. Fetch
    raw_html = fetch_url("prelims")

    # 2. Clean
    cleaned = clean_text(raw_html)

    # 3. Extract
    raw_topics = extract_topics(cleaned)

    # 4. Build structure
    structured = build_taxonomy(raw_topics)

    # 5. Write to DB
    db = SessionLocal()

    try:
        write_topics(db, structured)
    finally:
        db.close()

    print("✅ UPSC ingestion complete → data stored in PostgreSQL")

    return structured