import os, platform, time
try:
    import requests
except:
    os.system('pip install requests')
    os.system('git pull')
    import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;92m Congratulations ! Your Device Support this Tools")
    print(' Join Over Facebook Group For Any Help 😍 ')
    os.system('xdg-open https://www.facebook.com/groups/351076900316263/?ref=share');time.sleep(3)
    from AKING import login
    login()
elif bit == '32bit':
    print("\x1b[1;92m Congratulations ! Your Device Support this Tools")
    print(' Join Over Facebook Group For Any Help 😍 ')
    os.system('xdg-open https://www.facebook.com/groups/351076900316263/?ref=share');time.sleep(3)
    print('Soon')
    main()
