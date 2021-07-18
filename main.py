import getpass
import os
import sys

"""
Project Name: better_pip
Author: ARtcgb
Email:artcgb@ebay.onmicrosoft.com
Date: 2021/7/16
"""

try:
    def configuration_pip3_conf():
        """
        检测 + 配置pip源
        """
        system = sys.platform
        unix_list = ["darwin", "linux2", "Linux"]
        if system in unix_list:
            print(os.popen("mkdir ~/.pip"))
            with open("./pip.conf", "w+", encoding="utf-8") as pipfile:
                pipfile.write("""[global]
            index-url = https://pypi.tuna.tsinghua.edu.cn/simple
            [install]
            trusted-host = https://pypi.tuna.tsinghua.edu.cn""")
            print(os.popen("mv pip.conf ~/.pip/pip.conf"))
        else:
            print(os.popen("mkdir C:\\Users\\" + getpass.getuser() + "\\pip"))
            with open("C:\\Users\\" + getpass.getuser() + "\\pip\\pip.ini", "w+", encoding="utf-8") as pipfile:
                pipfile.write("""[global]
    index-url = https://pypi.tuna.tsinghua.edu.cn/simple
    [install]
    trusted-host = https://pypi.tuna.tsinghua.edu.cn""")
            print(os.popen("mv pip.ini C:\\Users\\" + getpass.getuser() + "\\pip"))
        print("配置完毕")


    def update_pip3():
        """
        更新pip3，python不存在版本冲突的话可以直接使用，否则将 python3 改为要更新版本的路径
        """
        print(os.popen("python3 -m install --upgrade pip").read())
        print("pip更新完成")


    def update_pip3_package():
        """
        检测并更新过期资源包
        """
        outdated_package_list = []
        for line in os.popen("pip3 list --outdated"):
            package = line.split()
            outdated_package_list.append(package[0])
        # 删除列表前两项(Python 中的无用表头及分割线)
        del outdated_package_list[0: 2]

        for outdated_package in outdated_package_list:
            print("updating:", outdated_package)
            print(os.popen("pip3 install " + outdated_package + " -U").read())
        print("更新完毕")


    def unset_pip3_conf():
        """
        重设pip3 配置文件
        """
        system = sys.platform
        unix_list = ["darwin", "linux2", "Linux"]
        if system in unix_list:
            print(os.popen("sudo rm ~/.pip/pip.conf"))
            print("重设完成")
        else:
            print(os.popen("del C:\\Users\\" + getpass.getuser() + "\\pip\\pip.ini"))
            print("重设完成")


    def main():
        print("欢迎！", getpass.getuser())
        print("Welcome! ", getpass.getuser())
        if os.popen("pip3 config list") == "":
            choice = input("检测到没有配置pip源，是否配置pip国内源？(y/n)")
            if choice == "y":
                configuration_pip3_conf()
                print('pip3源已设置完毕')
        while True:
            print("操作目录：1、重新配置pip3源 2、更新pip3 3、更新所有有新版本的第三方库 4、撤销pip3源(pip3 install 连续出现错误时选此项) exit 退出程序")
            choice = input("请输入要进行的操作：")
            if choice == "1":
                configuration_pip3_conf()
            elif choice == "2":
                update_pip3()
            elif choice == "3":
                update_pip3_package()
            elif choice == "4":
                unset_pip3_conf()
            elif choice == "exit":
                print("\nByebye")
                break

    if __name__ == '__main__':
        try:
            if sys.argv[1] == "-update" or sys.argv[1] == "-u":
                update_pip3_package()
            elif sys.argv[1] == "-update_pip3" or sys.argv[1] == "-U":
                update_pip3()
            elif sys.argv[1] == "-unset" or sys.argv[1] == "-un":
                unset_pip3_conf()
            elif sys.argv[1] == "-help":
                print('''-help 在终端中快速查看参数菜单
-update or -u 更新所有有新版本的库
-update_pip3 or -U 更新pip3
-unset or -un 重新设置pip3配置文件，未自行配置的只会影响pip3源，重设后为官方源''')
            else:
                main()
        except IndexError:
            main()
except KeyboardInterrupt:
    print("\nByebye")
