import datetime
import azure.functions as func
import logging
# from fastapi_endpoints import app as fastapi_app

# app = func.AsgiFunctionApp(app=fastapi_app, http_auth_level=func.AuthLevel.FUNCTION)
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    today = datetime.datetime.now().date()
    wkday = today.weekday()
    today_message = f"Today is {wkday}, {today.isoformat()}"

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. {today_message}.")
    else:
        return func.HttpResponse(
             f"This HTTP triggered function executed successfully. {today_message}",
             status_code=200
        )