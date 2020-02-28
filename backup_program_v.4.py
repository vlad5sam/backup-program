import os
import zipfile
import time

source = [r'D:\Python', r'D:\Универ\Стипендия']
target_dir = r'D:\Backup'
date = target_dir + os.sep + time.strftime('%Y-%m-%d')
time = time.strftime('%H.%M.%S')
comment = input('Введите Ваш комментарий --> ')
if len(comment) == 0:
    target = date + os.sep + time + '.zip'
else:
    target = date + os.sep + time + '_' + comment.replace(' ', '_') + '.zip'
if not os.path.exists(date):
    os.mkdir(date)
print('Каталог успешно создан', date)
zip_file = zipfile.ZipFile(target, 'w')
for path in source:
    for root, dirs, files in os.walk(path):
        for file in files:
            zip_file.write(os.path.join(root, file))
zip_file.close()