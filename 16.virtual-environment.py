# Create Virtual Environment
# miniconda, virtualenv, pyenv, venv

""" venv """
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

""" Miniconda """
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