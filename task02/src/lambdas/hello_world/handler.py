from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda
import json


_LOG = get_logger('HelloWorld-handler')


class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
    
    #  print(json.dumps(event))
             
       success = { "statusCode": 200,"headers": {"Content-Type": "application/json"}, "body": {"statusCode": 200, "message": "Hello from Lambda"},"isBase64Encoded": False}
       failure = { "statusCode": 400,"headers": {"Content-Type": "application/json"}, "body": {"statusCode": 400, "message": "Call failed"},"isBase64Encoded": False}


    # Check if the HTTP method is GET and path is "/hello"
       if event['requestContext']['http']['method'] == 'GET' and event['requestContext']['http']['path'] == '/hello':
    # Return the desired JSON response with status code 200
        return success
       else:
         return failure
       
    
    

HANDLER = HelloWorld()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)


