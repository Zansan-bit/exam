import re
def  mail(input_string):
    if (re.search('@',input_string)):
        if (re.search('.com',input_string)):
            print("メールアドレスです")
        else :
            print('何かがおかしい')
    else:
        print('何かおかしい')

mail(input('メールアドレスを入力してください'))
