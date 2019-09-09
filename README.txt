Приложение Небо
Автор: Вольнов Никита

Приложение позволяет по заданным координатам наблюдателя и направлению его взгляда
отрисовывать звездное небо, построенное по базе данных
"Н.Александрович. Каталог звезд и незвездных объектов, видимых в средних широтах северного полушария"
Звезды имеют цвет в зависимости от спектра.
Светила, имеющие склонение меньше -34 не представлены.
В приложении имеется возможнось вращать наблюдателя, используя клавиши WASD.

[English
    Application shows starry sky depending on the observer's coordinates and, date, time and view direction.
    Stars are taken from catalogue "Н.Александрович. Каталог звезд и незвездных объектов, видимых в средних широтах северного полушария"
]

Справка:

Пакетный режим (Console mode)
usage: app_package.py [-h] --lat LAT --long LONG [--datetime DATETIME]
                      --azimuth AZIMUTH --height HEIGHT [--filter FILTER]
                      [--angle ANGLE] [--database DATABASE] --filename
                      FILENAME [--size SIZE]

optional arguments:
  -h, --help           show this help message and exit
  --lat LAT            latitude of observer in format (N|S)A:MM:SS
  --long LONG          longitude of observer in format (W|E)A:MM:SS
  --datetime DATETIME  local datetime in format YYYY-MM-DD_HH:MM:SS/timezone
  --azimuth AZIMUTH    azimuth of view point
  --height HEIGHT      height of view point
  --filter FILTER      filter stars: do not show stars with apparent magnitude
                       more than given value
  --angle ANGLE        angle of view in degrees from 1 to 180
  --database DATABASE  path to database from current directory
  --filename FILENAME  file name image will be saved to
  --size SIZE          image size in format (width)x(height)
  
Пример запуска: --lat N70:0:10 --long E90:00:00 --height 90 --azimuth 30 --size 300x300 --filename stars.png

Графический режим (GUI mode)

usage: app_gui.py [-h] --lat LAT --long LONG [--datetime DATETIME] --azimuth
                  AZIMUTH --height HEIGHT [--filter FILTER] [--angle ANGLE]
                  [--database DATABASE] [--display DISPLAY]

optional arguments:
  -h, --help           show this help message and exit
  --lat LAT            latitude of observer in format (N|S)A:MM:SS
  --long LONG          longitude of observer in format (W|E)A:MM:SS
  --datetime DATETIME  local datetime in format YYYY-MM-DD_HH:MM:SS/timezone
  --azimuth AZIMUTH    azimuth of view point
  --height HEIGHT      height of view point
  --filter FILTER      filter stars: do not show stars with apparent magnitude
                       more than given value
  --angle ANGLE        angle of view in degrees from 1 to 180
  --database DATABASE  path to database from current directory
  --display DISPLAY    display settings in format (height)x(width) or full -
                       full screen mode
                       
Пример запуска: --lat N70:0:10 --long E90:00:00 --height 90 --azimuth 30 --display 700x700 --datetime 2018-10-11_10:00:00/5

Управление:
 - стрелки влево/вправо/вверх/вниз - вращение наблюдателя
 - минус/плюс(Shift + плюс) - отдаление/приближение
 
[English    
    Controls
    - arrows - rotate observer
    - "-/+" (or Shift + "+") - zoom out/zoom in
]