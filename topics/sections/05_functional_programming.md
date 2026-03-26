<!-- Part of Java Learning Roadmap — Section 5 -->

## ⚡ 6. Functional Programming in Java

- Lambda Expressions — `(params) -> expression`
- **Functional Interfaces** (`@FunctionalInterface`)
  - `Predicate<T>` — `test()`, `and()`, `or()`, `negate()`
  - `Function<T,R>` — `apply()`, `andThen()`, `compose()`
  - `Consumer<T>` — `accept()`, `andThen()`
  - `Supplier<T>` — `get()`
  - `BiFunction<T,U,R>`, `BinaryOperator<T>`, `UnaryOperator<T>`
- **Streams API**
  - Creating: `stream()`, `parallelStream()`, `Stream.of()`, `Stream.iterate()`
  - Intermediate: `filter()`, `map()`, `flatMap()`, `sorted()`, `distinct()`, `limit()`, `skip()`, `peek()`
  - Terminal: `collect()`, `forEach()`, `reduce()`, `count()`, `findFirst()`, `findAny()`, `anyMatch()`, `allMatch()`, `noneMatch()`
  - **Collectors**: `toList()`, `toSet()`, `toMap()`, `groupingBy()`, `partitioningBy()`, `joining()`, `counting()`, `collectingAndThen()`
  - Parallel Streams — pitfalls with shared mutable state
- **`Optional<T>`**
  - `of()`, `ofNullable()`, `empty()`
  - `isPresent()`, `isEmpty()`, `ifPresent()`, `orElse()`, `orElseGet()`, `orElseThrow()`, `map()`, `flatMap()`
- Method References — `Class::method`, `obj::method`, `Class::new`
- Default & Static Interface Methods

---
