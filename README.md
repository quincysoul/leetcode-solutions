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
1. `pyenv` is installed on latest, and with `pip` and `pipenv` modules (different if not Ubuntu):
```sh
sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

curl https://pyenv.run | bash
```
2. Read the output of the `pyenv` install script, it will ask you to add to `~/.bashrc` and/or `~/.zshrc` the following (different if not on Ubuntu):
```
export PATH="/home/quincy/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
2. ~/.profile or ~/.zshrc contains `pipenv` on `PATH` (different if not Ubuntu):
```sh
#Contents of ~/.profile
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi
```
3. Enter python dir, use `pipenv` with specified versions (say yes to installign python ver), and run tests with `green`
```sh
cd ./python_leetcode
pipenv --rm
pyenv install
pipenv shell
pipenv install
green
```

## Recommended VS Code Extensions
* Python Test Explorer
* Black formatter

## Recommended zsh Extensions
* [zsh-autoswitch-virtualenv](https://github.com/MichaelAquilina/zsh-autoswitch-virtualenv)

### `zsh-autoswitch-virtualenv` Required config for WSL
1. Open wsl.conf within Ubuntu WSL
```sh
sudo vim /etc/wsl.conf
```
2. `i` for insert, then paste:
```conf
[automount]
enabled = true
options = "metadata"
mountFsTab = false
```
3. Restart
4. If prompted, you can now `chmod 600 ./Pipenv`.