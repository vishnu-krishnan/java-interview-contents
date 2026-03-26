<!-- Part of Java Learning Roadmap — Section 17 -->

# 🔧 17. Java Build Tools & DevOps Basics

---

## 1. Definition

**Build Tools** (Maven, Gradle) are command-line utilities that completely automate the Java compilation lifecycle. They handle downloading third-party libraries, compiling `.java` to `.class` files, running automated tests, and packaging the final application.
**DevOps** in the Java context refers to the automated pipeline that takes that packaged application from a developer's Github branch and safely deploys it to a production server (CI/CD).

---

## 2. Why It Exists

*   **Dependency Management (The end of "JAR Hell"):** Before Maven, if you wanted to use Hibernate, you had to manually download `hibernate.jar`, put it in a `/lib` folder, and realize it crashed because it needed `logging.jar`, download that... and so on. Build tools resolve these "Transitive Dependencies" over the internet automatically.
*   **Reproducible Builds:** If `mvn clean package` works on Alice's MacBook, it is guaranteed to work exactly the same way on Bob's Windows machine and the Linux build server.
*   **CI/CD Pipeline Automation:** Instead of a developer manually FTP-uploading a `.jar` file to a server on Friday night, a robot (GitHub Actions / Jenkins) runs all tests, builds the `.jar`, builds a Docker image, and deploys it automatically when code is merged into the `main` branch.

---

## 3. How It Works Internally

### 3.1 The Maven Lifecycle
Maven operates strictly on a set sequence of phases. If you run `mvn install`, Maven executes EVERY phase before it sequentially:
1.  **validate:** Check project structure.
2.  **compile:** Compile `src/main/java` into `.class` files in the `/target` directory.
3.  **test:** Run JUnit tests in `src/test/java`. (If a test fails, the build STOPS here).
4.  **package:** Zip the compiled classes into a `.jar` or `.war`.
5.  **verify:** Run heavier integration tests.
6.  **install:** Copy the final `.jar` into your local `~/.m2` folder so your other local projects can use it.

### 3.2 Maven Transitive Dependency Resolution
If you declare Spring Boot as a dependency in your `pom.xml`, Maven downloads Spring Boot. It then reads Spring Boot's internal `pom.xml` and downloads its dependencies (Tomcat, Jackson, Slf4j). If two libraries ask for different versions of the same transitive dependency, Maven resolves the conflict using a "Nearest Definition" graph algorithm.

### 3.3 Git and the DAG
Git does not store files like a traditional file system. It stores a **Directed Acyclic Graph (DAG)** of snapshots. A commit is simply a securely hashed (SHA-1) pointer to the exact state of your tracked files at a specific millisecond, plus a pointer back to its "parent" commit.
*   **Merge:** Creates a new "Merge Commit" that joins two separate branch histories together.
*   **Rebase:** Rewrites history. It unplugs your feature branch from the past, and forcibly replugs it into the very tip of the `main` branch, creating a completely linear, clean history.

---

## 4. Code Examples

### 4.1 A minimal `pom.xml`
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.myapp</groupId>
    <artifactId>ecommerce-api</artifactId>
    <version>1.0.0-SNAPSHOT</version> <!-- SNAPSHOT means "still in development" -->

    <dependencies>
        <!-- Dependency -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
            <version>3.2.0</version>
        </dependency>

        <!-- Test Scoped: Only used in src/test/java, NOT deployed to prod! -->
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>5.10.0</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
</project>
```

### 4.2 GitHub Actions CI Pipeline (`.github/workflows/build.yml`)
```yaml
name: Java CI with Maven

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    # 1. Pull the code from Git
    - uses: actions/checkout@v3
    
    # 2. Setup Java 21
    - name: Set up JDK 21
      uses: actions/setup-java@v3
      with:
        java-version: '21'
        distribution: 'temurin'
        
    # 3. Cache dependencies to make future builds 10x faster
    - name: Cache Maven packages
      uses: actions/cache@v3
      with:
        path: ~/.m2
        key: maven-${{ hashFiles('**/pom.xml') }}
        
    # 4. Compile, Test, and Build the Fat JAR!
    - name: Build with Maven
      run: mvn -B clean package --file pom.xml
```

---

## 5. Interview Questions

| Question | Answer |
|---|---|
| Gradle vs Maven? | **Maven** relies on XML, enforces a very strict project structure, and is highly standardized. **Gradle** uses Groovy/Kotlin code, is extremely customizable, and is significantly faster in massive codebases due to its incremental build cache. Android uses Gradle exclusively. |
| Difference between `git rebase` and `git merge`? | `merge` preserves the exact timeline of when commits were made, creating a web-like graph. `rebase` rewrites history to create a perfectly straight line, making the git log infinitely easier to read. Never rebase a public/shared branch! |
| What is a "Snapshot" definition in Maven? | A version ending in `-SNAPSHOT` means the code is unstable and changing. Maven will check the remote repository for updates every single day. A non-snapshot version (like `1.0.0`) is immutable; Maven will download it once and *never* check for updates again. |
| What does `mvn clean install -DskipTests` do? | Deletes the `/target` folder (`clean`), compiles/packages/moves the JAR to the local `~/.m2` cache (`install`), but massively speeds up the process by completely skipping the JUnit test execution. |

---

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| Committing the `target/` or `.idea/` folder to Git | Pollutes the repository with thousands of compiled binary files that change every single time someone builds the project, causing hundreds of constant merge conflicts. | Always add `target/`, `.idea/`, and `*.jar` to your `.gitignore` file before your very first commit. |
| The "Diamond Dependency" Problem | You include Lib A (requires Guava v15) and Lib B (requires Guava v30). Maven arbitrarily picks Guava v15. Lib B calls a method only found in v30, and the app crashes at runtime with `NoSuchMethodError`. | Use `<dependencyManagement>` tags in Maven or explicitly exclude the older transitive dependency. |
| Running raw `mvn` or `gradle` | If Dave runs `mvn clean install` using Maven 3.6, and servers run Maven 3.9, builds might differ. | Always use the **Maven Wrapper** (`./mvnw clean install`). It auto-downloads the exact right version of Maven for the project into a local sandbox. |

---

## 7. Real-World Usage

| Tool | Where it shows up |
|---|---|
| **Jenkins** | The legacy industry standard CI/CD server. Highly customizable with Groovy scripts. |
| **GitHub Actions / GitLab CI** | Modern YAML-based pipelines attached directly to the git repositories. |
| **SonarQube / JaCoCo** | During the CI pipeline, JaCoCo tracks test coverage. SonarQube analyzes the source code for bugs. If code coverage is < 80% or SonarQube detects a Critical Security Bug, the CI pipeline throws a red "X" and *prevents* the developer from clicking the "Merge" button. |

---

## 8. Practice Tasks

1.  **Maven CLI Mastery:** Go to an existing Spring Boot project. Open the terminal. Run `./mvnw clean dependency:tree`. Watch it print out exactly what transitive libraries your project is dragging in.
2.  **Git Rebase Simulation:** Create a local git repo. Create `main` branch, add a commit. Create a `feature` branch, add 2 commits. Go back to `main`, add 1 commit. Go to `feature`, run `git rebase main`. Open a Git GUI (like GitKraken or `git log --graph`) to see the perfectly straight linear history.
3.  **Local Pipeline:** Modify a Spring Boot `pom.xml` to include the `jacoco-maven-plugin`. Run `mvn clean test`. Navigate to `target/site/jacoco/index.html` and open it in a browser to see exactly which lines of your code your unit tests missed.

---

## 9. Quick Revision

### Maven Scopes
*   `compile` (Default): Needed at compile time and runtime. Included in Fat JAR.
*   `provided`: Needed to compile (e.g., Servlet API), but Tomcat will provide it at runtime. NOT included in Fat JAR.
*   `test`: JUnit/Mockito. Only exists in `/test` folder.
*   `runtime`: MySQL Driver. Not directly referenced in Java code, but needed for DB connections at runtime.

### Git Daily Flow
`git fetch` → `git rebase origin/main` (Put my local changes on top of others) → `git push origin my-feature`

### CI vs CD
*   **Continuous Integration:** Compiling, testing, and SonarQube analysis on every Pull Request.
*   **Continuous Deployment:** Taking the successful `main` branch, building a Docker image, and pushing it to an AWS Production server automatically.
