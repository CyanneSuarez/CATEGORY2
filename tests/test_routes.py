# tests/test_routes.py

import unittest
from app import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_list_by_category(self):
        category = "Electronics"
        response = self.app.get(f'/items?category={category}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Electronics', response.data)

if __name__ == "__main__":
    unittest.main()
