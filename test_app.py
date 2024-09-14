# import pytest
# from app import app

# @pytest.fixture
# def client():
#     app.config['TESTING'] = True
#     with app.test_client() as client:
#         yield client

# @pytest.fixture
# def example_url():
#     return "https://www.youtube.com/watch?v=s7wmiS2mSXY"


# def test_post_request_with_valid_url(client, example_url):
#     """Test the POST request to the index route with a valid URL."""
#     response = client.post('/', data={'url': example_url})
#     assert response.status_code == 200
#     assert b'Generated Notes' in response.data 
#     assert b'Download Notes as Markdown' in response.data 

# def test_post_request_with_invalid_url(client):
#     """Test the POST request to the index route with an invalid URL."""
#     response = client.post('/', data={'url': ''})
#     assert response.status_code == 200
#     # No assertion for the non-ASCII string as it was removed

# def test_notes(client, example_url):
#     """Test the /api/generate_notes endpoint with valid JSON input."""
#     response = client.post('/api/generate_notes', json={'url': example_url})
#     assert response.status_code == 200
#     data = response.get_json()
#     assert "notes" in data

# def test_generate_notes_failure(client, example_url, monkeypatch):
#     """Test the /api/generate_notes endpoint when notes generation fails."""
#     def mock_generate_notes_from_url(url):
#         return None

#     monkeypatch.setattr('app.generate_notes_from_url', mock_generate_notes_from_url)
    
#     response = client.post('/api/generate_notes', json={'url': example_url})
#     assert response.status_code == 500
#     data = response.get_json()
#     assert data["error"] == "Failed to generate notes"




### Taking Risk
import pytest
from unittest.mock import patch
from app import create_app  # Assuming your Flask app is defined in app.py

# Initialize the Flask test client
@pytest.fixture
def client():
    app = create_app()  # Replace with how you create your app instance
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test case for a valid URL, mocking the transcription process
@patch('app.generate_notes_from_url')
def test_post_request_with_valid_url(mock_generate_notes, client):
    # Mock the function to return a fake transcription
    mock_generate_notes.return_value = "Mocked transcript content"
    
    # Simulate a POST request to your API
    response = client.post('/api/generate_notes', json={'url': 'https://www.youtube.com/watch?v=s7wmiS2mSXY'})
    
    # Check that the API returns a 200 status code
    assert response.status_code == 200
    assert response.json['notes'] == "Mocked transcript content"

# Test case for an invalid URL, mocking the error handling
@patch('app.generate_notes_from_url')
def test_post_request_with_invalid_url(mock_generate_notes, client):
    # Mock the function to raise a ValueError as it would for a bad URL
    mock_generate_notes.side_effect = ValueError("Invalid URL")
    
    response = client.post('/api/generate_notes', json={'url': 'invalid-url'})
    
    # Check that the API returns a 400 status code
    assert response.status_code == 400
    assert 'error' in response.json

# Another test case for successful note generation
@patch('app.generate_notes_from_url')
def test_notes(mock_generate_notes, client):
    mock_generate_notes.return_value = "Mocked transcript content"
    response = client.post('/api/generate_notes', json={'url': 'https://www.youtube.com/watch?v=s7wmiS2mSXY'})
    
    assert response.status_code == 200
    assert response.json['notes'] == "Mocked transcript content"

# Test case for failure in generating notes
@patch('app.generate_notes_from_url')
def test_generate_notes_failure(mock_generate_notes, client):
    mock_generate_notes.side_effect = ValueError("Failed to generate notes")
    
    response = client.post('/api/generate_notes', json={'url': 'https://www.youtube.com/watch?v=s7wmiS2mSXY'})
    
    assert response.status_code == 500
    assert 'error' in response.json


