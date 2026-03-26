<!-- Part of Java Learning Roadmap — Section 22 -->

## 🔭 20. Observability & Monitoring

- **Logging**
  - SLF4J + Logback / Log4j2
  - Structured logging — JSON format
  - Log levels — TRACE, DEBUG, INFO, WARN, ERROR
  - Async logging — don't block request threads
  - MDC (Mapped Diagnostic Context) — correlation IDs per thread
- **Metrics**
  - Micrometer — metrics facade for Spring Boot
  - **Prometheus** — pull-based metrics collection
  - **Grafana** — dashboards and alerting
  - Key metrics: JVM heap, GC pauses, thread count, HTTP request latency, error rate
- **Distributed Tracing**
  - OpenTelemetry (vendor-neutral)
  - Zipkin, Jaeger — trace visualization
  - Trace ID + Span ID propagation across services
- **Log Aggregation**
  - ELK Stack — Elasticsearch + Logstash + Kibana
  - EFK Stack — Elasticsearch + Fluentd + Kibana
- **Health Checks**
  - Spring Boot Actuator — `/health`, `/metrics`, `/info`, `/env`
  - Kubernetes Liveness & Readiness Probes
- **APM Tools** — Dynatrace, New Relic, Datadog, Splunk
- **Code Quality**
  - SonarQube — static analysis, coverage, code smells
  - PMD, Checkstyle, SpotBugs

---
