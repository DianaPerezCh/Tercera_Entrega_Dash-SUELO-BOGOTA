# Se importan Las librerias

import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
from PIL import Image

# Se crean las variables para ser insertadas en el Container de respuesta sísmica

Tituto1 = html.H3('Zonas de Respuesta Sismica')

#Se crea espacio para la elección de las localidades titulo, menu y grafica.
localidades = html.Div([
        html.H3('Localidad'),
        html.Hr()
    ],
    )

MenuDesplegable1 = html.Div([
        html.H5('CIUDAD BOLIVAR:Se colocora en menu desplegable las localidades de Bogotá'),
        html.Hr()
    ],
    )

Data1= Image.open('Localidad-RespuestaSismica.png')
Data1 = html.Img(src=Data1, width='600', height='600')

#Se crea espacio para la columna en blanca divisoria.
Division = ''

#Se crea espacio para la elección de la respuesta sismica del suelo titulo, menu y datos.
Suelos = html.Div([
        html.H3('Zonificación del suelo'),
        html.Hr()
    ],
    )

MenuRadio1 = html.Div([
        html.H5('Se colocora en menu de selección radio las zonificaciones de respuesta sísmica'),
    ],
    )

MenuRadio11 = html.Div([
        html.H5('Aluvial 300'),
        html.H5('Aluvial 100'),
        html.H5('Lacustre 50'),
        html.H5('Cerros'),
        html.H5('Depósito Ladera'),
        html.H5('Aluvial 50'),
        html.H5('Piedemonte C'),
        html.H5('Piedemonte A'),
        html.H5('Piedemonte B'),
        html.H5('Lacustre 200'),
        html.H5('Lacustre Aluvial 200'),
        html.H5('Lacustre Aluvial 300'),
        html.H5('Lacustre 500'),
        html.H5('Lacustre 300'),
        html.H5('Lacustre 100'),
        html.H5('Aluvial 200'),
        html.Hr(),
        html.H5('Dentro de la zonificación de la respuesta sismica Cerros se encuentra:'),
        html.H5('333949 Habitantes dentro de la localidad de CIUDAD BOLIVAR')
    ]
    )

#Recopilación de la Respuesta Sismica del HTML 
RespuestaSismica = dbc.Container(
    [
        dbc.Row([
            dbc.Col(Tituto1, md=12,style={'background-color':'#186A3B','textAlign':'center',"color":"white"}, ),
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(localidades, md=7,style={'background-color':'#E67E22','textAlign':'center',"color":"black"}, ),
            dbc.Col(Division, md=1,style={'background-color':'white','textAlign':'center',"color":"white"}, ),
            dbc.Col(Suelos, md=4,style={'background-color':'#E67E22','textAlign':'center',"color":"black"}, ),
            dbc.Col(MenuDesplegable1, md=7,style={'background-color':'#FAD7A0','textAlign':'center',"color":"black"}, ),
            dbc.Col(Division, md=1,style={'background-color':'white','textAlign':'center',"color":"white"}, ),
            dbc.Col(MenuRadio1, md=4,style={'background-color':'#FAD7A0','textAlign':'center',"color":"black"}, ),
            dbc.Col(Data1, md=7, style={'background-color':'#E67E22','textAlign':'center'}),
            dbc.Col(Division, md=1,style={'background-color':'white','textAlign':'center',"color":"white"}, ),
            dbc.Col(MenuRadio11, md=4,style={'background-color':'#FAD7A0','textAlign':'center',"color":"black"}, ),
        ]),
        html.Hr()
    ]
)