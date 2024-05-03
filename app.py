# Se importan Las librerias
import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
from PIL import Image

# Se importa el franted
from frontend.Presentacion import presentacion, Finalizacion
from frontend.respuesta_sismica import RespuestaSismica
from frontend.Zonificacion_Geotecnica import zonificacionGeotecnica
from frontend.Geologia_Urbana import GeologiaUrbana
from frontend.Geologia_Rural import Geologiarural

# Cuerpo de la aplicación
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    presentacion,
    RespuestaSismica,
    zonificacionGeotecnica,
    GeologiaUrbana,
    Geologiarural,
    Finalizacion
    ]
    )

if __name__ == '__main__' :
    app.run_server(debug=True)
