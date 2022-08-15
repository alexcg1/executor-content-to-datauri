from executor import ContentToDataURI
from docarray import Document, DocumentArray

exec = ContentToDataURI()

image_doc = Document(uri="idris.jpg")
image_doc.load_uri_to_image_tensor()

docs = DocumentArray(
    [
        image_doc
    ]
)

exec.convert_to_datauri(docs, parameters={})

print(docs)

print(image_doc.uri)
