import os

'''
@function remove_img
@description Função que realiza a remoção de uma img
@params {string} path
@return void
'''
def remove_img(path):
    try:
        os.remove(path)
    except:
        raise TypeError('Erro ao remover img')