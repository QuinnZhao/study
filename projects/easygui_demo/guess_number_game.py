import easygui
import random
import sys

easygui.msgbox(msg='欢迎来到猜数游戏',
               title='欢迎页',
               ok_button='知道了'
               )
continue_ = True
user_choice = easygui.ynbox(msg='我有一个介于1到99之间的神秘数字，请你来猜一猜\n' + \
                            '不过你只有6次机会\n' +
                            '同意请选择是，否则选择否',
                            title='说明页',
                            choices=['是','否'],
                            default_choice='是'
                            )
secret_number = random.randint(1,99)
if not user_choice:
    sys.exit()

def guess(screct_number):
    tries = 0
    while tries < 6:
        num = easygui.integerbox(msg='请输入一个1到99的整数',
                                 title='输入页'
                                 )
        if num < secret_number:
            easygui.msgbox(msg='输入的数字太小了，请重新输入大一点的数字',
                           title='提示页',
                           ok_button='知道了'
                           )
        elif num > secret_number:
            easygui.msgbox(msg='输入的数字太大了，请重新输入小一点的数字',
                           title='提示页',
                           ok_button='知道了'
                           )
        else:
             return easygui.ynbox(msg='恭喜你猜对了，你真棒\n\n' + '是否还继续猜数?',
                           title='恭喜',
                           choices=['是','否']
                           )
        tries += 1
    return easygui.ynbox(msg='有些小遗憾，机会已经用完\n\n' + '是否继续，相信自己是最棒的',
                  title='鼓励页',
                  choices=['是', '否']
                  )
while continue_:
    secret_number = random.randint(1,99)
    continue_ =  guess(secret_number)
        
