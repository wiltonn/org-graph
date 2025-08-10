#!/usr/bin/env python3
"""
Database initialization tool for org-graph.
Sets up Neo4j schema and sample data.
"""

import os
import sys
from neo4j import GraphDatabase
from typing import Any, Dict

# Connection settings
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")


def create_constraints(tx: Any) -> None:
    """Create database constraints and indexes."""
    constraints = [
        "CREATE CONSTRAINT IF NOT EXISTS FOR (c:Customer) REQUIRE c.id IS UNIQUE",
        "CREATE CONSTRAINT IF NOT EXISTS FOR (o:Organization) REQUIRE o.id IS UNIQUE",
        "CREATE INDEX IF NOT EXISTS FOR (c:Customer) ON (c.name)",
        "CREATE INDEX IF NOT EXISTS FOR (o:Organization) ON (o.name)",
    ]
    
    for constraint in constraints:
        tx.run(constraint)
        print(f"✓ {constraint[:50]}...")


def create_sample_data(tx: Any) -> None:
    """Create sample customer and organization data."""
    # Clear existing data
    tx.run("MATCH (n) DETACH DELETE n")
    
    # Create organizations
    orgs = [
        {"id": "org-1", "name": "Acme Corp"},
        {"id": "org-2", "name": "TechStart Inc"},
        {"id": "org-3", "name": "Global Systems"},
    ]
    
    for org in orgs:
        tx.run(
            "CREATE (o:Organization {id: $id, name: $name})",
            **org
        )
    
    # Create customers
    customers = [
        {"id": "cust-1", "name": "Alice Johnson", "org_id": "org-1"},
        {"id": "cust-2", "name": "Bob Smith", "org_id": "org-1"},
        {"id": "cust-3", "name": "Carol White", "org_id": "org-2"},
        {"id": "cust-4", "name": "David Brown", "org_id": "org-3"},
        {"id": "cust-5", "name": "Eve Davis", "org_id": "org-3"},
    ]
    
    for customer in customers:
        tx.run(
            """
            CREATE (c:Customer {id: $id, name: $name})
            WITH c
            MATCH (o:Organization {id: $org_id})
            CREATE (c)-[:BELONGS_TO]->(o)
            """,
            **customer
        )
    
    print(f"✓ Created {len(orgs)} organizations")
    print(f"✓ Created {len(customers)} customers")


def main() -> int:
    """Initialize Neo4j database."""
    print(f"Connecting to Neo4j at {NEO4J_URI}...")
    
    try:
        driver = GraphDatabase.driver(
            NEO4J_URI,
            auth=(NEO4J_USER, NEO4J_PASSWORD)
        )
        
        with driver.session() as session:
            # Create constraints
            session.execute_write(create_constraints)
            
            # Create sample data
            session.execute_write(create_sample_data)
            
            # Verify data
            result = session.run(
                "MATCH (c:Customer)-[:BELONGS_TO]->(o:Organization) "
                "RETURN count(c) as customer_count, count(distinct o) as org_count"
            )
            record = result.single()
            print(f"\n✅ Database initialized successfully!")
            print(f"   Customers: {record['customer_count']}")
            print(f"   Organizations: {record['org_count']}")
        
        driver.close()
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())