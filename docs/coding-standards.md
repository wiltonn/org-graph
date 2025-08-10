# Coding Standards (Stack-tailored)

- TypeScript strict mode on, ES2022 targets.
- GraphQL: prefer schema-first (SDL). Keep resolvers pure; I/O in services.
- Neo4j: keep Cypher in tagged templates; avoid string concatenation.
- ClickHouse: WRITE via batched inserts; READ with LIMIT/OFFSET for dev, cursors for prod.
- Kafka: topic names kebab-case; include version suffix when schema changes (e.g., `events-user-v2`).
- Commits: Conventional Commits.
- Tests: lightweight unit tests + one integration test per endpoint.
