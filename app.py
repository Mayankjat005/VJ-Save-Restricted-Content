import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<center> 
    <img src="https://telegra.ph/file/ea73be0ffe797b0c6d935.jpg" style="border-radius: 12px;"/> 
</center> 
<style>
    body { 
        background: antiquewhite;
    }
</style>"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
