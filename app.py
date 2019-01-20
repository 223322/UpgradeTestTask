import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import pyodbc
import re
from dash.dependencies import Input, Output

# In conn_str specify the path to the database
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\rfrep\Documents\Интерсвязь\DB_Logs.accdb;'
    )
cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()


category = []
crsr.execute("SELECT Category.Category from Category")
for row in crsr.fetchall():
    category.append(row[0])


date = []
crsr.execute("SELECT distinct Visit.Date FROM Visit;")
for row in crsr.fetchall():
    date.append(row[0])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.config [ 'suppress_callback_exceptions'] = True



#=================== Вкладки ================================
app.layout = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
                    
        dcc.Tab(label='№1',children=[dcc.Graph( id='first_question_bar'),
                                     html.Div(
                                             dcc.Slider(
                                                 id = 'first_question_slider_count_value',
                                                 min=10,
                                                 max=100,
                                                 value=0, 
                                                 marks={'10': '10', '33' : '33', '55': '55', '78' : '78', '100' : '80'}
                                        ), className = "slider")
                                     
        ]),
                                     
                                     

        dcc.Tab(label='№2',children=[html.Div([dcc.Dropdown(
                                                    id='crossfilter_second_question',
                                                    options=[{'label': i, 'value': i} for i in category],
                                                    value='all_to_the_bottom')]),  
                                                     
                                            html.Div([dcc.Graph(id='second_question_bar',
                                                                figure={'layout':{ 'title' : 'Посетители из какой страны чаще всего интересуются товарами из определенных категорий?'}},)]),
                                                      
                                                    html.Div(dcc.Slider(
                                                                         id = 'second_question_slider_count_value',
                                                                         min=10,
                                                                         max=100, 
                                                                         value=10,
                                                                         marks={'10': '10', '33' : '33', '55': '55', '100' : '72'}
                                                                         ), className = "slider")
        ]),
    
    
    
    
    
        dcc.Tab(label='№3', children=[html.Div([dcc.Dropdown(
                                                    id='crossfilter_third_question',
                                                    options=[{'label': i, 'value': i} for i in category],
                                                    value='all_to_the_bottom')]),  
                                                     
                                            html.Div(dcc.Graph(id='third_question_bar',
                                                                figure={'layout':{ 'title' : 'В какое время суток чаще всего просматривают определенную категорию товаров?'}},) ),
        ]),
    
    
    
    
    
        dcc.Tab(label='№4', children=[dcc.Dropdown(id='crossfilter_fourth_question',
                                                    options=[{'label': i, 'value': i} for i in date],),          
                                      html.Div(dcc.Graph(id='fourth_question_bar',
                                                                figure={'layout':{ 'title' : 'Какая нагрузка (число запросов) на сайт за астрономический час?'}})),
    
                                                                                          
        ]),
    
        dcc.Tab(label='№5', children=[html.Div(dcc.Dropdown(
                                                    id='crossfilter_fifth_question',
                                                    options=[{'label': i, 'value': i} for i in category],
                                                    value='all_to_the_bottom')),
                                            html.Div(dcc.Graph(id='fifth_question_bar',
                                                                figure={'layout':{ 'title' : 'Товары из какой категории чаще всего покупают совместно с товаром из заданной категории?'}},) ),
        ]),
                                                               
                                                               
        dcc.Tab(label='№6', children=[html.Div([
                                    html.P('Выбирете дату начала периода'),
                                    html.Div( [dcc.Dropdown(id='crossfilter_sixth_question_start_date',
                                                    options=[{'label': i, 'value': i} for i in date]),], className = "time")], className = "timeBlock"),
                                    html.Br(),
                                    html.Div([
                                    html.P('Выбирете дату окончания периода'),
                                    html.Div([dcc.Dropdown(id='crossfilter_sixth_question_end_date',
                                                    options=[{'label': i, 'value': i} for i in date])], className = "time")]),
                                                
                                    html.Div(id='display_sixth_question', children =[html.Br(),
                                                                                    html.Div([
                                                                                        html.H1(id='display_count_sixth_question_text', children='Отчет о "брошеных" корзинах',style={'textAlign': 'center'}),
                                                                                        html.H6('Количество "брошеных" корзин на данный период составляет: '),
                                                                                        html.H3(id='display_count_sixth_question', children=' ',style={'width' : '25px', 'display': 'inline'}),], className = "result")
                                                                                     ],)]),
    
        dcc.Tab(label='№7', children=[html.Div([
                                    html.P('Выбирете дату начала периода'),
                                    html.Div( [dcc.Dropdown(id='crossfilter_seventh_question_start_date',
                                                    options=[{'label': i, 'value': i} for i in date]),], className = "time")], className = "timeBlock"),
                                    html.Br(),
                                    html.Div([
                                    html.P('Выбирете дату окончания периода'),
                                    html.Div([dcc.Dropdown(id='crossfilter_seventh_question_end_date',
                                                    options=[{'label': i, 'value': i} for i in date])], className = "time")]),
                                                
                                    html.Div(id='display_seventh_question', children =[html.Br(),
                                                                                    html.Div([
                                                                                        html.H1(id='display_count_seventh_question_text', children='Отчет о количестве повторных покупок',style={'textAlign': 'center'}),
                                                                                        html.H6("Количество повторных покупок на данный период составляет: "),
                                                                                        html.H3(id='display_count_seventh_question', children=' ',style={'width' : '25px', 'display': 'inline'}),], className = "result")
                                                                                     ],)]),
    html.Div(id='tabs-content')
    ])
])
   
def SplitTime(startTime, hour):
    spl = re.split(':',startTime)
    tt = str(hour) +':'+spl[1]+':'+spl[2]
    return tt    

#=================== 1
@app.callback(Output('first_question_bar', 'figure'), [Input('first_question_slider_count_value', 'value')])
            
def update_first_question_graph(value):
    
    country = []
    count = []
    crsr.execute("SELECT Location.Country, count(Location.Country) FROM Location, Visit, Category WHERE Location.IP = Visit.IP AND Visit.Category = Category.ID_Category Group By Location.Country ORDER BY 2 DESC") 
    for row in crsr.fetchall()[:value]:
        country.append(row[0])
        count.append(row[1])  
    return {'data': [go.Bar(x = country, y = count)],
            'layout':{ 'title' : 'Посетители из какой страны совершают больше всего действий на сайте?'} } 
   
#=================== 2
@app.callback(Output('second_question_bar', 'figure'),
                       [Input('crossfilter_second_question', 'value'),
                        Input('second_question_slider_count_value', 'value')])
                
def update_second_question_graph(xaxis_column_name,value):

    select_category = xaxis_column_name    
    country = []
    count = []
    crsr.execute("SELECT Location.Country, count(Location.Country) FROM Location, Visit, Category WHERE Location.IP = Visit.IP AND Visit.Category = Category.ID_Category AND Category.Category = (?) Group By Location.Country ORDER BY 2 DESC", [(select_category)])
    for row in crsr.fetchall()[:value]:
        country.append(row[0])
        count.append(row[1])
  
    return {'data': [go.Bar(   x = country, y = count)],
             'layout':{ 'title' : 'Посетители из какой страны чаще всего интересуются товарами из определенных категорий?'}}
    
    
#=================== 3
@app.callback(Output('third_question_bar', 'figure'),
                       [Input('crossfilter_third_question', 'value'),])
                
def update_third_question_graph(xaxis_column_name):
    
    times_of_day = []
    count = []
    select_category = xaxis_column_name    
    crsr.execute("SELECT Visit.Times_of_Day, count(Visit.Times_of_Day) FROM Visit, Category WHERE Visit.Category = Category.ID_Category AND Category.Category = (?) Group By Visit.Times_of_Day ORDER BY 2 DESC", [(select_category)])
    for row in crsr.fetchall():
        times_of_day.append(row[0])
        count.append(row[1])

    return {'data': [go.Bar(x = times_of_day, y = count, marker=dict(
            color=['rgb(123,167,242)', 'rgba(222,45,38,0.8)',
               'rgb(241,242,123)', 'rgb(133,242,123)']),)],
             'layout':{ 'title' : 'В какое время суток чаще всего просматривают определенную категорию товаров?'}}


#=================== 4
@app.callback(Output('fourth_question_bar', 'figure'),
             [Input('crossfilter_fourth_question', 'value'),])
                
def update_fourth_question_graph(value):
    
    start_date = value
    startTime = '0:00:00'
    time = []
    count = []
    tt = '1:00:00'
    for hour in range(24):
        tt = SplitTime(startTime, hour)
        crsr.execute("select  count(*) from Visit where Visit.Time Between [?] and [?] and Visit.Date = [?];",[(startTime),(tt),(start_date)]) 
        time.append(hour)
        hour = +1
        startTime = tt
        for row in crsr.fetchall():
            count.append(row[0])    
    return {'data': [go.Bar(x = time, y = count)],
            'layout':{ 'title' : 'Какая нагрузка (число запросов) на сайт за астрономический час?'}}    


#=================== 5
@app.callback(Output('fifth_question_bar', 'figure'),
             [Input('crossfilter_fifth_question', 'value'),])
                
def update_fifth_question_graph(xaxis_column_name):


    select_category = xaxis_column_name  
    category = []
    count = []
    crsr.execute("SELECT Category.Category, Count(Category.Category) FROM Product, Category, Basket WHERE (((Basket.Cart_id) In (select Basket.Cart_id From Buy, Basket Where Buy.Cart_id = Basket.Cart_id and Basket.Goods in  (select Product.ID_Product From Product , Category Where Product.Category = Category.ID_Category and Category.Category = (?)))) AND ((Basket.Goods)=[Product].[ID_Product]) AND ((Product.Category)=[Category].[ID_Category]) AND ((Category.Category)<>([?]))) GROUP BY Category.Category ORDER BY 2 DESC;", [(select_category),(select_category)])
    for row in crsr.fetchall():
        category.append(row[0])
        count.append(row[1])
    
    return {'data': [go.Bar(x = category, y = count, marker=dict(
        color=['rgb(123,167,242)', 'rgba(222,45,38,0.8)',
               'rgb(241,242,123)', 'rgb(133,242,123)']),)],
             'layout':{ 'title' : 'Товары из какой категории чаще всего покупают совместно с товаром из заданной категории?'}}
    
#=================== 6
@app.callback(Output('display_count_sixth_question', 'children'),
             [Input('crossfilter_sixth_question_start_date', 'value'),
             Input('crossfilter_sixth_question_end_date', 'value')])
                
def update_sixth_question_graph(start_date,end_date):   

    count=[]
    crsr.execute("SELECT Count(*) FROM Basket WHERE (((Basket.Cart_id) Not In (select Basket.Cart_id From Buy, Basket Where Buy.Cart_id = Basket.Cart_id))) AND Basket.Date Between [?] and [?];",[(start_date),(end_date)]) 
    for row in crsr.fetchall():
        count.append(row[0])
 
    return  count[0]

#=================== 7
@app.callback(Output('display_count_seventh_question', 'children'),
             [Input('crossfilter_seventh_question_start_date', 'value'),
             Input('crossfilter_seventh_question_end_date', 'value')])
                
def update_seventh_question_graph(start_date,end_date):   

    count=[]
    crsr.execute("select count(*) from (SELECT count(Buy.User_id) AS Count_Visit FROM Buy  WHERE Buy.Date Between [?] and [?] Group By Buy.User_id ) AS Unique_User where  Unique_User.Count_Visit > 1 ;",[(start_date),(end_date)]) 
    for row in crsr.fetchall():
        count.append(row[0])
 
    return count[0]  
    
if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload_interval=25000,
    dev_tools_hot_reload_max_retry=50)