# 虚拟环境的使用 conda
## 列出所有已有的虚拟环境——ananconda
1. `conda env list`
2. `conda info -e `
   上述两种方式都可以，但是要是在终端里操作才行

## 创建一个虚拟环境
 `conda create -n env_name python=版本号(可以不写)`(虚拟环境的名字)

## 删除一个虚拟环境
 `conda env remove -n env_name`

## 激活并进入虚拟环境
`conda activate env_name`

## 退出虚拟环境
`conda deactivate`

## 安装 package
 `conda install package_name -n env_name`

## 查看安装的package
 进入虚拟环境后在终端输入
 `pip list`

## 删除package
 `conda remove package_name`

# 虚拟环境的使用 pipenv

## 进入工作目录
cd ~/workspace/demo   

## 初始化工作环境，创建 Pipfile
pipenv install     

## 安装所需要的包，如 numpy
pipenv install numpy    

## 在工作环境中运行代码
pipenv run python xxx.py

## 或者直接激活工作环境
pipenv shell

## 运行代码
python xxx.py            

## 退出环境
 exit

## 重现对方的运行环境
获取对方的虚拟环境带有pipfile 和 pipfile.lock的文件夹之后在终端输入pipenv install即可配置对方运行代码时环境以及package 的版本


