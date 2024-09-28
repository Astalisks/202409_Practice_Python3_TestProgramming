import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestFastAPI(unittest.TestCase):

    def test_read_root(self):
        # GETリクエストのテスト
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello, FastAPI!"})

    def test_create_item(self):
        # POSTリクエストのテスト
        response = client.post("/items/", json={"name": "Item A", "price": 100.0, "is_offer": True})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"name": "Item A", "price": 100.0, "is_offer": True})

        # 不正なデータを送った場合のテスト（validation error）
        response = client.post("/items/", json={"name": "Item A", "price": "invalid"})
        self.assertEqual(response.status_code, 422)

    def test_read_item(self):
        # GETリクエストの境界値テスト
        response = client.get("/items/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"item_id": 1, "name": "Item 1"})

        # 無効なitem_idの場合のエラーテスト
        response = client.get("/items/0")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"detail": "Invalid item_id. It must be greater than 0."})
