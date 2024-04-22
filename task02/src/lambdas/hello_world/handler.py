from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('HelloWorld-handler')


class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
    # Check if the HTTP method is GET and path is "/hello"
     if event['httpMethod'] == 'GET' and event['path'] == '/hello':
    # Return the desired JSON response with status code 200
        return {
      "statusCode": 200,
      "message": "Hello from Lambda"
    }
     else:
         return {
      "statusCode": 400,
      "message": "Invalid request method or path"
    }
    
    

HANDLER = HelloWorld()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)


