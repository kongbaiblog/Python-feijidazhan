import pygame
from pygame import *
import sys,os,random,threading
import time as tm
from threading import *

path=os.getcwd()
path=list(path)
i=0
while i<len(path):
    if path[i]=='\\':
        path[i]='/'
    i+=1
path=''.join(path)
print(path)

mouse_ctrl=False
T_cd=0.5
R_cd=10
MouseL_cd=10
my_plain_can_kill=[False,True]
background=0
Get_Tick=100

with open((path+'/set.ini'),'r',encoding='utf-8') as f:
    get_set=f.readlines()
    print(get_set)

line=0
while True:
    if '#' in get_set[line] and line+1<len(get_set):
        line+=1
    if 'control' in get_set[line]:
        #print(get_set[line][8:-1])
        if '0' in get_set[line]:
            mouse_ctrl=False
        if '1' in get_set[line]:
            mouse_ctrl=1
    if 'T=' in get_set[line]:
        if '\\n' in get_set[line]:
            T_cd=get_set[line][2:-1]
        else:
            T_cd=get_set[line][2:-1]
        print(T_cd)
    if 'R' in get_set[line]:
        if '\\n' in get_set[line]:
            R_cd=get_set[line][2:-1]
        else:
            R_cd=get_set[line][2:]
        #print(R_cd)
    if 'my_plain_kill' in get_set[line]:
        if '1' in get_set[line]:
            my_plain_can_kill=[False,False]
        if '0' in get_set[line]:
            my_plain_can_kill=[False,True]
    if 'background' in get_set[line]:
        if '1' in get_set[line]:
            background=1
        if '0' in get_set[line]:
            background=0
    if 'Tick' in get_set[line]:
        if '\\n' in get_set[line]:
            Get_Tick=float(get_set[line][5:-1])
        else:
            Get_Tick=float(get_set[line][5:])
        #print(Get_Tick)
    if line+1==len(get_set):
        break
    line+=1
back_other_plain=0
back_other_plain_two=0
back_other_plain_three=0

def Celled_Time():
    global back_other_plain
    tm.sleep(1)
    back_other_plain=1
    #print("线程T1")
def Celled_Time_T2():
    global back_other_plain_two
    tm.sleep(1)
    back_other_plain_two=1
    #print("线程T2")
def Celled_Time_T7():
    global back_other_plain_three
    tm.sleep(1)
    back_other_plain_three=1
    #print("线程T7")
def R_Time():
    #print('线程T3')
    R.R_lock=True
    R.R_pic=pygame.image.load(path+'/pic/RjinengLock.png')
    tm.sleep(float(R_cd))
    R.R_lock=False
    R.R_pic=pygame.image.load(path+'/pic/Rjineng.png')
def T_Time():
    #print('线程T4')
    E.E_pic=pygame.image.load(path+'/pic/Tjinenglock.png')
    E.E_lock=True
    tm.sleep(float(T_cd))
    E.E_lock=False
    E.E_pic=pygame.image.load(path+'/pic/Tjineng.png')
def MOUSE_Time():
    #print('线程5')
    MOUSEL.MOUSE_lock=True
    MOUSEL.MOUSE_pic=pygame.image.load(path+'/pic/shubiaoLlock.png')
    tm.sleep(int(MouseL_cd))
    MOUSEL.MOUSE_lock=False
    MOUSEL.MOUSE_pic=pygame.image.load(path+'/pic/shubiaoL.png')
def Can_not_kill_Time():
    tm.sleep(3)
    global my_plain_can_kill
    my_plain_can_kill[0]=True


threading_number=0
catch=threading.Thread(target=Celled_Time,name='T1',daemon=False)
T2_number=0
catch_T2=threading.Thread(target=Celled_Time_T2,name='T2',daemon=False)
T7_number=0
catch_T7=threading.Thread(target=Celled_Time_T7,name='T7',daemon=False)
R_number=0
catch_R=threading.Thread(target=R_Time,name='T3',daemon=False)
T_number=0
catch_T=threading.Thread(target=T_Time,name='T4',daemon=False)
MOUSE_number=0
catch_MOUSE=threading.Thread(target=MOUSE_Time,name='T5',daemon=False)
can_not_kill_number=0
can_not_kill=threading.Thread(target=Can_not_kill_Time,name='T6',daemon=False)

class Other_plain:
    '''敌飞机'''
    other_plain=pygame.image.load(path+"/pic/otherfly.png")
    other_plain_rect=other_plain.get_rect()
    other_plain_two=pygame.image.load(path+'/pic/otherfly2.png')
    other_plain_two_rect=other_plain_two.get_rect()
    other_plain_three=pygame.image.load(path+'/pic/otherfly3.png')
    other_plain_three_rect=other_plain_three.get_rect()
    other_plain_three_rect.x=random.randint(0,650)
    other_plain_two_rect.x=random.randint(0,650)
    other_plain_rect.x=random.randint(0,650)
    otherx=0
    othery=1
    otherx_t=0
    othery_t=1
    otherx_three=0
    othery_three=1
    speed=[otherx,othery]
    other_two_lock=False
    kill_lock=[False,False,False]

class Bullet:
    '''子弹'''
    bullet=pygame.image.load(path+'/pic/bullet.png')
    bullet_rect=bullet.get_rect()
    speed=[0,-1]

class R:
    '''R技能'''
    other_plain_kill=False
    R_lock=False
    R_pic=pygame.image.load(path+'/pic/Rjineng.png')    #color: #0099ff
    R_pic_rect=R_pic.get_rect()
    R_pic_rect.x=700
    R_pic_rect.y=900

class E:
    '''T技能,一开始是E,但E按键不得劲,所以改成了T,E这个类就不改了'''
    E_move=100
    E_lock=False
    E_pic=pygame.image.load(path+'/pic/Tjineng.png')
    E_pic_rect=E_pic.get_rect()
    E_pic_rect.x=600
    E_pic_rect.y=900
    last_key='w'

class MOUSEL:
    '''鼠标技能'''
    MOUSE_lock=False
    MOUSE_pic=pygame.image.load(path+'/pic/shubiaoL.png')
    MOUSE_pic_rect=MOUSE_pic.get_rect()
    MOUSE_pic_rect.x=500
    MOUSE_pic_rect.y=900

class GAME_OVER:
    '''游戏结束'''
    regame_pic=pygame.image.load(path+'/pic/regame.png')
    regame_pic_rect=regame_pic.get_rect()
    exit_pic=pygame.image.load(path+'/pic/exit.png')
    exit_pic_rect=exit_pic.get_rect()
    regame_pic_rect.x=100
    regame_pic_rect.y=200
    exit_pic_rect.x=100
    exit_pic_rect.y=430

pygame.init()
size=width,heigh=800,1000
screen=pygame.display.set_mode(size)
color=(0,0,0)
pygame.display.set_caption('飞机大战')

my_plain=pygame.image.load(path+"/pic/myfly.png")   #  68*48
my_plain_rect=my_plain.get_rect()
my_plain_rect.x=200
my_plain_rect.y=750
my_plain_how=True
clock=pygame.time.Clock()
speedn=10
biu=0
point=0
point_output=0
last_key="w"
can_not_kill.start()

#print(random.randint(0,500))
other=Other_plain()
bullet=Bullet()


while 1:
    speed=[0,0]
    if my_plain_how==True:
        speed_other=[other.otherx,other.othery]
        speed_other_two=[other.otherx_t,other.othery_t]
        speed_other_three=[other.otherx_three,other.othery_three]
    if my_plain_how==False:
        speed_other=[0,0]
        speed_other_two=[0,0]
        speed_other_three=[0,0]
    for event in pygame.event.get():

        key_pressed=pygame.key.get_pressed()
        if my_plain_how==True:
            if key_pressed[K_w]:
                speed[1]-=speedn
                E.last_key='w'
                #print('w')
            if key_pressed[K_s]:
                speed[1]+=speedn
                E.last_key='s'
            if key_pressed[K_a]:
                speed[0]-=speedn
                E.last_key='a'
            if key_pressed[K_d]:
                speed[0]+=speedn
                E.last_key='d'
            if key_pressed[K_SPACE] and biu!=2:
                #print('biu~')
                biu=1
            if key_pressed[K_LCTRL] and key_pressed[K_p]:
                print('己方飞机坐标:',my_plain_rect.x,',',my_plain_rect.y)
                print('\n敌方飞机:',other.other_plain_rect.x,',',other.other_plain_rect.y)
            if key_pressed[K_LSHIFT] and key_pressed[K_w]:
                my_plain=pygame.image.load(path+'/pic/myfly.png')
                last_key='w'
            if key_pressed[K_LSHIFT] and key_pressed[K_s]:
                my_plain=pygame.image.load(path+'/pic/myflyB.png')
                last_key='s'
            if key_pressed[K_LSHIFT] and key_pressed[K_a]:
                my_plain=pygame.image.load(path+'/pic/myflyL.png')
                last_key='a'
            if key_pressed[K_LSHIFT] and key_pressed[K_d]:
                my_plain=pygame.image.load(path+'/pic/myflyR.png')
                last_key='d'
            if key_pressed[K_r] and R.R_lock==False:
                R.other_plain_kill=True
                try:
                    catch_R.start()
                except:
                    catch_R='catch_R'+str(R_number)
                    catch_R=threading.Thread(target=R_Time,name='T3',daemon=False)
                    catch_R.start()
                    R_number+=1
            if key_pressed[K_t] and E.E_lock==False and mouse_ctrl!=1:
                if E.last_key=='d':
                    my_plain_rect.x+=E.E_move
                    if my_plain_rect.x+E.E_move>width:
                        my_plain_rect.x=750
                if E.last_key=='a':
                    my_plain_rect.x-=E.E_move
                    if my_plain_rect.x-E.E_move<0:
                        my_plain_rect.x=50
                if E.last_key=='w':
                    my_plain_rect.y-=E.E_move
                    if my_plain_rect.y-E.E_move<0:
                        my_plain_rect.y=50
                if E.last_key=='s':
                    my_plain_rect.y+=E.E_move
                    if my_plain_rect.y+E.E_move>heigh:
                        my_plain_rect.y=950
                try:
                    catch_T.start()
                except:
                    catch_T='catch_T'+str(T_number)
                    catch_T=threading.Thread(target=T_Time,name='T4',daemon=False)
                    catch_T.start()
                    T_number+=1


        if event.type==pygame.QUIT:
            print("QUIT")
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN and mouse_ctrl==False and MOUSEL.MOUSE_lock==False and my_plain_how==True:
            go_to=pygame.mouse.get_pos()
            my_plain_rect.x=go_to[0]
            my_plain_rect.y=go_to[1]
            print('传送至坐标:',go_to)
            try:
                catch_MOUSE.start()
            except:
                catch_MOUSE='catch_MOUSE'+str(MOUSE_number)
                catch_MOUSE=threading.Thread(target=MOUSE_Time,name='T5',daemon=False)
                catch_MOUSE.start()
                MOUSE_number+=1
        if event.type==pygame.MOUSEBUTTONDOWN and my_plain_how==False:
            if 100<=pygame.mouse.get_pos()[0]<=730:  #x:100,730   y:200,380 #x:100,730   y:430,610
                if 200<=pygame.mouse.get_pos()[1]<=380:
                    print('游戏重启中...')
                    try:
                        os.system('start '+path+'/play.py')
                    except:
                        os.system('start '+path+'/play.exe')
                    exit()
                if 430<=pygame.mouse.get_pos()[1]<=610:
                    print('退出中...')
                    exit()

    clock.tick(Get_Tick)

    if my_plain_rect.right>width:
        speed[0]=-1
    if my_plain_rect.left<0:
        speed[0]=1
    if my_plain_rect.bottom>heigh:
        speed[1]=-1
    if my_plain_rect.top<0:
        speed[1]=1

    if (other.other_plain_rect.y>heigh):
        other.other_plain_rect.y=1
        other.other_plain_rect.x=random.randint(0,650)
    if other.other_plain_two_rect.y>heigh:
        other.other_plain_two_rect.y=1
        other.other_plain_two_rect.x=random.randint(0,650)
    if other.other_plain_three_rect.y>heigh:
        other.other_plain_three_rect.y=1
        other.other_plain_three_rect.x=random.randint(0,650)
    #print(other.other_plain_rect.y)

    if biu==1:
        bullet.bullet_rect.x=my_plain_rect.x
        bullet.bullet_rect.y=my_plain_rect.y
        biu=2
    if biu==2:
        if last_key=='w':
            bullet.speed[1]-=1
        if last_key=='s':
            bullet.speed[1]+=1
        if last_key=='a':
            bullet.speed[0]-=1
        if last_key=='d':
            bullet.speed[0]+=1


    if bullet.bullet_rect.y<0 or bullet.bullet_rect.y>heigh or bullet.bullet_rect.x<0 or bullet.bullet_rect.x>width:
        bullet.bullet_rect.x=-10
        bullet.bullet_rect.y=-10
        biu=0
        bullet.speed=[0,0]


    if bullet.speed==[0,0]:
        bullet.bullet_rect.x=my_plain_rect.x
        bullet.bullet_rect.y=my_plain_rect.y-10


    if back_other_plain==1:
        #print("change")
        other.other_plain=pygame.image.load(path+'/pic/otherfly.png')
        other.othery=1
        other.other_plain_rect.x=random.randint(0,650)
        other.other_plain_rect.y=0
        back_other_plain=0
        other.kill_lock[0]=False


    if back_other_plain_two==1:
        #print("T2 True")
        other.other_plain_two=pygame.image.load(path+'/pic/otherfly2.png')
        other.othery_t=1
        other.other_plain_two_rect.x=random.randint(0,650)
        other.other_plain_two_rect.y=0
        back_other_plain_two=0
        other.kill_lock[1]=False

    if back_other_plain_three==1:
        #print("T7 True")
        other.other_plain_three=pygame.image.load(path+'/pic/otherfly3.png')
        other.othery_three=1
        other.other_plain_three_rect.x=random.randint(0,650)
        other.other_plain_three_rect.y=0
        back_other_plain_three=0
        other.kill_lock[2]=False


    if ((other.other_plain_rect.x-30)<=bullet.bullet_rect.x<=(other.other_plain_rect.x+30) and (other.other_plain_rect.y-20)<=bullet.bullet_rect.y<=(other.other_plain_rect.y+20) or R.other_plain_kill==True) and other.kill_lock[0]==False:
        point+=1
        print(point)
        other.kill_lock[0]=True
        other.othery=0
        other.other_plain=pygame.image.load(path+'/pic/otherflyboom.png')
        try:
            catch.start()
        except:
            catch='catch'+str(threading_number)
            threading_number+=1
            catch=threading.Thread(target=Celled_Time,name='T1'+str(threading_number),daemon=False)
            catch.start()
    #print(back_other_plain)


    if ((other.other_plain_two_rect.x-30)<=bullet.bullet_rect.x<=(other.other_plain_two_rect.x+30) and (other.other_plain_two_rect.y-20)<=bullet.bullet_rect.y<=(other.other_plain_two_rect.y+20) or R.other_plain_kill==True) and other.kill_lock[1]==False:
        point+=1
        print(point)
        other.kill_lock[1]=True
        other.othery_t=0
        other.other_plain_two=pygame.image.load(path+'/pic/otherflyboom.png')
        try:
            catch_T2.start()
        except:
            catch_T2='catch'+str(T2_number)
            T2_number+=1
            catch_T2=threading.Thread(target=Celled_Time_T2,name='T2'+str(T2_number),daemon=False)
            catch_T2.start()

    if ((other.other_plain_three_rect.x-30)<=bullet.bullet_rect.x<=(other.other_plain_three_rect.x+30) and (other.other_plain_three_rect.y-20)<=bullet.bullet_rect.y<=(other.other_plain_three_rect.y+20) or R.other_plain_kill==True) and other.kill_lock[2]==False:
        point+=1
        print(point)
        other.kill_lock[2]=True
        other.othery_three=0
        other.other_plain_three=pygame.image.load(path+'/pic/otherflyboom.png')
        try:
            catch_T7.start()
        except:
            catch_T7='catch'+str(T7_number)
            T7_number+=1
            catch_T7=threading.Thread(target=Celled_Time_T7,name='T7'+str(T7_number),daemon=False)
            catch_T7.start()
    
    if ((other.other_plain_rect.y-40)<=my_plain_rect.y<=(other.other_plain_rect.y+40) or (other.other_plain_two_rect.y-40)<=my_plain_rect.y<=(other.other_plain_two_rect.y+40) or (other.other_plain_three_rect.y-40)<=my_plain_rect.y<=(other.other_plain_three_rect.y+40)) and my_plain_can_kill==[True,True]:
       # print('敌飞机1:',other.other_plain_rect.x,',',other.other_plain_rect.y,'\n','敌飞机2:',other.other_plain_two_rect.x,',',other.other_plain_two_rect.y,'\n','我方飞机:',my_plain_rect.x,',',my_plain_rect.y)
        my_plain=pygame.image.load(path+'/pic/myflyboom.png')
        my_plain_how=False
        other.speed=[0,0]
        speed_other_two=[0,0]
        if point_output==0:
            print('————————————————分数为:',point,'————————————————')
            point_output+=1

    if mouse_ctrl==True and my_plain_how==True:
        go_to=pygame.mouse.get_pos()
        my_plain_rect.x=go_to[0]
        my_plain_rect.y=go_to[1]
    my_plain_rect=my_plain_rect.move(speed)
    other.other_plain_three_rect=other.other_plain_three_rect.move(speed_other_three)
    other.other_plain_two_rect=other.other_plain_two_rect.move(speed_other_two)
    other.other_plain_rect=other.other_plain_rect.move(speed_other)
    bullet.bullet_rect=bullet.bullet_rect.move(bullet.speed)
    screen.fill(color)
    if background==1:
        screen.blit(pygame.image.load(path+'/pic/bg.png'),(0,0))
    screen.blit(other.other_plain,other.other_plain_rect)
    screen.blit(other.other_plain_two,other.other_plain_two_rect)
    screen.blit(other.other_plain_three,other.other_plain_three_rect)
    screen.blit(bullet.bullet,bullet.bullet_rect)
    screen.blit(my_plain,my_plain_rect)
    screen.blit(R.R_pic,R.R_pic_rect)
    if mouse_ctrl!=1:
        screen.blit(E.E_pic,E.E_pic_rect)
        screen.blit(MOUSEL.MOUSE_pic,MOUSEL.MOUSE_pic_rect)
    if my_plain_how==False:
        screen.blit(GAME_OVER.regame_pic,GAME_OVER.regame_pic_rect)
        screen.blit(GAME_OVER.exit_pic,GAME_OVER.exit_pic_rect)
    R.other_plain_kill=False
    pygame.display.update()
