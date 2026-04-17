import pytest
from src.tools.search_tool import search


def test_search():
    result = search("华为手机")
    assert "华为手机" in result


def test_search_empty():
    result = search("")
    assert result is not None
