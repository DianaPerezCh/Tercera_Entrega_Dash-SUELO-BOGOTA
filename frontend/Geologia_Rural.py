# Se importan Las librerias

import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
from PIL import Image

# Se crean las variables para ser insertadas en el Container de las unidades geológicas

Tituto4 = html.H3('Geología Rural')

#Se crea espacio para la elección de las localidades titulo, menu y grafica.
localidades = html.Div([
        html.H3('Localidad'),
        html.Hr()
    ],
    )

MenuDesplegable4 = html.Div([
        html.H5('CIUDAD BOLIVAR:Se colocora en menu desplegable las localidades de Bogotá'),
        html.Hr()
    ],
    )

Data4= Image.open('Localidad-GeologiaRural.png')
Data4 = html.Img(src=Data4, width='500', height='650')

#Se crea espacio para la columna en blanca divisoria.
Division = ''

#Se crea espacio para la elección de la unidad geológica del suelo titulo, menu y datos.
UnidadesGeologicas2 = html.Div([
        html.H3('Unidades Geológicas'),
        html.Hr()
    ],
    )

MenuRadio4 = html.Div([
        html.H5('Se colocora en menu de selección radio las unidades geologicas'),
    ],
    )

MenuRadio42 = html.Div([
        html.H5('Sco (Q2c)'),
        html.H5('Ri2 (K2p)'),
        html.H5('Rd1 (K2lt)'),
        html.H5('Sfg (Qfg)'),
        html.H5('Sfg1 (Q1si)'),
        html.H5('Qal (Qal)'),
        html.H5('Rd2 (K2d)'),
        html.H5('Ri1 (E1c)'),
        html.H5('Rb5 (K2E1g)'),
        html.H5('Rb4 (E1b)'),
        html.H5('Rb6 (K2cp'),
        html.H5('Sfg2 (Q2chi)'),
        html.H5('Sa1 (N1m)'),
        html.H5('Rb3 (Pglf)'),
        html.H5('Rb2 (E2r)'),
        html.H5('Rb7 (K1f)'),
        html.H5('Cuerpo de Agua'),
        html.Hr(),
        html.H5('Dentro de la unidad geológica de Rb5 (K2E1g) se encuentra:'),
        html.H5('204 Habitantes dentro de la localidad de CIUDAD BOLIVAR')
    ]
    )

#Recopilación de la Zonificacion Geotecnica del HTML 
Geologiarural = dbc.Container(
    [
        dbc.Row([
            dbc.Col(Tituto4, md=12,style={'background-color':'#186A3B','textAlign':'center',"color":"white"}, ),
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(localidades, md=7,style={'background-color':'#E67E22','textAlign':'center',"color":"black"}, ),
            dbc.Col(Division, md=1,style={'background-color':'white','textAlign':'center',"color":"white"}, ),
            dbc.Col(UnidadesGeologicas2, md=4,style={'background-color':'#E67E22','textAlign':'center',"color":"black"}, ),
            dbc.Col(MenuDesplegable4, md=7,style={'background-color':'#FAD7A0','textAlign':'center',"color":"black"}, ),
            dbc.Col(Division, md=1,style={'background-color':'white','textAlign':'center',"color":"white"}, ),
            dbc.Col(MenuRadio4, md=4,style={'background-color':'#FAD7A0','textAlign':'center',"color":"black"}, ),
            dbc.Col(Data4, md=7, style={'background-color':'#E67E22','textAlign':'center'}),
            dbc.Col(Division, md=1,style={'background-color':'white','textAlign':'center',"color":"white"}, ),
            dbc.Col(MenuRadio42, md=4,style={'background-color':'#FAD7A0','textAlign':'center',"color":"black"}, ),
        ]),
        html.Hr()
    ]
)