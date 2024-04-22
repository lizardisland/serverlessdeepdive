from tests.test_hello_world import HelloWorldLambdaTestCase

class TestHelloWorld(HelloWorldLambdaTestCase):

    def test_valid_request(self):
        event = {'httpMethod': 'GET', 'path': '/hello'}
        result = self.HANDLER.handle_request(event, None)
        expected_result = {'statusCode': 200, 'message': 'Hello from Lambda'}
        self.assertEqual(result, expected_result)
