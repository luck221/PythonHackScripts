import os

class Utils:
    def __init__(self):
        pass
    
    @classmethod
    def output_command(self, i:int, command:str) -> None:
        """
        это красивый вывод команд , которые мы запускаем
        """

        print("+-"+len(command)*"-"+"---+")
        print(f"|{i}:: {command}")
        print("+-"+len(command)*"-"+"---+")

    def execute_command(self, filename:str) -> None:
        """
        должен быть "filename.txt" , пример файла:
        +-------------------------------------+
        |            filename.txt             |
        +-------------------------------------+
        |01 ls -al                            |
        |02 sudo apt update                   |
        |03 sudo apt upgrade                  |
        |...и так далее                         |
        +-------------------------------------+
        """
        #open fucking file , babe )
        with open(f"{filename}", mode="r", encoding="utf-8") as f:
                #create array with all command , which was in file
                array_command = f.read().split("\n")
                #execute and output all command from file
                for i, command in enumerate(array_command):
                    self.output_command(i, command)
                    os.system(command)