ExamVerseOS Ingestion Engine

Data Pipeline System for ExamVerseOS

---

## Overview

This repository contains the Ingestion Engine for ExamVerseOS.

Its responsibility is to:

- Fetch official examination data (starting with UPSC)
- Clean and normalize raw content
- Extract structured syllabus and topic information
- Build machine-readable knowledge datasets
- Output structured data for the ExamVerseOS database

This is the data production layer of the entire system.

---

## Role in ExamVerseOS

Official Sources → Ingestion Engine (THIS REPO) → Structured Dataset (JSON / DB-ready) → ExamVerseOS Database → API + AI + Search Systems

---

## Purpose

The ingestion engine ensures that:

- AI systems do NOT hallucinate data
- All knowledge is grounded in official sources
- Exam content is structured consistently
- New exams can be added through pipelines

---

## Current Focus

Primary supported exam:

- UPSC Civil Services Examination (CSE)

Modules included:

- Prelims syllabus ingestion
- Mains syllabus ingestion
- Topic extraction
- Basic taxonomy generation

---

## Pipeline Architecture

Fetchers
  ↓
Parsers
  ↓
Cleaners
  ↓
Extractors
  ↓
Builders
  ↓
Outputs (JSON / DB-ready data)

---

## Project Structure

```
app/
 ├── core/            → config & logging
 ├── sources/         → official data sources
 ├── pipelines/       → full ingestion workflows
 ├── parsers/         → raw text cleaning
 ├── extractors/      → structure extraction logic
 ├── builders/        → taxonomy & dataset creation
 ├── utils/           → helpers
 ├── outputs/         → generated datasets
```

---

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run UPSC pipeline

```bash
python app/main.py
```

### 3. Output

After execution, structured data is generated in:

```
app/outputs/upsc_syllabus.json
```

---

## Output Format (v1)

Example structure:

```json
[
  {
    "id": "topic_id",
    "name": "Geography: Climate Systems",
    "parent_exam": "upsc",
    "type": "topic"
  }
]
```

---

## Design Principles

### Official Data First

All outputs must originate from verified sources.

### Structured Before Intelligence

Raw text → structured knowledge → AI usage.

### Modular Pipelines

Each exam should be added as a separate pipeline.

### Re-runnable

Pipelines must be idempotent (safe to re-run).

---

## Current Status

- UPSC fetch pipeline: v1
- Rule-based extraction: active
- JSON output generator: active
- DB integration: pending

---

## Next Upgrades

- PostgreSQL direct writer
- LLM-based syllabus structuring
- PDF ingestion support
- PYQ ingestion pipeline
- Knowledge graph builder

---

## Notes

This system is under active development and currently focused only on UPSC.

---

## Goal

To build a universal ingestion system that converts any exam source into structured, AI-ready knowledge.

---

## Next Step

Connect ingestion → PostgreSQL database

That's the moment your system becomes a full data pipeline → backend → AI ecosystem instead of just a generator.