# StepKeySource

Defines how to extract the step key from documents for sequence analysis.  The step key identifies which stage/state a document is in for transition analytics.  Examples:     ASSIGNMENT_LABEL: Use the taxonomy's assigned label (e.g., \"inquiry\", \"proposal\")     ASSIGNMENT_NODE_ID: Use the taxonomy node ID (e.g., \"node_sales_inquiry\")     FIELD_PATH: Use a custom document field (e.g., \"metadata.workflow_stage\")

## Enum

* `ASSIGNMENT_LABEL` (value: `'assignment_label'`)

* `ASSIGNMENT_NODE_ID` (value: `'assignment_node_id'`)

* `FIELD_PATH` (value: `'field_path'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


