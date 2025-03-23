import FreeSimpleGUI as sg

"""alternative solution: place this function into a separate file and call using from xx import yy"""
def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


label_ft = sg.Text("Enter feet: ")
input_ft = sg.Input(key="feet")

label_in = sg.Text("Enter inches: ")
input_in = sg.Input(key="inches")

button = sg.Button("Convert")
output_label = sg.Text("", key="output")

window = sg.Window("Convertor",
                   [[label_ft, input_ft],
                    [label_in, input_in],
                    [button, output_label]
                    ])

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result} m", text_color="white")
    
window.close()
