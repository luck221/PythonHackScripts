from absinstallpackage import ABCInstallPackage
from utils import Utils

import os

class InstallPackage(ABCInstallPackage):
    """
    +---------------------------+
    | Все команды на данный момент |
    +---------------------------+

    1 install_packet(packet) , где packet название пакета кали , который вы хотите поставить
    2 install_msf(<filename>) , по-умолчанию идёт файл с полной установкой под Ubuntu
    """


    def __init__(self, file_cfg:str):
        """
        тут лютая хуйня , просто инициализация 
        всего необходимого говна для работы))))
        """
        self.utils = Utils()
        self.utils.execute_command(file_cfg)

    def install_packet(self, packet:str) -> None:
        """
        тут название пакета пиши без пробелов и он скачается !
        """
        os.system(f"sudo aptitude install -t kali-rolling {packet} -y")
    
    def install_msf(self, filename="msf.txt") -> None:
        """
        полная установка метасплоит на убунту + установка curl , воть )))))
        """
        self.utils.execute_command(filename)

    def test_install_any_tool(self, filename):
        pass
