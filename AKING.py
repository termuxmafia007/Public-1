import os,time,platform
os.system('clear')
print('[•] Checking Updates...')
os.system('git pull')
print('<------------------------------------>')
bit = platform.architecture()[0]
if bit=='64bit':
    print('[•] Join Over Facebook Group For Any Help')
    os.system('xdg-open https://www.facebook.com/groups/396673281944454/')
    import AKING
else:
    print('\033[1;31m[×] Sorry Device Not Support')
