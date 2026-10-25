# user-pip
> [!IMPORTANT]
> **本库使用MIT许可证，在分发时请保留署名！谢谢！**

> [!WARNING]
> 本库尚在开发阶段，可能有bug，如有bug请及时反馈，谢谢。

> [!TIP]
> 本库使用报错码形式报错均使用报错码形式（如2*000001等），可用[仓库yunchu-dev-specs](https://github.com/yunchu-git/yunchu-dev-specs)查看报错码

python的pip是一个库，**但是官方不建议直接调用**，本库使用`subprocess`标准库执行命令的方式来进行pip的python调用，调用时调用名为`pip_user`

# 使用示例
1. 安装库：
```Python
install("wxpython","pip3","https://mirrors.ctyun.cn/pypi/simple/")
```

参数1：要安装的库 参数2：pip对应的python版本 参数3：镜像源

2. 卸载库：
```Python
uninstall("wxpython","pip3",True)
```

参数1：要卸载的库 参数2：pip对应的python版本 参数3：确认删除

3. 更新库：
```Python
upgrade("wxpython","pip3","https://mirrors.ctyun.cn/pypi/simple/")
```

参数1：要更新的库 参数2：pip对应的python版本 参数3：镜像源

4. 查看库：
```Python
pip_list("pip3")
```

参数1：pip对应的python版本

5. 查看可更新库：
```Python
pip_upgrade_list("pip3","https://mirrors.ctyun.cn/pypi/simple/")
```

参数1：pip对应的python版本 参数2：镜像源

6. 安装pip：
```Python
pip_install("python3","pip3")
```

参数1：python版本 参数2：pip对应的python版本

7. 更新pip：
```Python
pip_upgrade("python3","pip3")
```

参数1：python版本 参数2：pip对应的python版本
