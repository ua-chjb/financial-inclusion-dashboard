import pandas as pd
import numpy as np

from dash import html, dcc, _dash_renderer
from dash_iconify import DashIconify
import dash_mantine_components as dmc
_dash_renderer._set_react_version('18.2.0')

# import plotly.express as px
# import plotly.graph_objs as go

from load_data import india, ys_df
from charts import residuals_vs_predicted, residual_distribution, all_coefficients, final_coefficients, predicted_vs_actuals
# from color import scientific_layout


############################### layout ##################################

# # # # # # # # # # # # # # tab_A # # # # # # # # # # # # # #

comp6_introdesc = dmc.Card(
    [
        dmc.Text(
            [
                "Project Introduction"
            ],
            fw=500,
            size="l",
            className="text_header"
        ),
        dmc.Text(
            "India has made great strides in alleviating poverty in the past decade, with notable gains in the elimination of extreme poverty, defined as earning less than the US purchasing power equivalent of $2.15 per day. To achieve this reduction, India has funded several assistance programs, to include MGNREGA (employment opportunities for rural households), PMAY (affordable housing), and PMJDY (banking services). Other approaches have included economic reforms, and ensuring adequate access to essential services. In spite of these advances, poverty levels still vary widely between regions.",
            c="gray",
            size="xs",
            className="text_standard_intro"
        ),
        dmc.Text(
            "DataKind was founded in 2012 around the idea of utilizing data analysis and data science for positive social impact in communities around the world. Staff and volunteers working for DataKind have completed data-for-good projects in a wide variety of fields, including climate, energy, health and medicine, education, economic opportunity, financial inclusion, and data collection and management. DataKind continues to adapt to the changing needs of the social impact sector, with a recent focus on assisting nonprofits in leveraging data science and AI technologies.",
            c="gray",
            size="xs",
            className="text_standard_intro"
        ),
        dmc.Text(
            "Under a DataKind DataKit initiative to study financial inclusion and economic opportunity in countries around the world, our team developed a machine learning model to determine the relative importance of inputs to poverty in India. Out of close to 300 features, our analysis revealed 14 variables of interest that covered a wide range of categories. These visualizations give an overview of the model and let you explore what we discovered. ",
            c="gray",
            size="xs",
            className="text_standard_intro"
        ),
        dmc.Text(
            "Team members: Tony M., Benjamin N., Pratik P., Husayn S., and Trevor W.",
            c="gray",
            size="xs",
            className="text_standard_intro_2"
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp6_introdesc"
)

tab_A = html.Div(
    [
        comp6_introdesc,
    ],
    className="dA"
)


# # # # # # # # # # # # # # tab_D # # # # # # # # # # # # # #

comp15_dropdownstate_v2 = dmc.Card(
    [
        dmc.MultiSelect(
            label="State / UT",
            placeholder="to show original graph, click the x",
            data=ys_df["state_ut"],
            value=[],
            maxValues=5,
            withScrollArea=True, 
            clearable=True,
            searchable=True,
            comboboxProps={"maxwidth":"45vw"},
            id="comp15_dropdownstate_COUNTRY",
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp15_dropdownstate"    
)


comp10p1_residuals = dmc.Card(
    [
        dcc.Graph(
            figure=residuals_vs_predicted(), 
            id="comp10_residuals_graph1", 
            className="g",
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp10p1_residuals"
)

comp10p2_residuals = dmc.Card(
    [
        dcc.Graph(
            figure=residual_distribution(), 
            id="comp10_residuals_graph2", 
            className="g",
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp10p2_residuals"
)

comp11_allfeaturecoefs = dmc.Card(
    [
        dcc.Graph(figure= all_coefficients(), id="comp11_allfeaturecoefs", className="g")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp11_allfeaturecoefs"
)

comp14_textofmodel = dmc.Card(
    [
        dmc.Text(
            "Model Selection - Distilling Complexity",
            fw=500,
            size="l",
            className="text_header"
        ),
        dmc.Text(
            "The team sourced, cleaned, and assembled a set of 298 variables related to financial inclusion and economic opportunity in India. In an effort to identify the most significant ones, a Ridge Regression model was built to identify the strongest predictors of poverty, as a percentage of total headcount in each state. The predictive model identified 14 variables, through a process of 5-fold cross validation. As a result of the model, it can be assumed that these 14 variables, when combined together, explain 92 % of the variance in the target variable. The model was chosen because of its suitability to handle data which consist of more variables than observations, and high degrees of multicollinearity amongst the variables.",
            c="gray",
            size="xs",
            className="text_standard"
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp14_textofmodel"
)

comp12_predsvsactuals = dmc.Card(
    [
        dcc.Graph(figure={}, id="comp12_predsvsactuals_GRAP", className="g")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp12_predsvsactuals"
)

comp13_finalcoefs = dmc.Card(
    [
        dcc.Graph(figure=final_coefficients(), id="comp13_finalcoefs_graph", className="g")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp13_finalcoefs"
)

tab_D_inline_grid = html.Div(
    [
        comp10p1_residuals, 
        comp10p2_residuals
    ],
    className="gd"
)

tab_D_inline = html.Div(
    [
        comp15_dropdownstate_v2,
        comp12_predsvsactuals,
        tab_D_inline_grid,
        comp14_textofmodel,
        comp13_finalcoefs

    ],
    className="in"
)

tab_D = html.Div(
    [
        comp11_allfeaturecoefs,
        tab_D_inline
    ],
    className="dD"
)

# # # # # # # # # # # # # # tab_E # # # # # # # # # # # # # #

comp7_dropdown_taba = dmc.Card(
    [
        dmc.Select(
            label="Variable",
            placeholder="select...",
            value=india.drop(["state_ut", "poverty_multi_tot_2019_DV"], axis=1).columns[0],
            data=india.drop(["state_ut", "poverty_multi_tot_2019_DV"], axis=1).columns,
            clearable=False,
            id="comp7_dropdown_taba_BEAU"
        ),
        dmc.Text(
            id="comp8_featdesc_ENTER",
            className="text_needmargin"
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp7_dropdown_taba"
)

comp8_featuredescription = dmc.Card(
    [
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    id="comp8_featuredescriptionDOO",
    className="t comp8_featuredescription"
)


comp78_inline = dmc.Card(
    [
        comp7_dropdown_taba,
        comp8_featuredescription
    ],
    className="in comp78_inline"
)

comp9_treed = dmc.Card(
    [
        dcc.Graph(figure={}, id="comp9_treed_YUS", style={"height": "100%"})
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp9_treed"
)

tab_E = html.Div(
    [
        comp78_inline,
        comp9_treed
    ],
    className="d dE"
)

# # # # # # # # # # # # # # tab_B # # # # # # # # # # # # # #

comp0_dropdowns_s1 = dmc.Card(
    [
        dmc.SegmentedControl(
            orientation="horizontal",
            id="comp0_dropdowns_s1_SC",
            value="Independent Variables",
            style={"width": "100%"},
            data=[
                {"value": "Independent Variables", "label": "Independent Variables"},
                {"value": "Dependent Variable", "label": "Dependent"},
            ],
            className="ic segmentedcontrol"
        ),
        dmc.Select(
            placeholder="select...",
            value=india.drop(["state_ut", "poverty_multi_tot_2019_DV"], axis=1).columns[0],
            data=india.drop(["state_ut", "poverty_multi_tot_2019_DV"], axis=1).columns,
            style={"display": "block"},
            clearable=False,
            id="comp0_dropdowns_s1_IND",
            className="ic dropdown"
        ),

        dmc.Select(
            placeholder="select...",
            value=india[["poverty_multi_tot_2019_DV"]].columns[0],
            data=[india[["poverty_multi_tot_2019_DV"]].columns[0]],
            style={"display": "none"},
            clearable=False,
            id="comp0_dropdowns_s1_DEP",
            className="ic dropdown"
        )        
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp0_dropdowns_s1"
)

comp4_featuretext = dmc.Card(
    [
        dmc.Text(
            "There are certain values for the states Ladakh and Jammu & Kashmir that are missing or indicated as zero, due to difficulty in collecting data. Obstacles are mainly of organizational character because of ongoing reforms (at the time of data collection), transition of administration in these states, or delays in the reporting process for logistical reasons.",
            c="gray",
            size="xs",
            className="text_standard"
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp4_featuretext"
)

comp1_chloromap = dmc.Card(
    [
        dcc.Graph(figure={}, id="comp1_chloromap_CBO")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp1_chloromap"
)

comp0p4_inline = html.Div(
    [
        comp0_dropdowns_s1,
        comp4_featuretext,
    ],
    className="in"
)

comp5_datatable = dmc.Card(
    [
        dmc.Container(id="comp5_datatable_BR")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp5_datatable"
)

tab_B_above = html.Div(
    [
        comp0p4_inline,
        comp1_chloromap,
    ],
    className="d dB"
)

tab_B_below = html.Div(
    [
        comp5_datatable
    ],
    className="dB1"
)

tab_B = html.Div(
    [
        tab_B_above,
        tab_B_below
    ]
)


# # # # # # # # # # # # # # tab_C # # # # # # # # # # # # # #

comp2_dropdowns = dmc.Card(
    [
        # dmc.MultiSelect(
        #     placeholder="select up to 3...",
        #     data=india["state_ut"],
        #     value=india["state_ut"][0:2],
        #     maxValues=3,
        #     withScrollArea=True, 
        #     clearable=False,
        #     searchable=True,
        #     comboboxProps={"width":"100%"},
        #     id="comp2_countryselect_COUNTRY",
        #     className="ic dropdown ddC notopmargin",
        # ),
        dmc.MultiSelect(
            label="Variables",
            placeholder="select up to 14...",
            data=india.drop(["state_ut", "poverty_multi_tot_2019_DV"], axis=1).columns,
            value=india.drop(["state_ut", "poverty_multi_tot_2019_DV"], axis=1).columns[6:11],
            maxValues=14,
            withScrollArea=True, 
            clearable=False,
            searchable=True,
            comboboxProps={"width":10000},
            id="comp2_countryselect_FEAT",
            # className="ic dropdown ddC",
        )
    ],
    withBorder=True,
    shadow="xs",
    radius="md", 
    className="t comp2_dropdowns",
    style={"width": "100%"}
)


comp3_scattermap = dmc.Card(
    [
        dcc.Store(id="comp3_STORE1", data=["Delhi", "Chandigarh"], storage_type="memory"),
        dcc.Graph(figure={}, id="comp3_scattermap_CBO")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp3_scattermap"
)


tab_C = html.Div(
    [
        comp2_dropdowns,
        comp3_scattermap
    ],
    className="d dC"
)
# # # # # # # # # # # # # # tabs # # # # # # # # # # # # # #

Tabs = html.Div(
    [
        dmc.Tabs(
            [
                dmc.TabsList(
                    [
                        dmc.TabsTab(
                            "Introduction",
                            leftSection=DashIconify(icon="material-symbols:bookmark-manager-rounded", width=20, color="black", className="icons-2"),
                            value="introduction"
                        ),
                        dmc.TabsTab(
                            "Model",
                            leftSection=DashIconify(icon="material-symbols:modeling-outline-rounded", width=20, color="black", className="icons-2"),
                            value="model"
                        ),
                        dmc.TabsTab(
                            "Variable Explorer",
                            leftSection=DashIconify(icon="material-symbols:explore-outline-rounded", width=20, color="black", className="icons-2"),
                            value="variable_explorer"),
                        dmc.TabsTab(
                            "Map",
                            leftSection=DashIconify(icon="material-symbols:travel-explore-rounded", width=20, color="black", className="icons-2"),
                            value="states"
                        ),
                        dmc.TabsTab(
                            "Comparison Tool",
                            leftSection=DashIconify(icon="material-symbols:combine-columns", width=20, color="black", className="icons-2"),
                            value="comp"
                        )
                    ]
                ),
                dmc.TabsPanel(
                    tab_A,
                    value="introduction"
                ),        
                dmc.TabsPanel(
                    tab_D,
                    value="model"
                ),        
                dmc.TabsPanel(
                    tab_E,
                    value="variable_explorer"
                ),        
                dmc.TabsPanel(
                    tab_B,
                    value="states"
                ),
                dmc.TabsPanel(
                    tab_C,
                    value="comp"
                ),
            ],
            color="red",
            value="introduction",
            variant="outline"
        )
    ],
    className="tabs_main nm"
)

# # # # # # # # # # # # # # mobile # # # # # # # # # # # # # #

mobile_component = html.Div(
    [
        dmc.Card(
            [
                dmc.Text(
                    "This dashboard is not optimized for mobile. Please access from a desktop.",
                    size="xs",
                )
            ],
            withBorder=True,
            shadow="sm",
            radius="md",
            className="mn-1"
        )
    ],
    className="mn-2"
)

# # # # # # # # # # # # # # title # # # # # # # # # # # # # #


title = dmc.Card(
    [
        dmc.Text(
            "Financial Inclusion in India",
            size="xl",
            fw=600
            )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t tit nm",
)

############################### composition ##################################

lyt = dmc.MantineProvider(
    [
        title,
        Tabs,
        mobile_component
    ]
)