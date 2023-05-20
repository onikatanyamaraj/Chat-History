from flask import Flask, request, jsonify
from ChatbotModel import ChatBotModel


app = Flask(__name__)
# persona_sentences = []
@app.route('/ask', methods=['POST','GET'])
def ask():

    data = request.get_json()
    uuid = data['uuid']
    question = data['question']

    reply = ""
    # 输入clear把之前的内容全部清空，
    if question == "重新开始":
        # persona_sentences.clear()
        reply += "历史是一面镜子，它照亮现实，也照亮未来。任何历史有关的问题请来问我！"
        return jsonify(uuid=uuid, code=200, message="请求成功", data=reply)
    # if len(persona_sentences) < 4:
    #     for _ in content.split("."):
    #         persona_sentences.append(content)
    #     reply = "need another {} sentences to set up personalities. ".format(max(4-len(persona_sentences),0))
    #     if len(persona_sentences) >= 4:
    #         reply+= "Please input your sentence. Input 'Clear' to clear personalities."
    else:
        reply = model.predict_answer(question)

    return jsonify(uuid=uuid, code=200, message="请求成功", data=reply)


@app.errorhandler(400)
def handle_bad_request(e):
    uuid = request.args.get('uuid')
    response = {
        'uuid': uuid,
        'code': 400,
        'message': str(e),
        'data': None
    }
    return jsonify(response)

@app.errorhandler(404)
def handle_not_found(e):
    uuid = request.args.get('uuid')
    response = {
        'uuid': uuid,
        'code': 404,
        'message': str(e),
        'data': None
    }
    return jsonify(response)

@app.errorhandler(405)
def handle_not_allowed(e):
    uuid = request.args.get('uuid')
    response = {
        'uuid': uuid,
        'code': 405,
        'message': str(e),
        'data': None
    }
    return jsonify(response)

@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(str(e))
    uuid = request.args.get('uuid')
    response = {
        'uuid': uuid,
        'code': 500,
        'message': str(e),
        'data': None
    }
    return jsonify(response)



if __name__ == '__main__':
    model = ChatBotModel()
    app.run(host='127.0.0.1', port=5001, debug=True)
