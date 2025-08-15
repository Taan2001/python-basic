""" 
    venv 
"""
# 1. Create with venv
# run cmd: 
# + py -m venv name_of_env
# + python -m venv name_of_env
# example: py -m venv my_env

# 2. Active 
# run cmd: ./name_of_env/Scripts/activate  
# example: ./my_env/Scripts/activate

# 3. Exit virtual environment
# run cmd: deactivate

import numpy as np

my_arr = np.array([[1, 2], [3, 4]])

my_new_arr = my_arr.reshape(1, -1)

print(f"my_new_arr: {my_new_arr}")

""" pip """
# 1. install lib with pip
# run cmd: pip install lib_name==version

# 2. upgrade lib version which installed
# run cmd: pip install --upgrade lib_name

# 3. display all libs which installed
# run cmd: pip list

# 4. display a libs which installed
# run cmd: pip list | grep lib_name # run only in linux

# 5. Save packages out file
# run cmd: pip freeze > requirements.txt

# 6. install libs from file requirements.txt
# run cmd: pip install -r requirements.txt


""" 
    miniconda 
"""
# 1. Create with venv
# run cmd: 
# + conda create --name name_of_env python=the_version
# example: conda create --name my_conda_env python=3.12.1

# 2. Active 
# run cmd: conda acitivate name_of_env 
# example: conda acitivate my_conda_env 

# 3. Exit virtual environment
# run cmd: conda deactivate

# 4. Remove virtual environment
# run cmd: conda env remove --name name_of_env
# example: conda env remove --name my_conda_env

# 5. Check env by conda
# run cmd: conda env list

""" install with condal """
# 1. install libs
# run cmd: conda install lib_name