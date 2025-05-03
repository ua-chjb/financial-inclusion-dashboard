from dash import Input, Output, State, exceptions
from urllib.request import urlopen
import json

with urlopen("https://datakit-march-april-public.s3.us-west-1.amazonaws.com/final_data/india_small.json") as response:
    states_uts = json.load(response)

from load_data import india
from charts import fig_geo, sorted_table, comparison_graph, show_feature_text, scatter_feature, predicted_vs_actuals

def callbacks_baby(app): 
    @app.callback(
        Output(component_id="comp0_dropdowns_s1_IND", component_property="value"),
        Output(component_id="comp0_dropdowns_s1_IND", component_property="style"), 
        Output(component_id="comp0_dropdowns_s1_DEP", component_property="value"),
        Output(component_id="comp0_dropdowns_s1_DEP", component_property="style"), 
        Input(component_id="comp0_dropdowns_s1_SC", component_property="value"),
    )
    def thebaggins(gandalfspipe):
        if gandalfspipe == "Independent Variables":
            return india.drop(["state_ut", "poverty_multi_tot_2019_DV"], axis=1).columns[0], {"display" : "block"}, None, {"display": "none"}
        else:
            return None, {"display" : "none"}, india[["poverty_multi_tot_2019_DV"]].columns[0], {"display": "block"}

    @app.callback(
        Output("comp1_chloromap_CBO", "figure"),
        Input("comp0_dropdowns_s1_IND", "value"),
        Input("comp0_dropdowns_s1_DEP", "value")        
    )
    def hillytops(merrysshoes, pippinspint):
        if merrysshoes and not pippinspint:
            return fig_geo(merrysshoes, states_uts)
        else:
            return fig_geo(pippinspint, states_uts)
    
    @app.callback(
            Output("comp3_STORE1", "data"),
            Input("comp3_scattermap_CBO", "clickData"),
            State("comp3_STORE1", "data")
    )
    def elephantes(clickData, stored_states):
        if not clickData:
            raise exceptions.PreventUpdate
        
        new_state = clickData["points"][0]["y"]

        if new_state in stored_states:
            stored_states.remove(new_state)
        else:
            stored_states.append(new_state)
        
        stored_states = stored_states[-2:]

        return stored_states


    @app.callback(
        Output("comp3_scattermap_CBO", "figure"),
        # Input("comp2_countryselect_COUNTRY", "value"),
        Input("comp2_countryselect_FEAT", "value"),
        Input("comp3_STORE1", "data")
    )
    # def sauron(ironmaiden, orc, mfkindragons):
    #     return comparison_graph(ironmaiden, orc, mfkindragons)
    def sauron(orc, mfkindragons):
        return comparison_graph(orc, mfkindragons)


    @app.callback(
        Output("comp5_datatable_BR", "children"),
        Input("comp0_dropdowns_s1_IND", "value"),
        Input("comp0_dropdowns_s1_DEP", "value")
    )
    def theageofman(legolas, aragorn):
        if legolas and not aragorn:
            return sorted_table(legolas)
        else:
            return sorted_table(aragorn)

    @app.callback(
        Output("comp9_treed_YUS", "figure"),
        Output("comp8_featuredescriptionDOO", "children"),
        Input("comp7_dropdown_taba_BEAU", "value")
    )
    def thedawnarises(gandalf):
        return scatter_feature(gandalf), show_feature_text(gandalf)

    @app.callback(
        Output("comp12_predsvsactuals_GRAP", "figure"),
        Input("comp15_dropdownstate_COUNTRY", "value")
    )
    def victory(lukeskywalker):
        return predicted_vs_actuals(lukeskywalker)