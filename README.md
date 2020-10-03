# multiprocessor-parser-csv

The script parses the directory with csv files in multiprocessor mode.
To run you need to pass 2 arguments:
directory path and numbers_process - number of process

Скрипт парсит каталог с csv файлами в многопроцессорном режиме
Для запуска требуется передать 2 аргумента:
Путь к каталогу и numbers_process - число процессов

csv format files for example:
https://yadi.sk/d/UZx3AN9lQCSh0g?w=1

Use:~/multiprocessor-parser_csv$ python3 run_script.py -p example-trades -f 4

Result to terminal:
Максимальная волатильность:
TICKER_SiH9 - 24.39 %
TICKER_PDM9 - 23.2 %
TICKER_PDH9 - 22.69 %
Минимальная волатильность:
TICKER_RNU9 - 0.98 %
TICKER_GOG9 - 0.97 %
TICKER_CHM9 - 0.95 %
Тикеры с нулевой волатильностью:
('TICKER_RRG9, TICKER_MTM9, TICKER_EDU9, TICKER_TRH9, TICKER_O4H9, '
 'TICKER_EuH0, TICKER_VIH9, TICKER_PDU9, TICKER_EuZ9, TICKER_PTU9, '
 'TICKER_JPM9, TICKER_CLM9, TICKER_RIH0, TICKER_CYH9')
work 3.9349 sec

If no such directory exists:
Result to terminal - Error: directory not found type <class 'FileNotFoundError'>