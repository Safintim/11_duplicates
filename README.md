# Поиск дубликатов

## Описание

Скрипт ищет файлы-дубликаты (дубликатами считаются файлы с одинаковым именем и размером) и выводит их адрес в консоль.

## Требования

*Python3*

## Как запустить

```sh
git clone https://github.com/Safintim/11_duplicates.git
cd 11_duplicates
python duplicates.py <path_to_dir>
```

## Примеры

```sh
python duplicates.py /homme/user/
Укажите правильный путь каталога
```

```sh
python duplicates.py /home/t/source/ 
/home/t/source/main.py
/home/t/source/TEST/main.py
```

## Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
