# PostProcessingPhase

Execution phases for post-processing applications.  Applications execute in phase order (lower = earlier). Within a phase, applications execute by priority (higher = earlier).  Phases:     TAXONOMY (1): Classification and labeling operations     CLUSTER (2): Grouping and clustering operations     ALERT (3): Notifications and alerts (default for alerts)  The default phase for each application type:     - TaxonomyApplicationConfig: TAXONOMY     - ClusterApplicationConfig: CLUSTER     - AlertApplicationConfig: ALERT  Users can override the phase via the `execution_phase` field to run applications in non-default order. For example, an alert can be configured to run in Phase 1 alongside taxonomies if early notification is needed.  Example:     # Default: Alert runs after taxonomies and clusters     AlertApplicationConfig(alert_id=\"alt_123\", execution_phase=PostProcessingPhase.ALERT)      # Override: Run alert early, in taxonomy phase     AlertApplicationConfig(alert_id=\"alt_urgent\", execution_phase=PostProcessingPhase.TAXONOMY)

## Enum

* `NUMBER_1` (value: `1`)

* `NUMBER_2` (value: `2`)

* `NUMBER_3` (value: `3`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


