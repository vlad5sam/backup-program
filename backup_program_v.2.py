import os
import time

source = [r'D:\Python', r'D:\Универ\Стипендия']
target_dir = r'D:\Backup'
date = target_dir + os.sep + time.strftime('%Y%m%d')
time = time.strftime('%H%M%S')
if not os.path.exists(date):
    os.mkdir(date)
print('Каталог успешно создан', date)
target = date + os.sep + time + '.zip'
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
print(zip_command)
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')