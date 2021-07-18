# Better_pip3

pip3功能集合脚本，适用于 Linux/macOS 以及 Windows（尚未测试）

# 使用方法

1、 `clone`至本地并 `cd`进入仓库

2、 终端执行 `python3 main.py`直接进入主程序，或通过`python3 main.py [参数]`形式快捷进行操作。 进入主程序后会自动检测 pip3 是否换源，为官方源的可自动切换至清华源。

## 参数菜单

形式：python3 main.py [参数]

```
-help 在终端中快速查看参数菜单
-update or -u 更新所有有新版本的库
-update_pip3 or -U 更新pip3
-unset or -un 重新设置pip3配置文件，未自行配置的只会影响pip3源，重设后为官方源
```

# 功能

设置 pip3 源

自动更新 pip3 过期的第三方库

更新pip3

重设 pip3 源
