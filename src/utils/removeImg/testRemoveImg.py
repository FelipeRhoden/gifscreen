import unittest, os.path, os
from PIL import ImageGrab
from .removeImg import remove_img

class TestRemove_img(unittest.TestCase):

  # Deveria excluir uma imagem
  def test_remove_img_remove(self):
    img = ImageGrab.grab((0,0,500,500))
    imgName = "tmp.png"
    img.save(imgName)
    img.close()
    pathExists = os.path.exists(imgName)
    self.assertTrue(pathExists)
    remove_img(imgName)
    pathExists = os.path.exists(imgName)
    self.assertFalse(pathExists)

if __name__ == '__main__':
  unittest.main()