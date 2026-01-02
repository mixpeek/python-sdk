from enum import Enum


class FaceIdentityExtractorParamsDetectionModel(str, Enum):
    SCRFD_10G = "scrfd_10g"
    SCRFD_2_5G = "scrfd_2.5g"
    SCRFD_500M = "scrfd_500m"

    def __str__(self) -> str:
        return str(self.value)
