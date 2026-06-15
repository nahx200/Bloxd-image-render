def convto_hsl(r,g,b):
    r1=r/255.0
    g1=g/255.0
    b1=b/255.0
    Cmax=max(r1,g1,b1)
    Cmin=min(r1,g1,b1)
    delta=Cmax-Cmin
    L=(Cmax+Cmin)/2
    #we dont use hue and saturation at this time...
    return [-1,-1,L]
from PIL import Image
DATA = open("export.txt","w")
txtimg = open("txtimg.txt","w")
image = Image.open("image.png")
w,h = image.size
#export JSON structure
image_data=[]
print(image.size)
for i in range(h):
    s=""
    for j in range(w):
        #print(str(image.getpixel( (j,i) ))+" "+str((j,i)))
        light=convto_hsl(image.getpixel( (j,i) )[0],image.getpixel( (j,i) )[1],image.getpixel( (j,i) )[2])[2]
        #print(light)
        if (light<=0.1):
            #set color to black
            image_data.append(0)
            s=s+"0"
        if (0.1<light and light<=0.2):
            #set color to gray
            image_data.append(1)
            s=s+"1"
        if (0.2<light and light<=0.5):
            #set color to white
            image_data.append(2)
            s=s+"2"
        if (0.5<light and light<=0.8):
            #color 3
            image_data.append(3)
            s=s+"3"
        if (0.8<light and light<=0.9):
            #color 4
            image_data.append(4)
            s=s+"4"
        if (light>0.9):
            #color 5
            image_data.append(5)
            s=s+"5"
    print("line "+str(i)+": "+s)
    txtimg.write(s+"\n")
    #test=input()
#print('{"size":['+str(w)+','+str(h)+'],"data":'+str(image_data)+'}')
output_string='{"size":['+str(w)+','+str(h)+'],"data":'+str(image_data)+'}'
#print(output_string)
enter_count=len(output_string)//1000
for i in range(0,len(output_string),1000):
    DATA.write(output_string[i:i+1000]+"\n\n")
