<!-- Part of Java Learning Roadmap — Section 15 -->

# 🌐 15. Web Development & API Design

---

## 1. Definition

**API (Application Programming Interface)** Design in the Java ecosystem primarily revolves around creating **RESTful** (Representational State Transfer) web services. 
*   **REST** uses standard HTTP methods (`GET`, `POST`, `PUT`, `DELETE`) to manipulate data over a network.
*   **Statelessness:** Every HTTP request from a client to the server must contain all the information needed to understand the request. The server does *not* remember previous requests (no server-side sessions).
*   **Resources:** Data entities (like Users or Orders) that are accessible via specific URIs.

---

## 2. Why It Exists

*   **Decoupling Frontend and Backend:** A React web app, an iOS app, and a Python script can all consume the exact same Java REST API. 
*   **Standardization:** Following REST principles means developers instantly know how to interact with your system without reading a 500-page manual. If they want to create a User, they instinctively know to send a `POST` request to `/users`.

---

## 3. How It Works Internally

### 3.1 HTTP and Jackson Serialization
When a client sends a JSON payload to a Spring Boot `@RestController`, the raw HTTP request bytes are intercepted by Tomcat. Spring uses the **Jackson Library** to "deserialize" the JSON String into a Java Object (like a DTO). When the Java method returns, Jackson "serializes" the Java Object back into a JSON String, and Tomcat sends it over the TCP socket as an HTTP Response.

### 3.2 The DTO (Data Transfer Object) Pattern
A Database `@Entity` should **never** be sent over the API or received from the API.
If your `UserEntity` has an `id`, `name`, `passwordHash`, and `createdAt` field, returning it directly in the API exposes the `passwordHash` to the public internet! 
Instead, you map the `UserEntity` into a `UserResponseDTO` (which only contains `id` and `name`) before returning it. 

### 3.3 HTTP Idempotency
An operation is **idempotent** if executing it 1 time has the exact same effect on the server as executing it 10,000 times.
*   `GET /users/5` (Idempotent. Reading doesn't change state).
*   `DELETE /users/5` (Idempotent. The first time deletes it. The next 9,999 times do nothing; it's already gone).
*   `PUT /users/5` (Idempotent. Replacing a user with identical data 10 times results in the same final state).
*   `POST /users` (NOT Idempotent. Clicking the "Submit Order" button 10 times will create 10 distinct orders and charge the credit card 10 times).

---

## 4. Code Examples

### 4.1 A Perfect REST Controller
```java
@RestController
@RequestMapping("/api/v1/users") // Resource NOUN, Versioned
public class UserController {

    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    // GET: Retrieve resource. Returns 200 OK.
    @GetMapping("/{id}")
    public ResponseEntity<UserResponseDto> getUser(@PathVariable Long id) {
        UserResponseDto dto = userService.getUserById(id);
        return ResponseEntity.ok(dto);
    }

    // POST: Create resource. Returns 201 Created.
    @PostMapping
    public ResponseEntity<UserResponseDto> createUser(@Valid @RequestBody UserCreateDto request) {
        UserResponseDto created = userService.createUser(request);
        
        // Best practice: Return the URI of the newly created resource
        URI location = ServletUriComponentsBuilder.fromCurrentRequest()
                .path("/{id}").buildAndExpand(created.getId()).toUri();
                
        return ResponseEntity.created(location).body(created);
    }

    // DELETE: Remove resource. Returns 204 No Content.
    @DeleteMapping("/{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT) 
    public void deleteUser(@PathVariable Long id) {
        userService.deleteUser(id);
    }
}
```

### 4.2 Global Exception Handling
REST APIs should return standardized error JSON, not raw HTML stack traces.
```java
@ControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(EntityNotFoundException.class)
    public ResponseEntity<Map<String, String>> handleNotFound(EntityNotFoundException ex) {
        Map<String, String> error = Map.of(
            "error", "Not Found",
            "message", ex.getMessage()
        );
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
    }
}
```

---

## 5. Interview Questions

| Question | Answer |
|---|---|
| Difference between `PUT` and `PATCH`? | `PUT` replaces the *entire* resource. If you omit a field in a PUT request, the server should set it to null. `PATCH` applies a *partial* update. It only updates the fields explicitly provided in the payload. |
| Difference between `401 Unauthorized` and `403 Forbidden`? | `401` means "I don't know who you are" (Missing or invalid auth token). `403` means "I know exactly who you are, but you don't have Admin permissions to do this." |
| What is PathVariable vs RequestParam? | `@PathVariable` extracts values from the URI path (`/users/{id}`). Used to identify a specific resource. `@RequestParam` extracts values from the query string (`/users?role=admin`). Used for filtering, sorting, or pagination. |
| Why is versioning URIs important? | If iPhone apps currently in the app store expect `v1` of your API, and you suddenly change the JSON structure for `v2`, all old iPhone apps immediately crash. Versioning allows both to run simultaneously. |
| Why is `PATCH` not always considered Idempotent? | If a PATCH request says `{"increment_counter": 5}`, running it 10 times will result in +50, changing the state every time. |

---

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| Using Verbs in the URI | `/api/getAllUsers` or `/api/deleteUser?id=5`. This violates REST principles entirely and acts like RPC (Remote Procedure Call). | URIs must be plural Nouns. The HTTP Method dictates the action. `GET /api/users` and `DELETE /api/users/5`. |
| Exposing Database Entities in Controllers | Causes tight coupling. If you rename a DB column from `firstname` to `first_name`, you accidentally change your API JSON contract and break all frontends! | Always map Entities to DTOs in the Service or Controller layer before returning them. |
| Returning `200 OK` for Errors | Returning `{ "status": "error", "metadata": "User not found" }` with an HTTP 200 header breaks API clients that rely on HTTP status codes to trigger error handling logic. | Always return proper HTTP Status Codes (404, 400, 500). |

---

## 7. Real-World Usage

| Pattern | Where it shows up |
|---|---|
| **Pagination & Sorting** | Fetching 10 million users via `GET /users` will crash the server. APIs implement `GET /users?page=1&size=20&sort=name,asc`. |
| **Richardson Maturity Model** | Level 3 REST APIs implement **HATEOAS** (Hypermedia as the Engine of Application State). The API JSON response includes navigational links (e.g., a "next_page" URL link inside the JSON response) so the client doesn't have to guess URIs. |
| **Circuit Breakers** | When Microservice A calls Microservice B's REST API, and B is down, A will hang indefinitely. Resilience4j is used to "break the circuit" and instantly return a fallback response. |

---

## 8. Practice Tasks

1.  **Anti-Pattern Fix:** Take the URI `/api/updateUserPass?userId=5&newPass=secret`. Refactor this into a proper RESTful URI using the correct HTTP method.
2.  **DTO Mapper:** Create a `User` entity with `id`, `name`, `password`, and `ssn`. Create a `UserPublicDto`. Use the `ModelMapper` or `MapStruct` library to automatically map the Entity to the DTO, asserting that the password and SSN are ignored.
3.  **ControllerAdvice:** Create a custom `UserAlreadyExistsException`. Write a `@RestControllerAdvice` class that catches this exception universally across all controllers and returns a clean JSON response with an HTTP `409 Conflict` status code.

---

## 9. Quick Revision

### HTTP Methods
*   `POST`: Create (Not Idempotent)
*   `GET`: Read (Idempotent, Safe)
*   `PUT`: Full Update (Idempotent)
*   `PATCH`: Partial Update (Not Idempotent strictly)
*   `DELETE`: Delete (Idempotent)

### Status Code Matrix
| Range | Meaning | Common Codes |
|---|---|---|
| **2xx** | Success | `200` OK, `201` Created, `204` No Content |
| **3xx** | Redirection | `301` Moved Permanently, `304` Not Modified (Cache valid) |
| **4xx** | Client Mistake | `400` Bad Request (Validation failed), `401` Identity Unknown, `403` Identity Known but blocked, `404` Not Found, `409` Conflict (Duplicate). |
| **5xx** | Server Mistake | `500` NPE/Crash, `503` Service Unavailable (Overload/Maintenance) |
