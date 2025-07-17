Instructions for training the model:

Setup:

Make a virtual environment: python -m venv
In that virtual environment: pip install ultralytics
While connected to a specific machines, copy dataset from /stash/portal/eurocity to /disk/local/scratch
Copy over code directory there as well, including virtual environment
Make sure the code and dataset directories are both under some parent directory, following the file structure in the README
Running it:

Directory to run from: /disk/local/scratch/project/code (code being this repository)
Start a new tmux session: tmux new
Activate the virtual environment: source .venv/bin/activate
run python3 train.py
Detach tmux session: ctrl+b then press d
Re-attach tmux session: tmux attach
Deactivate virtual environment: deactivate
