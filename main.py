from taipy.gui import Gui
from visualize_charts import visualizing_errors
from parse_json import pretty_print
from taipy.gui import navigate

root_md = ""

text = ""
url = ""
data_errors = {}
data_alerts = {}

page1 = """
# Accesibility Checker 
# Enter the URL of your website to easily perform an accessibility check

<|{text}|input|>
<|Check accessibility|button|on_action=on_button_action|>
"""

def on_button_action(state):
    global url, data_errors, data_alerts
    page = "accessibilitycharts"
    url = state.text
    print("url: " + url)
    json_data = pretty_print(url)
    errors_array = json_data[0]
    contrast_errors_array = json_data[1]
    alerts_array = json_data[2]

    result = visualizing_errors(errors_array, contrast_errors_array, alerts_array)
    state.data_errors = result[0]
    state.data_alerts = result[1]
    navigate(state, to=page)

page2 = """

## Accessibility Visualization

# Bar graph for errors

<|{data_errors}|chart|type=bar|x=Type of Error|y=Number of Errors|>

# Pie chart for errors

<|{data_errors}|chart|type=pie|values=Number of Errors|label=Type of Error|>

# Bar graph for alerts

<|{data_alerts}|chart|type=bar|x=Type of Alert|y=Number of Alerts|>

# Pie chart for alerts

<|{data_alerts}|chart|type=pie|values=Number of Alerts|label=Type of Alert|>

"""

pages = {
     "/": root_md,
    "enterurl": page1,
    "accessibilitycharts": page2
}

Gui(pages=pages).run(use_reloader=True, port=5001)
