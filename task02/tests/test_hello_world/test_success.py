from tests.test_hello_world import HelloWorldLambdaTestCase

class TestHelloWorld(HelloWorldLambdaTestCase):

   
    def test_valid_request(self):
      success = { "statusCode": 200,"headers": {"Content-Type": "application/json"}, "body": {"statusCode": 200, "message": "Hello from Lambda"},"isBase64Encoded": False}
  
      event = { "requestContext": { "http": { "method": "GET", "path": "/hello" } } }
  
      result = self.HANDLER.handle_request(event, None)
      expected_result = success
      self.assertEqual(result, expected_result)
   