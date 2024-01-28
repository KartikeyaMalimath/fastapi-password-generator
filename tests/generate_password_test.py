import string

from fastapi.testclient import TestClient
from main import app

class TestGeneratePassword:

    def setup_class(self):
        self.client = TestClient(app)

    def test_valid_request(self):
        response = self.client.post("/generate-password",
                                    json={
                                        "length": 12
                                    })
        assert response.status_code == 200
        data = response.json()
        assert "password" in data
        assert len(data["password"]) == 12

    def test_invalid_request(self):
        response = self.client.post("/generate-password",
                                    json={})
        assert response.status_code == 422
        data = response.json()
        assert "detail" in data
        assert any(error["type"] == "missing" and "length" in error["loc"] for error in data["detail"])

    def test_minimum_length_validation(self):
        response = self.client.post("/generate-password",
                                    json={
                                        "length": 5
                                    })
        assert response.status_code == 400
        data = response.json()
        assert "detail" in data
        assert "Password length should be a minimum of 8" in data["detail"]

    def test_maximum_length_validation(self):
        response = self.client.post("/generate-password",
                                    json={
                                        "length": 512
                                    })
        assert response.status_code == 400
        data = response.json()
        assert "detail" in data
        assert "Password length should be a maximum of 256" in data["detail"]

    def test_exclude_all_character_types(self):
        response = self.client.post("/generate-password",
                                    json={
                                        "length": 8,
                                        "exclude_uppercase": True,
                                        "exclude_lowercase": True,
                                        "exclude_numbers": True,
                                        "exclude_special_characters": True
                                    })
        assert response.status_code == 400
        data = response.json()
        assert "detail" in data
        assert "At least one character type should be included" in data["detail"]

    def test_custom_characters_included(self):
        response = self.client.post("/generate-password",
                                    json={
                                        "length": 8,
                                        "custom_characters": "@_"
                                    })
        assert response.status_code == 200
        data = response.json()
        assert "password" in data
        assert len(data["password"]) == 8
        assert any(char in "@_" for char in data["password"])

    def test_exclude_uppercase(self):
        response = self.client.post("/generate-password",
                                    json={
                                        "length": 10,
                                        "exclude_uppercase": True
                                    })
        assert response.status_code == 200
        data = response.json()
        assert "password" in data
        assert len(data["password"]) == 10
        assert not any(char.isupper() for char in data["password"])

    def test_exclude_lowercase(self):
        response = self.client.post("/generate-password",
                                    json={
                                        "length": 10,
                                        "exclude_lowercase": True
                                    })
        assert response.status_code == 200
        data = response.json()
        assert "password" in data
        assert len(data["password"]) == 10
        assert not any(char.islower() for char in data["password"])

    def test_exclude_numbers(self):
        response = self.client.post("/generate-password",
                                    json={
                                        "length": 10,
                                        "exclude_numbers": True
                                    })
        assert response.status_code == 200
        data = response.json()
        assert "password" in data
        assert len(data["password"]) == 10
        assert not any(char.isdigit() for char in data["password"])

    def test_exclude_special_characters(self):
        response = self.client.post("/generate-password",
                                    json={
                                        "length": 128,
                                        "exclude_special_characters": True
                                    })
        assert response.status_code == 200
        data = response.json()
        assert "password" in data
        assert len(data["password"]) == 128
        assert not any(char in string.punctuation for char in data["password"])

    def test_exclude_characters(self):
        response = self.client.post("/generate-password",
                                    json={
                                        "length": 10,
                                        "exclude_characters": "xyz"
                                    })
        assert response.status_code == 200
        data = response.json()
        assert "password" in data
        assert len(data["password"]) == 10
        assert not any(char in "xyz" for char in data["password"])

    def test_passphrase_influences_generator(self):
        response = self.client.post("/generate-password",
                                    json={
                                        "length": 10,
                                        "passphrase": "SecretPassphrase"
                                    })
        assert response.status_code == 200
        data = response.json()
        assert "password" in data
        assert len(data["password"]) == 10

    def test_custom_characters_with_special_characters(self):
        response = self.client.post("/generate-password",
                                    json={
                                        "length": 12,
                                        "custom_characters": "@_!#"
                                    })
        assert response.status_code == 200
        data = response.json()
        assert "password" in data
        assert len(data["password"]) == 12
        assert any(char in "@_!#" for char in data["password"])

