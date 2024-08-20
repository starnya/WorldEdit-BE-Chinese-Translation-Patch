import os
import polib

def convert_file(in_path):
    lang_file = open(in_path, 'r', encoding='utf-8')
    content = lang_file.readlines()
    lang_file.close()
    
    po = polib.POFile()
    po.metadata = {
        'Project-Id-Version': 'worldedit-for-bedrock',
        'Report-Msgid-Bugs-To': '',
        'POT-Creation-Date': '',
        'PO-Revision-Date': '2024-08-16 22:45',
        'Last-Translator': '',
        'Language-Team': 'Chinese Simplified',
        'MIME-Version': '1.0',
        'Content-Type': 'text/plain; charset=UTF-8',
        'Content-Transfer-Encoding': '8bit',
        'Plural-Forms': 'nplurals=1; plural=0;',
        'X-Crowdin-Project': 'worldedit-for-bedrock',
        'X-Crowdin-Project-ID': '492515',
        'X-Crowdin-Language': 'zh-CN',
        'X-Crowdin-SourceKey': 'msgstr',
        'X-Crowdin-File': '/[SIsilicon.WorldEdit-BE] master/texts/en_US.po',
        'X-Crowdin-File-ID': '9',
        'Language': 'zh_CN',
    }
    
    for line in content:
        if line.strip():
            key, value = line.strip().split('=', 1)
            value = value.rstrip('\t#')
            entry = polib.POEntry(msgid=key, msgstr=value)
            po.append(entry)
    
    po.save(in_path.replace('.lang', '.po'))
    print(f"{in_path} converted to {in_path.replace('.lang', '.po')}")

for file in os.listdir('.'):
    if file.endswith('.lang'):
        convert_file(file)