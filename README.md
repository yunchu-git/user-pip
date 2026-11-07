# user-pip
> [!IMPORTANT]
> **本库使用MIT许可证，在分发时请保留署名！谢谢！**

> [!WARNING]
> 本库尚在开发阶段，可能有bug，如有bug请及时反馈，谢谢。

python的pip是一个库，**但是官方不建议直接调用**，本库使用`subprocess`标准库执行命令的方式来进行pip的python调用，调用时调用名为`user_pip`

# 要求
1. Python版本大于等于3.8

# 安装方法
```bash
pip install user-pip
```

# 更新日志
|版本|日志|
|---|----|
|v0.0.2|添加了n个功能，修复若干bug|
|v0.0.1|库正式创建|

# 报错码
|报错码|报错码翻译|
|------|--------|
|2*000001|未确认卸载|
|2*000002|尝试卸载pip|

# 使用示例
## 关于install的命令
1. 安装库：
```Python
install("wxpython","pip3","https://mirrors.ctyun.cn/pypi/simple/")
```

参数1：库名 参数2：pip对应的python版本 参数3：镜像源

2. 安装pip：
```Python
pip_install("python3","pip3")
```

参数1：python版本 参数2：pip对应的python版本

3. 安装指定版本：
```Python
install_version("wxpython","4.3.2","pip3","https://mirrors.ctyun.cn/pypi/simple/")
```

参数1：库名 参数2：版本 参数3：pip对应的python版本 参数4：镜像源

4. 安装whl：
```Python
install_whl(r"C:/abc.whl","pip3")
```

参数1：whl文件地址 参数2：pip对应的python版本

## 关于uninstall的命令

1. 卸载库：
```Python
uninstall("wxpython","pip3",True)
```

参数1：库名 参数2：pip对应的python版本 参数3：确认删除

## 关于upgrade的命令

1. 更新库：
```Python
upgrade("wxpython","pip3","https://mirrors.ctyun.cn/pypi/simple/")
```

参数1：库名 参数2：pip对应的python版本 参数3：镜像源

2. 查看可更新库：
```Python
pip_upgrade_list("pip3","https://mirrors.ctyun.cn/pypi/simple/")
```

参数1：pip对应的python版本 参数2：镜像源

3. 更新pip：
```Python
pip_upgrade("python3","pip3")
```

参数1：python版本 参数2：pip对应的python版本

## 关于config的命令
1. 写入设置
```Python
config_set("global", "index-url", "https://pypi.tuna.tsinghua.edu.cn/simple","pip3")
```

参数1：节 参数2：键 参数3：值 参数4：pip对应的python版本

2. 读取设置
```Python
config_get("global", "index-url","pip3")
```

参数1：节 参数2：键 参数3：pip对应的python版本

3. 删除设置
```Python
config_unset("global", "index-url","pip3")
```

参数1：节 参数2：键 参数3：pip对应的python版本

## pip其他的命令
1. 查看库：
```Python
pip_list("pip3")
```

参数1：pip对应的python版本

2. 检查包依赖冲突：
```Python
pip_check("pip3")
```

参数1：pip对应的python版本

3. 显示已安装包的信息：
```Python
show_package("wxpython","pip3")
```

参数1：库名 参数2：pip对应的python版本