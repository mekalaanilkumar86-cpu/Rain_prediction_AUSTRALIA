import os

def test_required_files_exist():
  assert os.path.exists("requirements.txt")
  assert os.path.exists("app.py")
