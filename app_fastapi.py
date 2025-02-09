from datetime import datetime
import uvicorn
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
import models
# import models_dc as models
import config as cfg
import time


app = FastAPI()


# single_orders = []
# for k in range(cfg.num_req):
#     single_orders.append(
#         models.Order(
#             symbol=str(k),
#             instrument_id=str(k),
#             side='buy',
#             volume=50,
#             start_time=datetime.now().isoformat(timespec='milliseconds'),
#             end_time=datetime.now().isoformat(timespec='milliseconds'),
#         )
#     )
#
# resp_ = models.Responses(
#     id='10',
#     status=200,
#     message='ok',
#     data=models.Orders(single=single_orders)
# )
#
# resp_json = resp_#.__dict__

@app.get("/")
async def root(request: Request) -> Response:
    # tic = time.time()
    single_orders = []
    for k in range(cfg.num_order):
        single_orders.append(
            models.Order(
                symbol=str(k),
                instrument_id=str(k),
                side='buy',
                volume=50,
                start_time=datetime.now().isoformat(timespec='milliseconds'),
                end_time=datetime.now().isoformat(timespec='milliseconds'),
            )
        )

    # # toc = time.time()
    # elapsed_time = time.time() - tic
    # print(f"Elapsed time: {elapsed_time} seconds")
    #
    # tic = time.time()

    resp = Response(
        status_code=200,
        headers={"Content-Type": "application/json"},
        content=models.Orders(single=single_orders).model_dump_json(),
    )

    # # toc = time.time()
    # elapsed_time = time.time() - tic
    # print(f"Elapsed time: {elapsed_time} seconds")

    return resp

# @app.get("/", response_model=models.Responses)
# async def root():
#     single_orders = []
#     for k in range(cfg.num_order):
#         single_orders.append(
#             models.Order(
#                 symbol=str(k),
#                 instrument_id=str(k),
#                 side='buy',
#                 volume=50,
#                 start_time=datetime.now().isoformat(timespec='milliseconds'),
#                 end_time=datetime.now().isoformat(timespec='milliseconds'),
#             )
#         )
#
#     return models.Responses(
#         id='10',
#         status=200,
#         message='ok',
#         data=models.Orders(single=single_orders)
#     )

# @app.get("/", response_model=models.Responses)
# async def root():
#     return resp_json
#     # return JSONResponse(resp_json)


# @app.get("/")
# async def root():
#     return "Hello, World!"


if __name__ == '__main__':
    # execute this command in terminal
    # fastapi dev main.py
    # ab -n 20000 -c 10 http://127.0.0.1:8901/

    host = 'http://127.0.0.1'
    port = 8901
    r = f'{host}:{port}'
    docs = r + '/docs'
    print(r)
    print(docs)

    # uvicorn.run(app="main:app", host="0.0.0.0", port=9000, reload=True, workers=4)
    uvicorn.run(app="app_fastapi:app", host="0.0.0.0", port=port, workers=cfg.num_workers, log_level="warning")




