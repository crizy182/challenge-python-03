# Resolve the problem!!
import re

def run():
    # Start coding here
    file = open('./src/encoded.txt', 'r', encoding='utf-8')
    text = file.read()
    secret = ''.join(re.findall(r"[a-z\s]+",text))
    print(secret)
    


if __name__ == '__main__':
    run()
