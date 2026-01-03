# ClusteringAlgorithm

Supported clustering algorithms.  Two types of clustering are available: 1. Vector-based: Clusters documents by embedding similarity 2. Attribute-based: Clusters documents by metadata attributes  Vector-based algorithms (require feature_vector):     - kmeans: Partitions data into K clusters by minimizing within-cluster variance     - dbscan: Density-based clustering, finds clusters of arbitrary shape     - hdbscan: Hierarchical DBSCAN, auto-determines number of clusters     - agglomerative: Hierarchical clustering using linkage criteria     - spectral: Uses graph theory to find clusters     - gaussian_mixture: Probabilistic model assuming Gaussian distributions     - mean_shift: Finds clusters by locating density maxima     - optics: Ordering points to identify clustering structure  Attribute-based algorithm (requires attribute_config):     - attribute_based: Groups documents by metadata attributes (e.g., category, brand)

## Enum

* `KMEANS` (value: `'kmeans'`)

* `DBSCAN` (value: `'dbscan'`)

* `HDBSCAN` (value: `'hdbscan'`)

* `AGGLOMERATIVE` (value: `'agglomerative'`)

* `SPECTRAL` (value: `'spectral'`)

* `GAUSSIAN_MIXTURE` (value: `'gaussian_mixture'`)

* `MEAN_SHIFT` (value: `'mean_shift'`)

* `OPTICS` (value: `'optics'`)

* `ATTRIBUTE_BASED` (value: `'attribute_based'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


