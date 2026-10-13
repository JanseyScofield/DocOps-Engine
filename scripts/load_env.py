import os

def load_env_file(env_path):
    if not env_path or not os.path.exists(env_path):
        return

    with open(env_path, 'r', encoding='utf-8') as f:
        for line in f:
            clean_line = line.strip()
            if clean_line and not clean_line.startswith('#') and '=' in clean_line:
                key, val = clean_line.split('=', 1)
                key = key.strip()
                val = val.strip().strip('"').strip("'")
                if key:
                    os.environ[key] = val
