

# @app.get("/", response_class=HTMLResponse)
# async def display_menu(request: Request):
#     return HTMLResponse(content="""
#     <form action="/get_input" method="post">
#         <h2>Select a menu option (1-10):</h2>
#         <select name="menu_option">
#             <option value="1">Option 1 Linear Regression</option>
#             <option value="2">Option 2</option>
#         </select>
#         <br><br>
#         <input type="submit" value="Submit">
#     </form>
#     """, status_code=200)
#
#
# @app.post("/get_input", response_class=HTMLResponse)
# async def get_input(menu_option: int = Form(...)):
#     if menu_option == 1:
#         # Show form to accept two lists
#         return HTMLResponse(content="""
#         <h2>Enter X and Y values for Linear Regression</h2>
#         <form action="/linear_regression" method="post">
#             X values (comma-separated): <input type="text" name="x_values"><br><br>
#             Y values (comma-separated): <input type="text" name="y_values"><br><br>
#             <input type="submit" value="Run Linear Regression">
#         </form>
#         """, status_code=200)
#         print(HTMLResponse)
#     else:
#         # print(HTMLResponse)
#         return HTMLResponse(content=f"<h2>Option {menu_option} selected (not implemented)</h2>", status_code=200)


# @app.post("/linear_regression", response_class=HTMLResponse)
# async def run_linear_regression(x_values: str = Form(...), y_values: str = Form(...)):
#     try:
#         x_list = [float(x.strip()) for x in x_values.split(',')]
#         y_list = [float(y.strip()) for y in y_values.split(',')]
#
#         if len(x_list) != len(y_list):
#             return HTMLResponse(content="Error: X and Y must be the same length.", status_code=400)
#
#         X = np.array(x_list).reshape(-1, 1)
#         y = np.array(y_list)
#
#         model = LinearRegression()
#         model.fit(X, y)
#         slope = model.coef_[0]
#         intercept = model.intercept_
#
#         return HTMLResponse(content=f"""
#         <h2>Linear Regression Result</h2>
#         <p>Slope: {slope:.4f}</p>
#         <p>Intercept: {intercept:.4f}</p>
#         """, status_code=200)
#
#     except Exception as e:
#         return HTMLResponse(content=f"<h2>Error: {str(e)}</h2>", status_code=500)


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8080)


# from src.DataScience_Algorithms.utils.ImportsModule import *
# app = FastAPI()
#
# templates = Jinja2Templates(directory="templates")
#
# # Endpoint to display the menu
# @app.get("/", response_class=HTMLResponse)
# async def display_menu(request: Request):
#     menu = """
#     <form action="/get_input" method="post">
#         <h2>Select a menu option (1-10):</h2>
#         <select name="menu_option">
#             <option value="1">Option 1 Linear Regression</option>
#             <option value="2">Option 2</option>
#             <option value="3">Option 3</option>
#             <option value="4">Option 4</option>
#             <option value="5">Option 5</option>
#             <option value="6">Option 6</option>
#             <option value="7">Option 7</option>
#             <option value="8">Option 8</option>
#             <option value="9">Option 9</option>
#             <option value="10">Option 10</option>
#         </select>
#         <br><br>
#         <input type="submit" value="Submit">
#     </form>
#     """
#     return HTMLResponse(content=menu, status_code=200)
#
# # Endpoint to handle user input
# @app.post("/get_input", response_class=HTMLResponse)
# async def get_input(menu_option: int = Form(...)):
#     print(menu_option)
#     if menu_option == 1:
#         # User input Code here
#
#         @app.post("python main.py")
#         async def create_item(item: Item):
#             return {"received_names": item.names}
#
#
#     # # Process the user's selected option
#     # return HTMLResponse(content=f"<h2>You selected Option {menu_option}</h2>", status_code=200)
#
# if __name__ == "__main__":
#
#     uvicorn.run(app, host="0.0.0.0", port=8080)