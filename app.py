# Se importan Las librerias
import dash
from dash import Dash, html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from PIL import Image

# Se importa el franted
from frontend.Presentacion import presentacion, Finalizacion
from backend.respuesta_sismica import Tituto1, RespuestaSismica, consultarLocalidad, Division, Poblacion_RespuestaSismica
from backend.Zonificacion_Geotecnica import Tituto2, zonificacionGeotecnica, consultarLocalidad_1, Poblacion_zonificacionGeotecnica
from frontend.Geologia_Urbana import GeologiaUrbana
from frontend.Geologia_Rural import Geologiarural


# Cuerpo de la aplicación
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    presentacion,
            dbc.Row([
            dbc.Col(Tituto1, md=12,style={'background-color':'#186A3B','textAlign':'center',"color":"white"}, ),
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(RespuestaSismica, md=7,style={'background-color':'#E67E22','textAlign':'center',"color":"black"}, ),
            dbc.Col(Division, md=1,style={'background-color':'white','textAlign':'center',"color":"white"}, ),
            dbc.Col(Poblacion_RespuestaSismica, md=4,style={'background-color':'#E67E22','textAlign':'center',"color":"black"}, ),
        ]),
        html.Hr(),
            dbc.Row([
            dbc.Col(Tituto2, md=12,style={'background-color':'#186A3B','textAlign':'center',"color":"white"}, ),
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(zonificacionGeotecnica, md=7,style={'background-color':'#E67E22','textAlign':'center',"color":"black"}, ),
            dbc.Col(Division, md=1,style={'background-color':'white','textAlign':'center',"color":"white"}, ),
            dbc.Col(Poblacion_zonificacionGeotecnica, md=4,style={'background-color':'#E67E22','textAlign':'center',"color":"black"}, ),
        ]),
        html.Hr(),
    GeologiaUrbana,
    Geologiarural,
    Finalizacion
    ]
    )

#Conexion con la funcion del mapa - Seccion 1
@callback(
    Output("mapa", "figure"),
    Input("localidad_consultada", "value")
)

#Funcion a conectar del mapa  - Seccion 1
def update_map(localidad_consultada):
    return consultarLocalidad(localidad_consultada)

#Conexion con la funcion del mapa  - Seccion 2
@callback(
    Output("mapa_1", "figure"),
    Input("localidad_consultada_1", "value")
)

#Funcion a conectar del mapa  - Seccion 2
def update_map_1(localidad_consultada_1):
    return consultarLocalidad_1(localidad_consultada_1)

if __name__ == '__main__' :
    app.run_server(debug=True)
