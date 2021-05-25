from screenShot import screen_shot
import importlib
import unittest

class TestScreenShot(unittest.TestCase):


    # Deveria retornar uma item do tipo Imagem
    def test_sreen_shot_type(self):
        EQUAL = "<class 'PIL.Image.Image'>"
        IMG = screen_shot()
        TYPE = f'{type(IMG)}'
        self.assertEqual(TYPE, EQUAL)
        

    # Deveria retornar uma imagem com altura de 600 pixel e largura de 500 pixel
    def test_screen_shot_width_height(self):
        EQUALW = 500
        EQUALH = 600
        IMG = screen_shot([0,0,EQUALW, EQUALH])
        WIDTH, HEIGHT = IMG.size
        self.assertEqual(WIDTH, EQUALW)
        self.assertEqual(HEIGHT, EQUALH)
        

    # deveria retornar uma imagem com altura de 600 pixel e largura de 500 pixel
    # com 50 pixel a cima e 60 pixel na esquerda   
    def test_screen_shot_top_lef(self):
        EQUALW = 500
        EQUALH = 600
        LEFT = 60
        TOP = 50
        IMG = screen_shot((LEFT,TOP,EQUALW, EQUALH))
        WIDTH, HEIGHT = IMG.size
        self.assertEqual(WIDTH, EQUALW)
        self.assertEqual(HEIGHT, EQUALH)
        

if __name__ == '__main__':
    unittest.main()