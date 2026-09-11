from PIL import Image, ImageDraw
import os

os.makedirs("assets", exist_ok=True)

BG    = (15,23,32)
AMBER = (224,165,68)
INDIGO= (133,147,232)
MINT  = (58,211,163)
CYCLE = [AMBER,AMBER,INDIGO,INDIGO,MINT,MINT,MINT,MINT]   # 2 day, 2 night, 4 off

def draw_mark(size=1024, ss=4):
    S = size*ss
    im = Image.new("RGB",(S,S),BG)
    d  = ImageDraw.Draw(im)
    cx = cy = S/2
    R_out, R_in = S*0.395, S*0.245
    gap = 3.4                      # degrees of dark between segments
    for i,col in enumerate(CYCLE):
        a0 = -90 + i*45 + gap/2
        a1 = -90 + (i+1)*45 - gap/2
        d.pieslice([cx-R_out,cy-R_out,cx+R_out,cy+R_out], a0, a1, fill=col)
    d.ellipse([cx-R_in,cy-R_in,cx+R_in,cy+R_in], fill=BG)
    r = S*0.072
    d.ellipse([cx-r,cy-r,cx+r,cy+r], fill=MINT)
    return im.resize((size,size), Image.LANCZOS)

icon = draw_mark(1024)
icon.save("assets/icon.png")

for name in ("splash.png","splash-dark.png"):
    sp = Image.new("RGB",(2732,2732),BG)
    m  = draw_mark(820)
    sp.paste(m,((2732-820)//2,(2732-820)//2))
    sp.save("assets/"+name)

print("done")
