"""Offline smoke test for exploratory corpus analysis."""

import runpy

import matplotlib.pyplot as plt


def test_corpus_has_token_and_context_features(monkeypatch, tmp_path):
    """Execute the full example against its built-in labeled corpus."""
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(plt, "show", lambda: plt.close("all"))

    result = runpy.run_module("nlp.nlp_corpus_explore", run_name="__main__")

    assert len(result["corpus"]) == 22
    assert set(result["top_per_category_dict"]) == {"dog", "cat", "car", "truck"}
    assert result["tokenize"]("The DOG, ran!") == ["the", "dog", "ran"]
    assert ("dog", "ran") in result["bigrams_list"]
    assert "ran" in result["co_occurrence_dict"]["dog"]
