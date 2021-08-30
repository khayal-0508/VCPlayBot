
from os import path

from youtube_dl import YoutubeDL

from VCPlayBot.config import DURATION_LIMIT
from VCPlayBot.helpers.errors import DurationLimitError

ydl_opts = {
    "format": "bestaudio/best",
    "verbose": True,
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}

ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info["duration"] / 60)

    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"🛑 {DURATION_LIMIT} dəqiqədən böyük faylların yüklənməsinə icazə verilmir, "
            f"bu fayl {duration} dəqiqədir",
        )
    try:
        ydl.download([url])
    except:
        raise DurationLimitError(
            f"🛑 {DURATION_LIMIT} dəqiqədən böyük faylların yüklənməsinə icazə verilmir, "
            f"bu fayl {duration} dəqiqədir",
        )
    return path.join("downloads", f"{info['id']}.{info['ext']}")
