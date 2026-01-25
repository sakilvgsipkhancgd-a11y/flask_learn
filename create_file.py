from pathlib import Path
import subprocess
import os

class create_file:



    def sub_project(project_name,*sub_name):
        project_path = Path(f"{project_name}/")
        project_path.mkdir(parents=True, exist_ok=True)

        for name in sub_name:
            f = Path(f"{project_name}/{name}")
            print(name)
            f.mkdir(parents=True, exist_ok=True)


    def file_create(path_name,*file_name):
        floder_path = Path(path_name)#将字符串转换为Path对象以便进行路径操作
        absolute_path = floder_path.resolve()#获取绝对路径
        os.chdir(absolute_path)#切换到指定路径
        print(f"已进入文件夹{floder_path}")
        for name in file_name:
            print(name)
            with open(f"{name}",'x') as f:
                f.write("")#创建空文件





sub_project(input("请输入想要创建的项目名称"),*input("请输入想要创建的子文件夹名称，多个子文件夹用逗号隔开，如果没有直接回车").split(","))
file_create(input("请输入想要创建的文件夹路径"),*input("请输入想要创建的文件名称，多个文件用逗号隔开，没有直接回车即可").split(","))


