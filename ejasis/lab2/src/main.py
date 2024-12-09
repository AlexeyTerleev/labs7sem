from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
import time
import logging
from neural_mehod import neural_predict_language
from abc_method import abc_predict_language
from fw_method import fw_predict_language
from extract_raw_text import extract_text_from_html
import uvicorn


logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("fastapi.log"), 
        logging.StreamHandler() 
    ]
)

logger = logging.getLogger(__name__)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.mount(
    "/static", StaticFiles(directory=os.getcwd().removesuffix('/src') + '/'), name="static"
)


@app.get("/", response_class=FileResponse)
async def read_index():
    response = FileResponse(os.getcwd().removesuffix('/src') + "/static/index.html")
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


@app.get("/frequency")
async def frequency_method(current_file):
    language = fw_predict_language(current_file)
    return JSONResponse(content={"language": language})


@app.get('/alphabetical')
async def alphabetical_method(current_file):
    language = abc_predict_language(current_file)
    return JSONResponse(content={"language": language})


@app.get('/neural')
async def neural_method(current_file):
    language = neural_predict_language(current_file)
    return JSONResponse(content={"language": language})


@app.get('/access_file_content')
async def get_file(file_name: str) -> JSONResponse:
    result_dict = {"file_name": file_name, "raw_text": ""}
    match file_name.split('.')[-1]:
        case "html":
            try:
                result_dict["raw_text"] = extract_text_from_html(
                    os.getcwd().removesuffix('/src') + '/files/' + file_name)
                logger.debug(
                    os.getcwd().removesuffix('/src') + '/files/' + file_name)
            except:
                result_dict["raw_text"] = ""
                return HTTPException(500, "Error during html unpacking")
        case "txt":
            try:
                with open(os.getcwd().removesuffix('/src') + '/files/' + file_name, 'r', encoding='utf-8') as current_file:
                    logger.debug(
                        os.getcwd().removesuffix('/src') + '/files/' + file_name)
                    result_dict["raw_text"] = current_file.read()
                    logger.debug(current_file.closed)
            except:
                result_dict["raw_text"] = ""
                return HTTPException(500, "Error during txt unpacking")
    return JSONResponse(content=result_dict)


@app.post("/upload_file")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(f"files/{file.filename}")
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        return {"filename": file.filename, "path": file_path}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while uploading the file: {str(e)}")
    

if __name__ == "__main__":
    config = {
        "app": "main:app",
    }
    uvicorn.run(**config)
