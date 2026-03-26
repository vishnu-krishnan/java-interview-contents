<!-- Part of Java Learning Roadmap — Section 19 -->

# ☁️ 19. Deployment and Cloud (AWS)

---

## 1. Definition

**Cloud Computing** is the on-demand availability of computer system resources (data storage, computing power, databases) without direct active management by the user. It means renting servers from companies like Amazon (AWS), Microsoft (Azure), or Google (GCP) instead of buying physical hardware.

The Cloud operates in 3 main models:
1.  **IaaS (Infrastructure as a Service):** You rent a blank Linux server. You install Java, Tomcat, and manage OS patches yourself. (e.g., AWS EC2).
2.  **PaaS (Platform as a Service):** You upload a `.jar` file. Amazon handles the server, OS, and Java runtime fully automatically. (e.g., AWS Elastic Beanstalk, Heroku).
3.  **SaaS (Software as a Service):** Fully finished software you rent. (e.g., Gmail, Salesforce).

---

## 2. Why It Exists

*   **CapEx to OpEx:** Startups don't have $100,000 to buy servers. The cloud lets you pay 5 cents an hour for a tiny server and scale up only when users start paying you.
*   **Elasticity:** If your e-commerce site gets featured on the news, traffic spikes 10,000%. AWS can instantly launch 50 new servers automatically, and then destroy them an hour later when traffic dies, saving money.
*   **Global Reach:** Deploying your Java app simultaneously to data centers in New York, Tokyo, and Frankfurt takes exactly 3 mouse clicks.

---

## 3. How It Works Internally

### 3.1 AWS Core Services Map
*   **EC2 (Elastic Compute Cloud):** A Virtual Machine running Linux/Windows. It sits on top of a physical Amazon server via a Hypervisor.
*   **S3 (Simple Storage Service):** "Object Storage". It does not have folders/directories like a standard hard drive. Data is stored as flat objects with unique Keys. Terabytes of capacity for pennies. Cannot run an OS.
*   **RDS (Relational Database Service):** Amazon provides you a PostgreSQL endpoint. They handle automated daily backups, SSD patching, and instant failover to a backup server if the primary dies. 

### 3.2 Deployment Strategies
You cannot shut down a web server to upload a new `.jar` file; users will get "Site Down" errors. 
*   **Rolling Update:** You have 3 servers. Take Server A offline, update it, bring it online. Take Server B offline, update it... Zero downtime, but users might get different versions momentarily.
*   **Blue-Green:** You have the current Production (Blue). You spin up an entirely duplicate infrastructure (Green) and deploy v2 to it. You test Green thoroughly. Finally, you flip the DNS Router switch. Traffic instantly goes to Green. If Green crashes, you flip the switch back to Blue in 1 second. Zero downtime, maximum safety.

### 3.3 Serverless (AWS Lambda) & Cold Starts
Instead of paying for a server to sit idle 24/7 waiting for HTTP requests, **Serverless** means you upload a single Java function to AWS. When a request hits, AWS spins up a micro-container in milliseconds to run your function, and charges you only for the exact milliseconds it ran.
*   **Cold Start Problem:** Java is incredibly slow to start up. If a Lambda request triggers a brand new JVM boot, the user waits 5+ seconds (Cold Start). Subsequent requests hit the "Warm" JVM in 50ms. Use **AWS SnapStart** or **GraalVM Native Images** to fix Java cold starts.

---

## 4. Code Examples

### 4.1 Terraform (Infrastructure as Code)
Manually clicking through the AWS console is an anti-pattern. DevOps uses code (Terraform) to automatically provision cloud resources reliably.

```hcl
# main.tf - provisions a tiny Linux server in AWS
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "app_server" {
  ami           = "ami-0c55b159cbfafe1f0" # Amazon Linux 2
  instance_type = "t2.micro" # 1 vCPU, 1GB RAM (Free Tier)

  tags = {
    Name = "Spring-Boot-Production"
  }
}
```

### 4.2 S3 File Upload via Java (`aws-java-sdk-s3`)
```java
AmazonS3 s3Client = AmazonS3ClientBuilder.standard()
                        .withRegion(Regions.US_EAST_1)
                        .build();

// Uploading a user's profile picture to an S3 bucket 
String bucketName = "my-app-user-avatars";
String objectKey = "user_123_avatar.jpg";
File file = new File("local_avatar.jpg");

s3Client.putObject(new PutObjectRequest(bucketName, objectKey, file));
```

---

## 5. Interview Questions

| Question | Answer |
|---|---|
| Difference between deploying a DB on EC2 vs using RDS? | You *can* install PostgreSQL on an EC2 server manually. But you have to manage OS patches, DB backups, replication, and disaster recovery yourself. RDS manages all of this fully-automatically as a PaaS, saving massive engineering time. |
| What is a Canary Release? | Deploying the new v2 code to only 5% of users. You monitor error rates. If successful, you slowly ramp up to 20%, 50%, 100%. Safest strategy for massive companies. |
| What is a "Cold Start" in Serverless Architecture? | The time penalty incurred when the cloud provider must allocate hardware, boot the OS container, start the JVM, and load the Spring Context before the very first HTTP request can be served. |
| How do Java applications securely access AWS resources (like S3) without hardcoding passwords? | **IAM Roles**. Assign a role to the EC2 server (e.g., "S3-Upload-Role"). The AWS Java SDK automatically fetches temporary, rotating credentials seamlessly from the underlying server metadata without you ever typing a password. |

---

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| Hardcoding `AWS_ACCESS_KEY` in Java code | If committed to GitHub, bots will scrape the key in seconds, spin up 10,000 crypto-mining servers on your account, and bill you $50,000 overnight. | ALWAYS use AWS IAM Roles attached to your EC2 instance or Kubernetes pod. NEVER hardcode keys. |
| Making an S3 Bucket public intentionally | "I need users to see images!" Making the bucket public means anyone can list every file you own, finding sensitive bank statements or API keys you accidentally uploaded. | Block all public access. Generate **Pre-Signed URLs** via Java for users to temporarily view specific files for 5 minutes. |
| Blindly moving a monolithic Spring app to Lambda | Lambdas have a 15-minute maximum execution timeout and memory limits. Huge monolithic apps will crash or timeout. | Lambdas are for single, focused, fast functions. Monoliths belong on EC2, Fargate, or EKS. |

---

## 7. Real-World Usage

| Service | Where it shows up |
|---|---|
| **AWS S3 + CloudFront** | S3 holds the compiled React frontend `index.html` and `.js` files. CloudFront acts as a Global CDN, copying those files to edge locations worldwide so a user in Tokyo downloads the site in 10ms instead of waiting for a server in Ohio. |
| **AWS Elastic Load Balancer (ELB)** | Sits in front of 10 EC2 servers running your Spring Boot application across 3 separate data centers (Availability Zones). It evenly distributes web traffic to prevent crushing any single server. |
| **Spring Cloud AWS** | A library that radically simplifies connecting a Spring Boot app to AWS (e.g., auto-configuring `AmazonS3` beans for you based on the environment). |

---

## 8. Practice Tasks

1.  **IAM Role Check:** Open your AWS Console (Free tier). Create an S3 Bucket. Make it totally private. Create an IAM user with *only* S3 Put permissions. Download the keys locally, export them as env vars (`AWS_ACCESS_KEY_ID`), and run the Java S3 upload code. See it succeed. Now try to *delete* a file via Java and verify access is denied.
2.  **Deployment diagram:** Draw an architecture diagram showing an ELB at the front, routing to 3 different EC2 servers in a Private Subnet, which connect to an RDS PostgreSQL database in another Private subnet. Look at AWS Reference Architectures to check your work.

---

## 9. Quick Revision

### The Clouds
*   AWS (Amazon) = Market Leader. Concepts: EC2, S3, RDS, Lambda.
*   Azure (Microsoft) = Enterprise standard. Concepts: VMs, Blob Storage, SQL DB, Azure Functions.
*   GCP (Google) = Kubernetes native, Data analytics focus.

### Deployment Safety Scale
1.  **Upload zip over FTP (Dangerous!)** -> Minute-long downtime, manual errors.
2.  **Rolling Deployment (Safe)** -> Kills one server at a time. Slower to rollback.
3.  **Blue/Green (Very Safe)** -> Instant switchover. Instant rollback if it fails. High cost (requires 2x the servers temporarily).
4.  **Canary (Safest)** -> Expose to 1% of users. Monitor metrics. Ramp to 100% slowly.
