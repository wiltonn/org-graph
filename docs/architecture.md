# Architecture Overview

## Stack Components

### API Layer
- **GraphQL Yoga**: HTTP server and GraphQL endpoint
- **Node.js 20 + TypeScript**: Runtime and type safety

### Data Storage
- **Neo4j 5**: Graph database for customer relationships (bolt://localhost:7687)
- **ClickHouse 24**: Analytics database for metrics (http://localhost:8123)

### Event Streaming
- **Kafka**: Event bus for audit and system events (localhost:9092)

### Web Frontend
- **React + Vite**: Modern frontend with fast HMR

## Data Flow

1. **Client Request** → GraphQL API
2. **API** → Neo4j (customer data queries)
3. **API** → Kafka (audit events)
4. **Kafka** → ClickHouse (analytics ingestion)
5. **API Response** → Client

## Project Structure

```
org-graph/
├── packages/
│   ├── server/     # GraphQL API server
│   └── web/        # React frontend
├── docs/           # Documentation
├── tickets/        # Task tracking
├── promptpacks/    # AI prompts and patterns
├── tools/          # Python utilities
└── env/            # Environment configs
```