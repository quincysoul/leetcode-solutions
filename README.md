# leetcode-javascript
Below are my solutions to leetcode. I will generally aim to solve them in JavaScript, though may explore Python as well. The filename will associate it.

# Running js test suite
```sh
npm i
npm test
```
### Recommended VS Code Extensions
* ESLint

# Python3

## WSL with Ubuntu - Install `pyenv` and required items
<!-- 1. `python3.7` is already installed on latest, and with `pip` and `pipenv` modules.
```sh
sudo apt update
sudo apt install python3.7 python3-pip -y
python3.7 -m pip install --user pip
python3.7 -m pip install --user pipenv
``` -->
1. `pyenv is installed on latest, and with `pip` and `pipenv` modules.
```sh
sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

curl https://pyenv.run | bash
```
2. Read the output of the script, it will ask you to add to `~/.bashrc` and/or `~/.zshrc`:
```
export PATH="/home/quincy/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
2. ~/.profile or ~/.zshrc contains `pipenv` on `PATH`.
```sh
#Contents of ~/.profile
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi
```
3. Enter python dir and run tests with `green`
```sh
cd ./python_leetcode
pipenv shell
pipenv install
green
```

### Recommended VS Code Extensions
* Python Test Explorer
* Black formatter

##