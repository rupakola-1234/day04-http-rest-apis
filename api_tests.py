
import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_api(method, endpoint, body=None):
    url = BASE_URL + endpoint
    data = None

    headers = {"Accept": "application/json"}

    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"

    request = Request(
        url,
        data=data,
        headers=headers,
        method=method
    )

    print("\n" + "=" * 50)
    print(f"REQUEST: {method} {url}")

    try:
        with urlopen(request, timeout=20) as response:
            print("Status code:", response.status)
            print("Response headers:")

            for key, value in response.headers.items():
                if key.lower() in (
                    "content-type",
                    "cache-control",
                    "date",
                    "server"
                ):
                    print(f"  {key}: {value}")

            content = response.read().decode("utf-8")
            print("Response body:")

            if content:
                try:
                    print(json.dumps(
                        json.loads(content),
                        indent=2
                    ))
                except json.JSONDecodeError:
                    print(content)
            else:
                print("(Empty response body)")

    except HTTPError as error:
        print("Status code:", error.code)
        print("Error response:", error.read().decode("utf-8"))

    except URLError as error:
        print("Connection error:", error.reason)


# 1. GET collection
test_api("GET", "/posts")

# 2. GET individual post (path parameter)
test_api("GET", "/posts/1")

# 3. GET with query parameter
test_api("GET", "/posts?_limit=5")

# 4. POST a new post using JSON
test_api("POST", "/posts", {
    "title": "Day 4 API Project",
    "body": "Learning REST APIs using Python",
    "userId": 1
})

# 5. PUT: replacement-style update
test_api("PUT", "/posts/1", {
    "id": 1,
    "title": "Updated title",
    "body": "Updated post content",
    "userId": 1
})

# 6. PATCH: partial update
test_api("PATCH", "/posts/1", {
    "title": "Partially updated title"
})

# 7. DELETE a post
test_api("DELETE", "/posts/1")
