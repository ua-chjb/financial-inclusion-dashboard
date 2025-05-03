import plotly.express as px


plot_color="white"
grid_color = "#efefef"
grid_width = 2
axis_color = "#efefef"

font_color="black"
font_size = 10
title_size = 14


def scientific_layout(fig):

    return fig.update_layout({
        "plot_bgcolor": plot_color,
        "font": {"color": font_color, "size": font_size},
        "clickmode": "select",
        "title": {"x": 0.5, "font": {"size": title_size}},
        "legend": {"visible": False},
        "barcornerradius": 10,
        "coloraxis":{"showscale": False},
        "margin": {"t": 45, "b": 15, "r": 15, "l": 15},
        "scene": {
            # "plot_bgcolor": plot_color
            "xaxis": {"backgroundcolor": plot_color},
            "yaxis": {"backgroundcolor": plot_color},
            "zaxis": {"backgroundcolor": plot_color}
        }
    }).update_xaxes({
        "showgrid": True,
        "zeroline": False,
        "showline": True,
        "mirror": False,
        "gridcolor": grid_color,
        "gridwidth": grid_width,
        "linecolor": axis_color,
        "linewidth": 2,
        "ticks": ""
    }).update_yaxes({
        "showgrid": True,
        "zeroline": False,
        "showline": True,
        "mirror": False,
        "gridcolor": grid_color,
        "gridwidth": grid_width,
        "linecolor": axis_color,
        "linewidth": 2,
        "ticks": ""
    }).update_polars({
        "angularaxis": {"gridwidth": grid_width},
        "radialaxis": {"gridwidth": grid_width},
    })