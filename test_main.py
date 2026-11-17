
import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_welcome():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome Varsha!"
    }


def test_generate_success():
    response = client.post(
        "/generate",
        json={"text": "Hello World"}
    )

    assert response.status_code == 200
    assert response.json() == {
        "tokens": ["Hello", "World"],
        "checksum": sum(
            ord(char) for char in "Hello World"
        )
    }


def test_generate_single_word():
    response = client.post(
        "/generate",
        json={"text": "Python"}
    )

    assert response.status_code == 200
    assert response.json()["tokens"] == ["Python"]
    assert response.json()["checksum"] == 642


def test_generate_multiple_spaces():
    response = client.post(
        "/generate",
        json={"text": "Hello   Python"}
    )

    assert response.status_code == 200
    assert response.json()["tokens"] == [
        "Hello",
        "Python"
    ]
    assert response.json()["checksum"] == sum(
        ord(char) for char in "Hello   Python"
    )


def test_generate_empty_text():
    response = client.post(
        "/generate",
        json={"text": ""}
    )

    assert response.status_code == 200
    assert response.json() == {
        "tokens": [],
        "checksum": 0
    }


def test_generate_missing_text():
    response = client.post(
        "/generate",
        json={}
    )

    assert response.status_code == 422


def test_generate_invalid_text():
    response = client.post(
        "/generate",
        json={"text": 12345}
    )

    assert response.status_code == 422


def test_generate_unicode():
    text = "Hello 世界"

    response = client.post(
        "/generate",
        json={"text": text}
    )

    assert response.status_code == 200
    assert response.json()["tokens"] == [
        "Hello",
        "世界"
    ]
    assert response.json()["checksum"] == sum(
        ord(char) for char in text
    )


@pytest.mark.parametrize(
    "text, expected_tokens",
    [
        ("Hello World", ["Hello", "World"]),
        ("Python FastAPI", ["Python", "FastAPI"]),
        ("One", ["One"]),
        ("", []),
    ]
)
def test_generate_tokenization(text, expected_tokens):
    response = client.post(
        "/generate",
        json={"text": text}
    )

    assert response.status_code == 200
    assert response.json()["tokens"] == expected_tokens
    assert response.json()["checksum"] == sum(
        ord(char) for char in text
    )
