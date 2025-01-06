import unittest
from service_response import ServiceResponse


class TestServiceResponse(unittest.TestCase):
    def test_status(self):
        response = ServiceResponse(status=True, data={"key": "value"})
        self.assertTrue(response)
        self.assertEqual(response.data, {"key": "value"})

    def test_to_dict(self):
        response = ServiceResponse(status=False, reason="Error")
        self.assertEqual(response.to_dict(), {
            "status": False, "data": None, "error": None, "reason": "Error", "message": None
        })
