import argparse
import os
from pathlib import Path
from datetime import datetime
import sys
import re


def process_log(file_path):
    path = Path(file_path)
    files = []
    error_dict = {}
    time_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3})'
    time_in_logs = None

    # 1. Определяем файл или папка
    if os.path.isfile(file_path):
        print(f"Путь '{file_path}' найден и является файлом.")
    elif os.path.isdir(file_path):
        print(f"Путь '{file_path}' найден и является папкой.")
        files.extend(path.rglob('*'))
    else:
        print(f"Ошибка: Путь '{file_path}' не найден.")

    # Разбиение на блоки
    for file in files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                for line in f:
                    match = re.search(time_pattern, line)
                    if match:
                        time_in_logs = match.group(1)
                        error_dict[time_in_logs] = line
                    elif time_in_logs:
                        error_dict[time_in_logs] += line
        except Exception as e:
            print(f"Ошибка чтения {file}: {e}")

    return error_dict, files


def search_words_in_logs(error_dict, files, search_word):
    for file_path in files:
        print(f"\n--- Обработка файла: {os.path.basename(file_path)} ---")
        for time, content in error_dict.items():
            if search_word in content:
                words = content.split()
                try:
                    idx = words.index(search_word)
                    start = max(0, idx - 5)
                    end = idx + 6
                    found_text = " ".join(words[start:end])
                    print(f"Файл: {os.path.basename(file_path)} | Время: {time} | Текст: {found_text}")
                except ValueError:
                    continue


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Программа для обработки логов в указанной папке.")
    parser.add_argument('path', type=str, help='Полный путь к папке с логами')
    parser.add_argument("text", help="Строка для поиска")

    args = parser.parse_args()

    logs_data = process_log(args.path)
    search_words_in_logs(*logs_data, args.text)
