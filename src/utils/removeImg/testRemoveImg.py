import unittest, os.path, os
from PIL import ImageGrab
from .removeImg import remove_img

class TestRemove_img(unittest.TestCase):

  # Deveria excluir uma imagem
  def test_remove_img_remove(self):
    img = ImageGrab.grab((0,0,500,500))
    path = "tmp.png"
    img.save(path)
    img.close()
    pathExists = os.path.exists(path)
    self.assertTrue(pathExists)
    remove_img(path)
    pathExists = os.path.exists(path)
    self.assertFalse(pathExists)

  #deveria excluir uma imagem em um subdiretório
  def test_remove_img_subdir(self):
        dirname = 'img'
        os.mkdir(dirname)
        img = ImageGrab.grab((0,0,500,500))
        path = 'img/img.png'
        img.save(path)
        exist = os.path.exists(path)
        self.assertTrue(exist)
        remove_img(path)
        exist = os.path.exists(path)
        self.assertFalse(exist)    
        os.rmdir(dirname)

  #deveria retornar um erro ao excluir uma imagem
  def test_remove_img_except(self):
        path = 'img/img.png'
        path2 = 'img.ssd'
        with self.assertRaises(TypeError):
            remove_img(path)
        with self.assertRaises(TypeError):
            remove_img(path2)

if __name__ == '__main__':
  unittest.main()