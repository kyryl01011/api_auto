import httpx
from httpx import Request


def make_curl_from_request(request: Request) -> str:
    result: list[str] = [f"curl -X '{request.method}' '{request.url}'"]

    for header, value in request.headers.items():
        result.append(f"    -H '{header}: {value}'")

    try:
        request.read()
        if body := request.content:
            result.append(f"    -d '{body.decode('utf-8')}'")
    except UnicodeDecodeError:
        pass

    return '\\\n'.join(result)


if __name__ == '__main__':
    body = {
        "email": "user@mesample.com",
        "password": "string",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string"
    }
    response = httpx.request('POST', 'http://127.0.0.1:8000/api/v1/users', json=body)
    print(make_curl_from_request(response.request))
