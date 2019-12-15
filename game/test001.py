import sys
import pygame
import spritesheet
import random
#newsprite는 일단 필요 없는 파일

#슬라임 정보 


#일단은 기본 크기에 해당 150,119의 세 배
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 357

white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
pygame.display.set_caption("Pymon_v001")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pos_x = 20
pos_y = 20

clock = pygame.time.Clock()

#직접 가져오기
s1 = spritesheet.spritesheet('스프라이트_기본UI2.png')
s2 = spritesheet.spritesheet('스프라이트_슬라임형태.png')
s3 = spritesheet.spritesheet('스프라이트_버튼UI2.png')
s4 = spritesheet.spritesheet('스프라이트_미니게임2.png')
s5 = spritesheet.spritesheet('배경_우주.png')

#이제 넣어줌과 동시에 확대도 시켜주자!
#원래 변수를 넣어야 하지만 여기서는 합친 값121 지정
btu = (150,119)
btu2 = (152,121)
base = []
base.append(s1.image_at((1+btu2[0]*2, 1, btu[0] , btu[1])))
base[0] = pygame.transform.scale(base[0],(btu[0]*3,btu[1]*3))

#기본적인 배경
back_small = s1.image_at((1,1,136,40))
back_small = pygame.transform.scale(back_small,(136*3,40*3))
back_big = s1.image_at((1+152,1,150,119))
back_big = pygame.transform.scale(back_big,(150*3,119*3))

award_type = []
for i in range(0,3):
    award_type.append(s1.image_at((1+20*i,1+42, 18,18)))
    award_type[i]=pygame.transform.scale(award_type[i],(54,54))

award_recv = []
for i in range(0,3):
    award_recv.append(s1.image_at((1+20*(i+3),1+42,18,18)))
    award_recv[i]=pygame.transform.scale(award_recv[i],(54,54))

money_slot = s1.image_at((1,1+42+20, 27,7))
money_slot = pygame.transform.scale(money_slot,(81,21))

#아이템 슬롯과 업적 슬롯

item_slot = s1.image_at((1,1+42+20+20, 30,30))
item_slot = pygame.transform.scale(item_slot,(90,90))
item_selected = s1.image_at((1+32,1+42+20+20, 30,30))
item_selected = pygame.transform.scale(item_selected,(90,90))
item_nonslot = s1.image_at((1+32+32,1+42+20+20, 30,30))
item_nonslot = pygame.transform.scale(item_nonslot,(90,90))

award_slot = s1.image_at((1,1+42+20+20+32, 126,30))
award_slot = pygame.transform.scale(award_slot,(378,90))
award_selected = s1.image_at((1,1+42+20+20+32+32, 126,30))
award_selected = pygame.transform.scale(award_selected,(378,90))

#슬라임과 표정은 54,37로 같고, 점프만 54,45 좀 더 크다. 2칸씩 여분
slimetu = (54,37,45)
slimetu2 = (56,39,47)


#일반용과 미니게임용 2개로 나뉜다.
slimeE = []
slimeE2 = []
for i in range(0,16):
    slimeE.append(s2.image_at((1+slimetu2[0]*(i+1), 1, slimetu[0] , slimetu[1])))
    slimeE[i] = pygame.transform.scale(slimeE[i],(slimetu[0]*3,slimetu[1]*3))
    slimeE2.append(s2.image_at((1+slimetu2[0]*(i+1), 1, slimetu[0] , slimetu[1])))
    slimeE2[i] = pygame.transform.scale(slimeE2[i],(slimetu[0]*2,slimetu[1]*2))

for i in range(0,17):
    slimeE.append(s2.image_at((1+slimetu2[0]*i, 1+slimetu2[1], slimetu[0] , slimetu[1])))
    slimeE[i+16] = pygame.transform.scale(slimeE[i+16],(slimetu[0]*3,slimetu[1]*3))
    slimeE2.append(s2.image_at((1+slimetu2[0]*i, 1+slimetu2[1], slimetu[0] , slimetu[1])))
    slimeE2[i+16] = pygame.transform.scale(slimeE2[i+16],(slimetu[0]*2,slimetu[1]*2))

#일반용만
slimeB = []
for i in range(0,3) : 
    slimeB.append(s2.image_at((1, 1+slimetu2[1]*(i+2), slimetu[0] , slimetu[1])))
    slimeB[i] = pygame.transform.scale(slimeB[i],(slimetu[0]*3,slimetu[1]*3))
for i in range(0,3) : 
    slimeB.append(s2.image_at((1+slimetu2[0], 1+slimetu2[1]*(i+2), slimetu[0] , slimetu[1])))
    slimeB[i+3] = pygame.transform.scale(slimeB[i+3],(slimetu[0]*3,slimetu[1]*3))
for i in range(0,3) : 
    slimeB.append(s2.image_at((1+slimetu2[0]*2, 1+slimetu2[1]*(i+2), slimetu[0] , slimetu[1])))
    slimeB[i+6] = pygame.transform.scale(slimeB[i+6],(slimetu[0]*3,slimetu[1]*3))
for i in range(0,3) : 
    slimeB.append(s2.image_at((1+slimetu2[0]*2, 1+slimetu2[1]*(i+2), slimetu[0] , slimetu[1])))
    slimeB[i+9] = pygame.transform.scale(slimeB[i+9],(slimetu[0]*3,slimetu[1]*3))
for i in range(0,3) : 
    slimeB.append(s2.image_at((1+slimetu2[0]*2, 1+slimetu2[1]*(i+2), slimetu[0] , slimetu[1])))
    slimeB[i+12] = pygame.transform.scale(slimeB[i+12],(slimetu[0]*3,slimetu[1]*3))

#일반용과 미니게임 용
slimeJM = []
slimeJM2 = []                                           
for i in range(0,8):
    slimeJM.append(s2.image_at((1+slimetu2[0]*(i+5), 1+slimetu2[1]*2, slimetu[0] , slimetu[2])))
    slimeJM[i] = pygame.transform.scale(slimeJM[i],(slimetu[0]*3,slimetu[2]*3))
    slimeJM2.append(s2.image_at((1+slimetu2[0]*(i+5), 1+slimetu2[1]*2, slimetu[0] , slimetu[2])))                                       
    slimeJM2[i] = pygame.transform.scale(slimeJM2[i],(slimetu[0]*2,slimetu[2]*2))

#
#미니게임용 추가 이미지
#    
slimeB2 = []
slimeB2.append(s2.image_at((1, 1+slimetu2[1]*(2), slimetu[0] , slimetu[1])))
slimeB2[0] = pygame.transform.scale(slimeB2[0],(slimetu[0]*2,slimetu[1]*2))

#3종의 버튼
btntu = (27,17,38,26)
btntu2 = (29,19,40,28)

btnBase = []
for i in range(0,4) :
    btnBase.append(s3.image_at((1+btntu2[0]*i, 1, btntu[0] , btntu[0])))
    btnBase[i] = pygame.transform.scale(btnBase[i],(btntu[0]*3,btntu[0]*3))
    
btnCtrl = []
for i in range(0,3) :
    btnCtrl.append(s3.image_at((1+btntu2[1]*i+btntu2[0]*4, 1, btntu[1] , btntu[1])))
    btnCtrl[i] = pygame.transform.scale(btnCtrl[i],(btntu[1]*3,btntu[1]*3))
for i in range(0,3) :
    btnCtrl.append(s3.image_at((1+btntu2[1]*i+btntu2[0]*4, 1+btntu2[1], btntu[1] , btntu[1])))
    btnCtrl[i+3] = pygame.transform.scale(btnCtrl[i+3],(btntu[1]*3,btntu[1]*3))
    
btnGame = []
for i in range(0,3) :
    btnGame.append(s3.image_at((1+btntu2[2]*i, 1+btntu2[1]*2, btntu[2] , btntu[2])))
    btnGame[i] = pygame.transform.scale(btnGame[i],(btntu[2]*3,btntu[2]*3))

#친구 버튼
btnFriend = []

btnFriend.append(s3.image_at((1, 1+btntu2[1]*2+btntu2[2], btntu[3],btntu[3])))
btnFriend[0] = pygame.transform.scale(btnFriend[0],(btntu[3]*3,btntu[3]*3))
btnFriend.append(s3.image_at((1+btntu2[3], 1+btntu2[1]*2+btntu2[2], btntu[3],btntu[3])))
btnFriend[1] = pygame.transform.scale(btnFriend[1],(btntu[3]*3,btntu[3]*3))


#다양한 버튼들의 선택 틀도 저장한다.
btnBaseSel = s3.image_at((1, 1+btntu2[1]*2+btntu2[2]+btntu2[3], btntu[0],btntu[0]))
btnBaseSel = pygame.transform.scale(btnBaseSel, (btntu[0]*3, btntu[0]*3))

btnCtrlSel = s3.image_at((1+btntu2[0], 1+btntu2[1]*2+btntu2[2]+btntu2[3], btntu[1],btntu[1]))
btnCtrlSel = pygame.transform.scale(btnCtrlSel, (btntu[1]*3, btntu[1]*3))

btnGameSel = s3.image_at((1+btntu2[0]+btntu2[1], 1+btntu2[1]*2+btntu2[2]+btntu2[3], btntu[2],btntu[2]))
btnGameSel = pygame.transform.scale(btnGameSel, (btntu[2]*3, btntu[2]*3))

btnFriendSel = s3.image_at((1+btntu2[0]+btntu2[1]+btntu2[2], 1+btntu2[1]*2+btntu2[2]+btntu2[3], btntu[3],btntu[3]))
btnFriendSel = pygame.transform.scale(btnFriendSel, (btntu[3]*3, btntu[3]*3))

                 
#줄넘기는 직접 그려서 해결하자!
#전방향 1칸씩
#던전60,60
#계단68,22
#구름127, 80
#dt[3] = 70 등으로 불러온다.
#미니게임은 2배율만 한다!
gtu = (60,68,22,127,80)
gtu2 = (62,70,24,129,82)

dun_block = []
for i in range(0,5) :
    dun_block.append(s4.image_at((1+gtu2[0]*i, 1, gtu[0] , gtu[0])))
    dun_block[i] = pygame.transform.scale(dun_block[i],(gtu[0]*2,gtu[0]*2))
for i in range(0,5) :
    dun_block.append(s4.image_at((1+gtu2[0]*(i+9), 1, gtu[0] , gtu[0])))
    dun_block[i+5] = pygame.transform.scale(dun_block[i+5],(gtu[0]*2,gtu[0]*2))

dun_ghost = []
for i in range(0,4):
    dun_ghost.append(s4.image_at((1+gtu2[0]*(i+5), 1, gtu[0] , gtu[0])))
    dun_ghost[i] = pygame.transform.scale(dun_ghost[i],(gtu[0]*2,gtu[0]*2))
    
stair_block = []
for i in range(0,6):
    stair_block.append(s4.image_at((1+gtu2[1]*i, 1+gtu2[0], gtu[1] , gtu[2])))
    stair_block[i] = pygame.transform.scale(stair_block[i],(gtu[1]*2,gtu[2]*2))

stair_cloud = []
for i in range(0,6) : 
    stair_cloud.append(s4.image_at((1+gtu2[3]*i, 1+gtu2[0]+gtu2[2], gtu[3] , gtu[4])))
    stair_cloud[i] = pygame.transform.scale(stair_cloud[i],(gtu[3]*2,gtu[4]*2))
for i in range(0,6) : 
    stair_cloud.append(s4.image_at((1+gtu2[3]*i, 1+gtu2[0]+gtu2[2]+gtu2[4], gtu[3] , gtu[4])))
    stair_cloud[i] = pygame.transform.scale(stair_cloud[i],(gtu[3]*2,gtu[4]*2))

#애니메이션용 동전 10개
all_coin = []
for i in range(0,10):
    all_coin.append(s4.image_at((1+gtu2[0]*i, 1+gtu2[0]+gtu2[2]+gtu2[4]*2, gtu[0] , gtu[0])))
    all_coin[i] = pygame.transform.scale(all_coin[i],(gtu[0]+30 , gtu[0]+30))
    
#애니메이션용 섬광과 별 4개
stair_shine = []
for i in range(0,4):
    stair_shine.append(s4.image_at((1+gtu2[0]*(i+10), 1+gtu2[0]+gtu2[2]+gtu2[4]*2, gtu[0] , gtu[0])))
    stair_shine[i] = pygame.transform.scale(stair_shine[i],(gtu[0]*2 , gtu[0]*2))
    
#횃불 애니메이션 6개
dun_fire = []
for i in range(0,6):
    dun_fire.append(s4.image_at((1+gtu2[0]*i, 1+gtu2[0]*2+gtu2[2]+gtu2[4]*2, gtu[0] , gtu[0])))
    dun_fire[i] = pygame.transform.scale(dun_fire[i],(gtu[0]*2 , gtu[0]*2))

#보석 이미지 10개

all_jem = []
for i in range(0,10):
    all_jem.append(s4.image_at((1+gtu2[0]*(i+6), 1+gtu2[0]*2+gtu2[2]+gtu2[4]*2, gtu[0] , gtu[0]))) 
    all_jem[i] = pygame.transform.scale(all_jem[i],(gtu[0]*2 , gtu[0]*2))
   
#줄넘기 돌리는 도우미
rope_helper = []
for i in range(0,9):
    rope_helper.append(s4.image_at((1+gtu2[0]*i, 1+gtu2[0]*3+gtu2[2]+gtu2[4]*2, gtu[0] , gtu[0])))
    rope_helper[i] = pygame.transform.scale(rope_helper[i],(gtu[0]*2 , gtu[0]*2))

#유성
stair_meteor = []
for i in range(0,6):
    stair_meteor.append(s4.image_at((1+gtu2[0]*(i+9), 1+gtu2[0]*3+gtu2[2]+gtu2[4]*2, gtu[0] , gtu[0])))
    stair_meteor[i] = pygame.transform.scale(stair_meteor[i],(gtu[0]*2 , gtu[0]*2))

#게임 숫자 표시 기능
all_numberFont = []
for i in range(0,10):
    all_numberFont.append(s4.image_at((1+gtu2[0]*i, 1+gtu2[0]*4+gtu2[2]+gtu2[4]*2, gtu[0] , gtu[0])))
    all_numberFont[i] = pygame.transform.scale(all_numberFont[i],(gtu[0]*2 , gtu[0]*2))

#스코어(4), 플레이어게인(6), 시작(4), 코인(3), 게임오버(6)
all_order = []

all_order.append(s4.image_at((1, 1+gtu2[0]*5+gtu2[2]+gtu2[4]*2, gtu[0]+gtu2[0]*3 , gtu[0])))
#all_order[0] = pygame.transform.scale(all_order[0],(gtu[0]*2+gtu2[0]*6 , gtu[0]*2))

all_order.append(s4.image_at((1+gtu2[0]*4, 1+gtu2[0]*5+gtu2[2]+gtu2[4]*2, gtu[0]+gtu2[0]*5 , gtu[0])))
#all_order[1] = pygame.transform.scale(all_order[1],(gtu[0]*2+gtu2[0]*10 , gtu[0]*2))

all_order.append(s4.image_at((1+gtu2[0]*10, 1+gtu2[0]*5+gtu2[2]+gtu2[4]*2, gtu[0]+gtu2[0]*3 , gtu[0])))
all_order[2] = pygame.transform.scale(all_order[2],(369 , 90))

all_order.append(s4.image_at((1, 1+gtu2[0]*6+gtu2[2]+gtu2[4]*2, gtu[0]+gtu2[0]*2 , gtu[0])))
#all_order[3] = pygame.transform.scale(all_order[3],(gtu[0]*2+gtu2[0]*4 , gtu[0]*2))

all_order.append(s4.image_at((1+gtu2[0]*3, 1+gtu2[0]*6+gtu2[2]+gtu2[4]*2, gtu[0]+gtu2[0]*5 , gtu[0])))
#all_order[4] = pygame.transform.scale(all_order[4],(gtu[0]*2+gtu2[0]*10 , gtu[0]*2))


#우주 이미지
#우주 911 3426
stair_space = s5.image_at((1,1,911,3426))

'''
slime1 = s2.image_at((0,0,56,39))
slimeE1 = s2.image_at((56,0,56,39))
slimeEE1 = s2.image_at((112,0,56,39))
#3배율 사용!
img2 = pygame.transform.scale(img1,(450,357))
slime2 = pygame.transform.scale(slime1,(168,117))
slimeE2 = pygame.transform.scale(slimeE1,(168,117))
slimeEE2 = pygame.transform.scale(slimeEE1,(168,117))
#자르기 연구
#image3 = pygame.image.load('스프라이트_슬라임형태.png').convert_alpha()
#image33 = image3.subsurface((0,0,50,50))

#working하는 동안에는 동작이 되지 않는다. 다중 입력을 막는다
working = 0
emotion = -1

'''

#



#------------ 인자 모아둠 --------------------------
global On_norm
On_norm = 1
global On_game
On_game = 0
global On_miniGame_stair
On_miniGame_stair = 0
global On_miniGame_dun
On_miniGame_dun = 0


On_work = 0
On_aniCount = 0
key_delay = 0

norm_num = 0
motion_num = 0

btnB_active = 0
global btnB_ani
btnB_ani = 0

btnC_active = 0
global btnC_ani
btnC_ani = 0

btnG_active = 0
global btnG_ani
btnG_ani = 0


On_miniGame_stair = 0
On_miniGame_Dun = 0
global drag_x
drag_x = 0
global drag_y
drag_y = 0
global impSlime
#계단 생성 리스트 8개 기본으로 가지고 있기
stairs = []
prepare = 0
global coin_motion_num
coin_motion_num = 0

game_start_time_num = 0
game_end_time_num = 0

game_stair_reverse_check = 0
game_stair_reverse_state = 0



#이제 버튼은 이걸로 관리한다. 아무 선택이 되지 않은 것은 -1로 지
btnB_on = -1
btnC_on = -1
btnG_on = -1

#세부 선택 버튼
Sel_key = 0

#메뉴 선택용 임시 인수
mode = 0


#---------------------------------------------------

#아이템 목록
item_coin = 0
item_jem = [0,0,0,0,0,0]
item_jemS = [0,0,0,0]

'''
item_jem1 = 0
item_jem2 = 0
item_jem3 = 0
item_jem4 = 0
item_jem5 = 0
item_jem6 = 0
item_jemS1 = 0
item_jemS2 = 0
item_jemS3 = 0
item_jemS4 = 0
'''

#---------------------------------------------------

#새로운 UI 인자들


check_level = 1
Mode_case = 1
Main_case = 0
Sub_case = 0
Sel_case = 0

Sek_item = 0




#---------------------------------------------------

def call_back(types):
    screen.blit(base[0], (0,0))

def call_character(type, base, emo):
    screen.blit (slimeB[base], (150,150))
    screen.blit (slimeE[emo], (150,150))
    '''
    screen.blit (btnBase[0], (50,10))
    screen.blit (btnBase[1], (50,100))
    screen.blit (btnBase[2], (50,190))
    screen.blit (btnBase[3], (50,280))

    '''

#일반 상태 함수
def make_anime_sl_norm(num) :
    if(num >=0 and num < 8):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[0], (150,150))
    elif(num >=8 and num < 16):
        screen.blit (slimeB[1], (150,150))
        screen.blit (slimeE[0], (150,151))
    elif(num >=16 and num < 24):
        screen.blit (slimeB[2], (150,150))
        screen.blit (slimeE[0], (150,151))
    elif(num >=24 and num < 32):
        screen.blit (slimeB[1], (150,150))
        screen.blit (slimeE[0], (150,151))
    elif(num >=32 and num < 40):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[0], (150,150))
    else:
        screen.blit (slimeB[1], (80,80))
        screen.blit (slimeE[0], (80,80))

    back = num + 1
    return back

#먹기 함수
def make_anime_sl_jm(num):
    #테스트용 예시
    #screen.blit (slimeB[6], (150,150))
    #screen.blit (slimeE[6], (150,150))

    #보정이 필요하다 -24(8x3)만큼, 원래 기본보다 픽셀 크기 자체가 달라서
    #상승 (0~4)
    if(num < 2):
        screen.blit(slimeJM[0], (150,126))
    elif(num < 4):
        screen.blit(slimeJM[1], (150,124-6))
    elif(num < 6):
        screen.blit(slimeJM[2], (150,122-12))
    elif(num < 8):
        screen.blit(slimeJM[3], (150,120-18))
    elif(num < 10):
        screen.blit(slimeJM[4], (150,118-24))
    #하강(5~9)
    elif(num < 12):
        screen.blit(slimeJM[5], (150,121-18))
    elif(num < 14):
        screen.blit(slimeJM[6], (150,124-12))
    elif(num < 16):
        screen.blit(slimeJM[7], (150,126-6))
    elif(num < 18):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[2], (150,150))
    elif(num < 20):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[1], (150,150))
    else:
        screen.blit (slimeB[0], (80,80))
        screen.blit (slimeE[0], (80,80))
    back = num + 1
    return back

#게임 내 점프 함수
#크기 감소로 인해 좌표를 28,47만큼 보정해서 중앙으로 보낸다.
#스프라이트 크기 차이에 대한 y좌표는 16(8X2)만큼 보정한다.
#규칙을 바꾸면서 슬라임이 제자리에서 움직이도록 바꿨다. 화면만 움직인다.
#추가적인 점프를 추가한다.
def make_anime_sl_mgjm(num,dir):
    global impSlime
    global drag_x
    global drag_y
    if(num < 1):
        if dir==1:
            #screen.blit(slimeJM2[0], (178+17*1,173-12*1))
            screen.blit(slimeJM2[0], (178,173-4*1))
            drag_x = drag_x+17
            drag_y = drag_y-12
        else :
            impSlime = pygame.transform.flip(slimeJM2[0], True, False)
            #screen.blit(impSlime, (178-17*1,173-12*1))
            screen.blit(impSlime, (178,173-4*1))
            drag_x = drag_x-17
            drag_y = drag_y-12
    elif(num < 2):
        if dir==1:
            #screen.blit(slimeJM2[1], (178+17*2,173-12*2))
            screen.blit(slimeJM2[1], (178,173-4*2))
            drag_x = drag_x+17
            drag_y = drag_y-12
        else :
            impSlime = pygame.transform.flip(slimeJM2[1], True, False)
            #screen.blit(impSlime, (178-17*2,173-12*2))
            screen.blit(impSlime, (178,173-4*2))
            drag_x = drag_x-17
            drag_y = drag_y-12
    elif(num < 3):
        if dir==1:
            #screen.blit(slimeJM2[2], (178+17*3,173-12*3))
            screen.blit(slimeJM2[2], (178,173-4*3))
            drag_x = drag_x+17
            drag_y = drag_y-12
        else :
            impSlime = pygame.transform.flip(slimeJM2[2], True, False)
            #screen.blit(impSlime, (178-17*3,173-12*3))
            screen.blit(impSlime, (178,173-4*3))
            drag_x = drag_x-17
            drag_y = drag_y-12
    elif(num < 4):
        if dir==1:
            #screen.blit(slimeJM2[3], (178+17*4,173-12*4))
            screen.blit(slimeJM2[3], (178,173-4*4))
            drag_x = drag_x+17
            drag_y = drag_y-12
        else :
            impSlime = pygame.transform.flip(slimeJM2[3], True, False)
            #screen.blit(impSlime, (178-17*4,173-12*4))
            screen.blit(impSlime, (178,173-4*4))
            drag_x = drag_x-17
            drag_y = drag_y-12
    elif(num < 5):
        if dir==1:
            #screen.blit(slimeJM2[4], (178+17*5,173-12*5))
            screen.blit(slimeJM2[4], (178,173-4*5))
            drag_x = drag_x+17
            drag_y = drag_y-12
        else :
            impSlime = pygame.transform.flip(slimeJM2[4], True, False)
            #screen.blit(impSlime, (178-17*5,173-12*5))
            screen.blit(impSlime, (178,173-4*5))
            drag_x = drag_x-17
            drag_y = drag_y-12
    #하강(5~9)
    elif(num < 6):
        if dir==1:
            #screen.blit(slimeJM2[5], (178+17*6,173-12*5+6))
            screen.blit(slimeJM2[5], (178,173-4*4))
            drag_x = drag_x+17
            drag_y = drag_y+6
        else :
            impSlime = pygame.transform.flip(slimeJM2[5], True, False)
            #screen.blit(impSlime, (178-17*6,173-12*5+6))
            screen.blit(impSlime, (178,173-4*4))
            drag_x = drag_x-17
            drag_y = drag_y+6
    elif(num < 7):
        if dir==1:
            #screen.blit(slimeJM2[6], (178+17*7,173-12*5+11))
            screen.blit(slimeJM2[6], (178,173-4*3))
            drag_x = drag_x+17
            drag_y = drag_y+5
        else :
            impSlime = pygame.transform.flip(slimeJM2[6], True, False)
            #screen.blit(impSlime, (178-17*7,173-12*5+11))
            screen.blit(impSlime, (178,173-4*3))
            drag_x = drag_x-17
            drag_y = drag_y+5
    elif(num < 8):
        if dir==1:
            #screen.blit(slimeJM2[7], (178+17*8,173-12*5+16))
            screen.blit(slimeJM2[7], (178,173-4*2))
            drag_x = drag_x+17
            drag_y = drag_y+5
        else :
            impSlime = pygame.transform.flip(slimeJM2[7], True, False)
            #screen.blit(impSlime, (178-17*8,173-12*5+16))
            screen.blit(impSlime, (178,173-4*2))
            drag_x = drag_x-17
            drag_y = drag_y+5
    elif(num < 9):
        if dir==1:
            #screen.blit(slimeB2[0], (178+17*8,173-12*5+16+16))
            #screen.blit(slimeE2[2], (178+17*8,173-12*5+16+16))
            screen.blit(slimeB2[0], (178,189-4))
            screen.blit(slimeE2[2], (178,189-4))
        else :
            impSlime = pygame.transform.flip(slimeB2[0], True, False)
            #screen.blit(impSlime, (178-17*8,173-12*5+16+16))
            screen.blit(impSlime, (178,189-4))
            impSlime = pygame.transform.flip(slimeE2[2], True, False)
            #screen.blit(impSlime, (178-17*8,173-12*5+16+16))
            screen.blit(impSlime, (178,189-4))
    elif(num < 10):
        if dir==1:
            #screen.blit(slimeB2[0], (178+17*8,173-12*5+16+16))
            #screen.blit(slimeE2[1], (178+17*8,173-12*5+16+16))
            screen.blit(slimeB2[0], (178,189))
            screen.blit(slimeE2[1], (178,189))
        else :
            impSlime = pygame.transform.flip(slimeB2[0], True, False)
            #screen.blit(impSlime, (178-17*8,173-12*5+16+16))
            screen.blit(impSlime, (178,189))
            impSlime = pygame.transform.flip(slimeE2[1], True, False)
            #screen.blit(impSlime, (178-17*8,173-12*5+16+16))
            screen.blit(impSlime, (178,189))
    else:
        screen.blit (slimeB2[0], (80,80))
        screen.blit (slimeE2[0], (80,80))
    back = num + 1
    return back

def make_anime_sl_eat(num):
    #입 벌리기
    if(num < 2):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[4], (150,150))
    elif(num < 4):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[5], (150,150))
    elif( num < 6):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[6], (150,150))
    elif(num < 8):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[7], (150,150))
    elif(num < 12):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[8], (150,150))
    #입 다물기
    elif(num < 14):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[9], (150,150))
    elif(num < 16):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[10], (150,150))
    elif(num < 18):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[1], (150,150))
    else:
        screen.blit (slimeB[0], (80,80))
        screen.blit (slimeE[0], (80,80))

    back = num + 1
    return back


def make_anime_sl_fear(num):
    if(num < 2):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[11], (150,150))
    elif(num < 4):
        screen.blit (slimeB[0], (150,150))
        screen.blit (slimeE[12], (150,150))
    elif( num < 6):
        screen.blit (slimeB[0], (148,150))
        screen.blit (slimeE[13], (148,150))
    elif(num < 8):
        screen.blit (slimeB[0], (145,150))
        screen.blit (slimeE[14], (145,150))
    elif(num < 14):
        screen.blit (slimeB[0], (141,150))
        screen.blit (slimeE[15], (141,150))
    else:
        screen.blit (slimeB[0], (80,80))
        screen.blit (slimeE[0], (80,80))
        
    back = num + 1
    return back


    
'''
def exam_button(x,y,active):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if active==1:
        screen.blit (btnBase[0], (x,y))
        return 1
    elif x+81 > mouse[0] > x and y+81 > mouse[1] > y:
        screen.blit (btnBase[0], (x,y))
        if (click[0] == 1):
            return 1
        return 0
    elif x+81 > mouse[0] > x and y+81 > mouse[1] > y :
        screen.blit (btnBase[0], (x,y))
        return 1

def base_button(x,y,ext):
    global btnB_ani
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #ext는 펄쳐져 있는지 여부를 나타낸다.
    if ext == 0:
        if x+81 > mouse[0] > x and y+81 > mouse[1] > y and click[0] == 1:
            screen.blit (btnBase[1], (x,y))
            return 1
        else :
            screen.blit (btnBase[1], (x,y))
            return 0
    elif ext == 1:
        screen.blit (btnBase[3], (x,y-10*btnB_ani))
        screen.blit (btnBase[2], (x,y-5*btnB_ani))
        screen.blit (btnBase[1], (x,y))
        if btnB_ani < 17:
            btnB_ani = btnB_ani + 3
        if not(x+81 > mouse[0] > x and y+81 > mouse[1] > y) and click[0] == 1:
            btnB_ani = 0
            btnC_ani = 0
            btnG_ani = 0
            return 0
        return 1

def ctrl_button(x,y,ext):
    global btnC_ani
    global On_game
    global On_norm
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if ext == 0:
        if x+51 > mouse[0] > x and y+51 > mouse[1] > y and click[0] == 1:
            screen.blit (btnCtrl[0], (x,y))
            return 1
        else :
            screen.blit (btnCtrl[0], (x,y))
            return 0
    elif ext == 1:
        #3칸씩 18회 1~5 배수로 이동
        screen.blit (btnCtrl[5], (x,y+15*btnC_ani))
        screen.blit (btnCtrl[4], (x,y+12*btnC_ani))
        screen.blit (btnCtrl[3], (x,y+9*btnC_ani))
        screen.blit (btnCtrl[2], (x,y+6*btnC_ani))
        screen.blit (btnCtrl[1], (x,y+3*btnC_ani))
        screen.blit (btnCtrl[0], (x,y))
        if btnC_ani < 18:
            btnC_ani = btnC_ani + 3
        if x+51 > mouse[0] > x and y+51+12*18 > mouse[1] > y+12*18 and click[0] == 1:
            On_norm = 0
            On_game = 1
            return 0
        if not(x+51 > mouse[0] > x and y+51 > mouse[1] > y) and click[0] == 1:
            btnB_ani = 0
            btnC_ani = 0
            btnG_ani = 0    
            return 0
        return 1

def game_button(x,y):
    global btnG_ani
    global On_game
    global On_norm
    global On_miniGame_stair
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

        #3칸씩 18회 1~5 배수로 이동
    screen.blit (btnGame[2], (x+8*btnG_ani,y))
    screen.blit (btnGame[1], (x+4*btnG_ani,y))
    screen.blit (btnGame[0], (x,y))
    if btnG_ani < 36:
        btnG_ani = btnG_ani + 3
    if x+114 > mouse[0] > x and y+114 > mouse[1] > y and click[0] == 1:
        On_miniGame_stair = 1
    elif not(x+114 > mouse[0] > x and y+114 > mouse[1] > y) and click[0] == 1:
        btnB_ani = 0
        btnC_ani = 0
        #btnG_ani = 0
        if btnG_ani == 36 :
            btnG_ani = 0
            On_norm = 1
            On_game = 0
        return 0
    return 1

'''
def drag_ctrlx():
    global drag_x
    if drag_x == 0:
        return 0
    elif drag_x < 0:
        if drag_x <= -8:
            drag_x = drag_x + 8
        elif drag_x > -8:
            drag_x = 0
    elif drag_x > 0:
        if drag_x >= 8:
            drag_x = drag_x - 8
        elif drag_x < 8:
            drag_x = 0
        

def drag_ctrly():
    global drag_y
    if drag_y == 0:
        return 0
    elif drag_y < 0:
        if drag_y <= -3:
            drag_y = drag_y + 3
        elif drag_y > -3:
            drag_y = 0
    elif drag_y > 0:
        if drag_y >= 3:
            drag_y = drag_x - 3
        elif drag_y < 3:
            drag_y = 0
            
#계단 그리기
#y좌표에 해당하는 num은 1씩 늘려주기만 하면 되고
#x대 대한 랜덤 처리는 본 함수에서 처리한다.
def make_stair(x,num):
    global drag_x
    global drag_y
    if num <= 30:
        screen.blit (stair_block[0], (164-drag_x+136*x,263-drag_y-44*num))
    elif num <= 60:
        screen.blit (stair_block[1], (164-drag_x+136*x,263-drag_y-44*num))
    elif num <= 90 :
        screen.blit (stair_block[2], (164-drag_x+136*x,263-drag_y-44*num))
    elif num <= 150 :
        screen.blit (stair_block[3], (164-drag_x+136*x,263-drag_y-44*num))
    elif num <= 250 :
        screen.blit (stair_block[4], (164-drag_x+136*x,263-drag_y-44*num))
    #return (num+1)

#보상 그리기
def draw_prize(x,num,type):
    #type 1,2는 동전, 3~8은 보석, 9는 은하
    global drag_x
    global drag_y
    if type == 0:
        return
    elif type == 1:
        #동전 그리기
        screen.blit (all_coin[coin_motion_num], (164-drag_x+136*x+20,263-drag_y-44*num-85))
    elif type == 2:
        #섬광 동전 그리기
        screen.blit (all_coin[coin_motion_num], (164-drag_x+136*x+20,263-drag_y-44*num-85))
        return
    else :
        screen.blit (all_jem[type-3], (164-drag_x+136*x+10,263-drag_y-44*num-95))
    return

def make_rand_stair(x):
    i = random.randrange(0,2)
    if i == 0 and x>-8:
        return x-1
    elif i == 1 and x < 8:
        return x+1
    elif x<= -8 :
        return x+1
    elif x>= 8 :
        return x-1

#미리 계단 만들어 두기(함수 아님)
#항상 8개를 유지한다.
stairs = []
prizeType = []
total_stair = 0


#구간에 따라 보상을 랜덤하게 생성한다.
#0 : 없음 / 1 : 동전 / 2 : 함정 동전 / 3~8 : 보석1~6 / 9 : 은하석
def make_rand_prize(x):
    bonus = 4
    if x == 1:
        return 0
    if x < 30 :
        bonus = 6
    elif x < 60:
        bonus  = 8
    elif x < 90:
        bonus = 11
    elif x < 120 :
        bonus = 15
    elif x < 150 :
        bonus = 20
    elif x < 180 :
        bonus = 32
    else :
        bonus = 50
    i = random.randrange(0,20000)
    if i < 2*bonus:
        return 9
    elif i < 5*bonus:
        return 8
    elif i < 8*bonus:
        return 7
    elif i < 11*bonus:
        return 6
    elif i < 14*bonus:
        return 5
    elif i < 17*bonus:
        return 4
    elif i < 20*bonus:
        return 3
    elif i < 80*bonus:
        return 2
    elif i < 400*bonus:
        return 1
    else :
        return 0

def Get_Prize(type):
    global item_coin
    global item_jem
    global item_jemS
    if type == 1 or type == 2:
        item_coin = item_coin + 1
    elif type == 3:
        item_jem[0] = item_jem[0] + 1
    elif type == 4:
        item_jem[1] = item_jem[1] + 1
    elif type == 5:
        item_jem[2] = item_jem[2] + 1  
    elif type == 6:
        item_jem[3] = item_jem[3] + 1
    elif type == 7:
        item_jem[4] = item_jem[4] + 1
    elif type == 8:
        item_jem[5] = item_jem[5] + 1
    elif type == 9:
        item_jemS[0] = item_jemS[0] + 1
    elif type == 10:
        item_jemS[1] = item_jemS[1] + 1
    elif type == 11 :
        item_jemS[2] = item_jemS[2] + 1
    elif type == 12 :
        item_jemS[3] = item_jemS[3] + 1
        
#환경설정 UI 함수
def UI_SETTING(sel):
    global Sel_case
    
    screen.blit (back_big, (0,0))
      
    #fontObj = pygame.font.Font('arial', 50) 다른 방식이나 여기서는 불가..
    
    fontObj = pygame.font.SysFont('arial',20)
    # 폰트를 가져오고 크기도 설정한다.
    
    textSurfaceObj = fontObj.render('Face Recognition', True, (0,0,0))
    # 텍스트 객체를 생성한다. 첫번째 파라미터는 텍스트 내용, 두번째는 Anti-aliasing 사용 여부, 세번째는 텍스트 컬러를 나타낸다
    
    textRectObj = textSurfaceObj.get_rect();
    # 텍스트 객체의 출력 위치를 가져온다

    textRectObj = (36, 36, 0, 0)
    # 텍스트 객체의 출력 좌표를 설정한다 (뒤의 값 2개는 넣지 않아도 좋다)

    screen.blit(textSurfaceObj, textRectObj)

    textSurfaceObj = fontObj.render('Language', True, (0,0,0))
    textRectObj = textSurfaceObj.get_rect();
    textRectObj = (36, 126, 0, 0)
    screen.blit(textSurfaceObj, textRectObj)
    '''
    #이 명령어를 통해 가능한 폰트들을 검색 가능하다.
    l = pygame.font.get_fonts()
    print(l)
    sleep(5000)
    '''
    

    
    
#아이템 UI 함수
def UI_ITEM(sel):
    global item_coin
    global item_jem
    global item_jemS
    global Sel_case
    
    screen.blit (back_big, (0,0))
    screen.blit (money_slot, (282,12))

    #골드 표기용 글씨
    fontObj = pygame.font.SysFont('arial',16)
    textSurfaceObj = fontObj.render(str(item_coin), True, (255,255,255))
    textRectObj = textSurfaceObj.get_rect();
    textRectObj = (282+10, 12+1, 0, 0)
    screen.blit(textSurfaceObj, textRectObj)

    #게임 아이템 표기용 글씨
    fontObj = pygame.font.SysFont('arial',14)
    

    
    for i in range(0,3):
        for j in range(0,4):
            screen.blit (item_slot, (36+(90+6)*(j),36+(90+6)*(i)))

    for i in range(0,4):
        screen.blit (all_jem[i], (36+(90+6)*(i)-15,36-8))
        if item_jem[i] == 0:
            screen.blit (item_nonslot, (36+(90+6)*(i),36))
        else :
            textSurfaceObj = fontObj.render(str(item_jem[i]), True, (0,0,0))
            textRectObj = textSurfaceObj.get_rect();
            textRectObj = (36+(90+6)*(i)+90-20,36+90-28, 0, 0)
            screen.blit(textSurfaceObj, textRectObj)
            
    for i in range(0,2):
        screen.blit (all_jem[i+4], (36+(90+6)*(i)-15,36-8+96))
        if item_jem[i+4] == 0:
            screen.blit (item_nonslot, (36+(90+6)*(i),36+96))
        else :
            textSurfaceObj = fontObj.render(str(item_jem[i+4]), True, (0,0,0))
            textRectObj = textSurfaceObj.get_rect();
            textRectObj = (36+(90+6)*(i)+90-20,36+96+90-28, 0, 0)
            screen.blit(textSurfaceObj, textRectObj)
            
        
    for i in range(0,2):
        screen.blit (all_jem[i+6], (36+(90+6)*(i+2)-15,36-8+96))
        if item_jemS[i] == 0:
            screen.blit (item_nonslot, (36+(90+6)*(i+2),36+96))
        else :
            textSurfaceObj = fontObj.render(str(item_jemS[i]), True, (0,0,0))
            textRectObj = textSurfaceObj.get_rect();
            textRectObj = (36+(90+6)*(i+2)+90-20,36+96+90-28, 0, 0)
            screen.blit(textSurfaceObj, textRectObj)
        
    for i in range(0,2):
        screen.blit (all_jem[i+8], (36+(90+6)*(i)-15,36-8+96*2))
        if item_jemS[i+2] == 0:
           screen.blit (item_nonslot,  (36+(90+6)*(i),36+96*2))
        else :
            textSurfaceObj = fontObj.render(str(item_jemS[i+2]), True, (0,0,0))
            textRectObj = textSurfaceObj.get_rect();
            textRectObj = (36+(90+6)*(i)+90-20,36+96*2+90-28, 0, 0)
            screen.blit(textSurfaceObj, textRectObj)

    
    if 1<= Sel_case <= 4:
        screen.blit(item_selected, (36+(90+6)*(Sel_case-1),36+(90+6)*(0)))
    elif 5 <= Sel_case <= 8:
        screen.blit(item_selected, (36+(90+6)*(Sel_case-5),36+(90+6)*(1)))
    elif 9 <= Sel_case <= 12:
        screen.blit(item_selected, (36+(90+6)*(Sel_case-9),36+(90+6)*(2)))
    
    if sel == 1:
        if Sel_case < 12 :
            Sel_case = Sel_case + 1
        else :
            Sel_case = 1
            
    if sel == 2:
        if Sel_case > 1:
            Sel_case = Sel_case -1
        else :
            Sel_case = 12

    if sel == 3:
        if Sel_case > 4:
            Sel_case = Sel_case -4
        else :
            Sel_case = Sel_case + 8

    if sel == 4:
        if Sel_case <8:
            Sel_case = Sel_case +4
        else :
            Sel_case = Sel_case -8

        

    

def UI_AWARD():
    imp = 0

def UI_INTERIOR():
    imp = 0


#여기서 부터는 육성 UI
def UI_FOOD():
    imp = 0
def UI_PLAY():
    imp = 0
def UI_ENV():
    imp = 0


#-------------------------------------------------------------------

#-------------------------------------------------------------------
#변경된 실질 구현
        
while True:
    clock.tick(20)    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #배경 출력
    call_back(0)
    screen.blit (btnCtrl[0], (380,10))
    screen.blit (btnBase[1], (20,250))
    
    #연속 입력 방지 타이머
    if On_work == 1 :
        key_delay = key_delay + 1
    if key_delay == 3:
        On_work = 0
        key_delay = 0
        
    

    #키 입력 받기 On_work가 0일 때, 즉 애니메이션이 발생하지 않는 중일때만 입력 가능하다
    #키 입력 종류는 상하좌우, A(선택) / S(뒤로)이다.
    #미니게임에서 오류가 생겨서 미니게임 제외한다.
    if On_work == 0 and (check_level != 4 or Mode_case != 2):
        key_event = pygame.key.get_pressed()
        #여러개의 입력을 수행한다.
        
        if key_event[pygame.K_RIGHT]:
            if Mode_case == 1:
                #Ctrl 버튼
                if Main_case == 0:
                    Main_case = 2
                    Sub_case = 1
                    check_level=2
                #Base 뒤로 가기
                if Main_case == 1 and check_level == 2:
                    check_level = 1
                    Main_case = 0
                    btnB_ani = 0
            if check_level >= 3:
                Sel_key = 1
                    
            On_work = 1
                    
        elif key_event[pygame.K_LEFT]:
            if Mode_case == 1:
                #Base 버튼
                if Main_case == 0:
                    Main_case = 1
                    Sub_case = 3
                    check_level=2
                #Ctrl 뒤로 가기
                if Main_case == 2 and check_level == 2:
                    check_level = 1
                    Main_case = 0
                    btnC_ani = 0
            if check_level >= 3:
                Sel_key = 2
                    
            On_work = 1
                    

        elif key_event[pygame.K_UP]:
            if Mode_case == 1:
                if Main_case == 1 and check_level == 2:
                    if Sub_case > 1 :
                        Sub_case = Sub_case - 1
                    elif Sub_case == 1 :
                        Sub_case = 3
                elif Main_case == 2 and check_level == 2:
                    if Sub_case > 1:
                        Sub_case = Sub_case - 1
                    elif Sub_case == 1 :
                        Sub_case = 6
            if check_level >= 3 :
                Sel_key = 3
            On_work = 1
                        
        elif key_event[pygame.K_DOWN]:
            if Mode_case == 1:
                if Main_case == 1 and check_level == 2:
                    if Sub_case < 3:
                        Sub_case = Sub_case + 1
                    elif Sub_case == 3 :
                        Sub_case = 1
                elif Main_case == 2 and check_level == 2:
                    if Sub_case <6:
                        Sub_case = Sub_case + 1
                    elif Sub_case == 6:
                        Sub_case = 1
            if check_level >= 3:
                Sel_key = 4
            On_work = 1
            
        pygame.event.get()
        if event.type == pygame.KEYDOWN:
            if event.unicode =='a':
                if Mode_case == 1:
                    if Main_case > 0 and check_level== 2:
                        check_level = check_level + 1
                        Sel_case = 1
                if check_level >= 3:
                    Sel_key = 5
                    if Mode_case == 2:
                        check_level = 4
                On_work = 1
            elif event.unicode =='s':
                if check_level == 2:
                    check_level = 1
                    Main_case = 0
                    Sub_case = 0
                elif check_level == 3:
                    Mode_case = 1
                    check_level = 2
                    if Main_case == 1:
                        btnB_ani = 18
                    elif Main_case == 2:
                        btnC_ani = 18
                    Sel_case = 0
                else :
                    check_level = 1
                if check_level >= 3:
                    Sel_key = 6
                        
                On_work = 1
       
    
    #출력 관련-------------------------------------------------------
    if Mode_case == 1:
        #기본적인 숨쉬는 애니메이션 나오는 기본 화면
        norm_num = make_anime_sl_norm(norm_num)
        if norm_num == 40:
            norm_num = 0
            
        if Main_case == 0:
            #숨쉬는 것만 표기
            imp = 0
        elif Main_case == 1:
            #육성 중 1번 ~ 3번 선택----------------------------------------
            if check_level == 2:
                #기본 좌표 설정
                x = 20
                y = 250
                #해당 좌표 기준으로 출력
                screen.blit (btnBase[3], (x,y-10*btnB_ani))
                screen.blit (btnBase[2], (x,y-5*btnB_ani))
                screen.blit (btnBase[1], (x,y))
                
                if Sub_case == 1:
                    screen.blit (btnBaseSel, (x,y-10*btnB_ani))                    
                elif Sub_case == 2:
                    screen.blit (btnBaseSel, (x,y-5*btnB_ani))   
                elif Sub_case == 3:
                    screen.blit (btnBaseSel, (x,y))
                    
                if btnB_ani < 18:
                    btnB_ani = btnB_ani + 3

            elif check_level == 3:
                imp = 0
                
            
        #컨트롤 관련 UI-------------------------------------------------------
        elif Main_case == 2:
            #컨트롤 중 1번 ~ 6번 선택
            if check_level == 2 :
                x = 380
                y = 10
                #해당 좌표 기준으로 출력
                screen.blit (btnCtrl[5], (x,y+15*btnC_ani))
                screen.blit (btnCtrl[4], (x,y+12*btnC_ani))
                screen.blit (btnCtrl[3], (x,y+9*btnC_ani))
                screen.blit (btnCtrl[2], (x,y+6*btnC_ani))
                screen.blit (btnCtrl[1], (x,y+3*btnC_ani))
                screen.blit (btnCtrl[0], (x,y))

                
                if Sub_case == 1:
                    screen.blit (btnCtrlSel, (x,y))
                elif Sub_case == 2:
                    screen.blit (btnCtrlSel, (x,y+3*btnC_ani))
                elif Sub_case == 3:
                    screen.blit (btnCtrlSel, (x,y+6*btnC_ani))
                elif Sub_case == 4:
                    screen.blit (btnCtrlSel, (x,y+9*btnC_ani))
                elif Sub_case == 5:
                    screen.blit (btnCtrlSel, (x,y+12*btnC_ani))
                elif Sub_case == 6:
                    screen.blit (btnCtrlSel, (x,y+15*btnC_ani))
                if btnC_ani < 18:
                    btnC_ani = btnC_ani + 3
                    
            elif check_level == 3:
                if Sub_case == 1:
                    #나가기
                    imp = 0
                elif Sub_case == 2:
                    #환경설정
                    UI_SETTING(Sel_key)
                    Sel_key = 0
                elif Sub_case == 3:
                    #아이템
                    #check_level == 3
                    #Sel_case = 1
                    UI_ITEM(Sel_key)
                    Sel_key = 0
                elif Sub_case == 4:
                    #업적
                    imp = 0
                elif Sub_case == 5:
                    #미니게임
                    Mode_case = 2
                    Main_case = 0
                    Sub_case  = 0
                    Sel_case = 1
                    btnC_ani = 0
                    total_stair = 0
                elif Sub_case == 6:
                    #인테리어
                    imp = 0
                                   
                imp = 0


        #친구 관련 UI--------------------------------------------------------
        elif Main_case == 3:
            imp = 0
            

    #미니게임-------------------------------------------------------------
    elif Mode_case == 2:
        #게임 선택 창
        if check_level == 3:
            screen.fill((225,198,53))
            x = 24
            y = 200
            screen.blit (btnGame[2], (x+8*btnG_ani,y))
            screen.blit (btnGame[1], (x+4*btnG_ani,y))
            screen.blit (btnGame[0], (x,y))

            if 1 <= Sel_case <= 3:
                screen.blit (btnGameSel, (x+4*(Sel_case-1)*btnG_ani,y))
            
            
            if btnG_ani < 36:
                btnG_ani = btnG_ani + 3

            '''
            Sel_case = Sel_case + 1
            if Sel_case == 4:
                Sel_case = 1
            '''
            
            if Sel_key == 1:
                if Sel_case < 3:
                    Sel_case = Sel_case + 1
                else :
                    Sel_case = 1

            elif Sel_key == 2:
                if Sel_case > 1:
                    Sel_case = Sel_case - 1
                else :
                    Sel_case = 3

            Sel_key = 0

            
        #계단 미니게임----------------------------------------------------------
        elif Sel_case == 1 and check_level == 4:
            #계단 게임 진행 준비------------------
            if total_stair == 0:
                On_work = 0
                motion_num = 0
                coin_motion_num = 0
                stairs = []
                stairs.clear()
                stairs.append(0)
                prizeType = []
                prizeType.clear()
                drag_x = 0
                drag_y = 0
                imp = 0
                for i in range (1,400):
                    #랜덤 계단 생성 함
                    imp = make_rand_stair(imp)
                    stairs.append(imp)
                    prizeType.append(make_rand_prize(i))
                total_stair = 8
                game_start_time_num = 0
                game_end_time_num = 0
                game_stair_reverse_check = 0
                game_stair_reverse_state = 0
            #실질 계단 게임 진행------------------
            elif total_stair != 0:

                #동전 모션 조정
                if coin_motion_num == 10:
                    coin_motion_num = 0

                #우주 화면 표기
                screen.blit (stair_space, (-230-drag_x//5,-3070-drag_y//5))
                
                #계단 만들기와 보상 만들기
                #stairs[x]로 값을 가져올 수 있다.
                for i in range (total_stair-8,total_stair):
                    make_stair(stairs[i],i)
                for i in range (total_stair-8,total_stair):
                    draw_prize(stairs[i],i,prizeType[i])  
                #screen.blit (stair_space, (-230,-3070))


                if On_work == 0 :
                    screen.blit(slimeB2[0], (178,189))
                    screen.blit(slimeE2[0], (178,189))
         
                if game_start_time_num != -1:
                    game_start_time_num =  game_start_time_num + 1
                    if 20 >= game_start_time_num >=5 : 
                        screen.blit (all_order[2], (45,100))
                    elif game_start_time_num > 20:
                        game_start_time_num = -1
                elif On_work == 0 :
                    key_event = pygame.key.get_pressed()
                    if key_event[pygame.K_RIGHT]:
                        On_work = 2
                    if key_event[pygame.K_LEFT]:
                        On_work = 3
                elif On_work == 2 :
                    #점프 애니메이션과 먹는 모션 처리 / 5번에서 먹기 처리 / 혼란 처리
                    motion_num = make_anime_sl_mgjm(motion_num,1)
                    if motion_num == 5:
                        if (stairs[total_stair-7] - stairs[total_stair-8]) == 1:
                            Get_Prize(prizeType[total_stair-7])
                        if prizeType[total_stair-7] == 2:
                            game_stair_reverse_check = 1
                        prizeType[total_stair-7] = 0
                    elif 5 < motion_num <9:
                        if game_stair_reverse_check == 1:
                            if motion_num == 6:
                                screen.blit(stair_shine[2], (178,189))
                            elif motion_num == 7:
                                screen.blit(stair_shine[1], (178,189))
                            elif motion_num == 8:
                                screen.blit(stair_shine[0], (178,189))
                    elif motion_num == 10 :
                        motion_num = 0
                        On_work = 0
                        if (stairs[total_stair-7] - stairs[total_stair-8]) == -1:
                            On_work = 4
                        total_stair = total_stair + 1
                        game_stair_reverse_check = 0
                elif On_work == 3 :
                    #점프 애니메이션과 먹는 모션 처리 / 5번에서 먹기 처리 / 혼란 처리
                    motion_num = make_anime_sl_mgjm(motion_num,-1)
                    if motion_num == 5:
                        if (stairs[total_stair-7] - stairs[total_stair-8]) == -1:
                            Get_Prize(prizeType[total_stair-7])
                        if prizeType[total_stair-7] == 2:
                            game_stair_reverse_check = 1
                        prizeType[total_stair-7] = 0
                    elif 5 < motion_num <9:
                        if game_stair_reverse_check == 1:
                            if motion_num == 6:
                                screen.blit(stair_shine[2], (178,189))
                            elif motion_num == 7:
                                screen.blit(stair_shine[1], (178,189))
                            elif motion_num == 8:
                                screen.blit(stair_shine[0], (178,189))
                    elif motion_num == 10 :
                        motion_num = 0
                        On_work = 0
                        if (stairs[total_stair-7] - stairs[total_stair-8]) == 1:
                            On_work = 4
                        total_stair = total_stair + 1
                        game_stair_reverse_check = 0
                elif On_work == 4:
                    screen.blit (all_order[4], (45,80))
                    if game_end_time_num <15:
                        game_end_time_num = game_end_time_num + 1
                    if game_end_time_num == 15:
                        screen.blit (all_order[1], (45,150))

                    pygame.event.get()
                    if event.type == pygame.KEYDOWN:
                        if event.unicode =='a':
                            total_stair = 0
                        if event.unicode =='s':
                            Mode_case = 1
                            check_level = 1
                            On_work = 0
                            btnB_ani = 0
                            btnC_ani = 0
                
                coin_motion_num = coin_motion_num + 1
            
        #던전 미니게임------------------------------------------------------
        elif Sel_case == 2 and check_level == 4:
            imp = 0

        #줄넘기 미니게임
        elif Sel_case == 3 and check_level == 4:
            imp = 0
            




    '''
    ###-----------------------------------
    
    if On_norm == 1 :
        #이건 기본적으로 수행하는 평소 모습
        #On_work로 현재 동작 중인지 인지해 추가 명령을 막는다.
        call_back(0)
        if On_work == 0 :
            norm_num = make_anime_sl_norm(norm_num)
            if norm_num == 40:
                norm_num = 0
            #기존의 부동 출력 방식
            #call_character(0, 0, 0)

        #본격 애니메이션 받기
        if On_work == 0 :
            key_event = pygame.key.get_pressed()
            if key_event[pygame.K_UP]:
                On_work = 1
            if key_event[pygame.K_RIGHT]:
                On_work = 2
            if key_event[pygame.K_LEFT]:
                On_work = 3
                
        #이건 특별히 수행하는 애니메이션 다중 수행을 막는다.
        if On_work == 1 :
            motion_num = make_anime_sl_jm(motion_num)
            if motion_num == 20 :
                motion_num = 0
                On_work = 0
                norm_num = 0
            
        if On_work == 2 :
            motion_num = make_anime_sl_eat(motion_num)
            if motion_num == 18 :
                motion_num = 0
                On_work = 0
                norm_num = 0

        if On_work == 3 :
            motion_num = make_anime_sl_fear(motion_num)
            if motion_num == 14 :
                motion_num = 0
                On_work = 0
                norm_num = 0

        #btnB_active = exam_button(200,200,btnB_active)
        #실제 버튼 구현 부분!!        
        btnB_active = base_button(20,250,btnB_active)
        btnC_active = ctrl_button(380,10,btnC_active)
        #game_button(30,200)
        
        #pygame.draw.circle(screen, white, (pos_x, pos_y), 20)
        
#미니게임 구현 부분--------------------------------------------------------
    #게임 선택 버튼 화면
    elif On_norm == 0 and On_game == 1 and not (On_miniGame_stair == 1):
        screen.fill((225,198,53))
        game_button(24,200)
        #screen.blit (stair_space, (800,800))
        
    #처음에 계단 생성
    elif On_miniGame_stair == 1 and total_stair == 0:
        coin_motion_num = 0
        stairs = []
        stairs.append(0)
        prizeType = []
        imp = 0
        for i in range (1,400):
            #랜덤 계단 생성 함
            imp = make_rand_stair(imp)
            stairs.append(imp)
            prizeType.append(make_rand_prize(i))
        total_stair = 8
        game_start_time_num = 0
        game_end_time_num = 0
        game_stair_reverse_check = 0
        game_stair_reverse_state = 0
        
    #실질 계단 게임 진행
    elif On_miniGame_stair == 1 and total_stair != 0:

        #동전 모션 조정
        if coin_motion_num == 10:
            coin_motion_num = 0

        #우주 화면 표기
        screen.blit (stair_space, (-230-drag_x//5,-3070-drag_y//5))
        
        #계단 만들기와 보상 만들기
        #stairs[x]로 값을 가져올 수 있다.
        for i in range (total_stair-8,total_stair):
            make_stair(stairs[i],i)
        for i in range (total_stair-8,total_stair):
            draw_prize(stairs[i],i,prizeType[i])  
        #screen.blit (stair_space, (-230,-3070))
        if On_work == 0 :
            screen.blit(slimeB2[0], (178,189))
            screen.blit(slimeE2[0], (178,189))
 
        if game_start_time_num != -1:
            game_start_time_num =  game_start_time_num + 1
            if 20 >= game_start_time_num >=5 : 
                screen.blit (all_order[2], (45,100))
            elif game_start_time_num > 20:
                game_start_time_num = -1
        elif On_work == 0 :
            key_event = pygame.key.get_pressed()
            if key_event[pygame.K_RIGHT]:
                On_work = 1
            if key_event[pygame.K_LEFT]:
                On_work = 2
                
        if On_work == 1 :
            #점프 애니메이션과 먹는 모션 처리 / 5번에서 먹기 처리 / 혼란 처리
            motion_num = make_anime_sl_mgjm(motion_num,1)
            if motion_num == 5:
                if (stairs[total_stair-7] - stairs[total_stair-8]) == -1:
                    Get_Prize(prizeType[total_stair-7])
                if prizeType[total_stair-7] == 2:
                    game_stair_reverse_check = 1
                prizeType[total_stair-7] = 0
            elif 5 < motion_num <9:
                if game_stair_reverse_check == 1:
                    if motion_num == 6:
                        screen.blit(stair_shine[2], (178,189))
                    elif motion_num == 7:
                        screen.blit(stair_shine[1], (178,189))
                    elif motion_num == 8:
                        screen.blit(stair_shine[0], (178,189))
            elif motion_num == 10 :
                motion_num = 0
                On_work = 0
                norm_num = 0
                if (stairs[total_stair-7] - stairs[total_stair-8]) == -1:
                    On_work = 3
                total_stair = total_stair + 1
                game_stair_reverse_check = 0
        if On_work == 2 :
            #점프 애니메이션과 먹는 모션 처리 / 5번에서 먹기 처리 / 혼란 처리
            motion_num = make_anime_sl_mgjm(motion_num,-1)
            if motion_num == 5:
                if (stairs[total_stair-7] - stairs[total_stair-8]) == -1:
                    Get_Prize(prizeType[total_stair-7])
                if prizeType[total_stair-7] == 2:
                    game_stair_reverse_check = 1
                prizeType[total_stair-7] = 0
            elif 5 < motion_num <9:
                if game_stair_reverse_check == 1:
                    if motion_num == 6:
                        screen.blit(stair_shine[2], (178,189))
                    elif motion_num == 7:
                        screen.blit(stair_shine[1], (178,189))
                    elif motion_num == 8:
                        screen.blit(stair_shine[0], (178,189))
            elif motion_num == 10 :
                motion_num = 0
                On_work = 0
                norm_num = 0
                if (stairs[total_stair-7] - stairs[total_stair-8]) == 1:
                    On_work = 3
                total_stair = total_stair + 1
                game_stair_reverse_check = 0
        if On_work == 3:
            screen.blit (all_order[4], (45,80))
            if game_end_time_num <15:
                game_end_time_num = game_end_time_num + 1
            if game_end_time_num == 15:
                screen.blit (all_order[1], (45,150))
            # 게임을 패배했을 경우 여기로 소환된다.

        coin_motion_num = coin_motion_num + 1
    #elif  On_miniGame_Dun == 1 :
    '''
    pygame.display.update()    


        
