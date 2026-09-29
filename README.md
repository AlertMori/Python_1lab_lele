# Лабораторная работа 1. Параметры ОС

Скрипт `os_info.py` определяет, в какой ОС он запущен (Linux, macOS или Windows),
собирает параметры системы и сохраняет их в файл `os_info.json`.

## Запуск

```
python os_info.py
```

## Как работает

1. ОС определяется по значению `sys.platform`.
2. Параметры собираются стандартными модулями Python: `platform`, `os`,
   `shutil`, `socket`, `getpass`, `datetime`. Внешние модули и утилиты ОС
   не используются.
3. Результат записывается в JSON модулем `json`.

## Собираемые параметры

| Параметр | Описание |
|---|---|
| `os_name` | Название ОС: Linux, macOS или Windows |
| `os_release` | Выпуск ОС / версия ядра |
| `os_version` | Подробная версия (номер сборки) |
| `architecture` | Архитектура процессора (x86_64, arm64, AMD64) |
| `cpu_count` | Количество логических ядер процессора |
| `disk_total_gb` | Объём системного диска, ГБ |
| `disk_free_gb` | Свободное место на системном диске, ГБ |
| `hostname` | Имя компьютера |
| `username` | Имя текущего пользователя |
| `home_dir` | Домашняя папка пользователя |
| `python_version` | Версия Python |
| `collected_at` | Дата и время сбора данных |

## Пример результата

```json
{
    "os_name": "Linux",
    "os_release": "6.18.44",
    "os_version": "#1 SMP PREEMPT_DYNAMIC",
    "architecture": "x86_64",
    "cpu_count": 2,
    "disk_total_gb": 251.97,
    "disk_free_gb": 29.99,
    "hostname": "vm",
    "username": "user",
    "home_dir": "/home/user",
    "python_version": "3.11.15",
    "collected_at": "2026-09-29T19:15:32"
}
```
