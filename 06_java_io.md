<!-- Part of Java Learning Roadmap — Section 6 -->

# 💾 6. Java Input/Output (I/O)

---

## 1. Definition

**Java I/O (Input/Output)** provides the APIs necessary to read from and write to data sources/destinations (files, network connections, memory buffers). 

It is divided into two primary eras:
1.  **Classic I/O (`java.io`):** Stream-oriented, blocking APIs. Handles byte streams (8-bit) and character streams (16-bit).
2.  **New I/O (`java.nio` / NIO.2):** Buffer and Channel-oriented, non-blocking APIs introduced in Java 1.4 and enhanced in Java 7 (`java.nio.file.Files`).

---

## 2. Why It Exists

Applications are useless if they cannot interact with the outside world.
*   **File Storage:** Reading configs, saving logs, parsing CSVs.
*   **Networking:** Sending bytes over TCP/UDP Sockets (Tomcat handling HTTP).
*   **Persistence (Serialization):** Converting living Java Objects on the Heap into a binary byte array to store in Redis, save to a disk, or send across a network to another microservice.

---

## 3. How It Works Internally

### 3.1 Streams vs Buffers
*   **Stream (`java.io`):** Reads data one byte/character at a time directly from the OS file descriptor. Extremely slow because every `read()` triggers an OS system call.
*   **Decorated Buffered Stream:** Wraps the raw stream. Grabs a large chunk (e.g., 8KB) from the OS at once into RAM. Future `read()` calls pull from RAM, which is thousands of times faster.

### 3.2 Java NIO (Channels & Buffers)
Unlike Streams which are one-way (Input *or* Output), **Channels** are two-way connections to the OS. Data is read from a Channel into a **Buffer** (a dedicated block of memory), processed, and written back out. 
NIO supports **Non-Blocking I/O**: A single thread can ask a Channel "do you have data?" If no, the thread moves on to serve another Channel instead of waiting (blocking) endlessly (this is how Netty / Spring WebFlux works).

### 3.3 The Serialization Engine
When `ObjectOutputStream` serializes an object:
1.  It checks if the class implements the marker interface `Serializable`.
2.  It copies the class metadata (name, fields) and the `serialVersionUID`.
3.  It converts all non-`transient`, non-`static` primitive fields to bytes.
4.  It traverses object references (like a `List<Address>`) and recursively serializes them (the referenced classes must ALSO be `Serializable`).

---

## 4. Code Examples

### 4.1 Quick File Read/Write (Java 11+)
```java
Path filePath = Path.of("config.txt");

// Write string to file
Files.writeString(filePath, "server.port=8080");

// Read entire file to string
String content = Files.readString(filePath);
System.out.println(content);
```

### 4.2 Handling Large Files (Classic `java.io`)
```java
// USE try-with-resources to ensure streams close automatically!
File file = new File("huge_log.txt");

try (BufferedReader br = new BufferedReader(new FileReader(file))) {
    String line;
    // Reads line by line, maintaining low memory footprint O(1)
    while ((line = br.readLine()) != null) {
        if (line.contains("ERROR")) {
            System.out.println(line);
        }
    }
} catch (IOException e) {
    e.printStackTrace();
}
```

### 4.3 Object Serialization (Deep Dive)
```java
// 1. Must implement Serializable
class UserSession implements Serializable {
    // 2. Add UID to prevent crashes if we add fields later
    private static final long serialVersionUID = 1L; 
    
    String username;
    // 3. transient prevents sensitive data from being serialized
    transient String pwdHash; 

    public UserSession(String u, String p) {
        this.username = u;
        this.pwdHash = p;
    }
}

public class Serializer {
    public static void main(String[] args) throws Exception {
        UserSession session = new UserSession("alice", "secret123");

        // Serialize DTO -> Byte Stream
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("session.ser"))) {
            oos.writeObject(session);
        }

        // Deserialize Byte Stream -> Live Object
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream("session.ser"))) {
            UserSession restored = (UserSession) ois.readObject();
            System.out.println(restored.username); // 'alice'
            System.out.println(restored.pwdHash);  // 'null' (because it was transient)
        }
    }
}
```

---

## 5. Interview Questions

| Question | Answer |
|---|---|
| Difference between `InputStream` and `Reader`? | `InputStream` handles raw 8-bit bytes (images, zips). `Reader` handles 16-bit characters (text files). |
| What is `transient` keyword? | Marks a field so it's ignored by the JVM serialization engine. It restores to its default value (`null`, `0`) upon deserialization. |
| Difference between `Serializable` and `Externalizable`? | `Serializable` is a marker interface (no methods); JVM does all the work. `Externalizable` requires overriding `readExternal` and `writeExternal` to manually control exactly what bytes are written, providing better performance. |
| Why use `BufferedReader` instead of `FileReader`? | `FileReader` hits the hard drive for every single character. `BufferedReader` pulls 8KB at a time into RAM, reducing slow physical disk reads dramatically. |
| What causes `InvalidClassException`? | The `serialVersionUID` of the `.class` file trying to deserialize the byte stream does not match the ID stored inside the byte stream. Always declare the UID explicitly! |

---

## 6. Common Mistakes

| Mistake | Problem | Fix |
|---|---|---|
| Not closing IO streams | File handle leaks. The OS limits how many files a process can hold open. Maxing it out crashes the app. | ALWAYS use `try-with-resources`. It auto-calls `.close()` even if exceptions are thrown. |
| Using `Files.readAllLines()` on a 5GB log file | Reads 5GB directly into JVM Heap memory, instantly causing `OutOfMemoryError` (OOM). | Use `Files.lines(path)` which returns a `Stream<String>` and streams the file lazily line-by-line. |
| Serializing a class containing a non-serializable object | E.g. `User` is Serializable, but contains a `Department` which isn't. | Throws `NotSerializableException` at runtime. Ensure the entire object graph implements `Serializable`. |

---

## 7. Real-World Usage

| API | Where it shows up |
|---|---|
| **`Files.lines()`** | Parsing massive multi-gigabyte server access logs to search for specific error codes using Stream API filters. |
| **`ObjectOutputStream`** | Spring Session storing user sessions in a Redis cluster. The Java Web App converts the Session object to bytes, saves in Redis, and other servers reconstruct it. |
| **`java.nio` (NIO)** | Netty, WebFlux, and Kafka use NIO for incredibly fast, non-blocking networking over TCP/IP, handling 100k+ connections on few threads. |

---

## 8. Practice Tasks

1.  **File Copying Benchmark:** Write a program to copy a 1GB MP4 file in three ways: 1) `FileInputStream` byte-by-byte (don't actually run this to completion, just note how slow it is). 2) `BufferedInputStream`. 3) `Files.copy(source, target)`. Compare times.
2.  **Streaming processing:** Create a 1M line CSV file. Use `Files.lines(path)` to read it, filter rows where column values > 100, and write those rows to a new file using `Files.write()`.
3.  **Serialization breaker:** Create a `Student` class. Serialize it to disk. Then, add a new field `int age` to the `Student` class, recompile, and try to deserialize the old file. Observe the `InvalidClassException`. Fix it by adding a `serialVersionUID`.

---

## 9. Quick Revision

### I/O Matrix
| Data Type | Raw (Slow) | Buffered (Fast) | High-Level Tool |
|---|---|---|---|
| **Bytes (Images)** | `FileInputStream` | `BufferedInputStream` | `Files.readAllBytes()` |
| **Chars (Text)** | `FileReader` | `BufferedReader` | `Files.readString()` |

### Key Concepts
*   **java.io = Blocking, Stream-based.**
*   **java.nio = Non-Blocking, Buffer + Channel based.**
*   `try-with-resources` requires the object to implement `AutoCloseable`.
*   `transient` ignores fields during Serialization.
*   `serialVersionUID` acts as version control for Serialized bytes.
