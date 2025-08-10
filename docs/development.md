# Development Guide

## Prerequisites

- Node.js 20+
- Python 3.11+
- Docker & Docker Compose
- pnpm

## Setup

### 1. Install Dependencies
```bash
pnpm install
```

### 2. Start Infrastructure
```bash
docker-compose up -d
```

This starts:
- Neo4j (7474 web, 7687 bolt)
- ClickHouse (8123 HTTP)
- Kafka (9092 broker)

### 3. Initialize Database
```bash
python tools/prep.py
```

### 4. Run Development Servers
```bash
# API server
pnpm --filter @org-graph/server dev

# Web frontend (separate terminal)
pnpm --filter @org-graph/web dev
```

## Workflow

### Two-Track Development

1. **Feature Track**: Implementation in `/packages`
2. **Planning Track**: Design in `/docs`, `/promptpacks`

### Creating Tasks

1. Add ticket to `/tickets/T-YYYY-XXX/`
2. Create prompt in `/promptpacks/`
3. Implement using tools in `/tools/`
4. Update docs in `/docs/`

## Testing

```bash
# Run all tests
pnpm test

# Run specific package tests
pnpm --filter @org-graph/server test
```