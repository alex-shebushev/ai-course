# Minimal FastAPI example
from fastapi import FastAPI
from pydantic import BaseModel
import uuid, datetime


app = FastAPI()


CATEGORIES = [
    'research_abstract',
    'literature_review',
    'thesis_summary',
    'conference_paper',
]


class GeminiResult(BaseModel):
    classification: str
    sentiment: str
    confidence_score: float
    entities: dict


class SensitivityRequest(BaseModel):
    classification: str
    confidence_score: float


@app.get('/health')
def health():
    return {'status': 'ok'}


@app.get('/categories')
def categories():
    return {'categories': CATEGORIES}


@app.post('/sensitivity')
def sensitivity(data: SensitivityRequest):
    confidential = {'thesis_summary'}
    internal = {'research_abstract', 'literature_review', 'conference_paper'}

    if data.classification in confidential:
        level = 'confidential'
    elif data.classification in internal:
        level = 'internal'
    else:
        level = 'public'

    return {
        'classification': data.classification,
        'sensitivity': level,
        'confidence_score': data.confidence_score,
        'evaluated_at': datetime.datetime.utcnow().isoformat(),
    }


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
