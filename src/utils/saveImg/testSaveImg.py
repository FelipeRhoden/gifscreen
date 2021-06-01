import unittest, os.path, os
from PIL import ImageGrab
from .saveImg import save_img

class Testsave_img(unittest.TestCase):

    # Deveria Salvar uma imagem
    def test_save_img_save(self):
        img = ImageGrab.grab((0,0,500,500))
        path = 'img.png'
        save_img(img, path)
        exist = os.path.exists(path)
        if (exist) : 
            os.remove(path) 
        self.assertTrue(exist)
    
    # Deveria Salvar um subdiretorio
    def test_save_img_subdir(self):
        dirname = 'img'
        os.mkdir(dirname)
        img = ImageGrab.grab((0,0,500,500))
        path = 'img/img.png'
        save_img(img, path)
        exist = os.path.exists(path)
        if (exist) : 
            os.remove(path) 
            os.rmdir(dirname)
        self.assertTrue(exist)

    # Deveria Retornar um Erro ao Salvar uma imagem
    def test_save_img_except(self):
        img = ImageGrab.grab((0,0,500,500))
        path = 'img/img.png'
        path2 = 'img.ssd'
        with self.assertRaises(TypeError):
            save_img(img, path)
        with self.assertRaises(TypeError):
            save_img(img, path2)



if __name__ == '__main__':
    unittest.main()

        
