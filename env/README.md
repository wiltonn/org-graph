# Environment Configuration

This directory contains environment configuration templates.

## Setup

1. Copy `.env.example` to `.env` in the root directory:
   ```bash
   cp env/.env.example .env
   ```

2. Update values in `.env` with your local settings

## Variables

### Database Connections
- `NEO4J_*`: Neo4j graph database settings
- `CLICKHOUSE_*`: ClickHouse analytics database settings
- `KAFKA_*`: Kafka event streaming settings

### Application
- `PORT`: API server port (default: 4000)
- `NODE_ENV`: Environment mode (development/production)
- `VITE_API_URL`: Frontend API endpoint

## Security

- Never commit `.env` files with real credentials
- Use environment-specific secrets management in production
- Rotate credentials regularly