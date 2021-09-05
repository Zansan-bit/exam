# exam
import re
target = '@'

def check(Email):
    idx = Email.find(target)
    r = Email[idx+len(target):]
    r =f'メールアドレス{Email}のドメインは{r}'
    print(r)

check(input('入力してください'))
