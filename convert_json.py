# Converts freeCodeCamp JSON files into their original files
import json
import os

for dir, dirs, files in os.walk(os.getcwd()):
    dirs[:] = [d for d in dirs if not d.startswith('.')]

    for file in files:
        fcc_name, fcc_ext = os.path.splitext(file)

        if(fcc_ext == '.json'):
            with open(os.path.join(dir, file)) as f:
                fcc_data = json.load(f)

            # Make a new file with name of JSON file
            if len(fcc_data) == 1:
                key = [*fcc_data][0]
                o_ext = os.path.splitext(key)[1]

                with open(os.path.join(dir, f'{fcc_name}{o_ext}'), 'w') as f:
                    f.write(fcc_data[key])

            # Make files in directory named the same as JSON file
            elif len(fcc_data) > 1:
                o_dir = os.path.join(dir, fcc_name)

                if not os.path.exists(o_dir):
                    os.makedirs(o_dir)

                for key in fcc_data:
                    with open(os.path.join(dir, fcc_name, key), 'w') as f:
                        f.write(fcc_data[key])
