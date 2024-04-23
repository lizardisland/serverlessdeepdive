from tests.test_hello_world import HelloWorldLambdaTestCase

class TestHelloWorld(HelloWorldLambdaTestCase):

  
    def test_invalid_request_method(self):
       
        failure = { "statusCode": 400,"headers": {"Content-Type": "application/json"}, "body": {"statusCode": 400, "message": "Call failed"},"isBase64Encoded": False}

        event = { "requestContext": { "http": { "method": "GET", "path": "/helloo" } } }
        result = self.HANDLER.handle_request(event, None)
        expected_result = failure
        self.assertEqual(result, expected_result)

    def test_invalid_request_path(self):
      
        failure = { "statusCode": 400,"headers": {"Content-Type": "application/json"}, "body": {"statusCode": 400, "message": "Call failed"},"isBase64Encoded": False}

        event = { "requestContext": { "http": { "method": "POST", "path": "/hello" } } }
        result = self.HANDLER.handle_request(event, None)
        expected_result = failure
        self.assertEqual(result, expected_result)


    