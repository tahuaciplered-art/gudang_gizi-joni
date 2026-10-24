import os, requests
from flask import Flask, request
BOT_TOKEN=os.environ.get("BOT_TOKEN","")
CHANNEL_ID=os.environ.get("CHANNEL_ID","")
app=Flask(__name__)
@app.route("/")
def home():
 return f"<h1>Gudang Gizi Joni OK!</h1><form action=/upload method=post enctype=multipart/form-data><input type=file name=file><button>Upload Film</button></form><p>Channel: {CHANNEL_ID}</p>"
@app.route("/upload",methods=["POST"])
def up():
 f=request.files.get("file")
 r=requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument",data={"chat_id":CHANNEL_ID},files={"document":(f.filename,f.stream,f.mimetype)}).json()
 if not r.get("ok"): return str(r)
 fid=r["result"]["document"]["file_id"]
 gf=requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getFile?file_id={fid}").json()
 link=f"https://api.telegram.org/file/bot{BOT_TOKEN}/{gf['result']['file_path']}"
 return f"Berhasil Upload!<br><a href='{link}'>{link}</a><br><br><a href='/'>Balik Upload Lagi</a>"
