'''
@function save_img
@description Função que salva uma imagem do tipo pillow
@params {Image} img
@params {String} path
@return void
'''

def save_img(img, path):
    try:
        img.save(path)
    except:
        raise TypeError('Erro ao salvar imagem')