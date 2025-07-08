#ORDER SUMMARY
def order_summary(item,*arguments,**keywords):
    print("--You ordered:",item)
    print("--Additional notes:")
    for arg in arguments:
        print(arg)
    print('-' * 40)
    for kw in keywords:
        print(kw,":",keywords[kw])

order_summary(
    "pizza",
    "Extra cheese",
    "Extra spicy.",
    customer="alice",
    location="Table 5",
    Time="7.30 PM"
)


#ENHANCED ORDER SUMMARY

def order_summary(item,*arguments,**keywords):
    print("--YOU ORDERED:",item.upper())
    print("--Additional notes:")
    for arg in arguments:
        print(arg)
    print('-' * 40)
    for kw in sorted(keywords):
        print(f"{kw.ljust(8)}: {keywords[kw]}")

order_summary(
    "pizza",
    "Extra cheese",
    "Extra spicy.",
    customer="alice",
    location="Table 5",
    Time="7.30 PM"
)

#SPECIAL PARAMETER IN KEYWORD ARGUMENTS(creating function)

#1
def draw_lines(x1,y1,/,x2,y2,*,color="black",width=1):
    print(f"Draw from ({x1},{y1}) to ({x2}, {y2}) in {color} with width {width}")
          
draw_lines(0,0,10,10,color="red",width=3)

#2

def create_rectangle(x,y,/,height,width,*,fill_color="blue",border_color="black"):
    print(f"Rectangle at ({x}, {y}) of size ({height} * {width}) with border color {border_color} and fill with {fill_color}")

create_rectangle(0,0,height=80,width=80,fill_color="green")

#as i dont give border color it uses default color as border color
#and also after'/' i can use these as keywords or positional,before(/) only positional

#3

def draw_circle(x,y,/,radius,*,fill_color="pink",border_color="blue"):
    print(f"circle at ({x}, {y}) of radius {radius} with {border_color} color and filled with {fil_color}")

draw_circle(0,0,4,fill_color="yellow")

#4

def play_sound(file_path,/,volume,*,loop=False):
    print(f"Playing {file_path} at volume {volume}, loop: {loop}")


play_sound("sound.wav", 0.5, loop=True) 






