import os
import time

source = [r'D:\Python', r'D:\Универ\Стипендия']
target_dir = r'D:\Backup'
date = target_dir + os.sep + time.strftime('%Y%m%d')
time = time.strftime('%H%M%S')
comment = input('Введите Ваш комментарий --> ')
if len(comment) == 0:
    target = date + os.sep + time + '.zip'
else:
    target = date + os.sep + time + '_' + comment.replace(' ', '_') + '.zip'
if not os.path.exists(date):
    os.mkdir(date)
print('Каталог успешно создан', date)
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')