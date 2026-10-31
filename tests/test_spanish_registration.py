"""Spanish metadata/annotation policy. Synthetic fixtures are never published."""
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import validate as v


def notes():
    return {"schemaVersion": 1, "id": "paquita-salas-s01e01-scene-01", "lines": [
        {"seg": 0, "trans": "Year.", "words": [{"t": "Año.", "lemma": "año", "stress": "ˈaɲo",
         "pos": "noun", "gloss": "year", "gram": "m sg"}]}], "lexicon": {"año": {
        "lemma": "año", "stress": "ˈaɲo", "pos": "noun", "gloss": "year", "gender": "m",
        "meanings": [{"en": "year", "note": ""}], "forms": {"title": "Forms", "columns": ["", "sg", "pl"],
        "rows": [{"cells": ["form", "año", "años"]}]}, "moreForms": [], "examples": [{"text": "Un año.", "trans": "One year."},
        {"text": "Dos años.", "trans": "Two years."}], "related": []}}}


def check(tmp_path, doc):
    file = tmp_path / "scene-01.notes.json"
    file.write_text(json.dumps(doc, ensure_ascii=False))
    rep = v.Report()
    v.check_notes(file, {"id": doc["id"], "segments": [{"v": "test", "t": "Año."}]}, "es", True, rep)
    return rep.errors


def test_real_spanish_identity_and_native_ipa_are_supported(tmp_path):
    assert v.SHOWS["paquita-salas"] == "es" and v.PAIR["es"] == "es-en"
    assert check(tmp_path, notes()) == []
    for farewell in ("¡Adiós!", "Hasta luego.", "Nos vemos."):
        assert v.FAREWELL["es"].search(farewell)
    rep = v.Report()
    v.target_ok("es", "¿Qué año es? ¡Hasta mañana!", "test", rep)
    assert rep.errors == []


@pytest.mark.parametrize("bad", [None, "[ˈaɲo]", "áño", "Aɲo", "aɲó"])
def test_every_spanish_word_requires_bare_ipa_not_russian_stress_or_spelling(tmp_path, bad):
    doc = notes()
    doc["lines"][0]["words"][0]["stress"] = bad
    assert check(tmp_path, doc)


def test_spanish_inflected_entries_require_written_forms(tmp_path):
    doc = notes()
    doc["lexicon"]["año"]["forms"] = None
    assert any("es noun/adj/verb needs a forms table" in error for error in check(tmp_path, doc))


def test_spanish_cannot_be_relabelled_as_french_or_use_cyrillic():
    rep = v.Report()
    v.target_ok("es", "Привет!", "test", rep)
    assert any("Cyrillic in Spanish" in error for error in rep.errors)
    script = {"pair": "es-en", "id": "paquita-salas-s01e01-scene-01"}
    schema = v.load_schema("script")
    properties = schema["properties"]
    assert not v.schema_errors(script["pair"], properties["pair"], schema)
    assert not v.schema_errors(script["id"], properties["id"], schema)
    assert not v.schema_errors("sources/paquita-salas/s01/e01.es.srt", properties["source"]["properties"]["file"], schema)
    assert v.schema_errors("invented-show-s01e01-scene-01", properties["id"], schema)
