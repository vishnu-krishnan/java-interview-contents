<!-- Part of Java Learning Roadmap — Section 18 -->

# 🐳 18. Docker & Kubernetes

---

## 1. Definition

**Docker** is a platform designed to create, deploy, and run applications inside isolated environments called **Containers**. A container packages the application (`.jar`), the runtime (Java JRE), and the underlying OS libraries (Alpine Linux) into a single standard unit.
**Kubernetes (K8s)** is a container orchestration system. While Docker builds the container, K8s decides which physical server to put it on, how to scale it from 1 to 100 copies based on CPU load, and how to route traffic to it.

---

## 2. Why It Exists

*   **The "It works on my machine" Problem:** A developer's Mac has Java 21 installed. The production server has Java 8 installed. The code crashes. With Docker, the developer ships the exact Linux OS and Java 21 runtime *inside* the container. It runs identically everywhere.
*   **Microservice Scaling:** Manually SSH-ing into 10 Linux servers to upload 10 separate `.jar` files takes hours. Kubernetes automates this deployment and scales the application globally across thousands of nodes in seconds.
*   **Self-Healing:** If an application deadlocks and runs out of memory, Kubernetes notices it stopped responding, immediately shoots the container in the head, and spins up a fresh one without human intervention.

---

## 3. How It Works Internally

### 3.1 Docker (Linux Namespaces & Cgroups)
Unlike a Virtual Machine (VMware, VirtualBox) which boots up an entirely separate, heavy guest OS with its own kernel, Containers share the Host OS kernel.
*   **Namespaces:** Provide isolation (The container thinks it's the only process on the machine, with its own isolated Hard Drive).
*   **Cgroups (Control Groups):** Provide resource limiting (The container is mathematically restricted to only use 512MB of RAM, even if the physical server has 64GB).

### 3.2 Kubernetes Architecture
*   **Control Plane (Master Node):** The brain. The `kube-apiserver` receives your YAML instructions. The `kube-scheduler` looks at your worker nodes and decides which one has enough free RAM to run your container.
*   **Worker Nodes:** The physical servers running your code. They run `kubelet`, an agent that talks to Docker/containerd to actually start the containers.
*   **Pod:** The absolute smallest deployable unit in K8s. A pod wraps one (or sometimes more) Docker containers.
*   **Service (ClusterIP/LoadBalancer):** Pods are born and die constantly; their IP addresses constantly change. A Service acts as a static Front Desk IP address that routes traffic to whichever Pods happen to be alive at the moment.

---

## 4. Code Examples

### 4.1 A Production-Ready Java Dockerfile
```dockerfile
# Stage 1: Fast build using a tiny base image
FROM eclipse-temurin:21-jre-alpine

# Security: Never run containers as root! Create a non-root user.
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Copy the Fat JAR from the target folder into the container
COPY target/myapp.jar /app.jar

# Run the app. 
# CRITICAL: Use MaxRAMPercentage so the JVM respects the K8s container memory limits!
ENTRYPOINT ["java", "-XX:MaxRAMPercentage=75.0", "-jar", "/app.jar"]
```

### 4.2 Kubernetes Deployment YAML
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deployment
spec:
  replicas: 3 # Run 3 identical copies of this container instantly
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp-container
        image: myrepo/myapp:1.0
        resources:
          limits:
            memory: "512Mi" # K8s limits the OS container to 512MB
        # Self-Healing: If Spring Boot's Actuator health endpoint returns 500, kill it.
        livenessProbe:
          httpGet:
            path: /actuator/health/liveness
            port: 8080
          initialDelaySeconds: 15
```

---

## 5. Interview Questions

| Question | Answer |
|---|---|
| Difference between a Docker Image and a Container? | An **Image** is the read-only template containing the application code and OS (like an OOP Class). A **Container** is a running instantiation of that Image (like an Object). |
| Difference between Liveness and Readiness Probes? | **Liveness Probe:** Checks if the app is deadlocked. Action: K8s *restarts* the container. **Readiness Probe:** Checks if the app is fully done loading cache/DB connections. Action: K8s temporarily *stops sending web traffic* to the container until it's ready. |
| What is a DaemonSet in K8s? | A Deployment scales pods based on load. A DaemonSet guarantees that exactly 1 copy of a Pod runs on *every single physical node* in the cluster. Used for log collectors (Filebeat) or monitoring agents (Datadog). |
| What happens if a Java process tries to use 2GB RAM in a 1GB Docker Container? | The Linux Kernel OOMKiller (Out of Memory Killer) instantly terminates the container process with an exit code of 137. |

---

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| Using `-Xmx512m` in Docker | If you deploy to K8s with a 1GB memory limit, your Java app will never utilize more than 512MB, wasting half the server. | Use `-XX:MaxRAMPercentage=75.0`. The JVM dynamically calculates 75% of whatever limit K8s enforces on the container. |
| Building massive 1GB Images | Using `FROM ubuntu` as a base image wastes bandwidth, slows down pipeline builds, and introduces 500+ unnecessary OS security vulnerabilities. | Use heavily stripped down base images like `eclipse-temurin:21-jre-alpine` (often under 100MB). |
| Putting the Database in the same container | "I'll run Tomcat and PostgreSQL inside the same Dockerfile." Containers are meant to be ephemeral and single-purpose. When K8s restarts the app, your database gets wiped out. | 1 Process per Container. App in one container. DB in another container (or preferably AWS RDS). |

---

## 7. Real-World Usage

| Tool | Where it shows up |
|---|---|
| **Spring Boot Layered Jars** | If you change 1 line of code, Docker typically rebuilds the entire 50MB image. Spring Boot separates your third-party dependencies into a separate "Layer". Because dependencies rarely change, Docker caches them perfectly, making future image builds take < 1 second. |
| **K8s ConfigMaps & Secrets** | You don't hardcode `application-prod.yml` inside the Docker image. You build the image *once*, then inject configuration as a ConfigMap from K8s, and DB passwords as K8s Secrets during deployment. |
| **K8s Horizontal Pod Autoscaler (HPA)** | Watches CPU usage. If your app hits 80% CPU because of a Black Friday traffic spike, K8s automatically changes `replicas: 3` to `replicas: 20` to absorb the load. |

---

## 8. Practice Tasks

1.  **Containerize your app:** Take a Spring Boot `.jar`. Write a simple Dockerfile. Build it: `docker build -t myapp .`. Run it: `docker run -p 8080:8080 myapp`. Hit it in your browser.
2.  **Break the JVM:** Create an infinite loop appending strings to an array to cause an OutOfMemoryError. Run it in docker with `docker run -m 100m myapp`. Observe how the Linux OOMKiller terminates the process when the OS hits 100MB before the JVM throws its own exception.
3.  **K8s Minikube:** Install Minikube locally (a single-node K8s cluster). Deploy the YAML from Section 4.2. Run `kubectl get pods` and then violently delete one using `kubectl delete pod [name]`. Watch K8s instantly spin up a replacement out of thin air.

---

## 9. Quick Revision

### The OS vs Container vs JVM Stack
1. Hardware Server (64GB RAM)
2. Host OS (Linux Kernel)
3. Container Cgroups Constraint (1GB RAM)
4. JVM MaxRAMPercentage 75% (750MB Heap)
5. Spring Boot Application

### K8s Terminology
*   **Pod:** A running container wrapper.
*   **Deployment:** The manager that ensures X number of pods are running.
*   **Service:** The static IP address that load balances traffic to the moving Pods.
*   **Liveness:** "Kill me if I freeze."
*   **Readiness:** "Don't send me web traffic yet, I'm still booting."
