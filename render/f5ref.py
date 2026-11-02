"""Reference-prompt helpers for the English F5 engine (pure Python: unit-testable without torch)."""


def ref_text_for_f5(text):
    """The F5 api convention: the reference text ends with '. ' (or the sentence's own end mark plus a space)."""
    t = text.strip()
    if t.endswith((".", "!", "?")):
        return t + " "
    return t + ". "


def trim_plan(cfg, voice, total_seconds, text):
    """-> (seconds_to_keep, ref_text) for a voice. No refTrim entry = the whole clip with its full text."""
    tr = (cfg.get("refTrim") or {}).get(voice)
    if not tr:
        return total_seconds, text
    return min(float(tr["seconds"]), total_seconds), tr["text"]
