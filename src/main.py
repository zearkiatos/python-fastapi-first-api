import zoneinfo
from fastapi import FastAPI, Query
from datetime import datetime
from typing import Literal, Optional

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

country_timezones = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
    "US": "America/New_York",
    "CA": "America/Toronto",
    "VE": "America/Caracas",
    "CL": "America/Santiago"
}

time_formats = {
    "24h": "%H:%M:%S",
    "12h": "%I:%M:%S %p",
    "iso": "%Y-%m-%dT%H:%M:%S%z",
    "date": "%Y-%m-%d"
}

@app.get("/time/{iso_code}")
async def time(
    iso_code: str,
    time_format: Optional[Literal["24h", "12h", "iso", "date"]] = Query(default=None),
):
    iso_code_upper = iso_code.upper()

    timezone_str = country_timezones.get(iso_code_upper)

    timezone = zoneinfo.ZoneInfo(timezone_str)
    current_time = datetime.now(timezone)
    if time_format:
        timeformat_str = time_formats.get(time_format)
        if timeformat_str:
            current_time = current_time.strftime(timeformat_str)
    return {"time": current_time}