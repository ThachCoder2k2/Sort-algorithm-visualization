import pygame
import sys
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((900, 650))

pygame.display.set_caption("Bai tap lon CTDL&TT - Nguyen Hoang Thach - 20010822")
clock=pygame.time.Clock()
input_rect = pygame.Rect(300, 270, 360, 32)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
run = True
click=False
width = 900
length = 600
clr_ind = 0
user_text=''
clr =[(0, 204, 102), (255, 0, 0), (0, 0, 153), (255, 102, 0)]
fnt = pygame.font.SysFont("comicsans", 30)
fnt1 = pygame.font.SysFont("comicsans", 20)
def draw(array,arr_clr,n):
    txt = fnt.render("Chon 1 giai thuat sap xep", 1, (0, 0, 0))
    screen.blit(txt, (40, 20))
    txt1 = fnt.render("Bam R de nhap day moi",1, (0, 0, 0))
    screen.blit(txt1, (40, 40))
    #txt2 = fnt1.render("Selection sort", 1, (0, 0, 0))
    #screen.blit(txt2, (40, 60))
    element_width =(width-150)//n
    boundry_arr = 900 / n
    boundry_grp = 550 /100
    pygame.draw.line(screen,(255,100,100), (0,95), (900,95),10)
    for i in range(1, 100):
        pygame.draw.line(screen,(224, 224, 224),(0, 5.5 * i + 100), (900, 5.5 * i + 100), 1)
    maxarr=-sys.maxsize-1
    for i in range (1,n):
        if array[i]>maxarr:
            maxarr=array[i]
    tile=maxarr/100
    if tile<1:
        tile=1
    else:
        tile=tile+5
    for i in range(1, n):
        number=str(array[i])
        txtnb=fnt.render(number,1,(0,0,0))
        pygame.draw.line(screen, arr_clr[i],(boundry_arr * i-3, 100),(boundry_arr * i-3,(array[i]*boundry_grp)/(tile) + 100),element_width)
        screen.blit(txtnb,(boundry_arr * i-13, array[i]*boundry_grp/(tile)+ 120))
def draw_text(text,font,color,surface,x,y):
    textobj= font.render(text,1,color)
    textrect=textobj.get_rect()
    textrect.topleft=(x,y)
    surface.blit(textobj,textrect)

def refill(array,arr_clr,n):
    screen.fill((255, 255, 255))
    draw(array,arr_clr,n)
    pygame.display.update()
    pygame.time.delay(50)
  

def input_array(n):
    array =[0]*n
    for i in range (1,n):
        check=0
        run=True
        user_array=''
        active=False
        i_tt=str(i)
        while run:
            screen.fill((255, 255, 255))
            text1=fnt.render("Nhap array[",True,(0,0,0))
            text2=fnt.render(i_tt,True,(0,0,0))
            text3=fnt.render("]",True,(0,0,0))
            screen.blit(text1,(300,250))
            screen.blit(text2,(420,250))
            screen.blit(text3,(440,250))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run=False
  
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
  
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_array = user_array[:-1]
                    else:
                        user_array += event.unicode
                    if event.key == pygame.K_RETURN:
                        if i==n-1:
                            program_sorting(array,n)
                        else:
                            #input_array(n_nhap)
                            check=1
                            break
            if (check==1):
                break            
            if active:
                color = color_active
            else:
                color = color_passive
            if(len(user_array)>0):
                array[i]=int(user_array)
            pygame.draw.rect(screen, color, input_rect)   
            text_surface =fnt.render(user_array, True, (255, 255, 255))
            screen.blit(text_surface, (input_rect.x+10, input_rect.y+10))
            input_rect.w = max(100, text_surface.get_width()+10)
            pygame.display.flip()
            clock.tick(60)
        if (check==1):
            continue
        pygame.QUIT()
def input_n():
    run=True
    user_text=''
    active=False
    while run:
        screen.fill((255, 255, 255))
        text=fnt.render("Nhap n",True,(0,0,0))
        screen.blit(text,(300,250))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
  
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
                if event.key == pygame.K_RETURN:
                    input_array(n_nhap+1)
                    #pass
        if active:
            color = color_active
        else:
            color = color_passive
        if (len(user_text)>0):
            n_nhap=int(user_text)
        pygame.draw.rect(screen, color, input_rect)   
        text_surface =fnt.render(user_text, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect.x+10, input_rect.y+10))
        input_rect.w = max(100, text_surface.get_width()+10)
        pygame.display.flip()
        clock.tick(60)
    pygame.QUIT()
def Selectionsort(array, l, r,arr_clr):
    
    pygame.event.pump() 
    for i in range (l,r+1): 
        arr_clr[i]= clr[1]
        refill(array,arr_clr,len(array))
        m=i
        for j in range(i+1,r+1):
            arr_clr[j]=clr[3]
            refill(array,arr_clr,len(array))
            t=m
            if (array[m]>array[j]):
                m=j
            if (m!=i):
                if (t!=i):
                    arr_clr[t]=clr[0]
                arr_clr[m]=clr[2]  
                refill(array,arr_clr,len(array))  
            arr_clr[j]=clr[0]
            if m==j:
                arr_clr[m]=clr[2]
        if (m!=i):
            t=array[m]
            array[m]=array[i]
            array[i]=t 
        arr_clr[m]=clr[0]       
        arr_clr[i]=clr[0]
def bubblesort(array,l,r,arr_clr):
    pygame.event.pump() 
    for i in range(l,r+1):
        arr_clr[i]=clr[1];
        refill(array,arr_clr,len(array))
        for j in range(r,i,-1):
            arr_clr[j]=clr[3];
            refill(array,arr_clr,len(array))
            if (array[j]<array[j-1]):
                arr_clr[j]=clr[2];
                arr_clr[j-1]=clr[2];
                refill(array,arr_clr,len(array))
                t=array[j]
                array[j]=array[j-1]
                array[j-1]=t
                arr_clr[j]=clr[3];
                arr_clr[j-1]=clr[0];
                refill(array,arr_clr,len(array))
            arr_clr[j]=clr[0]
        arr_clr[i]=clr[0]
def insertionsort(array,l,r,arr_clr):
    pygame.event.pump()
    for i in range(l+1,r+1):
        arr_clr[i]=clr[1];
        refill(array,arr_clr,len(array))
        x=array[i]
        j=i-1
        arr_clr[j]=clr[3];
        refill(array,arr_clr,len(array))
        check=0
        while x<array[j] and j>=1:
            check=1
            arr_clr[j]=clr[3];
            refill(array,arr_clr,len(array))
            array[j+1]=array[j];
            j=j-1
        #arr_clr[i]=clr[1];
        if check==1:
            arr_clr[j+1]=clr[2];
            refill(array,arr_clr,len(array))
            array[j+1]=x 
        for z in range(j,i):
            arr_clr[z]=clr[0]
        refill(array,arr_clr,len(array)) 
        arr_clr[i]=clr[0];              
def main_menu():
    run=True
    #click=False
    while run:
        screen.fill((255,255,255))
        mx,my= pygame.mouse.get_pos()
        text=fnt.render("Bam vao de bat dau",True,(0,0,0))
        draw_text("Bai ket thuc hoc phan CTDL&TT",fnt,(0,0,0),screen,300,250)
        draw_text("Bai 2: Sap xep can ban",fnt,(0,0,0),screen,340,270)
        draw_text("Nguoi thuc hien: Nguyen Hoang Thach",fnt,(0,0,0),screen,300,330)
        draw_text("Massv:20010822",fnt,(0,0,0),screen,300,350)
        button_1=pygame.Rect(370,370,200,50)
        #draw_text("Bat dau",fnt,(0,0,0),screen,330,330)
        if button_1.collidepoint((mx,my)):
            if click:
                input_n()
                #program_sorting()
        pygame.draw.rect(screen,(255,0,0),button_1);
        screen.blit(text,(370,380))
        click=False
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    click=True
        pygame.display.update()
        #mainClock.tick(60)
    pygame.QUIT()
def program_sorting(array1,n):
    run=True
    click=False
    array =[0]*n
    arr_clr =[(0, 204, 102)]*n
    for i in range(1, n):
        arr_clr[i]= clr[0]
        array[i]=array1[i];
    while run:
        screen.fill((255, 255, 255))
        mx,my= pygame.mouse.get_pos()
        button_1=pygame.Rect(300,45,180,50)
        button_2=pygame.Rect(490,45,180,50)
        button_3=pygame.Rect(680,45,180,50)
        if button_1.collidepoint((mx,my)):
            if click:
                insertionsort(array,1,len(array)-1,arr_clr)
                click=False
        if button_2.collidepoint((mx,my)):
            if click:
                bubblesort(array,1,len(array)-1,arr_clr)
                click=False
        if button_3.collidepoint((mx,my)):
            if click:
                Selectionsort(array, 1, len(array)-1,arr_clr) 
                click=False
        text_1=fnt.render("Insertion Sort",True,(0,0,0))
        text_2=fnt.render("Bubble Sort",True,(0,0,0))
        text_3=fnt.render("Selection Sort",True,(0,0,0))
        pygame.draw.rect(screen,(100,100,100),button_1)
        pygame.draw.rect(screen,(100,100,100),button_2)
        pygame.draw.rect(screen,(100,100,100),button_3)
        screen.blit(text_1,(310,55))
        screen.blit(text_2,(500,55))
        screen.blit(text_3,(690,55))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    input_n()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    click=True    
        draw(array,arr_clr,n)
        pygame.display.update()
    pygame.quit()
main_menu()      
