import easygui
import random
import sys

easygui.msgbox(msg='',
               title='欢迎页',
               ok_button='知道了',
               image='1.gif'
               )
continue_ = True
user_choice = easygui.ynbox(msg='',
                            title='说明页',
                            choices=['是','否'],
                            default_choice='是',
                            image='2.gif'
                            )
secret_number = random.randint(1,99)
if not user_choice:
    sys.exit()

def guess(screct_number):
    tries = 0
    while tries < 6:
        num = easygui.integerbox(msg='输入整数',
                                 title='输入页',
                                 image='5.gif'
                                 )
        if num < secret_number:
            easygui.msgbox(msg='',
                           title='提示页',
                           ok_button='知道了',
                           image='1.png'
                           )
        elif num > secret_number:
            easygui.msgbox(msg='',
                           title='提示页',
                           ok_button='知道了',
                           image='2.png'
                           )
        else:
             return easygui.ynbox(msg='恭喜',
                           title='恭喜',
                           choices=['是','否'],
                           image='3.png'
                           )
        tries += 1
    return easygui.ynbox(msg='',
                  title='鼓励页',
                  choices=['是', '否'],
                  image='4.png'
                  )
while continue_:
    secret_number = random.randint(1,99)
    continue_ =  guess(secret_number)
        
