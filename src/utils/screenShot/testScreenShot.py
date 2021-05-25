from screenShot import screen_shot
import unittest

class TestScreenShot(unittest.TestCase):


    # Deveria retornar uma item do tipo Imagem
    def test_sreen_shot_type(self):
        equal = "<class 'PIL.Image.Image'>"
        img = screen_shot()
        typeImg = f'{type(img)}'
        self.assertEqual(typeImg, equal)
        

    # Deveria retornar uma imagem com altura de 600 pixel e largura de 500 pixel
    def test_screen_shot_width_height(self):
        equalW = 500
        equalH = 600
        img = screen_shot([0,0,equalW, equalH])
        width, height = img.size
        self.assertEqual(width, equalW)
        self.assertEqual(height, equalH)
        

    # deveria retornar uma imagem com altura de 600 pixel e largura de 500 pixel
    # com 50 pixel a cima e 60 pixel na esquerda   
    def test_screen_shot_top_lef(self):
        equalW = 500
        equalH = 600
        left = 60
        top = 50
        img = screen_shot((left,top,equalW, equalH))
        width, height = img.size
        self.assertEqual(width, equalW)
        self.assertEqual(height, equalH)
    
    # deveria retornar um imagem da tela mesmo inteira 
    # mesmo sem enviar os parametros certos
    def test_screen_shot_except(self):
        left = 60
        top = 50
        equal = "<class 'PIL.Image.Image'>"
        img = screen_shot((left,top))
        typeImg = f'{type(img)}'
        self.assertEqual(typeImg, equal)
        img = screen_shot('test')
        typeImg = f'{type(img)}'
        self.assertEqual(typeImg, equal)

if __name__ == '__main__':
    unittest.main()