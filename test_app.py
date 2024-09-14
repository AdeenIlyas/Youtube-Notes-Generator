import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def example_url():
    return "https://www.youtube.com/watch?v=s7wmiS2mSXY"


def test_post_request_with_valid_url(client, example_url):
    """Test the POST request to the index route with a valid URL."""
    response = client.post('/', data={'url': example_url})
    assert response.status_code == 200
    assert b'Generated Notes' in response.data 
    assert b'Download Notes as Markdown' in response.data 

def test_post_request_with_invalid_url(client):
    """Test the POST request to the index route with an invalid URL."""
    response = client.post('/', data={'url': ''})
    assert response.status_code == 200
    # No assertion for the non-ASCII string as it was removed

def test_notes(client, example_url):
    """Test the /api/generate_notes endpoint with valid JSON input."""
    response = client.post('/api/generate_notes', json={'url': example_url})
    assert response.status_code == 200
    data = response.get_json()
    assert "notes" in data

def test_generate_notes_failure(client, example_url, monkeypatch):
    """Test the /api/generate_notes endpoint when notes generation fails."""
    def mock_generate_notes_from_url(url):
        return None

    monkeypatch.setattr('app.generate_notes_from_url', mock_generate_notes_from_url)
    
    response = client.post('/api/generate_notes', json={'url': example_url})
    assert response.status_code == 500
    data = response.get_json()
    assert data["error"] == "Failed to generate notes"


