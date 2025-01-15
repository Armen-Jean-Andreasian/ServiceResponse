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

    def test_typehint(self):
        try:
            response: ServiceResponse[bool, str] = ServiceResponse(status=False, error="Error")
            self.assertIsInstance(response, ServiceResponse)
            self.assertIsInstance(response.status, bool)
            self.assertIsInstance(response.error, str)
            self.assertIsNone(response.data)
        except TypeError:
            self.fail("TypeError raised: 'ServiceResponse' is not subscriptable")


if __name__ == '__main__':
    unittest.main()
