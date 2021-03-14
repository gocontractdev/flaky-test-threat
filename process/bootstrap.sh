# This script will only work if you run it from the main not within the process folder
# Please do not try to do this manually since it brakes the order of operations
# reactivate the env (if forgotten)
deactivate
# create environment:
if [ -d "venv/ez_env/" ]; then
  echo 'env exists'
else
  python -m venv venv/ez_env
fi
source venv/ez_env/bin/activate

pip install --upgrade pip
pip --version
echo 'Installing requirements'
pip install -r requirements.txt
pip install "textdistance[extras]" # for speed performance
echo 'DONE'

# clone and place assignment 2 files here
if [ -d "data/temp/assignment2/" ]; then
    echo "Already exists -- skipped the cloning..."
else
  echo "Cloning the Assignment 2 repository; Please Wait..."
  cd  data/temp
  mkdir "assignment2/"
  sudo chown -R "assignment2/"
  sudo chmod -R g+rw "assignment2/"
  cd "assignment2/"
  git clone https://github.com/gocontractdev/flaky-tests-reproduction.git .
  # back to the process to run the main python file
  cd ../../../
fi

python process/generator.py