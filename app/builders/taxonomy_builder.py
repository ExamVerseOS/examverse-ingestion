import hashlib

def build_taxonomy(raw_topics):
    structured = []

    for t in raw_topics:
        topic_id = hashlib.md5(t["raw"].encode()).hexdigest()

        structured.append({
            "id": topic_id,
            "name": t["raw"].title(),
            "exam_id": "upsc",
            "subject_id": None,
            "type": "topic"
        })

    return structured