import json

import pytest  # noqa

from crud.recipes import RecipeCRUD


def test_create_recipe(test_app, monkeypatch):
    test_request_payload = {
        "title": "Test",
        "description": "TestRecipe",
        "instructions": "Test",
        "ingredients": [{"name": "Test", "quantity": "1"}],
    }
    test_response_payload = {
        "id": 1,
        "title": "Test",
        "description": "TestRecipe",
        "instructions": "Test",
        "ingredients": [{"id": 1, "name": "Test", "quantity": "1"}],
        "created_by": None
    }

    async def mock_post(self, payload):
        return test_response_payload
    
    monkeypatch.setattr(RecipeCRUD, "create_recipe", mock_post)

    response = test_app.post(
        "/api/recipes/",
        content=json.dumps(test_request_payload),
    )

    assert response.json() == test_response_payload
    assert response.status_code == 201

def test_get_recipes_not_found(test_app, monkeypatch):
    async def mock_get(self, recipe_id):
        return None
    
    monkeypatch.setattr(RecipeCRUD, "get_recipe", mock_get)

    response = test_app.get(
        "/api/recipes/1",
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Recipe not found"}

def test_get_recipe(test_app, monkeypatch):
    test_response_payload = {
        "id": 1,
        "title": "Test",
        "description": "TestRecipe",
        "instructions": "Test",
        "ingredients": [{"id": 1, "name": "Test", "quantity": "1"}],
        "created_by": None
    }

    async def mock_get(self, recipe_id):
        return test_response_payload
    
    monkeypatch.setattr(RecipeCRUD, "get_recipe", mock_get)

    response = test_app.get(
        "/api/recipes/1",
    )

    assert response.json() == test_response_payload
    assert response.status_code == 200

def test_get_recipes(test_app, monkeypatch):
    test_response_payload = [
        {
            "id": 1,
            "title": "Test",
            "description": "TestRecipe",
            "instructions": "Test",
            "ingredients": [{"id": 1, "name": "Test", "quantity": "1"}],
            "created_by": None
        }
    ]

    async def mock_get(self):
        return test_response_payload
    
    monkeypatch.setattr(RecipeCRUD, "get_recipes", mock_get)

    response = test_app.get(
        "/api/recipes/",
    )

    assert response.json() == test_response_payload
    assert response.status_code == 200

def test_update_recipe(test_app, monkeypatch):
    test_request_payload = {
        "title": "Test",
        "description": "TestRecipe",
        "instructions": "Test",
        "ingredients": [{"name": "Test", "quantity": "1"}],
    }
    test_response_payload = {
        "id": 1,
        "title": "Test",
        "description": "TestRecipe",
        "instructions": "Test",
        "ingredients": [{"id": 1, "name": "Test", "quantity": "1"}],
        "created_by": None
    }

    async def mock_put(self, recipe_id, payload):
        return test_response_payload

    async def mock_get(self, recipe_id):
        return 1
    
    monkeypatch.setattr(RecipeCRUD, "update_recipe", mock_put)
    monkeypatch.setattr(RecipeCRUD, "get_recipe", mock_get)

    response = test_app.put(
        "/api/recipes/1",
        content=json.dumps(test_request_payload),
    )

    assert response.json() == test_response_payload
    assert response.status_code == 200

def test_update_recipe_not_found(test_app, monkeypatch):
    test_request_payload = {
        "title": "Test",
        "description": "TestRecipe",
        "instructions": "Test",
        "ingredients": [{"name": "Test", "quantity": "1"}],
    }

    async def mock_get(self, recipe_id):
        return None
    
    monkeypatch.setattr(RecipeCRUD, "get_recipe", mock_get)

    response = test_app.put(
        "/api/recipes/1",
        content=json.dumps(test_request_payload),
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Recipe not found"}

def test_delete_recipe(test_app, monkeypatch):
    async def mock_get(self, recipe_id):
        return 1

    async def mock_delete(self, recipe_id):
        return None
    
    monkeypatch.setattr(RecipeCRUD, "get_recipe", mock_get)
    monkeypatch.setattr(RecipeCRUD, "delete_recipe", mock_delete)

    response = test_app.delete(
        "/api/recipes/1",
    )

    assert response.status_code == 204

def test_get_recipes_by_title(test_app, monkeypatch):
    test_response_payload = [
        {
            "id": 1,
            "title": "Test",
            "description": "TestRecipe",
            "instructions": "Test",
            "ingredients": [{"id": 1, "name": "Test", "quantity": "1"}],
            "created_by": None
        }
    ]

    async def mock_get(self, title):
        return test_response_payload
    
    monkeypatch.setattr(RecipeCRUD, "get_recipes_by_title", mock_get)

    response = test_app.get(
        "/api/recipes/search/Test",
    )

    assert response.json() == test_response_payload
    assert response.status_code == 200