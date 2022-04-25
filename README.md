## 安装虚拟环境
### windows
```shell
virtualenv --version
pip3 install virtualenv
pip3 install virtualenvwrapper-win
```

### linux（由于windows本地装了git bash，命令行使用git的，这里安装linux版的）
```shell
virtualenv --version
pip3 install virtualenv
pip3 install virtualenvwrapper
export WORKON_HOME=/e/colorful-appstore/python/install/python/virtual-env
export VIRTUALENVWRAPPER_PYTHON=/e/colorful-appstore/python/install/python.exe
# 打开终端自动启用
source /etc/profile
source /e/colorful-appstore/python/install/Scripts/virtualenvwrapper.sh
```

## 虚拟环境使用
1. 激活virtualenvwrapper命令
```shell
source /e/colorful-appstore/python/install/Scripts/virtualenvwrapper.sh
```

2. 创建一个新的环境
```
mkvirtualenv basic --python=python3
```

3. 切换到新环境
```
workon basic
```

4. 退出环境
```
deactivate
```

5. 删除环境
```
rmvirtualenv basic
```

6. virtualenvwrapper设置环境变量 
   1. 打开test的postactivate钩子文件vim ~/Envs/test/bin/postactivate
    ```shell
    #!/bin/zsh
    # This hook is sourced after this virtualenv is activated.
    # 在当前会话加入环境变量
    export ENV=dev
    ```
   2. 这时当执行workon test 激活虚拟环境后便会执行postactivate将项目环境变量Env设置为dev
   3. 在postactivate 中还可以执行诸如pip install -r requirements.txt，pip install -e conf等shell 操作 
   

# 使用
```shell
 virtualenv venv 
 virtualenv -p /usr/bin/python2.7 venv
```
# 启动mongodb
```shell
mongod --dbpath "E:\mongoDB\data\db"
```