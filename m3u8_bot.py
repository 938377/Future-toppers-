import os
from pyrogram import Client, filters
import subprocess

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client("m3u8_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply_text("👋 Welcome! Send me a `.m3u8` video link to get your video.")

@app.on_message(filters.text & ~filters.command("start"))
async def download_video(client, message):
    url = message.text.strip()
    if not url.endswith(".m3u8"):
        await message.reply_text("❌ Please send a valid `.m3u8` URL.")
        return

    status = await message.reply("📥 Downloading video. Please wait...")
    filename = f"{message.chat.id}_video.mp4"
    cmd = f'yt-dlp -o "{filename}" --downloader ffmpeg --hls-use-mpegts "{url}"'

    try:
        subprocess.run(cmd, shell=True, check=True)
        await message.reply_video(video=filename, caption="✅ Here is your downloaded video!")
        os.remove(filename)
    except Exception as e:
        await message.reply(f"❌ Failed to download: `{e}`")

app.run()
