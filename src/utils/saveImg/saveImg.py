import os.path, os

def saveImg(img, path):
    try:
        img.save(path)
    except:
        raise TypeError('Erro ao salvar imagem')