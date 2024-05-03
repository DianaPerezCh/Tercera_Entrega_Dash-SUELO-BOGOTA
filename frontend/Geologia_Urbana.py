# Se importan Las librerias

import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
from PIL import Image

# Se crean las variables para ser insertadas en el Container de las unidades geológicas

Tituto3 = html.H3('Geología Urbana')

#Se crea espacio para la elección de las localidades titulo, menu y grafica.
localidades = html.Div([
        html.H3('Localidad'),
        html.Hr()
    ],
    )

MenuDesplegable3 = html.Div([
        html.H5('CIUDAD BOLIVAR:Se colocora en menu desplegable las localidades de Bogotá'),
        html.Hr()
    ],
    )

Data3= Image.open('Localidad-GeologiaUrbana.png')
Data3 = html.Img(src=Data3, width='500', height='650')

#Se crea espacio para la columna en blanca divisoria.
Division = ''

#Se crea espacio para la elección de la unidad geológica del suelo titulo, menu y datos.
UnidadesGeologicas1 = html.Div([
        html.H3('Unidades Geológicas'),
        html.Hr()
    ],
    )

MenuRadio3 = html.Div([
        html.H5('Se colocora en menu  de selección radio las unidades geologicas'),
    ],
    )

MenuRadio31 = html.Div([
        html.H5('KPgg'),
        html.H5('KPggi'),
        html.H5('KPggm'),
        html.H5('KPggs'),
        html.H5('Ksgd'),
        html.H5('Ksglt'),
        html.H5('Ksgp'),
        html.H5('Ng(rm)'),
        html.H5('NgQt'),
        html.H5('Ngm'),
        html.H5('Pgb'),
        html.H5('Pgc'),
        html.H5('Pgri'),
        html.H5('Pgrm'),
        html.H5('Pgui'),
        html.H5('Qch2'),
        html.H5('Qch3'),
        html.Hr(),
        html.H5('Dentro de la unidad geológica de Pgb se encuentra:'),
        html.H5('13884 Habitantes dentro de la localidad de CIUDAD BOLIVAR')
    ]
    )

#Recopilación de la Zonificacion Geotecnica del HTML 
GeologiaUrbana = dbc.Container(
    [
        dbc.Row([
            dbc.Col(Tituto3, md=12,style={'background-color':'#186A3B','textAlign':'center',"color":"white"}, ),
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(localidades, md=7,style={'background-color':'#E67E22','textAlign':'center',"color":"black"}, ),
            dbc.Col(Division, md=1,style={'background-color':'white','textAlign':'center',"color":"white"}, ),
            dbc.Col(UnidadesGeologicas1, md=4,style={'background-color':'#E67E22','textAlign':'center',"color":"black"}, ),
            dbc.Col(MenuDesplegable3, md=7,style={'background-color':'#FAD7A0','textAlign':'center',"color":"black"}, ),
            dbc.Col(Division, md=1,style={'background-color':'white','textAlign':'center',"color":"white"}, ),
            dbc.Col(MenuRadio3, md=4,style={'background-color':'#FAD7A0','textAlign':'center',"color":"black"}, ),
            dbc.Col(Data3, md=7, style={'background-color':'#E67E22','textAlign':'center'}),
            dbc.Col(Division, md=1,style={'background-color':'white','textAlign':'center',"color":"white"}, ),
            dbc.Col(MenuRadio31, md=4,style={'background-color':'#FAD7A0','textAlign':'center',"color":"black"}, ),
        ]),
        html.Hr()
    ]
)