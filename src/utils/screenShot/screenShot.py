from PIL import ImageGrab

def screen_shot(screenInfo = None):
    try:
        if (type(screenInfo) == list or type(screenInfo) == tuple):
            BBOX = (
                screenInfo[0],
                screenInfo[1],
                screenInfo[2] + screenInfo[0],
                screenInfo[3] + screenInfo[1] 
            )
            IMG = ImageGrab.grab(BBOX)
        else:
            IMG = ImageGrab.grab()
            
    except:     
        IMG = ImageGrab.grab()
    
    finally:
        return IMG 