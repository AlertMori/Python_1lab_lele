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
    "os_name": "Windows",
    "os_release": "11",
    "os_version": "10.0.26200",
    "architecture": "AMD64",
    "cpu_count": 18,
    "disk_total_gb": 440.82,
    "disk_free_gb": 370.48,
    "hostname": "DESKTOP-0H89TIR",
    "username": "alert",
    "home_dir": "C:\\Users\\alert",
    "python_version": "3.14.6",
    "collected_at": "2026-09-29T19:47:08"
}
```
