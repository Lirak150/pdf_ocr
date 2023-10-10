# ТЗ

Написать алгоритм распознавания и поиска текста из pdf файла.

Пример файла https://www.archive-nnov.ru/?id=24998 (печатный документ), https://www.archive-nnov.ru/?id=37046 (рукописный документ).
Пример реализации: https://www.genotek.ru/archives/ 

# PDF OCR

Файл для распознования должен лежать в директории ocr_files.
Чтобы запустить скрипт, сначала нужно собрать образ (make build_image), а потом запустить через make run.
Когда скрипт запросит имя файла, то ввести basename (только имя с расширением).
