from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.retriever_signal_metadata_type_0 import RetrieverSignalMetadataType0
    from ..models.retriever_signal_signal_data import RetrieverSignalSignalData


T = TypeVar("T", bound="RetrieverSignal")


@_attrs_define
class RetrieverSignal:
    """Single retriever signal event.

    Attributes:
        timestamp (datetime.datetime): Event timestamp
        execution_id (str): Execution identifier
        signal_type (str): Type of signal
        signal_data (RetrieverSignalSignalData): Signal-specific data
        metadata (None | RetrieverSignalMetadataType0 | Unset): Additional metadata
    """

    timestamp: datetime.datetime
    execution_id: str
    signal_type: str
    signal_data: RetrieverSignalSignalData
    metadata: None | RetrieverSignalMetadataType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.retriever_signal_metadata_type_0 import RetrieverSignalMetadataType0

        timestamp = self.timestamp.isoformat()

        execution_id = self.execution_id

        signal_type = self.signal_type

        signal_data = self.signal_data.to_dict()

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, RetrieverSignalMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "execution_id": execution_id,
                "signal_type": signal_type,
                "signal_data": signal_data,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.retriever_signal_metadata_type_0 import RetrieverSignalMetadataType0
        from ..models.retriever_signal_signal_data import RetrieverSignalSignalData

        d = dict(src_dict)
        timestamp = isoparse(d.pop("timestamp"))

        execution_id = d.pop("execution_id")

        signal_type = d.pop("signal_type")

        signal_data = RetrieverSignalSignalData.from_dict(d.pop("signal_data"))

        def _parse_metadata(data: object) -> None | RetrieverSignalMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = RetrieverSignalMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RetrieverSignalMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        retriever_signal = cls(
            timestamp=timestamp,
            execution_id=execution_id,
            signal_type=signal_type,
            signal_data=signal_data,
            metadata=metadata,
        )

        retriever_signal.additional_properties = d
        return retriever_signal

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
