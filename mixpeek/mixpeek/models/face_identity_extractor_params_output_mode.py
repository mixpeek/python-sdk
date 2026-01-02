from enum import Enum


class FaceIdentityExtractorParamsOutputMode(str, Enum):
    PER_FACE = "per_face"
    PER_IMAGE = "per_image"

    def __str__(self) -> str:
        return str(self.value)
