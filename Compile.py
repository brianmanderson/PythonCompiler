import os
import shutil
import compileall

command_text = "python -m compileall ."
path_base = r'C:\Users\Markb\Modular_Projects\Make_Raystation_Data_Structure\package_files'
if os.path.exists(path_base):
    shutil.rmtree(path_base)
os.makedirs(path_base)
shutil.copy(os.path.join(path_base, '..', 'BuildDataBase.py'), os.path.join(path_base, 'BuildDataBase.py'))

out_info = os.path.join(path_base, 'InfoStructure')
local_info = os.path.join(path_base, '..', 'InfoStructure')
out_abstract_info = os.path.join(out_info, 'AbstractInfoStructure')
local_abstract_info = os.path.join(local_info, 'AbstractInfoStructure')
local_saver = os.path.join(path_base, '..', 'RaystationDatabaseSaver')
out_saver = os.path.join(path_base, 'RaystationDatabaseSaver')
for i in [out_abstract_info, out_info, out_saver]:
    if not os.path.exists(i):
        os.makedirs(i)

for local_folder, out_folder in zip([local_info, local_abstract_info, local_saver],
                                    [out_info, out_abstract_info, out_saver]):
    for file in os.listdir(local_folder):
        if file.endswith('.py'):
            shutil.copy(os.path.join(local_folder, file), os.path.join(out_folder, file))


success = compileall.compile_dir(path_base, force=True)
if not success:
    print("Compilation failed.")
else:
    print("Compilation completed. Now moving .pyc files...")
    for root, dirs, files in os.walk(path_base):
        for f in files:
            if f.endswith('.py'):
                os.remove(os.path.join(root, f))
        if root.endswith('__pycache__'):
            pycache_path = root
            parent_path = os.path.abspath(os.path.join(root, '..'))  # the directory just above __pycache__

            for filename in os.listdir(pycache_path):
                if filename.endswith('.pyc'):
                    src = os.path.join(pycache_path, filename)

                    # Optionally strip version tags like `.cpython-311.pyc`
                    base_name = filename.split('.')[0] + '.pyc'
                    dst = os.path.join(parent_path, base_name)
                    # if os.path.exists(dst):
                    #     os.remove(dst)
                    print(f"Moving {src} → {dst}")
                    os.rename(src, dst)

            # Optionally remove __pycache__ folder
            shutil.rmtree(pycache_path)
shutil.copy(os.path.join('.', 'run_builder.py'), os.path.join(path_base, 'main.py'))