<!-- Part of Java Learning Roadmap — Section 15 -->

## 🌐 12. Web Development & API Design

- Java Servlets, JavaServer Pages (JSP)
- **RESTful API Design Principles**
  - Statelessness, Uniform Interface, Resource-based URIs
  - HTTP Status Codes: 200, 201, 204, 400, 401, 403, 404, 409, 500, 503
  - HTTP Methods — `GET`, `POST`, `PUT`, `PATCH`, `DELETE`
  - Idempotency — which methods are idempotent
  - API Versioning — URI (`/v1/`), Header, Query Param
  - Pagination — `page`, `size`, `sort` parameters
  - HATEOAS
- **DTO Pattern** — separates API contract from domain model
- **Swagger / OpenAPI** documentation (`springdoc-openapi`)
- **Rate Limiting** — token bucket, sliding window
- GraphQL — alternative to REST for flexible queries
- **REST vs gRPC**

  | Feature | REST | gRPC |
  |---|---|---|
  | Protocol | HTTP/1.1 | HTTP/2 (multiplexing, streaming) |
  | Data Format | JSON (human-readable) | Protocol Buffers (binary, compact) |
  | Performance | Slower (JSON parsing) | Faster (binary serialization) |
  | Contract | OpenAPI/Swagger (optional) | `.proto` file (mandatory, strict) |
  | Browser Support | Excellent | Limited (needs gRPC-Web proxy) |
  | Streaming | Limited (SSE, WebSocket) | Native bi-directional streaming |
  | Best For | Public APIs, web clients | Internal microservice comms |

---
