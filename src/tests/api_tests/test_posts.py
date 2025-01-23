import requests
import pytest
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Test for fetching a post
def test_fetch_post(base_url, headers, mocker, mock_response):
    logging.info("Starting test_fetch_post")
    mock_data = {"userId": 1, "id": 1, "title": "sample title", "body": "sample body"}
    mocker.patch('requests.get', return_value=mock_response(json_data=mock_data))

    response = requests.get(f"{base_url}/posts/1", headers=headers)
    assert response.status_code == 200
    assert response.json() == mock_data
    logging.info("Completed test_fetch_post successfully")

# Test for creating a post
def test_create_post(base_url, headers, post_payload, mocker, mock_response):
    logging.info("Starting test_create_post")
    mocker.patch('requests.post', return_value=mock_response(status_code=201, json_data={"id": 101, **post_payload}))

    response = requests.post(f"{base_url}/posts", json=post_payload, headers=headers)
    assert response.status_code == 201
    assert response.json() == {"id": 101, **post_payload}
    logging.info("Completed test_create_post successfully")

# Test for updating a post
def test_update_post(base_url, headers, post_payload, mocker, mock_response):
    logging.info("Starting test_update_post")
    updated_payload = {**post_payload, "title": "updated title"}
    mocker.patch('requests.put', return_value=mock_response(json_data={**updated_payload, "id": 1}))

    response = requests.put(f"{base_url}/posts/1", json=updated_payload, headers=headers)
    assert response.status_code == 200
    assert response.json() == {**updated_payload, "id": 1}
    logging.info("Completed test_update_post successfully")

# Test for deleting a post
def test_delete_post(base_url, headers, mocker, mock_response):
    logging.info("Starting test_delete_post")
    mocker.patch('requests.delete', return_value=mock_response(json_data={"status": "Post deleted"}))

    response = requests.delete(f"{base_url}/posts/1", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"status": "Post deleted"}
    logging.info("Completed test_delete_post successfully")

# Parameterized test for fetching multiple posts
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_fetch_multiple_posts(base_url, headers, post_id, mocker, mock_response):
    logging.info(f"Starting test_fetch_multiple_posts for post_id: {post_id}")
    mocker.patch('requests.get', return_value=mock_response(json_data={"id": post_id}))
    response = requests.get(f"{base_url}/posts/{post_id}", headers=headers)
    assert response.json()["id"] == post_id
    logging.info(f"Completed test_fetch_multiple_posts for post_id: {post_id} successfully")