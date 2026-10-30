import json,tempfile,unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import validate as v

class Metadata(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
  (self.root/'word-origins').mkdir()
 def tearDown(self):self.temp.cleanup()
 def put(self,doc):
  (self.root/'word-origins/ru-en.json').write_text(json.dumps(doc))
 def errors(self):
  report=v.Report();v.check_metadata(self.root,report);return report.errors
 def test_history_is_checked_without_requiring_audio_or_scenes(self):
  self.put({'schemaVersion':1,'pair':'ru-en','entries':{'он':{'etymology':'A history.','history':[{'stage':'Earlier','form':'x','meaning':'y'}]}}})
  self.assertEqual([],self.errors())
 def test_pair_must_match_filename(self):
  self.put({'schemaVersion':1,'pair':'fr-en','entries':{}})
  self.assertTrue(any('file name' in e for e in self.errors()))
 def test_unstructured_word_family_is_rejected(self):
  self.put({'schemaVersion':1,'pair':'ru-en','entries':{'он':{'etymology':'A history.','rootFamily':['x']}}})
  self.assertTrue(self.errors())
 def test_source_links_must_be_https(self):
  self.put({'schemaVersion':1,'pair':'ru-en','entries':{'он':{'etymology':'A history.','sources':[{'title':'Source','url':'javascript:alert(1)'}]}}})
  self.assertTrue(self.errors())
