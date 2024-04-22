from tests.test_hello_world import HelloWorldLambdaTestCase

class TestHelloWorld(HelloWorldLambdaTestCase):

    def test_invalid_request_method(self):
       
        event = {'httpMethod': 'POST', 'path': '/hello'}
        result = self.HANDLER.handle_request(event, None)
        expected_result = {'statusCode': 400, 'message': 'Invalid request method or path'}
        self.assertEqual(result, expected_result)

    def test_invalid_request_path(self):
      
        event = {'httpMethod': 'GET', 'path': '/test'}
        result = self.HANDLER.handle_request(event, None)
        expected_result = {'statusCode': 400, 'message': 'Invalid request method or path'}
        self.assertEqual(result, expected_result)

