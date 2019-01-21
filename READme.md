1. ��� ���������� ������ ���-���������� ���������� ���������� ��������� ��������� Python. ��� ����� � ������� ���������� �� ������� ��������� �������: 
pip install dash, 
pip install dash_html_components, 
pip install dash_core_components, 
pip install plotly.graph_objs, 
pip install pyodbc, 
pip install pandas, 
pip install pysyge, 
pip install Dispatch.
��������: ���� ����� ��������� ���������� Dash ���������� ��� ������ ("UnsupportedOperation: not writable") ��� ���������� ��������������� ����������� ������� echo �� ������ ../site-packages/click/utils.py.
�������� �� ��������� ��� ��������� ����� ������ ���� sys.stdout ������ None. ���� ����� ����� ������� ��� ����������� ������� secho �� ������ ../site-packages/click/termui.py

��� ������ ������� � ����������� ��������.

2. � ������� Jupyter Notebook ��������� ���� Parser_Log.ipynb. ��� ���������� ��� ������ � �������� ����� ����� ��������� csv-����� ��� ���� ������.
3. ��������� � ������� Jupyter Notebook ��������� ���� Access.ipynb ��� �������� ���� ������.
4. �������� ��:

������� Basket:
PRIMARY KEY (ID_Basket)
FOREIGN KEY (IP) REFERENCES Location(IP)
FOREIGN KEY (Goods) REFERENCES Product(ID_Product)
FOREIGN KEY (Cart_id) REFERENCES Buy(Cart_id)

������� Product:
PRIMARY KEY (ID_Product)
FOREIGN KEY (Category) REFERENCES Category(ID_Category)

������� Buy:
PRIMARY KEY (Cart_id)
FOREIGN KEY (IP) REFERENCES Location(IP)

������� Category:
PRIMARY KEY (ID_Category)

������� Location:
PRIMARY KEY (IP)

������� Visit:
PRIMARY KEY (Visit)
FOREIGN KEY (IP) REFERENCES Location(IP)
FOREIGN KEY (Category) REFERENCES Category(ID_Category)
FOREIGN KEY (Product) REFERENCES Product(ID_Product)

5. ����� �������� app.py �������� � ���������� conn_str �������� ���� �� ����.
6. ����� ������� ���������� ��������� �� ������������ �����.  
