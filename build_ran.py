import os
import psutil

class VM(object):

    def __init__(self, rdzenie: int, memory: int, type: bool, patch_iso: str, mode: int, file: str, bild_file: bool, size_file: int, edd: bool):
        self.file = file
        self.memory = memory
        self.cpu = rdzenie
        self.type = type
        self.iso = patch_iso
        self.edd = edd
        """
        rdzenie to ilość rdzeni przeznaczona na maszyne
        type to definiowanie czy maszyna jest już stworzona czy dopiero zaczynamy instalację
        memory to ilość RAM-u 
        patch_iso to ścieżka lokalna do pliku ISO
        mode = 0 dla zwykłego działania, 1 dla testów
        """
        
        self.get_memory()
        self.get_cpu()

        if mode == 1:
            self.test()
        else:
            if not bild_file:
                try:
                    os.system(f"qemu-img create -f qcow2 {file} {size_file}G")
                except SyntaxError:
                    print("Błąd składni lub za mało miejsca na dysku")
                    exit(1)
            self.run()
        
    def get_memory(self):
        available_memory = psutil.virtual_memory().total / 1024 ** 2
        if self.memory > available_memory - 500:
            self.memory = available_memory - 750
        elif self.memory < 512:
            self.memory = 512
    
    def get_memory_flag(self) -> str:
        return f"-m {int(self.memory)}"

    def get_cpu(self): 
        if self.cpu > os.cpu_count():
            self.cpu = os.cpu_count() - 1
        elif self.cpu < 1:
            self.cpu = 1

    def get_iso(self):
        if os.path.exists(self.iso):
            return f"-cdrom {self.iso}"
        else:
            print("Nie ma pliku ISO w podanej ścieżce")
            exit(1)

    def get_cpu_flag(self) -> str:
        return f"-cpu max -smp {self.cpu} -enable-kvm"
    
    def run(self):
        command = f"qemu-system-x86_64 {self.get_cpu_flag()} {self.get_memory_flag()} -drive file={self.file},format=qcow2"
        
        if not self.type:
            command += f" {self.get_iso()} -boot d"
        else:
            command += " -boot order=c"
        
        os.system(command)

    def test(self):
        command = f"qemu-system-x86_64 {self.get_cpu_flag()} {self.get_memory_flag()} -drive file={self.file},format=qcow2"
        if not self.type:
            command += f" {self.get_iso()} -boot d"
        print(command)
