from PIL import ImageGrab

'''
@function screen_shot
@description Função que realiza o print da tela
@params {list, tuple, None} screenInfo 
@return Image
'''
def screen_shot(screenInfo = None):
    try:
        if (type(screenInfo) == list or type(screenInfo) == tuple):
            bbox = (
                screenInfo[0],
                screenInfo[1],
                screenInfo[2] + screenInfo[0],
                screenInfo[3] + screenInfo[1] 
            )
            img = ImageGrab.grab(bbox)
        else:
            img = ImageGrab.grab()
            
    except:     
        img = ImageGrab.grab()
    
    finally:
        return img 