1. Для корректной работы веб-приложения необходимо установить несколько библиотек Python. Для этого в консоли необходимо по очереди прописать команды: 
pip install dash, 
pip install dash_html_components, 
pip install dash_core_components, 
pip install plotly.graph_objs, 
pip install pyodbc,
pip install pypyodbc,
pip install pandas, 
pip install pysyge, 
pip install Dispatch.
Внимание: если после установке библиотеки Dash появляется эта ошибка ("UnsupportedOperation: not writable") вам необходимо отредактировать определение функции echo по адресу ../site-packages/click/utils.py.
Значение по умолчанию для параметра файла должно быть sys.stdout вместо None. Тоже самое нужно сделать для определения функции secho по адресу ../site-packages/click/termui.py

Эта ошибка связана с обновлением анаконды.

2. С помощью Jupyter Notebook запустите файл Parser_Log.ipynb. При завершении его работы в корневую папку будут добавлены csv-файлы для базы данных.
3. Запустите с помощью Jupyter Notebook запустите файл Access.ipynb для создания базы данных (на всякий случай готовая база данных прилагается).
4. Описание БД:

Таблица Basket:
PRIMARY KEY (ID_Basket)
FOREIGN KEY (IP) REFERENCES Location(IP)
FOREIGN KEY (Goods) REFERENCES Product(ID_Product)
FOREIGN KEY (Cart_id) REFERENCES Buy(Cart_id)

Таблица Product:
PRIMARY KEY (ID_Product)
FOREIGN KEY (Category) REFERENCES Category(ID_Category)

Таблица Buy:
PRIMARY KEY (Cart_id)
FOREIGN KEY (IP) REFERENCES Location(IP)

Таблица Category:
PRIMARY KEY (ID_Category)

Таблица Location:
PRIMARY KEY (IP)

Таблица Visit:
PRIMARY KEY (Visit)
FOREIGN KEY (IP) REFERENCES Location(IP)
FOREIGN KEY (Category) REFERENCES Category(ID_Category)
FOREIGN KEY (Product) REFERENCES Product(ID_Product)

5. Перед запуском app.py замените в переменной conn_str замените путь до базы.
6. После запуска приложения перейдите на предложенный адрес.  
