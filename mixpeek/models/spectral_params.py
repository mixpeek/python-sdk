from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.spectral_params_kernel_params_type_0 import SpectralParamsKernelParamsType0


T = TypeVar("T", bound="SpectralParams")


@_attrs_define
class SpectralParams:
    """Parameters for Spectral clustering algorithm.

    Attributes:
        n_clusters (int | Unset): Number of clusters to form Default: 8.
        eigen_solver (None | str | Unset): The eigenvalue decomposition strategy ('arpack', 'lobpcg', 'amg', or None)
        n_components (int | None | Unset): Number of eigenvectors to use for spectral embedding
        random_state (int | None | Unset): Random seed for reproducibility Default: 42.
        n_init (int | Unset): Number of times k-means will run with different centroid seeds Default: 10.
        gamma (float | Unset): Kernel coefficient for rbf, poly, sigmoid, laplacian and chi2 kernels Default: 1.0.
        affinity (str | Unset): How to construct the affinity matrix ('nearest_neighbors', 'rbf', 'precomputed',
            'precomputed_nearest_neighbors') Default: 'rbf'.
        n_neighbors (int | Unset): Number of neighbors to use when constructing the affinity matrix using nearest
            neighbors Default: 10.
        eigen_tol (float | Unset): Stopping criterion for eigendecomposition Default: 0.0.
        assign_labels (str | Unset): Strategy to assign labels in the embedding space ('kmeans' or 'discretize')
            Default: 'kmeans'.
        degree (float | Unset): Degree of the polynomial kernel. Ignored by other kernels Default: 3.0.
        coef0 (float | Unset): Zero coefficient for polynomial and sigmoid kernels Default: 1.0.
        kernel_params (None | SpectralParamsKernelParamsType0 | Unset): Parameters for the kernel function
        n_jobs (int | Unset): Number of parallel jobs to run (-1 means using all processors) Default: 1.
        verbose (bool | Unset): Verbosity mode Default: False.
    """

    n_clusters: int | Unset = 8
    eigen_solver: None | str | Unset = UNSET
    n_components: int | None | Unset = UNSET
    random_state: int | None | Unset = 42
    n_init: int | Unset = 10
    gamma: float | Unset = 1.0
    affinity: str | Unset = "rbf"
    n_neighbors: int | Unset = 10
    eigen_tol: float | Unset = 0.0
    assign_labels: str | Unset = "kmeans"
    degree: float | Unset = 3.0
    coef0: float | Unset = 1.0
    kernel_params: None | SpectralParamsKernelParamsType0 | Unset = UNSET
    n_jobs: int | Unset = 1
    verbose: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.spectral_params_kernel_params_type_0 import SpectralParamsKernelParamsType0

        n_clusters = self.n_clusters

        eigen_solver: None | str | Unset
        if isinstance(self.eigen_solver, Unset):
            eigen_solver = UNSET
        else:
            eigen_solver = self.eigen_solver

        n_components: int | None | Unset
        if isinstance(self.n_components, Unset):
            n_components = UNSET
        else:
            n_components = self.n_components

        random_state: int | None | Unset
        if isinstance(self.random_state, Unset):
            random_state = UNSET
        else:
            random_state = self.random_state

        n_init = self.n_init

        gamma = self.gamma

        affinity = self.affinity

        n_neighbors = self.n_neighbors

        eigen_tol = self.eigen_tol

        assign_labels = self.assign_labels

        degree = self.degree

        coef0 = self.coef0

        kernel_params: dict[str, Any] | None | Unset
        if isinstance(self.kernel_params, Unset):
            kernel_params = UNSET
        elif isinstance(self.kernel_params, SpectralParamsKernelParamsType0):
            kernel_params = self.kernel_params.to_dict()
        else:
            kernel_params = self.kernel_params

        n_jobs = self.n_jobs

        verbose = self.verbose

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if n_clusters is not UNSET:
            field_dict["n_clusters"] = n_clusters
        if eigen_solver is not UNSET:
            field_dict["eigen_solver"] = eigen_solver
        if n_components is not UNSET:
            field_dict["n_components"] = n_components
        if random_state is not UNSET:
            field_dict["random_state"] = random_state
        if n_init is not UNSET:
            field_dict["n_init"] = n_init
        if gamma is not UNSET:
            field_dict["gamma"] = gamma
        if affinity is not UNSET:
            field_dict["affinity"] = affinity
        if n_neighbors is not UNSET:
            field_dict["n_neighbors"] = n_neighbors
        if eigen_tol is not UNSET:
            field_dict["eigen_tol"] = eigen_tol
        if assign_labels is not UNSET:
            field_dict["assign_labels"] = assign_labels
        if degree is not UNSET:
            field_dict["degree"] = degree
        if coef0 is not UNSET:
            field_dict["coef0"] = coef0
        if kernel_params is not UNSET:
            field_dict["kernel_params"] = kernel_params
        if n_jobs is not UNSET:
            field_dict["n_jobs"] = n_jobs
        if verbose is not UNSET:
            field_dict["verbose"] = verbose

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spectral_params_kernel_params_type_0 import SpectralParamsKernelParamsType0

        d = dict(src_dict)
        n_clusters = d.pop("n_clusters", UNSET)

        def _parse_eigen_solver(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        eigen_solver = _parse_eigen_solver(d.pop("eigen_solver", UNSET))

        def _parse_n_components(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        n_components = _parse_n_components(d.pop("n_components", UNSET))

        def _parse_random_state(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        random_state = _parse_random_state(d.pop("random_state", UNSET))

        n_init = d.pop("n_init", UNSET)

        gamma = d.pop("gamma", UNSET)

        affinity = d.pop("affinity", UNSET)

        n_neighbors = d.pop("n_neighbors", UNSET)

        eigen_tol = d.pop("eigen_tol", UNSET)

        assign_labels = d.pop("assign_labels", UNSET)

        degree = d.pop("degree", UNSET)

        coef0 = d.pop("coef0", UNSET)

        def _parse_kernel_params(data: object) -> None | SpectralParamsKernelParamsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                kernel_params_type_0 = SpectralParamsKernelParamsType0.from_dict(data)

                return kernel_params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SpectralParamsKernelParamsType0 | Unset, data)

        kernel_params = _parse_kernel_params(d.pop("kernel_params", UNSET))

        n_jobs = d.pop("n_jobs", UNSET)

        verbose = d.pop("verbose", UNSET)

        spectral_params = cls(
            n_clusters=n_clusters,
            eigen_solver=eigen_solver,
            n_components=n_components,
            random_state=random_state,
            n_init=n_init,
            gamma=gamma,
            affinity=affinity,
            n_neighbors=n_neighbors,
            eigen_tol=eigen_tol,
            assign_labels=assign_labels,
            degree=degree,
            coef0=coef0,
            kernel_params=kernel_params,
            n_jobs=n_jobs,
            verbose=verbose,
        )

        spectral_params.additional_properties = d
        return spectral_params

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
