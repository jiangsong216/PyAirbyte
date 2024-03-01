# Copyright (c) 2024 Airbyte, Inc., all rights reserved.
"""Methods for converting Airbyte records into documents."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pydantic import BaseModel


if TYPE_CHECKING:
    import datetime


MAX_SINGLE_LINE_LENGTH = 60
AIRBYTE_DOCUMENT_RENDERING = "airbyte_document_rendering"
TITLE_PROPERTY = "title_property"
CONTENT_PROPS = "content_properties"
METADATA_PROPERTIES = "metadata_properties"


class Document(BaseModel):
    """A PyAirbyte document is a specific projection on top of a record.

    Documents have the following structure:
    - id (str): A unique string identifier for the document.
    - content (str): A string representing the record when rendered as a document.
    - metadata (dict[str, Any]): Associated metadata about the document, such as the record's IDs
      and/or URLs.

    This class is duck-typed to be compatible with LangChain project's `Document` class.
    """

    id: str | None = None
    content: str
    metadata: dict[str, Any]
    last_modified: datetime.datetime | None = None

    def __str__(self) -> str:
        return self.content

    @property
    def page_content(self) -> str:
        """Return the content of the document.

        This is an alias for the `content` property, and is provided for duck-type compatibility
        with the LangChain project's `Document` class.
        """
        return self.content