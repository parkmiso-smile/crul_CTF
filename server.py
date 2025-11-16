from flask import Flask, request

app = Flask(__name__)
# Flask 애플리케이션 객체를 생성한다. __name__은 현재 모듈의 이름이다.

@app.route('/') 
def index():
    ua = request.headers.get("User-Agent")
#현재 요청의 헤더에서 'User-Agent' 값을 추출하여 ua 변수에 저장합니다
   
    if ua == "KingHacker/1.0":
        return "FLAG{CURL_UA_BYPASS_SUCCES}"
    # 추출한 User-Agent 값이 "KingHacker/1.0"과 일치하는지 확인하고 일치하면 flag를 출력한다.
    else:
        return "Access Denied: Your browser is not allowed."
   

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
