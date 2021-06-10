import unittest, os.path, os
from PIL import ImageGrab

class TestRemove_img(unittest.TestCase):

  # Deveria excluir uma imagem
  def test_remove_img_remove(self):
    img = ImageGrab.grab((0,0,500,500))
    imgName = "tmp.png"
    img.save(imgName)
