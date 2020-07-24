import os
import flask
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import dash_defer_js_import as dji
import numpy as np
from components import solve

external_stylesheets = ['https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css',
                        'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.18.1/styles/monokai-sublime.min.css']

external_scripts = ['https://code.jquery.com/jquery-3.2.1.slim.min.js',
                    'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js',
                    'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js']

# Server definition

server = flask.Flask(__name__)
app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                external_scripts=external_scripts,
                server=server)

filepath = os.path.split(os.path.realpath(__file__))[0]
narrative_text = open(os.path.join(filepath, "narrative.md"), "r").read()
refs_text = open(os.path.join(filepath, "references.md"), "r").read()
edvs_text = open(os.path.join(filepath, "edvs.md"), "r").read()
mathjax_script = dji.Import(src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS-MML_SVG")

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            <script type="text/x-mathjax-config">
            MathJax.Hub.Config({
                tex2jax: {
                inlineMath: [ ['$','$'],],
                processEscapes: true
                }
            });
            </script>
            {%renderer%}
        </footer>
    </body>
</html>
'''

# COMPONENTS
# ==========

def display_SIR_solution(data) -> dcc.Graph:
    S, I, R = data
    tspace = np.linspace(0, len(S), len(S))

    fig = go.Figure()

    # Susceptible
    fig.add_trace(go.Scatter(x = tspace, y = S, mode="lines", name="Susceptible"))

    # Infectious
    fig.add_trace(go.Scatter(x = tspace, y = I, mode="lines", name="Infectious"))

    # Recovered
    fig.add_trace(go.Scatter(x = tspace, y = R, mode="lines", name="Removed"))

    return fig


## Interactors
## -----------


R0_slider = dcc.Slider(id="r0_input", min=0, max=6.5, step=0.01, value=2.67, marks={x: str(x) for x in [0, 1, 2, 3, 4, 5, 6]})
delta_slider = dcc.Slider(id="delta_input", min=0, max=1, step=0.01, value=0.25, marks={x: f"{100*x:.0f}%" for x in np.linspace(0, 1, 11)})
tau_slider = dcc.Slider(id="tau_input", min=3, max=20, step=0.5, value=8.5, marks={x: str(x) for x in [3+2*x for x in range(0, 9)]})


# APP LAYOUT
# ==========

app.layout = html.Div([
    dbc.Container(children=[
        dcc.Markdown(narrative_text, dangerously_allow_html=True),
        dcc.Graph(id="sir_solution", figure=display_SIR_solution(solve(delta=0.5, R0=2.67, tau=8.5))),
        dbc.Row(children=[dbc.Col(children=[R0_slider], className="col-md-8"), dbc.Col(children=["$R_0$ (basic reproduction number)"], className="col-md-4")]),
        html.Br(),
        dbc.Row(children=[dbc.Col(children=[delta_slider], className="col-md-8"),
                          dbc.Col(children=["$\delta$ (social distancing fraction)"], className="col-md-4")]),
        html.Br(),
        dbc.Row(children=[dbc.Col(children=[tau_slider], className="col-md-8"),
                          dbc.Col(children=["$\\tau$ (duration of illness)"], className="col-md-4")]),
        html.Br(),
        html.Br(),
        dcc.Markdown(edvs_text, dangerously_allow_html=True),
        html.Br(),
        dcc.Markdown(refs_text, dangerously_allow_html=True)
    ]),
    mathjax_script
])


# INTERACTION
# ===========

@app.callback(Output("sir_solution", "figure"),
              [Input("r0_input", "value"),
               Input("delta_input", "value"),
               Input("tau_input", "value")])
def update_plot(r0_input, delta_input, tau_input):
    return display_SIR_solution(solve(delta=delta_input, R0=r0_input, tau=tau_input))


if __name__ == '__main__':
    app.run_server(debug=True)
