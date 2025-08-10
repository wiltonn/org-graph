TASK-ID: {{ticket_id}}
GOAL: {{one_sentence_goal}}

STACK:
- API: Node 20 + TypeScript + GraphQL Yoga
- DBs: Neo4j 5 (bolt), ClickHouse 24 (HTTP)
- Events: Kafka (kafkajs)
- Web: React + Vite

PATHS (allowed to edit):
{{paths_list}}

CONSTRAINTS:
{{constraints_bullets}}

CHANGE PLAN (follow strictly):
{{changeplan_steps}}

TESTS TO UPDATE/ADD:
{{test_items}}

RELEVANT CONTEXT (line-range slices):
{{inline_slices}}

When you need more context, ask for a single additional slice specifying exact file and line range.
Produce: (1) unified diffs, (2) new files in full, (3) a <120-word rationale.
