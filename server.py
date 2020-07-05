from fastapi import FastAPI, UploadFile, File
import numpy
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
import traceback
app = FastAPI()

app.mount("/public", StaticFiles(directory="public"), name="public")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
async def root():
    return FileResponse("./public/index.html", media_type="text/html")


@app.post("/cartoonify")
async def cartoonify(image: UploadFile = File(...)):
    return {"filename": image.filename}



def process():
    import cv2

    num_down = 2  # number of downsampling steps
    num_bilateral = 7  # number of bilateral filtering steps

    img_rgb = cv2.imread("img_example.jpg")

    # downsample image using Gaussian pyramid
    img_color = img_rgb
    for _ in range(num_down):
        img_color = cv2.pyrDown(img_color)

    # repeatedly apply small bilateral filter instead of
    # applying one large filter
    for _ in range(num_bilateral):
        img_color = cv2.bilateralFilter(img_color, d=9,
                                        sigmaColor=9,
                                        sigmaSpace=7)

    # upsample image to original size
    for _ in range(num_down):
        img_color = cv2.pyrUp(img_color)