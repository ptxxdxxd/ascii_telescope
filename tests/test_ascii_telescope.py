"""Offline tests: no network, image sources are faked."""

import io

import numpy as np
import pytest
import requests
from PIL import Image

import ascii_telescope as at


def test_ascii_frame_has_the_configured_size():
    image = np.random.default_rng(0).random((300, 400), dtype=np.float32)
    lines = at.image_to_ascii(image).split("\n")
    assert len(lines) == at.HEIGHT
    assert all(len(line) == at.WIDTH for line in lines)


def test_dark_maps_to_space_and_bright_to_densest_char():
    image = np.zeros((100, 100), dtype=np.float32)
    image[:, 50:] = 255.0
    lines = at.image_to_ascii(image).split("\n")
    assert lines[0][0] == at.ASCII_CHARS[0]
    assert lines[0][-1] == at.ASCII_CHARS[-1]


def test_flat_image_renders_blank_instead_of_dividing_by_zero():
    image = np.full((50, 50), 7.0, dtype=np.float32)
    art = at.image_to_ascii(image)
    assert set(art.replace("\n", "")) == {at.ASCII_CHARS[0]}


class _FakeResponse:
    def __init__(self, content):
        self.content = content

    def raise_for_status(self):
        pass


def _png_bytes(width, height):
    buf = io.BytesIO()
    Image.new("RGB", (width, height), (200, 100, 50)).save(buf, format="PNG")
    return buf.getvalue()


def test_falls_back_to_next_source_and_crops_to_a_centred_square(monkeypatch):
    calls = []

    def fake_get(url, timeout, headers):
        calls.append(url)
        if len(calls) == 1:
            raise requests.ConnectionError("first source down")
        return _FakeResponse(_png_bytes(120, 80))

    monkeypatch.setattr(at.requests, "get", fake_get)
    result = at.fetch_latest_image()
    assert result is not None
    image, name = result
    assert name == at.SOURCES[1]["name"]
    assert image.shape == (80, 80)
    assert image.dtype == np.float32
    assert calls == [s["url"] for s in at.SOURCES[:2]]


def test_returns_none_when_every_source_fails(monkeypatch):
    def fake_get(url, timeout, headers):
        raise requests.Timeout("down")

    monkeypatch.setattr(at.requests, "get", fake_get)
    assert at.fetch_latest_image() is None


def test_corrupt_image_is_skipped(monkeypatch):
    responses = iter([b"not an image", _png_bytes(64, 64)])
    monkeypatch.setattr(at.requests, "get", lambda url, timeout, headers: _FakeResponse(next(responses)))
    image, name = at.fetch_latest_image()
    assert name == at.SOURCES[1]["name"]
    assert image.shape == (64, 64)
