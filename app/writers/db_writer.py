from sqlalchemy.orm import Session
from examverse_db.models.topic import Topic

def write_topics(db: Session, topics: list):

    for t in topics:
        exists = db.query(Topic).filter(Topic.id == t["id"]).first()

        if exists:
            continue

        obj = Topic(
            id=t["id"],
            name=t["name"],
            exam_id=t.get("exam_id", "upsc"),
            subject_id=t.get("subject_id"),
            type=t.get("type", "topic")
        )

        db.add(obj)

    db.commit()