from jina import Executor, DocumentArray, requests, Document
from typing import Any, Dict, Optional, Sequence


def to_datauri(doc: Document):
    # the `convert_content_to_datauri` method doesn't work with tensors so have to do this
    if hasattr(doc, "tensor"):
        doc.convert_image_tensor_to_blob()
        doc.convert_content_to_datauri()
        doc.convert_blob_to_image_tensor()

    else:
        doc.convert_content_to_datauri()

    return doc


class ContentToDataURI(Executor):
    def __init__(self, traversal_paths: str = "@r", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.traversal_paths = traversal_paths

    @requests()
    def convert_to_datauri(
        self, docs: DocumentArray, parameters: Dict[str, Any], **kwargs
    ):
        traversal_paths = parameters.get("traversal_paths", self.traversal_paths)

        docs[traversal_paths].apply(to_datauri)
