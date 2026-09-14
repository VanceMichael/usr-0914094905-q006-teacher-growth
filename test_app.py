import os,tempfile,unittest
from app import init_db
class TestStore(unittest.TestCase):
 def test_init(self):
  with tempfile.TemporaryDirectory() as d:
   os.environ['DATABASE_PATH']=d+'/db'; init_db(); self.assertTrue(os.path.exists(d+'/db'))
