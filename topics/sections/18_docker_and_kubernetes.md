<!-- Part of Java Learning Roadmap — Section 18 -->

## 🐳 14. Docker & Kubernetes

- **Docker**
  - Image vs Container
  - `Dockerfile` — `FROM`, `RUN`, `COPY`, `EXPOSE`, `ENTRYPOINT`, `CMD`
  - Multi-stage builds
  - Docker Compose — multi-container apps
  - Dockerizing a Spring Boot App
- **JVM in Containers**
  - JVM ergonomics — heap sized to host, not container
  - `-XX:MaxRAMPercentage=75` — container-aware heap
  - JVM GC behavior under OOMKill
- **Kubernetes**
  - Pods, Deployments, Services, ConfigMaps, Secrets
  - Liveness & Readiness Probes — `/actuator/health`
  - Horizontal Pod Autoscaler (HPA)
  - Resource limits (`requests` and `limits`)
  - Blue-Green Deployment, Rolling Updates, Canary
- **Cloud Platforms**
  - AWS — EC2, S3, RDS, ECS, Lambda, ELB, IAM, CloudWatch
  - Azure, GCP basics

---
