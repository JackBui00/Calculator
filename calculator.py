import PySimpleGUI as sg


def Main():

    viewable_value = sg.Text()
    layout = [[viewable_value],
            [sg.Button("c",size = (8,1)), sg.Button("«",size = (8,1))],
            [sg.Button("7",size = (8,1)), sg.Button("8",size = (8,1)), sg.Button("9",size = (8,1)), sg.Button("/",size = (8,1))],
            [sg.Button("4",size = (8,1)), sg.Button("5",size = (8,1)), sg.Button("6",size = (8,1)), sg.Button("*",size = (8,1))],
            [sg.Button("1",size = (8,1)), sg.Button("2",size = (8,1)), sg.Button("3",size = (8,1)), sg.Button("-",size = (8,1))],
            [sg.Button(".",size = (8,1)), sg.Button("0",size = (8,1)), sg.Button("=",size = (8,1)), sg.Button("+",size = (8,1))],
            ]

    window = sg.Window("Calculator", layout)
    buffer = ""
    temp = ''

#Loop GUI
    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED:
            break
        
        elif event == "c":
            buffer = ""
            viewable_value.update("Cleared")
        
        elif event == "=":
            buffer = str(calculate(buffer))
            viewable_value.update(buffer)
            

        elif event == "*" or "+" or "-" or "/":
            buffer += event
            viewable_value.update(buffer)

    
        else:
            buffer += event
            temp = event
            viewable_value.update(temp)
            
        print(buffer)

    window.close()




def calculate(string):
    return eval(string)

if __name__ == "__main__":
    Main()