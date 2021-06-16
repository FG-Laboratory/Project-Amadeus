import platform
import subprocess

def Shutdown(minutes=0):
    if platform.system() == 'Windows':
        subprocess.call('shutdown /s /t {}'.format(minutes * 60), shell=True)
        return True
    elif platform.system() == 'Linux':
        if minutes == 0:
            subprocess.call('shutdown -p now', shell=True)
        else:
            subprocess.call('shutdown -p +{}'.format(minutes), shell=True)
        return True
    else:
        return False


def AbortShutdown():
    if platform.system() == 'Windows':
        subprocess.call('shutdown /a', shell=True)
        return True
    elif platform.system() == 'Linux':
        subprocess.call('shutdown -a', shell=True)
        return True
    else:
        return False


# Для тестирования при прямом запуске этот скрипт должен запланировать, а затем отменить выключение винды
if __name__ == '__main__':
    Shutdown(minutes=100)
    AbortShutdown()
