**Podstawowe API dla quemu**
Puki co zaimplementowałem tylko uruchamianie VM w trybie instalacji i zwykłego uruchomienia.

## Flagi (patrz Uruchamianie żeby zobaczyć jak je wpisywać z argumentami)
- **`-memory `** – Ilość RAMU dla VM 
- **`-cpu `** – Ilość rdzeni procesora
- **`-mode`** – tryb uruchamiania fale = tryb instalacji, true = tryb uruchomienia
- **`-iso`** – ścieżka do iso (Podaj tylko w trakcie instalacji systemu).
- **`-file`** – ścieżka do pliku systemu zacznij ją od 2 jeśli chcesz stwożyć nowy plik dysku lub 1 jeśli już istnieje
- **`-size_f`** – rozmiar dysku (podaj tylko w trakcie tworzenia)


## Uruchamianie
```bash
    source py/bin/activate #Uruhcamianie środowiska wirtualnego python z wgranymi bibliotekami
    Przykładowe uruchomienie
    sudo python3 main.py -memory 4048 -cpu 4 -mode false -iso /home/admin/iso/ser2k22.iso -file 2/home/admin/image.img -size_f 40 

```
