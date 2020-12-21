height=1000
width=1000
frames_per_second=20#Задаем размеры поля
frame_number=0
frame_period=20
l=100#Размер яблок, угольков и змейки
v=1#
yx1=50#Точка отсчета передвижения по x
yv1=50#Точка отсчета передвижения по y
r=1# 
r1=1#
j=1#Счетчик победных очков
h=1#
t=3#Этап игры, 3-главное меню, 4-выбор уровня сложности, 1-процесс игры, 2-победа,0-поражение
o=1#
pv=1#
s3=1#Направление движения змейки в главном меню по x
s4=0#Направление движения змейки в главном меню по y
x=50
x1=x-75
x2=x1-75
x3=x2-75
x4=x3-75
x5=x4-75
x6=x5-75
x7=x6-75
x8=x7-75
x9=x8-75
x10=x9-75
x11=x10-75
x12=x11-75
x13=x12-75
x14=x13-75
x15=x14-75
x16=x15-75
x17=x16-75
x18=x17-75
x19=x18-75
x20=x19-75#координаты появления звеньев змеи по x
y=50
y1=y
y2=y
y3=y
y4=y
y5=y
y6=y
y7=y
y8=y
y9=y
y10=y
y11=y
y12=y
y13=y
y14=y
y15=y
y16=y
y17=y
y18=y
y19=y
y20=y#
gx1=-100
gx2=-100
gx3=-100
gx4=-100
gx5=-100
gy1=-100
gy2=-100
gy3=-100
gy4=-100
gy5=-100#координаты появления звеньев змеи по y
px=100
px1=80
px2=60
px3=40
px4=20
px5=0#
py=50
py1=50
py2=50
py3=50
py4=50
py5=50#

def setup():
  size(height,width)
  stroke (200,100,0)
  frameRate(frames_per_second)#Сщздаем поле
  
def draw():
    global n,m,l,t,v,xv1,yv1,r,r1,j,mouseClicked,h,o
    global p
    global gx1,gy1,gx2,gx3,gx4,gx5,gy2,gy3,gy4,gy5
    global x,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20
    global y,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20
    global ux1,ux2,ux3,uy1,uy2,uy3
    global pv,px,px1,px2,px3,px4,px5,py,py1,py2,py3,py4,py5,s3,s4,pux1,pux2,pux2,puy1,puy2,puy3,r2,r3
    background(40,160,60)
    if t==1 or t==0 or t==2: #На этапах игры: игра,поражение,победа, действуют следующие правила
        background(40,160,60)
        ellipse(x,y,l,l)
        fill(190,50,50)
        ux1=x+s1*45+r1*s1*20
        uy1=y+s2*45+r1*s2*20#координаты центра языка змеи, измениятся в зависимости от направления движения змеи, также иногда змея вытаскивает язык изо рта
        l1=15+15*s1**2+r1*40*s1
        l2=15+15*s2**2+r1*40*s2#Размеры языка, переодично изменяются(змея вытаскивает язык изо рта)
        r=r+1
        ellipse(ux1,uy1,l1,l2)#
        fill(0,0,0)
        ux2=ux1+(s1**2-1)*20-s1*30-r1*s1*20
        uy2=uy1+(s2**2-1)*20-s2*30-r1*s2*20#Создание координат глаз у змеи, делаем их независимыми от изменения координат языка
        ellipse(ux2,uy2,7,7)#Создание глаз
        fill(0,0,0)
        ux3=ux1-(s1**2-1)*20-s1*30-r1*s1*20
        uy3=uy1-(s2**2-1)*20-s2*30-r1*s2*20#Создание глаз у змеи, делаем их независимыми от изменения координат языка
        ellipse(ux3,uy3,7,7)#Создание глаз
        fill(103,79,47)
        fill(255,0,60)
        if r%10==0:#Частота высовывания языка изо рта змеёй
            r1=1
        else:
            r1=0
        ellipse(n,m,l,l)#Создаем яблоко
        fill(120,180,0)
        quad(n,m-35,n+5,m-70,n+40,m-100,n+35,m-70)#Создаем листик у яблока
        fill(0)
        ellipse(gx1,gy1,l,l)
        ellipse(gx2,gy2,l,l)
        ellipse(gx3,gy3,l,l)
        ellipse(gx4,gy4,l,l)
        ellipse(gx5,gy5,l,l)#Создаем угольки
        fill(140,100,0)
        if x>950:
            x=50
            xv1=50
            v=1
        if x<50:
            x=950
            xv1=950
            v=1
        if y>950:
            y=50
            yv1=50
            v=1
        if y<50:
            y=950
            yv1=950
            v=1#Змейка движется как по тору, по достижению одной стенки, вылезает из противоположной
        if gx1-l/1.2<x<gx1+l/1.2 and gy1-l/1.2<y<gy1+l/1.2:
            t=0
        if gx2-l/1.2<x<gx2+l/1.2 and gy2-l/1.2<y<gy2+l/1.2:
            t=0
        if gx3-l/1.2<x<gx3+l/1.2 and gy3-l/1.2<y<gy3+l/1.2:
            t=0
        if gx4-l/1.2<x<gx4+l/1.2 and gy4-l/1.2<y<gy4+l/1.2:
            t=0
        if gx5-l/1.2<x<gx5+l/1.2 and gy5-l/1.2<y<gy5+l/1.2:
            t=0#В случае столкновения змейки с угольком игрок проигрывает
        if n-l/1.2<x<n+l/1.2 and m-l/1.2<y<m+l/1.2:
            p=p+1#При столкновении змейки с яблоком переменная, отвечающая за появление новых звеньев змеи возрастает
            n=random (50,950)
            m=random (50,950)#При столкновении змейки с яблоком появлется новое яблоко, в случайном месте
            j=j+1#При столкновении змейки с яблоком добавляется один победный балл
        if p>0:
            ellipse(x1,y1,l,l)
        if p>1:
            ellipse(x2,y2,l,l)
        if p>2:
            ellipse(x3,y3,l,l)
        if p>3:
            ellipse(x4,y4,l,l)
        if p>4:
            ellipse(x5,y5,l,l)
        if p>5:
            ellipse(x6,y6,l,l)
        if p>6:
            ellipse(x7,y7,l,l)
        if p>7:
            ellipse(x8,y8,l,l)
        if p>8:
            ellipse(x9,y9,l,l)
        if p>9:
            ellipse(x10,y10,l,l)
        if p>10:
            ellipse(x11,y11,l,l)
        if p>11:
            ellipse(x12,y12,l,l)
        if p>12:
            ellipse(x13,y13,l,l)
        if p>13:
            ellipse(x14,y14,l,l)
        if p>14:
            ellipse(x15,y15,l,l)
        if p>15:
            ellipse(x16,y16,l,l)
        if p>16:
            ellipse(x17,y17,l,l)
        if p>17:
            ellipse(x18,y18,l,l)
        if p>18:
            ellipse(x19,y19,l,l)
        if p>19:
            ellipse(x20,y20,l,l)#Появление новых звеньев змеи в зависимости от количества съеденных яблок
        if p>20:
            t=2#Победа по достижению определенного количества съеденных яблок
        if x6-l/1.2<x<x6+l/1.2 and y6-l/1.2<y<y6+l/1.2 and p>5:
            t=0
        if x7-l/1.2<x<x7+l/1.2 and y7-l/1.2<y<y7+l/1.2 and p>6:
            t=0
        if x8-l/1.2<x<x8+l/1.2 and y8-l/1.2<y<y8+l/1.2 and p>7:
            t=0
        if x9-l/1.2<x<x9+l/1.2 and y9-l/1.2<y<y9+l/1.2 and p>8:
            t=0
        if x10-l/1.2<x<x10+l/1.2 and y10-l/1.2<y<y10+l/1.2 and p>9:
              t=0
        if x11-l/1.2<x<x11+l/1.2 and y11-l/1.2<y<y11+l/1.2 and p>10:
              t=0
        if x12-l/1.2<x<x12+l/1.2 and y12-l/1.2<y<y12+l/1.2 and p>11:
              t=0
        if x13-l/1.2<x<x13+l/1.2 and y13-l/1.2<y<y13+l/1.2 and p>12:
              t=0
        if x14-l/1.2<x<x14+l/1.2 and y14-l/1.2<y<y14+l/1.2 and p>13:
              t=0
        if x15-l/1.2<x<x15+l/1.2 and y15-l/1.2<y<y15+l/1.2 and p>14:
              t=0
        if x16-l/1.2<x<x16+l/1.2 and y16-l/1.2<y<y16+l/1.2 and p>16:
              t=0
        if x17-l/1.2<x<x17+l/1.2 and y17-l/1.2<y<y17+l/1.2 and p>17:
              t=0
        if x18-l/1.2<x<x18+l/1.2 and y18-l/1.2<y<y18+l/1.2 and p>18:
              t=0
        if x19-l/1.2<x<x19+l/1.2 and y19-l/1.2<y<y19+l/1.2 and p>19:
              t=0#Поражение при столкновении головы змеи с0 звеньями змеи
        if t==1:
            x=xv1+s1*speed*v
            y=yv1+s2*speed*v#Передвижение от последней сохраненной точки
            if (-1)**o==1:#На 2 перемещения головы, одно перемещение звеньев
                x20=x19
                y20=y19
                x19=x18
                y19=y18          
                x18=x17
                y18=y17
                x17=x16
                y17=y16
                x16=x15
                y16=y15
                x15=x14
                y15=y14
                x14=x13
                y14=y13
                x13=x12
                y13=y12
                x12=x11
                y12=y11
                x11=x10
                y11=y10
                x10=x9
                y10=y9
                x9=x8
                y9=y8
                x8=x7
                y8=y7
                x7=x6
                y7=y6
                x6=x5
                y6=y5
                x5=x4
                y5=y4
                x4=x3
                y4=y3
                x3=x2
                y3=y2
                x2=x1
                y2=y1#Звенья перетекают в другие звенья, стоящие ближе к голове
                x1=x-25*s1
                y1=y-25*s2#первое звено перемещается с задержкой от головы, что бы были видны глаза
            v=v+1#Рост переменной, отвественной за передвижение
            o=o+1#Рост вспомагательной переменной, отвечающей за "На 2 перемещения головы приходится одно перемещение звеньев"
    if t==0:
        h=h+1
        if(-1)**h==1:
             fill(0,0,255)
        else:
            fill(255,0,0)#Меняем фон таблички за текстом
        rect(190,90,600,120)
        rect(80,645,780,70)
        rect(160,440,670,75)#Создаем таблички за текстом
        fill(0)
        textSize(128);
        text("You lose!", 200, 200); 
        textSize(54);
        text("To start a new game press 2",100,700);#Создаем текст
        if j==1:
            textSize(64);
            text("You skored 1 points", 170, 500);
        if j==2:
            textSize(64);
            text("You skored 2 points", 170, 500);
        if j==3:
            textSize(64);
            text("You skored 3 points", 170, 500);
        if j==4:
            textSize(64);
            text("You skored 4 points", 170, 500);
        if j==5:
            textSize(64);
            text("You skored 5 points", 170, 500);
        if j==6:
            textSize(64);
            text("You skored 6 points", 170, 500);
        if j==7:
            textSize(64);
            text("You skored 7 points", 170, 500);
        if j==8:
            textSize(64);
            text("You skored 8 points", 170, 500);
        if j==9:
            textSize(64);
            text("You skored 9 points", 170, 500);
        if j==10:
            textSize(64);
            text("You skored 10 points", 170, 500);
        if j==11:
            textSize(64);
            text("You skored 11 points", 170, 500);
        if j==12:
            textSize(64);
            text("You skored 12 points", 170, 500);
        if j==13:
            textSize(64);
            text("You skored 13 points", 170, 500);
        if j==14:
            textSize(64);
            text("You skored 14 points", 170, 500);
        if j==15:
            textSize(64);
            text("You skored 15 points", 170, 500);
        if j==16:
            textSize(64);
            text("You skored 16 points", 170, 500);
        if j==17:
            textSize(64);
            text("You skored 17 points", 170, 500);
        if j==18:
            textSize(64);
            text("You skored 18 points", 170, 500);
        if j==19:
            textSize(64);
            text("You skored 19 points", 170, 500);
        if j==20:
            textSize(64);
            text("You skored 20 points", 170, 500);#Показываем количество набранных баллов
    if t==2:
        h=h+1
        if h%20==0:
             fill(0,0,255)
        else:
            fill(255,0,0)
        rect(190,390,600,120)
        rect(80,645,780,70)
        textSize(128);
        text("You win!", 200, 500);
        textSize(54); 
        text("To start a new game press 2",100,700);#Аналогично с прошлым пунктом
    if t==3:
        background(100,160,100)
        stroke(0)
        if 320<mouseX<670 and 300<mouseY<370:
            fill(180,180,70)
        else:
            fill(140,100,0)#Табличка меняет цвет при наведении на неее курсора
        rect(320,300,350,70)
        fill(0)
        textSize(54); 
        text("start game",350,350);#Пишем текст
        if px1>750 and py1<250:
            s3=0
            s4=1
            px=px1
            py=py1
            pv=1
        if px1>750 and py1>750:
            s3=-1
            s4=0
            px=px1
            py=py1
            pv=1
        if px1<250 and py1>750:
            s3=0
            s4=-1
            px=px1
            py=py1
            pv=1
        if px1<250 and py1<250:
            s3=1
            s4=0
            px=px1
            py=py1
            pv=1#Правила движения змейки(по квадрату), изменений направления
        px1=px+30*s3*pv
        py1=py+30*s4*pv
        px5=px4
        py5=py4
        px4=px3
        py4=py3
        px3=px2
        py3=py2
        px2=px1
        py2=py1
        pv=pv+1#Правила движения змейки, аналогично с основной змейкой
        ellipse(px1,py1,l,l)
        pux1=px1+s3*45
        puy1=py1+s4*45
        fill(180,120,0)
        pux2=pux1+(s3**2-1)*20-s3*30
        puy2=puy1+(s4**2-1)*20-s3*30
        ellipse(pux2,puy2,5,5)
        pux3=pux1-(s3**2-1)*20-s3*30
        puy3=puy1-(s4**2-1)*20-s4*30
        ellipse(pux3,puy3,5,5)
        ellipse(px2,py2,l,l)
        ellipse(px3,py3,l,l)
        ellipse(px4,py4,l,l)
        ellipse(px5,py5,l,l)#Создаем голову змейки,глаза и звенья
        fill(255,60,0)
        ellipse(500,500,l,l)#Создаем яблоко
        fill(120,180,0)
        quad(500,465,505,430,540,400,535,430)#Создаем листочек
    if t==4:
        background(100,160,100)
        if 200<mouseX<800 and 240<mouseY<320:
            fill(0,200,120)#Цвет табличек меняется в зависимости от выбираемой сложности при наведении на них курсора
        rect(200,240,600,80)
        fill(100,44,206)
        if 150<mouseX<850 and 440<mouseY<520:
            fill(0,60,250)
        rect(150,440,700,80)
        fill(100,44,206)
        if 200<mouseX<800 and 640<mouseY<720:
            fill(200,40,40)#Цвет табличек меняется в зависимости от выбираемой сложности при наведении на них курсора
        rect(200,640,600,80)#Создаем таблички
        fill(0)
        textSize(54); 
        text("low level of difficulty",220,300); 
        text("medium level of difficulty",170,500);
        text("high level of difficulty",220,700);#Создаем текст
        fill(100,44,206)
    
def keyPressed(): 
    global s1,s2,t,v,xv1,yv1,r
    global x,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20
    global y,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20
    if t==1:#Если течет фаза самой игры, выполняется следующее
        if key == 'w':
            s1=0
            s2=-1
        if key == 's':
            s1=0
            s2=1
        if key == 'a': 
            s1=-1
            s2=0
        if key == 'd': 
            s1=1
            s2=0#Изменение направления движения змеи
        if key == 'w' or key == 's' or key == 'd' or key == 'a':
            xv1=x
            yv1=y#Сохраняем текущие координаты головы
            v=1#Сбрасываем счетчик расстояния до последней сохранненой точки
        
def keyReleased(): 
    global n,m,t,j
    if key == '1':
        n=random (50,950)
        m=random (50,950)#При нажатии "1" яюлоко появляется в новом, случайном месте
    if key == '2':
        t=4
        j=1#При нажатии "2" игра переходит в фазу выбора сложности, победные баллы сбрасываются
        
def mouseReleased():
    global t,x,y,x1,y1,n,m,t,xv1,yv1,v,r,t,s1,s2,speed
    global gx1,gy1,gx2,gx3,gx4,gx5,gy2,gy3,gy4,gy5
    global p
    if t==3:
        if mouseButton == LEFT and 320<mouseX<670 and 300<mouseY<370:
           t=4#Если в фазе главного меню нажать на табличку игра преходит в фазу выбора уровня сложности
    if t==4:
        if mouseButton == LEFT and 200<mouseX<800 and 240<mouseY<320:
            speed=15#При выборе низкого уровня сложности скорость змейки и количество угольков минимальна
        if mouseButton == LEFT and 150<mouseX<850 and 440<mouseY<520:
            gy2=random (100,950)
            gy3=random (100,950)
            gx2=random (100,950)
            gx3=random (100,950)
            speed=20#При среднем уровне сложности скороть змеи и количество угольков увеличивается
        if mouseButton == LEFT and 200<mouseX<800 and 640<mouseY<720:
            gy2=random (100,950)
            gy3=random (100,950)
            gx4=random (100,950)
            gx5=random (100,950)
            gy4=random (100,950)
            gy5=random (100,950)
            gx2=random (100,950)
            gx3=random (100,950)
            speed=25#Пр высоком уровне сложности они еще раз увеличиваются
        if mouseButton == LEFT and 200<mouseX<800 and (240<mouseY<320 or 440<mouseY<520 or 640<mouseY<720):#Начало игры
            n=random (50,950)
            m=random (50,950)#Появление яблока в случайном месте
            t=1#Игра переходит в свой основной этап
            s1=1
            s2=0#Настраиваем направление движени змейки
            x=50
            y=50#Начальные координаты змейки
            xv1=50
            yv1=50#начальные сохраненные точки
            v=1#Сбрасываем расстояние от последней сохраненной точки
            gx1=random (100,950)
            gy1=random (100,950)#создаем уголек в случайном месте
            p=0#даем начальное значение переменной ответственной за появление новых звеньев змеи
            
        
        


        
        
        
        
        
