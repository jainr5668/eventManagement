import json
import os, shutil

# shutil.rmtree('dist\\@lnc')
# shutil.rmtree('dist\\@patterns')
from translate import Translator

language_dict = {
    "en": "english",
    "de": "german",
    "es": "spanish",
    "zh": "chinese",
    "fr": "french",
    "ja": "japanese",
}
english_phrases = json.load(open("src\\assets\\i18n\\en.json"))
for key in language_dict.keys():
    translator = Translator(from_lang="english", to_lang=language_dict[key])
    translation = {}
    for phrase in english_phrases.keys():
        translation[phrase] = translator.translate(english_phrases[phrase])
    open("src\\assets\\i18n\\{}.json".format(key), "w").write(json.dumps(translation))


for command in [
    "dir src\\services\\*.ts /b /s > ts-files.txt",
    "npx tsc @ts-files.txt --declaration --removeComments --outDir dist\@lnc",
    "del ts-files.txt",
    "npx ng serve --host 0.0.0.0 --disable-host-check",
]:
    os.system(command)
    # 'dir src\\app\\patterns\\*.ts /b /s > ts-files.txt',
    #             'npx tsc @ts-files.txt --declaration --removeComments --outDir dist\@patterns',
