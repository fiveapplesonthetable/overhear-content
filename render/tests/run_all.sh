#!/bin/sh
# Pure tests with system python; audio, TTS-import and uroman tests need venv-qwen, so run again with the Qwen venv (pytest borrowed from system dist-packages, appended last).
cd "$(dirname "$0")/.." || exit 1
python3 -m pytest -q tests --ignore=tests/test_audio.py --ignore=tests/test_narrator.py --ignore=tests/test_chatterbox_ar.py --ignore=tests/test_portuguese_routing.py --ignore=tests/test_native_text.py "$@"
${OVERHEAR_HOME:-$HOME/overhear}/venv-qwen/bin/python -I -c "
import sys; sys.path.append('$(python3 -c 'import pytest,os;print(os.path.dirname(os.path.dirname(pytest.__file__)))')'); sys.path.insert(0,'.')
import pytest; sys.exit(pytest.main(['-q','tests/test_audio.py','tests/test_narrator.py','tests/test_chatterbox_ar.py','tests/test_portuguese_routing.py','tests/test_native_text.py','-p','no:cacheprovider']))"
