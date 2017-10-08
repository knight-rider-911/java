import subprocess


def restart(res):
    cmd = 'shutdown -r -t 60'
    if res == 'y':
        p = subprocess.Popen(cmd, shell=True)
        p.wait()
        print('Ok, shutdown')
    elif res == 'n':
        print('Go to work, kid')
    else:
        print('I don\'t understand')


if __name__ == '__main__':
    res = input('Restart? (y/n): ')
    a = restart(res)
    print(a)
