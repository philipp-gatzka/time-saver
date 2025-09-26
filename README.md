# Timesaver

<!-- TOC -->
* [Timesaver](#timesaver)
  * [Version Matrix](#version-matrix)
  * [Rationale](#rationale)
  * [Local Build](#local-build)
<!-- TOC -->

## Version Matrix

| Name                     | Version |
|--------------------------|---------|
| Java                     | 21      |
| Spring Boot              | 3.5.5   |
| Vaadin (UI)              | 24.9.0  |
| JPA Provider (Hibernate) | 6.5.x   |
| PostgreSQL JDBC Driver   | 42.7.x  |

## Rationale

- Java 21: current LTS with modern language/runtime features and broad ecosystem support.
- Spring Boot 3.5.5: compatible with Java 21 and recent dependency stack.
- Vaadin 24.9.0: stable Long-Term Maintenance line compatible with Java 21.
- Hibernate 6.5.x: aligns with Spring Boot 3.5 and Jakarta Persistence 3.1.
- PostgreSQL JDBC 42.7.x: current stable driver with performance and protocol improvements.

## Local Build

- Prerequisite: Java 21 installed and active (java -version should report 21).
- Build: use your build tool’s standard build command to compile and run tests.