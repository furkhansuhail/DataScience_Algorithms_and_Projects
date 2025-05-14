from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.DataScience_Algorithms.entity import DataIngestionConfig
from src.DataScience_Algorithms.utils.ImportsModule import *
from src.DataScience_Algorithms.pipeline.LinearRegression_Pipeline import LinearRegression_Execution
from main import LinearRegression_RunCommand
from main import LogisticRegression_RunCommand


import uvicorn
import threading
import os

app = FastAPI()

shutdown_button_html = """
    <form action="/shutdown" method="post" style="margin-top: 20px;">
        <input type="submit" value="Shutdown Server" style="background-color:red; color:white;">
    </form>
"""

templates = Jinja2Templates(directory="templates")

back_to_menu_button_html = """
    <form action="/" method="get" style="margin-top: 20px;">
        <input type="submit" value="Back to Main Menu" style="background-color:green; color:white;">
    </form>
"""


# Step 1: Menu page
@app.get("/", response_class=HTMLResponse)
async def display_menu(request: Request):
    menu = """
    <form action="/get_input" method="post">
        <h2>Select a menu option (1-10):</h2>
        <select name="menu_option">
            <option value="1">Option 1 Linear Regression</option>
            <option value="2">Option 2 Logistic Regression</option>
            <option value="3">Option 3</option>
            <option value="4">Option 4</option>
            <option value="5">Option 5</option>
            <option value="6">Option 6</option>
            <option value="7">Option 7</option>
            <option value="8">Option 8</option>
            <option value="9">Option 9</option>
            <option value="10">Option 10</option>
        </select>
        <br><br>
        <input type="submit" value="Submit">
    </form>
    """
    return HTMLResponse(content=menu + back_to_menu_button_html + shutdown_button_html, status_code=200)


# Step 2: Redirect to form for Option 1 for Linear Regression
@app.post("/get_input", response_class=HTMLResponse)
async def get_input(menu_option: int = Form(...)):
    if menu_option == 1:
        form_html = """
        <form action="/submit_lists" method="post">
            <label>Enter list 1 (comma-separated):</label><br>
            <input type="text" name="list1"><br><br>

            <label>Enter list 2 (comma-separated):</label><br>
            <input type="text" name="list2"><br><br>

            <label>Enter value to Predict:</label><br>
            <input type="text" name="ValueTOPredict"><br><br>

            <input type="submit" value="Submit Lists">
        </form>
        """
        return HTMLResponse(content=form_html + back_to_menu_button_html + shutdown_button_html)

    elif menu_option == 2:
        form_html = """
            <form action="/submit_lists_LogisticRegression" method="post">
                <label>Enter list 1 (comma-separated):</label><br>
                <input type="text" name="list1"><br><br>

                <label>Enter list 2 (comma-separated):</label><br>
                <input type="text" name="list2"><br><br>

                <input type="submit" value="Submit Lists">
            </form>
            """
        return HTMLResponse(content=form_html + back_to_menu_button_html + shutdown_button_html)

    else:
        return HTMLResponse(
            content=f"<h2>You selected Option {menu_option}</h2>" + back_to_menu_button_html + shutdown_button_html)
    # else:
    #     return HTMLResponse(content=f"<h2>You selected Option {menu_option}</h2>"+ back_to_menu_button_html + shutdown_button_html)




# Step 1.a: Handle the two input lists for LinearRegression
@app.post("/submit_lists", response_class=HTMLResponse)
async def submit_lists(list1: str = Form(...), list2: str = Form(...), ValueTOPredict: str = Form(...)):
    try:
        list1_values = [float(x.strip()) for x in list1.split(',')]
        list2_values = [float(x.strip()) for x in list2.split(',')]
        ValueTOPredict = [float(x.strip()) for x in ValueTOPredict.split(',')]

        if len(list1_values) != len(list2_values):
            return HTMLResponse(content="""
                <h3>Error: List 1 and List 2 must have the same number of elements.</h3>
                """ + shutdown_button_html)

        # linearRegressionModel = LinearRegression_Execution(list1_values, list2_values, ValueTOPredict)
        # prediction = linearRegressionModel.predicted_value

        linearRegressionModel = LinearRegression_RunCommand(list1_values, list2_values, ValueTOPredict)
        prediction = linearRegressionModel.predicted_value
        print(prediction)

        return HTMLResponse(content=f"""
            <h3>Received List 1: {list1_values}</h3>
            <h3>Received List 2: {list2_values}</h3>
            <h3>Prediction for {ValueTOPredict[0]} is: {prediction}</h3>
            {back_to_menu_button_html}
            {shutdown_button_html}
        """)
    except ValueError:
        return HTMLResponse(content="""
            <h3>Error: Please enter only numeric values, separated by commas.</h3>
            """ + back_to_menu_button_html + shutdown_button_html)




@app.post("/submit_lists_LogisticRegression", response_class=HTMLResponse)
async def submit_lists_LogisticRegression(list1: str = Form(...), list2: str = Form(...), ValueTOPredict: str = Form(...)):
    try:
        list1_values = [float(x.strip()) for x in list1.split(',')]
        list2_values = [float(x.strip()) for x in list2.split(',')]
        ValueTOPredict = [float(x.strip()) for x in ValueTOPredict.split(',')]

        if len(list1_values) != len(list2_values):
            return HTMLResponse(content="""
                <h3>Error: List 1 and List 2 must have the same number of elements.</h3>
                """ + shutdown_button_html)

        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        linearRegressionModel = LogisticRegression_RunCommand(list1_values, list2_values)
        # prediction = linearRegressionModel.predicted_value
        # print(prediction)

        return HTMLResponse(content=f"""
            <h3>Received List 1: {list1_values}</h3>
            <h3>Received List 2: {list2_values}</h3>
            <h3>Prediction for {ValueTOPredict[0]} is: 0 </h3> 
            {back_to_menu_button_html}
            {shutdown_button_html}
        """)
        # {prediction}</h3>
    except ValueError:
        return HTMLResponse(content="""
            <h3>Error: Please enter only numeric values, separated by commas.</h3>
            """ + back_to_menu_button_html + shutdown_button_html)






# Graceful shutdown
@app.post("/shutdown")
async def shutdown():
    def stop():
        os._exit(0)
    threading.Thread(target=stop).start()
    return HTMLResponse("<h3>Server is shutting down...</h3>")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
