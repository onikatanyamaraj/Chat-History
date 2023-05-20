import requests
import time
import os
from aip import AipSpeech
from ChatbotConfig import *


# def getUserLoginStatus(code):
#     url = WXLoginURL.format(AppID, AppSecret, code)
#     i = 0
#     while i < 5:
#         i += 1
#         try:
#             response = requests.get(url=url)
#             user_id = response.json()['openid']
#             session_id = response.json()['session_key']
#             return user_id, session_id
#         except requests.exceptions.RequestException as e:
#             print(f"Error: {e} Happened, wait for 3 seconds")
#             time.sleep(3)
#     print("Tried for 5 times, Still failed")
#     return None, None


def getChatbotResult(uuid, question):
    params = {"uuid": uuid, "question": question}
    print("getChatbotResult获取参数", params)
    i = 0
    while i < 5:
        i += 1
        try:
            response = requests.post(url=BotBackendURL, json=params)
            answer = response.json()['data']
            print(answer)
            return answer
        except requests.exceptions.RequestException as e:
            print(f"Error: {e} Happened, wait for 3 seconds")
            time.sleep(3)
    print("Tried for 5 times, Still failed")
    return None


# def saveAudioFile(userID, sessionID, audio_f):
#     f_name = str(int(round(time.time() * 1000))) + '.m4a'
#     f_dir = os.path.join(LocalTempAudioDir, userID, sessionID)
#     if not os.path.exists(f_dir):
#         os.makedirs(f_dir)
#     f_name = os.path.join(f_dir, f_name)
#     audio_f.save(f_name)
#     return f_name
#
#
# def getAudioText(audio_file):
#     bd_client = AipSpeech(appId=BDAppID, apiKey=BDApiKey, secretKey=BDAppSecret)
#     with open(audio_file, 'rb') as f:
#         result = bd_client.asr(speech=f.read(), format='m4a', options={'dev_id': 1537})
#     if result['err_no'] == 0:
#         return result['result'][0]
#     else:
#         return ''

