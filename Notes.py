# First ssh into the VPN

## ssh samguv_guest@platoon.its.pdx.edu

# Then change directories to this

## cd /stash/portal/eurocity

# Doing this ls /stash/portal/eurocity, will show you the folder names inside

# Just pressing cd will bring you back to your home diretory

# I have 100 gb of storage on my PSU vpn server

#  Will tell me how much space is being used in each folder in my directory

## du -sh *

# Doing this will allow you to delete something in a specific folder

## cd ~/eurocity_data
## rm -r ECP_day_img_train

# Doing this will allow you to unzip a file into a spot in my directory that's what the -d means

## unzip /stash/portal/eurocity/ECP_day_img_train.zip -d /u/samguv_guest/datasets/
## unzip /stash/portal/eurocity/ECP_day_img_val.zip -d /u/samguv_guest/datasets/
## unzip /stash/portal/eurocity/ECP_day_labels_train.zip -d /u/samguv_guest/datasets/
## unzip /stash/portal/eurocity/ECP_day_labels_val.zip -d /u/samguv_guest/datasets/

# Use this to create a new folder

## mkdir

# To copy pycharm files to the directory

## scp /path/to/your/file.py samguv_guest@platoon.its.pdx.edu:/u/samguv_guest/my_project/
## scp "C:/Users/samgu/PycharmProjects/PSU Project 2025/countObject.py" samguv_guest@platoon.its.pdx.edu:/u/samguv_guest/2025-PSU-REU-Sam/

# To check for python and python version

## python3 --version

# Creates a virtual environment inside my code directory

## cd ~/2025-PSU-REU-Sam
## python3 -m venv .venv

# Will check to see if you're VE is there, -a shows hidden files

## ls -a

# Activates the virtual environment and allows you to work in it,
# Your shell prompt will change (usually you’ll see (.venv) before your prompt).
# Now any python or pip commands will run inside this isolated environment.

## source .venv/bin/activate
## Note saying deactivate leaves the VE

# You can use this pip command only when on internet to download packages

## pip install

# Shows all the packages you have
# (| putting this after and then some package name checks for a specifc package)

## pip list

# Tmux allows you to run your code when you are disconnected from the server,
# here are some Tmux commands
# Action -> Command -> What It Does

## Start a new session -> tmux new -s session_name -> Opens a new persistent shell
## Detach from session -> Ctrl + b, then d -> Leaves the session running in background
## List active sessions -> tmux ls -> Shows running sessions
## Reattach to session -> tmux attach -t session_name -> Go back into a running session
## Exit a session -> exit (inside tmux) -> Ends session when done
## tmux kill-server, ends all sessions
## tmux kill-session -t <session-name>, ends a specific session

# To upload my github to my directory

## git clone https://github.com/SamGuven/2025-PSU-REU-Sam.git .

# Then to run python files use

## python3 train.py

# To pull new changes from the github

## git pull

# Once in the server to login to a specific gpu use this command

## ssh samguv_guest@fab04
## Password: bsIK7ImB35vhb

### Order should be get on SERVER then TMUX then VE, and I can install packages on the VE

# Installs pip

## python -m ensurepip --upgrade

# To enter scroll mode, and press q to cancel

## Ctrl + b (then) [

# To delete all files that aren't of a specfic type, in a specific file

## find . -type f ! -name "*.txt" -delete

# To delete all empty subfolders

## find . -type d -empty -delete

# To clear the cache files

## find /u/samguv_guest/datasets/ECP/ -name "*.cache" -delete
