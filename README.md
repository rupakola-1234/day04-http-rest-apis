
# Day 4 - HTTP, REST and APIs

## 1. Objective

The objective of this project is to understand HTTP, REST APIs,
request and response formats, status codes, and CRUD operations
by interacting with a publicly available REST API.

## 2. API Used

API Name: JSONPlaceholder

Website: https://jsonplaceholder.typicode.com/

Endpoint used: https://jsonplaceholder.typicode.com/posts

JSONPlaceholder is a free fake REST API used for learning and
testing. It returns sample JSON data and simulates write operations.

Tool used: Python with built-in urllib and json libraries.

## 3. Requests Performed

### Request 1: GET collection

Method: GET

URL: https://jsonplaceholder.typicode.com/posts

Purpose: Retrieve a collection of posts.

Expected status: 200 OK

### Request 2: GET individual resource

Method: GET

URL: https://jsonplaceholder.typicode.com/posts/1

Purpose: Retrieve the post whose ID is 1.

Expected status: 200 OK

The number 1 is a path parameter.

### Request 3: GET with a query parameter

Method: GET

URL: https://jsonplaceholder.typicode.com/posts?_limit=5

Purpose: Retrieve only five posts.

Expected status: 200 OK

The query parameter is _limit=5.

### Request 4: POST with a JSON request body

Method: POST

URL: https://jsonplaceholder.typicode.com/posts

Request body:

{
  "title": "Day 4 API Project",
  "body": "Learning REST APIs using Python",
  "userId": 1
}

Expected status: 201 Created

Purpose: Simulate creating a new post.

### Request 5: PUT

Method: PUT

URL: https://jsonplaceholder.typicode.com/posts/1

Purpose: Send a replacement-style update for post 1.

Expected status: 200 OK

### Request 6: PATCH

Method: PATCH

URL: https://jsonplaceholder.typicode.com/posts/1

Request body:

{
  "title": "Partially updated title"
}

Expected status: 200 OK

Purpose: Simulate updating only one field.

### Request 7: DELETE

Method: DELETE

URL: https://jsonplaceholder.typicode.com/posts/1

Purpose: Simulate deleting post 1.

Expected status: 200 OK

Note: JSONPlaceholder simulates these write operations. Changes
are not permanently saved to its underlying dataset.

## 4. Sample Request and Response

Sample request:

GET https://jsonplaceholder.typicode.com/posts/1

Sample response:

{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati",
  "body": "quia et suscipit suscipit recusandae consequuntur expedita"
}

The actual response contains the complete title and body returned
by the API.

Status code: 200 OK

Content-Type: application/json; charset=utf-8

JSON stands for JavaScript Object Notation. It represents data
using objects, arrays, keys, and values.

## 5. Five Observations About APIs

1. APIs allow different applications to communicate with each other
   using defined endpoints and HTTP methods.

2. GET requests retrieve information. A collection endpoint can
   return multiple resources, while an endpoint containing an ID
   can return one resource.

3. Query parameters can limit or filter results. For example,
   ?_limit=5 requests five posts.

4. HTTP status codes communicate the outcome of a request.
   For example, 200 means success and 404 means the resource
   was not found.

5. Requests and responses can contain headers and bodies.
   Headers provide metadata, while JSON bodies can carry the
   data being sent or received.

Additional observation: POST, PUT, PATCH, and DELETE can be
tested with a public testing API without building a backend.

## 6. Explanation of HTTP Methods

### GET

GET retrieves information from a server.
It should not change the resource.

Example: GET /posts/1

### POST

POST submits data to a server, commonly to create a resource.

Example: POST /posts

### PUT

PUT replaces a resource representation or creates a resource
at a known URI when the API supports that behavior.
It is intended to be idempotent.

Example: PUT /posts/1

### PATCH

PATCH applies partial changes to a resource.
Its idempotency depends on the particular patch operation.

Example: PATCH /posts/1

### DELETE

DELETE requests removal of a resource.
It is intended to be idempotent, meaning repeating the same
request should have the same intended final effect.

Example: DELETE /posts/1

## 7. PUT vs PATCH

PUT generally sends a complete replacement representation.
PATCH sends only the changes that need to be applied.

## 8. Request and Response Details

- Path parameter: /posts/1 identifies a particular post.
- Query parameter: ?_limit=5 controls the result set.
- Request headers: Accept and Content-Type describe accepted
  or submitted data formats.
- Request body: Contains data sent to the server, such as JSON.
- Response body: Contains the returned data or an error message.
- Response headers: Provide metadata such as content type.
- Status code: Indicates the outcome of the request.

## 9. Common HTTP Status Codes

- 200 OK: Request succeeded.
- 201 Created: A resource was created.
- 204 No Content: Request succeeded without a response body.
- 400 Bad Request: Request data is invalid.
- 401 Unauthorized: Authentication is required or invalid.
- 403 Forbidden: The server refuses the operation.
- 404 Not Found: The resource was not found.
- 500 Internal Server Error: An unexpected server error occurred.

## 10. API Error Responses

An API may return an error status and a JSON body describing
the problem. The exact format depends on the API.

Example:

{
  "error": "Resource not found"
}

This is an illustrative example, not a verified JSONPlaceholder
error response.

A client should check the status code and response body before
assuming that a request succeeded.

## 11. CRUD Operations

CRUD stands for:

- Create: POST
- Read: GET
- Update: PUT or PATCH
- Delete: DELETE

These operations represent the basic ways applications work
with stored resources.

## 12. Conclusion

This project provided practical experience with a public REST API.
I tested collection and individual-resource requests, query
parameters, request bodies, response bodies, HTTP headers,
status codes, and CRUD methods.

I also learned the difference between PUT and PATCH and the
basic meaning of idempotency.

The Python script used in this project is available as api_tests.py.


## 13. Actual Test Results

All seven API requests completed successfully.

| HTTP Method | Endpoint | Actual Status |
|---|---|---|
| GET | /posts | 200 OK |
| GET | /posts/1 | 200 OK |
| GET | /posts?_limit=5 | 200 OK |
| POST | /posts | 201 Created |
| PUT | /posts/1 | 200 OK |
| PATCH | /posts/1 | 200 OK |
| DELETE | /posts/1 | 200 OK |

### Headers Observed

- Content-Type: application/json; charset=utf-8
- Cache-Control: max-age=43200 for the GET requests
- Server: cloudflare

The POST, PUT, PATCH, and DELETE responses used
Cache-Control: no-cache.

### Sample POST Response

{
  "title": "Day 4 API Project",
  "body": "Learning REST APIs using Python",
  "userId": 1,
  "id": 101
}

The API returned status 201, indicating successful simulated
creation of a post.

### Idempotency

GET is intended to be safe and idempotent. PUT and DELETE are
intended to be idempotent. Repeating the same POST can create
additional resources, so POST is not generally idempotent.
PATCH may or may not be idempotent, depending on the operation.

### Testing Limitation

JSONPlaceholder is a testing API. Write requests return simulated
results and do not permanently modify its stored dataset.

