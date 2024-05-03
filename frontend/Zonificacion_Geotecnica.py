# Se importan Las librerias

import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
from PIL import Image

# Se crean las variables para ser insertadas en el Container de Zonificación Geotecnica

Tituto2 = html.H3('Zonificación Geotécnica')

#Se crea espacio para la elección de las localidades titulo, menu y grafica.
localidades = html.Div([
        html.H3('Localidad'),
        html.Hr()
    ],
    )

MenuDesplegable2 = html.Div([
        html.H5('CIUDAD BOLIVAR:Se colocora en menu desplegable las localidades de Bogotá'),
        html.Hr()
    ],
    )

Data2= Image.open('Localidad-zonificaciongeotecnica.png')
Data2 = html.Img(src=Data2, width='600', height='600')

#Se crea espacio para la columna en blanca divisoria.
Division = ''

#Se crea espacio para la elección de la zonificacion geotecnica del suelo titulo, menu y datos.
Geotecnia = html.Div([
        html.H3('Geotecnia'),
        html.Hr()
    ],
    )

MenuRadio2 = html.Div([
        html.H5('Se colocora en menu de selección radio las zonificaciones de respuesta sísmica'),
    ],
    )

MenuRadio21 = html.Div([
        html.H5('Depósito ladera'),
        html.H5('Cerros A'),
        html.H5('Cerros B'),
        html.H5('Relleno'),
        html.H5('Cauce'),
        html.H5('Excavación'),
        html.H5('Aluvial'),
        html.H5('Piedemonte B'),
        html.H5('Basura'),
        html.H5('Piedemonte A'),
        html.H5('Piedemonte C'),
        html.H5('Suelo residual'),
        html.H5('Lacustre A'),
        html.H5('Lacustre C'),
        html.H5('Llanura A'),
        html.H5('Lacustre B'),
        html.H5('Llanura B'),
        html.Hr(),
        html.H5('Dentro de la zonificación de geotecnia Cerros A se encuentra:'),
        html.H5('115670 Habitantes dentro de la localidad de CIUDAD BOLIVAR')
    ]
    )

#Recopilación de la Zonificacion Geotecnica del HTML 
zonificacionGeotecnica = dbc.Container(
    [
        dbc.Row([
            dbc.Col(Tituto2, md=12,style={'background-color':'#186A3B','textAlign':'center',"color":"white"}, ),
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(localidades, md=7,style={'background-color':'#E67E22','textAlign':'center',"color":"black"}, ),
            dbc.Col(Division, md=1,style={'background-color':'white','textAlign':'center',"color":"white"}, ),
            dbc.Col(Geotecnia, md=4,style={'background-color':'#E67E22','textAlign':'center',"color":"black"}, ),
            dbc.Col(MenuDesplegable2, md=7,style={'background-color':'#FAD7A0','textAlign':'center',"color":"black"}, ),
            dbc.Col(Division, md=1,style={'background-color':'white','textAlign':'center',"color":"white"}, ),
            dbc.Col(MenuRadio2, md=4,style={'background-color':'#FAD7A0','textAlign':'center',"color":"black"}, ),
            dbc.Col(Data2, md=7, style={'background-color':'#E67E22','textAlign':'center'}),
            dbc.Col(Division, md=1,style={'background-color':'white','textAlign':'center',"color":"white"}, ),
            dbc.Col(MenuRadio21, md=4,style={'background-color':'#FAD7A0','textAlign':'center',"color":"black"}, ),
        ]),
        html.Hr()
    ]
)