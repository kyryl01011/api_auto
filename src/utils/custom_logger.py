import logging

from httpx import Request, Response


class CustomLogger:
    def print_request(self, request: Request):
        logging.info(f'[REQUEST] Send {request.method} to {request.url}')
        logging.info(f'[REQUEST] Headers: {request.headers}')
        logging.info(f'[REQUEST] Payload: {request.content}')

    def print_response(self, response: Response):
        logging.info(f'[RESPONSE] Status: {response.status_code} from {response.url}')
        logging.info(f'[RESPONSE] Headers: {response.headers}')
        logging.info(f'[RESPONSE] Payload: {response.content}')
