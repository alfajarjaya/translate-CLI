import requests
import importlib.util
import sys

def github(username, repository, branch, file_path, module_name):
    url = f"https://raw.githubusercontent.com/{username}/{repository}/{branch}/db/indonesia.py"
    response = requests.get(url)
    
    if response.status_code == 200:
        code = response.text
        spec = importlib.util.spec_from_loader(module_name, loader=None, origin=url)
        mod = importlib.util.module_from_spec(spec)
        exec(code, mod.__dict__)
        
        sys.modules[module_name] = mod
        return mod
    
    else:
        print("Gagal")
        return None

username = "alfajarjaya"
repository = "translate-CLI"
branch = "main"
file_path = "translate-CLI/db/indonesia"
module_name = "indonesiaToEnglish"

source_code = github(username, repository, branch, file_path, module_name)

if source_code is not None:
    info = source_code.indonesiaToEnglish()
else:
    print(f"Gagal {file_path} di repo {repository}")
