import os 
import subprocess
from datetime import datetime
from collections import  namedtuple
from dotenv import dotenv_values


def load_env_variables():
    # Load environment variables from .env file then override the values with those located in the
    # system environment variables.
    config_dict = {
        **dotenv_values('.env'),
        **os.environ # Override loaded values with environment variables
    }

    config = {}
    for k, v in config_dict.items():
        if k.startswith('_'):
            continue

        if str(v).lower() in ['true', 'false']:
            v = bool(v)

        config[k] = v


    # Create an object `settings` that will permit to call the environment variables using dot notation.
    # e.g. >>> settings.ACCESS_KEY
    #      >>> settings.SECRET_KEY
    settings = namedtuple('Settings', config.keys())(*config.values())

    return settings 

settings = load_env_variables()

def extension(file_path):
    if not file_path: 
        return None 
    ext = file_path.split('.')[-1]
    return ext  


def run_batch_processes():
    remote_upload_folder = str(datetime.utcnow().strftime("%m-%d-%Y"))

    files = os.listdir('./output')
    
    for file in files:
        if extension(file) in settings.EXTENSIONS:
            res = subprocess.run([
                "duck", 
                "--username", settings.USERNAME, 
                "--password", settings.PASSWORD,
                "--existing", "overwrite",
                "--upload", f'"{settings.BASE_URL}/amz-feeds/{remote_upload_folder}/"',
                f'output/{file}'
            ])

            print(f"Uploading {file}: Process completed with exit code %s" % res.returncode)
            
    print(f"Upload Process completed with exit code %s" % res.returncode)

if __name__ == "__main__":
    run_batch_processes()
