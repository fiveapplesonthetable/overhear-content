"""Offline adapter contracts only: no model/GPU is initialized by these tests."""
from pathlib import Path
from types import SimpleNamespace
import numpy as np
import pytest

import chatterbox_ar
import config
import plan


def test_arabic_cache_signature_is_independent_and_does_not_invalidate_other_sentences():
    settings=config.load_settings(); original={lang:plan.cache_key(settings,'voice','reference',lang,'text') for lang in ['ru','en','fr','ja']}
    settings['ttsAr']={'model':'chatterbox-multilingual-v2','modelLocal':'/private/model','temperature':.6}
    for lang,key in original.items(): assert key==plan.cache_key(settings,'voice','reference',lang,'text')
    first=plan.cache_key(settings,'voice','reference','ar','نعم.')
    settings['ttsAr']['temperature']=.7
    assert first!=plan.cache_key(settings,'voice','reference','ar','نعم.')
    assert config.engine_label(settings,'ar')=='chatterbox-multilingual-v2'


def test_checkpoint_requires_complete_existing_local_snapshot(tmp_path):
    with pytest.raises(ValueError,match='downloading is disabled'):
        chatterbox_ar.checkpoint({'ttsAr':{'modelLocal':str(tmp_path)}})
    for name in chatterbox_ar.REQUIRED_FILES:(tmp_path/name).write_bytes(b'unit fixture, never loaded')
    assert chatterbox_ar.checkpoint({'ttsAr':{'modelLocal':str(tmp_path)}})==tmp_path


def test_native_arabic_generation_passes_real_reference_without_padding(tmp_path):
    reference=tmp_path/'reference.wav';reference.write_bytes(b'fake test signal; no synthesis')
    calls=[]
    class Tensor:
        def detach(self):return self
        def cpu(self):return self
        def numpy(self):return np.ones((1,240),dtype=np.float32)*.1
    class Model:
        sr=24000
        def generate(self,**kwargs):calls.append(kwargs);return Tensor()
    engine=object.__new__(chatterbox_ar.ChatterboxArEngine)
    engine.s={'ttsAr':{'temperature':.65,'cfg_weight':.35,'exaggeration':.4}}
    engine.torch=SimpleNamespace(manual_seed=lambda _:None)
    engine.voices=SimpleNamespace(lang_of=lambda _:'ar',ref_path=lambda _:reference)
    engine.q=Model()
    result=engine.generate([('reviewed-saudi-voice','ar','يعني قصدي.')],seed=11)
    assert len(result)==1 and result[0].shape==(240,)
    assert calls==[{'text':'يعني قصدي.','language_id':'ar','audio_prompt_path':str(reference),
                   'temperature':.65,'cfg_weight':.35,'exaggeration':.4,'repetition_penalty':2.0,'min_p':.05,'top_p':1.0}]
    with pytest.raises(ValueError):engine.generate([('voice','Japanese','text')],seed=11)
