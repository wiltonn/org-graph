# API Endpoint Implementation Template

## Context
- **Endpoint**: `[ENDPOINT_NAME]`
- **Method**: `[QUERY/MUTATION]`
- **Purpose**: `[DESCRIPTION]`

## Requirements
- [ ] Input validation
- [ ] Authorization check
- [ ] Neo4j query
- [ ] Kafka event emission
- [ ] Error handling
- [ ] Response formatting

## Schema Definition
```graphql
type [Type] {
  # fields
}

type Query/Mutation {
  [endpoint](args): [ReturnType]
}
```

## Implementation Checklist
1. Add GraphQL type definitions
2. Create resolver function
3. Implement Neo4j query logic
4. Add Kafka audit event
5. Handle errors gracefully
6. Add unit tests
7. Update API documentation