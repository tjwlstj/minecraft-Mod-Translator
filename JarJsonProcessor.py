import zipfile
from pathlib import Path
import shutil
import commentjson

from Translator import doTranslateGPT

def jarJsonManager(_jarPath:str):
    temp_dir = Path('./temp')
    
    if not temp_dir.exists():
        temp_dir.mkdir()
    
    mod_path = Path(_jarPath)
    mod_list = mod_path.glob('*.jar')
    
    
    for mod_file in mod_list:
        try:
            with zipfile.ZipFile(mod_file, 'r') as jar:
                jar.extractall(temp_dir / mod_file.name.replace('.jar',''))
                
            target_json_path = next(temp_dir.rglob('en_us.json'), None)
            if not target_json_path:
                print(f"Not found '{target_json_path}' in JAR.")
                return -1
            
            translated_data = None
            
            with target_json_path.open('r', encoding='utf-8') as json_file:
                data = commentjson.load(json_file)
                data = commentjson.dumps(data, ensure_ascii=False, indent=4)
                translated_data = doTranslateGPT(data)
                
            # 이제 JAR 파일 내부에 ko_kr.json 집어넣고 재압축하면 끝
            ko_kr_path = target_json_path.parent / 'ko_kr.json'
            
            with ko_kr_path.open('w', encoding='utf-8') as json_file:
                commentjson.dump(translated_data, json_file, ensure_ascii=False, indent=4)
            
            
            new_jar_file = Path(f"./translated/{Path(mod_file).stem}_modified.jar")
            shutil.make_archive(new_jar_file.with_suffix(''), 'zip', temp_dir)
            final_jar_file = new_jar_file.with_suffix('.jar')
            shutil.move(f"./translated/{new_jar_file.stem}.zip", final_jar_file)
            
            print(f"{mod_file.name}  translated complelte!")
            
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)
    
if __name__ == '__main__':
    jarJsonManager('./mod')
