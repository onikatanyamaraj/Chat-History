from flask import Flask, request, jsonify, Response
from ChatbotUtils import *


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World</h1>'


@app.route('/SendMessageService', methods=['POST'])
def sendMessageService():
    data = request.get_json()
    # history_input是历史聊天记录的列表[{'role': 'system', 'content': '当你的回复中涉及代码块时，请在markdown语法中标明语言类型。如果不涉及，请忽略这句话。'}, {'role': 'user', 'content': '你好'}]
    uuid = data['uuid']
    # paras_input是{'temperature': 1.0, 'top_p': 1.0, 'presence_penalty': 0.0, 'frequency_penalty': 0.0}的json
    history = data['question']
    print(uuid, history)
    # 调用后台接口生成response
    response = getChatbotResult(uuid, history)
    print("开始"+response+"结束")
    print("hi")
    return jsonify(response)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)

# @app.route('/')
# def index():
#     return '<h1>Hello World</h1>'
#
# @app.route('/img/<imgName>')
# def getImage(imgName):
#     img_path = os.path.join(IMGPath, imgName)
#     mdict = {
#         'jpeg': 'image/jpeg',
#         'jpg': 'image/jpeg',
#         'png': 'image/png',
#         'gif': 'image/gif'
#     }
#     mime = mdict[imgName.split('.')[-1]]
#     with open(img_path, 'rb') as f:
#         image = f.read()
#     return Response(image, mimetype=mime)
#
#
# @app.route('/LoginService', methods=['POST'])
# def loginService():
#     code = request.json.get('code')
#     user_id, session_id = getUserLoginStatus(code=code)
#     if user_id is None:
#         user_id=''
#         session_id=''
#     return jsonify(userID=user_id, sessionID=session_id)
#
#
# @app.route('/SendMessageService', methods=['POST'])
# def sendMessageService():
#     sessionID = request.json.get('sessionID')
#     content = request.json.get('content')
#     answer = getChatbotResult(sessionID=sessionID, content=content)
#     if answer is None:
#         answer = ErrorAnswer
#     return jsonify(text=answer)
#
#
# @app.route('/SendAudioService', methods=['POST'])
# def sendAudioService():
#     user_id = request.values.get('userID')
#     session_id = request.values.get('sessionID')
#     audio_f = request.files['file']
#     audio_file = saveAudioFile(userID=user_id, sessionID=session_id, audio_f=audio_f)
#     content = getAudioText(audio_file)
#     answer = getChatbotResult(sessionID=session_id, content=content)
#     if answer is None:
#         answer = ErrorAnswer
#     return jsonify(audio=content, text=answer)

# if __name__ == "__main__":
#     app.run(host='127.0.0.1', port=5000, debug=True)