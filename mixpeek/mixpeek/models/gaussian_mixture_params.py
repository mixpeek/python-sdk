from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GaussianMixtureParams")


@_attrs_define
class GaussianMixtureParams:
    """Parameters for Gaussian Mixture Model clustering.

    Attributes:
        n_components (int | Unset): Number of mixture components Default: 1.
        covariance_type (str | Unset): Type of covariance parameters ('full', 'tied', 'diag', 'spherical') Default:
            'full'.
        tol (float | Unset): Convergence threshold Default: 0.001.
        reg_covar (float | Unset): Regularization added to the diagonal of covariance Default: 1e-06.
        max_iter (int | Unset): Maximum number of EM iterations Default: 100.
        n_init (int | Unset): Number of initializations to perform Default: 1.
        init_params (str | Unset): Method used to initialize weights, means and covariances ('kmeans' or 'random')
            Default: 'kmeans'.
        weights_init (list[Any] | None | Unset): Initial weights
        means_init (list[Any] | None | Unset): Initial means
        precisions_init (list[Any] | None | Unset): Initial precisions
        random_state (int | None | Unset): Random seed for reproducibility Default: 42.
        warm_start (bool | Unset): If True, use the solution of the last fit as initialization Default: False.
        verbose (int | Unset): Enable verbose output Default: 0.
        verbose_interval (int | Unset): Number of iterations between each verbose message Default: 10.
    """

    n_components: int | Unset = 1
    covariance_type: str | Unset = "full"
    tol: float | Unset = 0.001
    reg_covar: float | Unset = 1e-06
    max_iter: int | Unset = 100
    n_init: int | Unset = 1
    init_params: str | Unset = "kmeans"
    weights_init: list[Any] | None | Unset = UNSET
    means_init: list[Any] | None | Unset = UNSET
    precisions_init: list[Any] | None | Unset = UNSET
    random_state: int | None | Unset = 42
    warm_start: bool | Unset = False
    verbose: int | Unset = 0
    verbose_interval: int | Unset = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        n_components = self.n_components

        covariance_type = self.covariance_type

        tol = self.tol

        reg_covar = self.reg_covar

        max_iter = self.max_iter

        n_init = self.n_init

        init_params = self.init_params

        weights_init: list[Any] | None | Unset
        if isinstance(self.weights_init, Unset):
            weights_init = UNSET
        elif isinstance(self.weights_init, list):
            weights_init = self.weights_init

        else:
            weights_init = self.weights_init

        means_init: list[Any] | None | Unset
        if isinstance(self.means_init, Unset):
            means_init = UNSET
        elif isinstance(self.means_init, list):
            means_init = self.means_init

        else:
            means_init = self.means_init

        precisions_init: list[Any] | None | Unset
        if isinstance(self.precisions_init, Unset):
            precisions_init = UNSET
        elif isinstance(self.precisions_init, list):
            precisions_init = self.precisions_init

        else:
            precisions_init = self.precisions_init

        random_state: int | None | Unset
        if isinstance(self.random_state, Unset):
            random_state = UNSET
        else:
            random_state = self.random_state

        warm_start = self.warm_start

        verbose = self.verbose

        verbose_interval = self.verbose_interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if n_components is not UNSET:
            field_dict["n_components"] = n_components
        if covariance_type is not UNSET:
            field_dict["covariance_type"] = covariance_type
        if tol is not UNSET:
            field_dict["tol"] = tol
        if reg_covar is not UNSET:
            field_dict["reg_covar"] = reg_covar
        if max_iter is not UNSET:
            field_dict["max_iter"] = max_iter
        if n_init is not UNSET:
            field_dict["n_init"] = n_init
        if init_params is not UNSET:
            field_dict["init_params"] = init_params
        if weights_init is not UNSET:
            field_dict["weights_init"] = weights_init
        if means_init is not UNSET:
            field_dict["means_init"] = means_init
        if precisions_init is not UNSET:
            field_dict["precisions_init"] = precisions_init
        if random_state is not UNSET:
            field_dict["random_state"] = random_state
        if warm_start is not UNSET:
            field_dict["warm_start"] = warm_start
        if verbose is not UNSET:
            field_dict["verbose"] = verbose
        if verbose_interval is not UNSET:
            field_dict["verbose_interval"] = verbose_interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        n_components = d.pop("n_components", UNSET)

        covariance_type = d.pop("covariance_type", UNSET)

        tol = d.pop("tol", UNSET)

        reg_covar = d.pop("reg_covar", UNSET)

        max_iter = d.pop("max_iter", UNSET)

        n_init = d.pop("n_init", UNSET)

        init_params = d.pop("init_params", UNSET)

        def _parse_weights_init(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                weights_init_type_0 = cast(list[Any], data)

                return weights_init_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        weights_init = _parse_weights_init(d.pop("weights_init", UNSET))

        def _parse_means_init(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                means_init_type_0 = cast(list[Any], data)

                return means_init_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        means_init = _parse_means_init(d.pop("means_init", UNSET))

        def _parse_precisions_init(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                precisions_init_type_0 = cast(list[Any], data)

                return precisions_init_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        precisions_init = _parse_precisions_init(d.pop("precisions_init", UNSET))

        def _parse_random_state(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        random_state = _parse_random_state(d.pop("random_state", UNSET))

        warm_start = d.pop("warm_start", UNSET)

        verbose = d.pop("verbose", UNSET)

        verbose_interval = d.pop("verbose_interval", UNSET)

        gaussian_mixture_params = cls(
            n_components=n_components,
            covariance_type=covariance_type,
            tol=tol,
            reg_covar=reg_covar,
            max_iter=max_iter,
            n_init=n_init,
            init_params=init_params,
            weights_init=weights_init,
            means_init=means_init,
            precisions_init=precisions_init,
            random_state=random_state,
            warm_start=warm_start,
            verbose=verbose,
            verbose_interval=verbose_interval,
        )

        gaussian_mixture_params.additional_properties = d
        return gaussian_mixture_params

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
