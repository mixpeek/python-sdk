from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KMeansParams")


@_attrs_define
class KMeansParams:
    """Parameters for K-Means clustering algorithm.

    Attributes:
        n_clusters (int | Unset): Number of clusters to form Default: 8.
        max_iter (int | Unset): Maximum number of iterations Default: 300.
        random_state (int | None | Unset): Random seed for reproducibility Default: 42.
        n_init (int | Unset): Number of times k-means will run with different centroid seeds Default: 10.
        tol (float | Unset): Tolerance for convergence Default: 0.0001.
        init (str | Unset): Method for initialization ('k-means++' or 'random') Default: 'k-means++'.
        verbose (int | Unset): Verbosity mode Default: 0.
        copy_x (bool | Unset): If True, the original data is not modified Default: True.
        algorithm (str | Unset): K-means algorithm to use ('lloyd', 'elkan', or 'auto') Default: 'lloyd'.
    """

    n_clusters: int | Unset = 8
    max_iter: int | Unset = 300
    random_state: int | None | Unset = 42
    n_init: int | Unset = 10
    tol: float | Unset = 0.0001
    init: str | Unset = "k-means++"
    verbose: int | Unset = 0
    copy_x: bool | Unset = True
    algorithm: str | Unset = "lloyd"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        n_clusters = self.n_clusters

        max_iter = self.max_iter

        random_state: int | None | Unset
        if isinstance(self.random_state, Unset):
            random_state = UNSET
        else:
            random_state = self.random_state

        n_init = self.n_init

        tol = self.tol

        init = self.init

        verbose = self.verbose

        copy_x = self.copy_x

        algorithm = self.algorithm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if n_clusters is not UNSET:
            field_dict["n_clusters"] = n_clusters
        if max_iter is not UNSET:
            field_dict["max_iter"] = max_iter
        if random_state is not UNSET:
            field_dict["random_state"] = random_state
        if n_init is not UNSET:
            field_dict["n_init"] = n_init
        if tol is not UNSET:
            field_dict["tol"] = tol
        if init is not UNSET:
            field_dict["init"] = init
        if verbose is not UNSET:
            field_dict["verbose"] = verbose
        if copy_x is not UNSET:
            field_dict["copy_x"] = copy_x
        if algorithm is not UNSET:
            field_dict["algorithm"] = algorithm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        n_clusters = d.pop("n_clusters", UNSET)

        max_iter = d.pop("max_iter", UNSET)

        def _parse_random_state(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        random_state = _parse_random_state(d.pop("random_state", UNSET))

        n_init = d.pop("n_init", UNSET)

        tol = d.pop("tol", UNSET)

        init = d.pop("init", UNSET)

        verbose = d.pop("verbose", UNSET)

        copy_x = d.pop("copy_x", UNSET)

        algorithm = d.pop("algorithm", UNSET)

        k_means_params = cls(
            n_clusters=n_clusters,
            max_iter=max_iter,
            random_state=random_state,
            n_init=n_init,
            tol=tol,
            init=init,
            verbose=verbose,
            copy_x=copy_x,
            algorithm=algorithm,
        )

        k_means_params.additional_properties = d
        return k_means_params

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
