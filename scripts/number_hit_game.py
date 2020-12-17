#!/usr/bin/env python3

import random
import rospy
from std_msgs.msg import Int32

rospy.init_node('game')
pub = rospy.Publisher('game', Int32, queue_size=1)
rate = rospy.Rate(10)

x = 0   # 変数定義
a = 0   # 変数定義
b = 0   # 変数定義

round = 0   # 現在のラウンド
miss = 0    # ミスした回数
flag = 0    # 0なら線形、1なら二乗の計算

a_range_factor = 10 # aの範囲を決めるための補正値
b_range_factor = 25 # bの範囲を決めるための補正値
x_range_factor = 35 # xの範囲を決めるための補正値

max_round = 10  # ゲームをやる回数
mul_round = 5   # 2乗が出てくるタイミング

# ax + b
def x_linear(tmp):
    return a * tmp + b

# ax² + b
def x_square(tmp):
    # -ax² + b
    if(tmp < 0):
        return -1 * a * tmp * tmp + b
    # +ax² + b
    else:
        return a * tmp * tmp + b

print('説明')
print('数当てゲームを10回やります。')
print('10回の合計回数をなるべく少なくしてください。')
print('入力する数値は特定の規則に乗っ取って変化します。')

# a, b, 答えを決める
while(round < max_round):
    
    # 始まるタイミングでラウンドを増やす
    round = round + 1
    print()
    print(round , end='')
    print('ステージ')

    # 乱数でa, bの値を決める
    a = random.randint(-1 * round * a_range_factor, round * a_range_factor)
    b = random.randint(-1 * round * b_range_factor, round * b_range_factor)
    
    print('以下の答えになる整数を探してください。')
    
    # 二乗が出てもよいなら乱数でどっちを出題するか決める
    if(round >= mul_round):
        flag = random.randint(0, 1)
    
    # 作成した式に範囲内で代入を行い
    if(flag == 0):
        answer = x_linear(random.randint(-1 * round * x_range_factor, round * x_range_factor))
    else:
        answer = x_square(random.randint(0, round * x_range_factor))
    
    print('xを入力してください。')
    print('今回のステージでのxの取る範囲は', -1 * round * x_range_factor , '≦ x ≦ ', round * x_range_factor, 'です。')
    print(answer)
    
    # 入力部
    while not rospy.is_shutdown():
        
        print('整数を入力してください。')
        x = input()
        
        if(flag == 0):
            x = x_linear((int)(x))
        else:
            x = x_square((int)(x))
        
        print(x)
        pub.publish(x)
        rate.sleep()
        
        if(x == answer):
            print('クリア')
            break
        else:
            miss = miss + 1

# スコアを決める
print('スコア : ', miss, '!')
