from fastapi import FastAPI
from open_gopro import WirelessGoPro, Params
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
app = FastAPI()


@app.get("/connectCameras")
async def connect_to_cameras():
    with WirelessGoPro() as gopro:
        gopro.ble_command.set_shutter(Params.Toggle.ENABLE)
    return {"message": "Cameras connected"}


@app.get("/record")
async def record():
    with WirelessGoPro() as gopro:
        gopro.ble_command.set_shutter(Params.Toggle.ENABLE)
    return {"message": "Recording started"}


@app.get("/stopRecording")
async def stopRecording():
    with WirelessGoPro() as gopro:
        gopro.ble_command.set_shutter(Params.Toggle.DISABLE)
    return {"message": "Recording stopped"}


@app.get("/getBattery")
async def getBattery():
    with WirelessGoPro() as gopro:
        battery_level = gopro.getBattery()
    return {"message": battery_level}


@app.get("/disconnectCameras")
async def disconnectCameras():
    with WirelessGoPro() as gopro:
        gopro.close()
    return {"message": "Cameras disconnected)"}


@app.get("/livestream")
async def livestream():
    livestream_url = "http://192.168.1.100:8080/live" # cambiar IP obvio
    return {"livestream_url": livestream_url}
    

#@app.get("/getVideo")
#async def getVideo():
#    response = {
#        "video": "https://res.cloudinary.com/dfpitoil1/video/upload/eo_10,so_6.5/v1681685906/fargowg6dr7m8wj9njcg.mp4"}
#    return JSONResponse(content=jsonable_encoder(response))
