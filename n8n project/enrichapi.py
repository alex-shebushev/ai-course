# Minimal FastAPI example
from fastapi import FastAPI
from pydantic import BaseModel
import uuid, datetime


app = FastAPI()


class GeminiResult(BaseModel):
    classification: str
    sentiment: str
    confidence_score: float
    entities: dict

@app.post('/enrich')
def enrich(data: GeminiResult):
    dept_map = dept_map = { 'research_abstract': 'Research Office', 'literature_review': 'Library / Research Services', 'thesis_summary':    'Graduate School', 'conference_paper':  'Research Office' }
    return {
        'document_id': str(uuid.uuid4()),
        'department': dept_map.get(data.classification, 'General'),
        'sensitivity':  'restricted' if data.classification == 'thesis_summary' else 'internal',
        'routing_tag': 'needs-review' if data.confidence_score < 0.7 else 'auto-approved',
        'processed_at': datetime.datetime.utcnow().isoformat()
    }
