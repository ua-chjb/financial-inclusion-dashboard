import pandas as pd
import numpy as np
from itertools import *

from dash import html
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

import dash_mantine_components as dmc

from load_data import india, india_norm, india_pop, india_desc, ys_df, coef_df, final_coef_df

# # # # # # # # # # # # # # # # fig_geo # # # # # # # # # # # # # # # # # 

def fig_geo(feature, states_uts):

    fig = go.Figure()

    fig = fig.add_trace(
        go.Choroplethmap(
            geojson=states_uts,
            locations=india['state_ut'],
            z=india[feature],
            featureidkey="properties.name",
            colorscale=px.colors.sequential.Reds,
            marker={"line": {"width": 0.001, "color": "white"}}
        )
    ).update_layout({
        "title": {"text": f"{feature}", "x": 0.5},
        "margin": {"t": 0, "b": 0, "r": 0, "l": 0},
        "clickmode": "select",
        "map": {
            "center": {"lon":78.9629, "lat": 20.5937},
            "zoom": 3,
            "bounds": {
                "north": 42,
                "east": 108,
                "south": -2,
                "west": 53 
            },
            "uirevision": "static"
        },

    })


    return fig


# # # # # # # # # # # # # # # # table from dmc # # # # # # # # # # # # # # # # # 


def sorted_table(feature):

    filtered_df = india.sort_values(by=feature, ascending=False)
    filtered_df["rank"] = range(1, len(filtered_df)+1)

    ordered_collst = ["rank", "state_ut", feature] + list(filtered_df.drop(["rank", "state_ut", feature], axis=1).columns)
    filtered_df = filtered_df[ordered_collst]

    head = list(filtered_df.columns)
    body = [list(row) for _, row in filtered_df.iterrows()]

    table = dmc.Table(
        verticalSpacing="xs",
        horizontalSpacing="xs",
        striped=True,
        highlightOnHover=True,
        withTableBorder=True,
        withColumnBorders=True,
        data={
            "head": head,
            "body": body
        },
    )

    return dmc.ScrollArea(
        children=table
    )


# # # # # # # # # # # # # # # # fig_scatterpolar+bar # # # # # # # # # # # # # # # # # 


def comparison_graph(collst, additional_state):

    states_uts1 = additional_state if additional_state else []

    colors_cyc = cycle(px.colors.qualitative.T10[:len(states_uts1)])

    bigfig = make_subplots(
        rows=1, cols=2, specs=[[{"type": "polar"}, {"type": "xy"}]],
        # subplot_titles=("Dependent Variables", "Independent Variables"),
        horizontal_spacing=0.2
    )
    
    df1 = india_norm.set_index("state_ut")
    df2 = df1.sort_values(by=["poverty_multi_tot_2019_DV"], ascending=True)

    bigfig.add_trace(
        go.Bar(
            x=df2["poverty_multi_tot_2019_DV"],
            y=df2.index,
            marker={"color": [next(colors_cyc) if ut in states_uts1 else "gray" for ut in df2.index]},
            orientation="h",
            showlegend=False
        ), row=1, col=2
    )

    for state in states_uts1:

        bigfig.add_trace(
            go.Scatterpolar(
                theta = df1[collst].columns,
                r = df1.loc[state, collst].values,
                fill="toself",
                mode="markers",
                marker={
                    "symbol":"diamond", 
                    "color": next(colors_cyc),
                },
                line= {"width": 0},
                opacity=0.5,
                name=state,
                showlegend=False,
                connectgaps=True,
            ), row=1, col=1
        )

    bigfig.add_trace(
        go.Scatterpolar(
            theta=[None],
            r=[None],
            showlegend=False
        ), row=1, col=1
    )

    for annotation in bigfig.layout.annotations:
        annotation.y+=0.05

    return bigfig.update_layout({
        "yaxis": {"tickfont": {"size": 8}},
        "xaxis": {"tickfont": {"size": 8}},        
        "margin": {"t": 40, "b": 40, "r": 40, "l": 40},
        "clickmode": "event",
        "polar": {
            "radialaxis": {"tickfont": {"size": 8}},
            "angularaxis": {"tickfont": {"size": 10}},
        }
    })


# # # # # # # # # # # # # # # # scatter_treed # # # # # # # # # # # # # # # # # 

def scatter_treed(feature):

    fig = px.scatter_3d(
        india_pop,
        x="total_population",
        y="poverty_multi_tot_2019_DV",
        z=feature,
        color="poverty_multi_tot_2019_DV",
        size="total_population",
        color_continuous_scale="Reds"
    ).update_traces({"marker": {"size": india_pop["total_population"]*20}})

    fig.update_layout(coloraxis_showscale=False)

    return fig.update_layout({
        "clickmode":"select",
        "margin": {"t": 0, "b": 0, "r": 0, "l": 0},     
        "scene": {
             "xaxis": {"title": {"font": {"size": 10}},
                       "tickfont": {"size": 10}},
             "yaxis": {"title": {"font": {"size": 10}},
                       "tickfont": {"size": 10}},
             "zaxis": {"title": {"font": {"size": 10}},
                       "tickfont": {"size": 10}},
             
        }
    })

# # # # # # # # # # # # # # # # normal scatter # # # # # # # # # # # # # # # # # 

def scatter_feature(feature):

    fig = px.scatter(
        india_pop,
        x=feature,
        y="poverty_multi_tot_2019_DV",
        size="total_population",
        hover_data="state_ut",
        color="poverty_multi_tot_2019_DV",
        color_continuous_scale="Reds",
        # color_discrete_sequence=["rgb(211, 82, 82)"]
    ).update_traces({
        "marker": {"size": india_pop["total_population"]*5},
        "line": {"width": .001, "color": "black"}
    }).update_layout({
        "xaxis": {"title": {"font": {"size": 11}}, "tickfont": {"size": 8}},
        "yaxis": {"title": {"font": {"size": 11}}, "tickfont": {"size": 8}},
        "coloraxis_showscale": False,
        "clickmode":"select",
        "margin": {"t": 0, "b": 0, "r": 0, "l": 0}
    })

    return fig


scatter_feature("has_tv")

# # # # # # # # # # # # # # # # text # # # # # # # # # # # # # # # # # 

def show_feature_text(feature):
        ft_mk = india_desc["features"] == feature
        ft_text = india_desc.loc[ft_mk, "descriptions"].values[0]

        if india_desc.loc[ft_mk, "analysis"].values[0] is not np.nan:
            ft_text2 = india_desc.loc[ft_mk, "analysis"].values[0]

            ft_text_elementv2 = html.Div(
                [
                    dmc.Text(
                        "Description",
                        c="black",
                        size="sm",
                        fw=500,
                        className="text_header_2"
                    ),
                    dmc.Text(
                        ft_text,
                        c="gray",
                        size="xs",
                        className="text_standard_intro"
                    ),
                    dmc.Text(
                        "Analysis",
                        c="black",
                        size="sm",
                        fw=500,
                        className="text_header_2"
                    ),
                    dmc.Text(
                        ft_text2,
                        c="gray",
                        size="xs",
                        className="text_standard_intro_2"
                    )
                ]
            )
            # ft_text_element = dmc.Text(
            #     [
            #         "Description: ",
            #         ft_text,
            #         html.Br(),
            #         html.Br(),
            #         "Analysis: ",
            #         ft_text2
            #     ],
            #     c="gray",
            #     size="xs",
            # )

            return ft_text_elementv2

        else:
            ft_text_elementv2 = html.Div(
                [
                    dmc.Text(
                        "Description",
                        c="black",
                        size="sm",
                        fw=500,
                        className="text_header_2"
                    ),
                    dmc.Text(
                        ft_text,
                        c="gray",
                        size="xs",
                        className="text_standard_intro_2"
                    ),
                ],
            )
   
            return ft_text_elementv2
    
# # # # # # # # # # # # # # # # residuals vs predicted # # # # # # # # # # # # # # # # # 
def residuals_vs_predicted():

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=ys_df["y_preds"],
            y=ys_df["y"]-ys_df["y_preds"],
            mode="markers",
            marker={"color": "#202A44"},
            name=""
        )
    )

    fig.add_hline(y=0, line_color="red")

    fig.update_layout({
        "title": {"text": "Residuals vs Predicted Values", "x": 0.5, "font": {"size": 11}},
        "xaxis": {"title": {"text": "Predictions (from poverty_multi_tot_2019_DV)", "font": {"size": 11}}, "tickfont": {"size": 8}},
        "yaxis": {"title": {"text": "Residuals", "font": {"size": 11}}, "tickfont": {"size": 8}},
        "clickmode": "select",
        "margin": {"t": 25, "b": 0, "r": 0, "l": 0}

})

    return fig


# # # # # # # # # # # # # # # # residual_distribution # # # # # # # # # # # # # # # # # 
def residual_distribution():

    fig = px.histogram(ys_df["y"]-ys_df["y_preds"], color_discrete_sequence=["#202A44"], nbins=30)

    fig.update_layout({"title": {"text": "Residual Distribution", "x": 0.5}, "legend": {"visible": False}})

    return fig.update_layout({
        "title": {"font": {"size": 11}},
        "xaxis": {"title": {"font": {"size": 11}}},
        "yaxis": {"title": {"font": {"size": 11}}},
        "clickmode": "select",
        "margin": {"t": 25, "b": 0, "r": 0, "l": 0}        
        })


# # # # # # # # # # # # # # # # all_coefficients # # # # # # # # # # # # # # # # # 
def all_coefficients():

    fig = px.bar(
        coef_df.sort_values(by="Feature", ascending=False),
        y="Feature",
        x="Coefficient",
        color_discrete_sequence=["#202A44"]
    )

    fig.update_layout({
        "title": {"text": "All Feature Importances", "x": 0.5, "font": {"size": 11}},
        "xaxis": {"title": {"font": {"size": 11}}, "tickfont": {"size": 8}},
        "yaxis": {"title": {"font": {"size": 11}}, "tickfont": {"size": 8}},
        "clickmode": "select",
        "margin": {"t": 25, "b": 0, "r": 0, "l": 0}            
    })

    return fig


# # # # # # # # # # # # # # # # final_coefficients # # # # # # # # # # # # # # # # # 
def final_coefficients():

    fig = px.bar(
        final_coef_df.sort_values(by=["Abs_Coefficient"], ascending=True)[:15],
        y="Feature",
        x="Abs_Coefficient",
        color_discrete_sequence=[px.colors.sequential.Magma[8]]
    ).update_layout({
        "title": {"text": "Top 14 Variables", "x": 0.5}
    })

    return fig.update_layout({
        "title": {"font": {"size": 11}},
        "xaxis": {"title": {"font": {"size": 11}}, "tickfont": {"size": 8}},
        "yaxis": {"title": {"font": {"size": 11}}, "tickfont": {"size": 8}},        
        "clickmode": "select",
        "margin": {"t": 25, "b": 0, "r": 0, "l": 0}        
    })


# # # # # # # # # # # # # # # # predicted_vs_actuals # # # # # # # # # # # # # # # # # 

def predicted_vs_actuals(filter):

    if len(filter) > 0:
        st_mk = ys_df["state_ut"].isin(filter)
        df = ys_df[st_mk]
    else:
        df = ys_df

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["y"],
            y=df["y_preds"],
            text=df["state_ut"],
            mode="markers+text",
            textposition="top center",
            textfont={"size": 9},
            marker={"color": "#202A44"},
            showlegend=False
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[min(ys_df["y"]), max(ys_df["y"])],
            y=[min(ys_df["y"]), max(ys_df["y"])],
            mode="lines",
            line={"color": "red", "dash": "dash"},
            showlegend=False
        )
    )

    fig.update_layout({
        "title": {"text": "Actual vs Predicted Values", "x": 0.5, "font": {"size": 11}},
        "xaxis": {"range": [-2, 36], "title": {"font": {"size": 11}}, "tickfont": {"size": 8}},
        "yaxis": {"range": [-2, 36], "title": {"font": {"size": 11}}, "tickfont": {"size": 8}},           
        "clickmode": "select",
        "margin": {"t": 25, "b": 0, "r": 0, "l": 0}  
    })

    return fig
