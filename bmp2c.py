from PIL import Image
import numpy as np

im = Image.open('gif1.gif')
im.seek(0)
duration = 0
with open("giff.c", "w") as f:
    f.write("#include <avr/pgmspace.h>\n\nconst int boyut PROGMEM = "+str(im.n_frames)+";\n\nconst uint8_t giff[][504] PROGMEM = {\n")
    while im.tell()<im.n_frames:
        f.write("\n{")
        resim_array = np.array(im.resize((84,48)).convert('1'))
        for i in range (0,int(resim_array.size/resim_array[0].size),8):
            for j in range(resim_array[0].size):
                sayi=0
                for k in range(8):
                    if resim_array[i+k][j] == False:
                        sayi += pow(2, k)
                f.write("0x{:02X}".format(sayi)+", ")
        f.write("}, ")
        duration += im.info['duration']
        if(im.tell()+1 == im.n_frames):
            break
        im.seek(im.tell() + 1)
    f.write("\n};\n\nconst int sure PROGMEM = "+str(int(duration/im.n_frames))+";")
    f.close()
"""for a in range(1, 19):
    resim_array = np.array(Image.open(str(a)+".png").resize((84,48)).convert('1'))
    with open("r"+str(a)+".c", "w") as f:
        f.write("#include <avr/pgmspace.h>\n\nconst uint8_t r"+str(a)+"[] PROGMEM = {\n")
        for i in range (0,int(resim_array.size/resim_array[0].size),8):
            for j in range(resim_array[0].size):
                sayi=0
                for k in range(8):
                    if resim_array[i+k][j] == False:
                        sayi += pow(2, k)
                f.write("0x{:02X}".format(sayi)+", ")
        
        f.write("\n};")
        f.close()"""