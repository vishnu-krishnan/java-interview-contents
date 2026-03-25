## 🚀 Sharing My Interview Journey: Database Questions Edition 🚀
During my recent interviews for a Java Fullstack Developer position, I came across several interesting questions—especially around database design and optimization. I’m sharing some of those questions to help with your interview preparation ....

Difference DDL and DML
Difference Delete Drop Truncate
Difference between WHERE vs HAVING explain with example
Difference between INNER JOIN vs LEFT JOIN
What is normalization?
What is primary key vs unique key
What is index and why it is used?
Difference between Statement vs PreparedStatement
What is connection pooling?
How Java connects to DB? also can we connects mupltiple DB in java application
@Transcation how it works internally ? on which level you use at class level or method level : prepare all concepts in-depth
what are the ACID properties ?
What is Hibernate?
What is Java Persistence API?
Difference between Hibernate and JPA
What is Entity?
What are annotations (@Entity, @Id, @Column)? how you join two entity which annotations used write with example
What is Lazy vs Eager loading? what happen if I use Lazy in fetch type
What is cascade type?
What is Session vs EntityManager?
which parameter need to condiser while design a database
How to optimize slow query
What happens if transaction fails midway
How to scale database for millions of users
How to improve query performance?
What is indexing strategy? perpare with example
What is caching?
What is N+1 problem in Hibernate?
How to avoid full table scan?

Find the 2nd highest salary using subquery and without subquery
Find duplicate records
Get Nth highest salary
Find employees with no manager or with manager
Get top 3 records per department
Find common records between two tables
Delete duplicate rows but keep one
Find employee and their manager name from same table
Show the top 3 products by sales in each region.
Table: Sales
SaleID Region Product Amount
1 East Pen 200
2 East Book 500
3 East Bag 300
4 West Pen 150
5 West Book 700
6 West Bag 250
---
## Why “N+1 Query Problem” Can Kill Your Application Performance

Your API works fine…
Your database is healthy…

But your application is still slow.

You might be facing the N+1 Query Problem.

What is N+1 Problem?

It happens when your application makes:
 1 query to fetch a list
 N additional queries to fetch related data

So instead of 1 efficient query, you end up with N+1 database calls.

Simple Example

You fetch a list of 100 users:
SELECT * FROM users;

Then for each user:
SELECT * FROM orders WHERE user_id = ?;

Total queries = 101 instead of 1

Why It’s Dangerous

Hidden Performance Killer
 Works fine in development, fails at scale.
Increases DB Load
 More queries = more CPU, memory, latency.
Slows Down APIs
 Response time increases drastically with data size.

Where It Happens (Java World)
- Hibernate / JPA lazy loading
- Improper entity relationships
- Fetching nested data without optimization

How to Fix It
Use JOIN FETCH in JPA
Use DTO projections
Apply batch fetching
Analyze queries with logs (hibernate.show_sql)

Pro Tip:
 If your API gets slower as data grows…
 It’s often not your logic - it’s your queries.

In backend systems, efficiency is not just about code - it’s about how you talk to your database.

Have you ever debugged an N+1 issue in production?