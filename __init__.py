from .node import *
from .install import *

NODE_CLASS_MAPPINGS = {
    'SAMModelLoader (segment anything plus)': SAMModelLoader,
    'GroundingDinoModelLoader (segment anything plus)': GroundingDinoModelLoader,
    'GroundingDinoSAMSegment (segment anything plus)': GroundingDinoSAMSegment,
    'InvertMask (segment anything plus)': InvertMask,
    "IsMaskEmpty  (segment anything plus)": IsMaskEmptyNode,
}

__all__ = ['NODE_CLASS_MAPPINGS']


