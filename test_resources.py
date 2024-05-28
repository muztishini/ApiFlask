from app import app
from flask import json

correct_json = {
    "id": 1,
    "title": "string",
    "description": "string",
    "created_at": "2024-05-23 12:40:22",
    "updated_at": "2024-05-28 12:01:03"
}


def test_get_tasks():
    response = app.test_client().get('/tasks', content_type='application/json')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200


def test_get_task():
    response = app.test_client().get('/tasks/1', content_type='application/json')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data == correct_json


def test_create_task():
    response = app.test_client().post('/tasks', data=json.dumps({'title': "string", 'description': "string"}),
                                      content_type='application/json')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200


def test_update_task():
    response = app.test_client().put('/tasks/1', data=json.dumps({'title': "string", 'description': "string"}),
                                     content_type='application/json')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200


def test_delete_task():
    response = app.test_client().delete('/tasks/24')
    assert response.status_code == 200
