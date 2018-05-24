from requests import post, session
from constants import *
import json
from salt_sign_generator import salt_sign_generator


class Translator:

    def __init__(self, input_text=None, result=[]):
        self.result = result
        self.input_text = input_text
        self.translate()

    def translate(self):
        post_form['q'] = self.input_text.strip()
        resp = post(URL, data=post_form,headers=HEADERS)
        contents = json.loads(resp.text)
        if contents['errorCode'] != '0':
            return
        translation = contents.get('translation', None)[-1]
        self.result.append(translation + '\n')
        self.result.append('\n' + '*' * 10 + '\n')
        # speak_url = contents.get('tSpeakUrl', None)
        # print(speak_url)
        if not contents.get('web', None) or not contents.get('basic', None):
            return

        basic = contents['basic']
        # uk_speech_url = basic.get('uk-speech', None)
        # us_speech_url = basic.get('us-speech', None)
        explains = basic.get('explains', None)
        #p rint(uk_speech_url)
        # print(us_speech_url)
        for item in explains:
            self.result.append(item + '\n')
        self.result.append('\n' + '*' * 10 + '\n')
        for item in contents['web']:
            self.result.append(item['key'] + ','.join(item['value']) + '\n')


class TranslatorNew:

    def __init__(self, input_text=None, result=[]):
        self.result = result
        self.input_text = input_text
        self._translate()

    def _translate(self):
        self._get_contents()
        self._contents_parse()


    def _get_contents(self):
        post_form1['i'] = self.input_text
        # salt, sign = salt_sign_generator(self.input_text)
        salt, sign = salt_sign_generator( post_form1['i'])
        post_form1['salt'] = salt
        post_form1['sign'] = sign

        with session() as s:
            resp = s.post(URL1, data=post_form1, headers=Headers_1)
            self.contents = json.loads(resp.text)

    def _contents_parse(self):
        if self.contents.get('errorCode', None) != 0 or not self.contents:
            return

        translate_result = ''
        for item in self.contents['translateResult']:
            for in_item in item:
                translate_result += in_item['tgt'] # + '\n'
            translate_result += '\n'
        translate_result += '\n' + '*' * 10 + '\n'
        smart_result = self.contents.get('smartResult',None)
        if not smart_result:
            self.result.append(translate_result)
            return
        for item in smart_result['entries']:
            translate_result += item
        self.result.append(translate_result)