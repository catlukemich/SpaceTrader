import pygame
import json

images = {}

def loadImage(path):
    global images
    if path not in images:
        images[path] = pygame.image.load(path).convert_alpha()
        return images[path]
    else:
        return images[path]

def loadJSON(path):
    f = open(path)
    data = json.load(f)
    return data

anims = {}
def loadAnim(directory, start, end):
    key = directory + str(start) + ".." + str(end)

    if key not in anims:
        frames = []
        for i in range(start,end):
            filename = str(i).zfill(4) + ".png"
            filepath = directory + "/" + filename
            frames.append(loadImage(filepath))

        anims[key] = frames
        return frames
    else:
        return anims[key]



sounds = {}
def loadSound(path):
    global sounds
    if path not in sounds:
        sounds[path] = pygame.mixer.Sound(path)
        return sounds[path]
    else:
        return sounds[path]

def loadNames(path):
    ''' 
    Return a tuple that contains two lists:
    list of male names     and their probabilities 
    list of female names   and their probabilities 
    loaded  from an external text file (space separated "name probability"). 
    '''
    txt_file = open(path, "r")
    lines = txt_file.readlines()
    names = ([],[])
    for line in lines:
        name = line.split("\t")[0]
        prob = float(line.split("\t")[1])
        names[0].append(name)
        names[1].append(prob)
    return names

    