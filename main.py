from build_ran import VM
import argparse
import logging

def main():
    # Inicjalizacja zmiennych
    memory: int = 0
    cpu: int = 0
    type_p: bool = False
    path_to_iso: str = ''
    file = ''
    mode_f = False
    size = 0

    # Konfiguracja loggera
    logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

    # Tworzymy parser argumentów
    parser = argparse.ArgumentParser(description="Przykład programu z argumentami.")
    
    # Dodajemy argumenty
    parser.add_argument('-memory', type=int, required=True, help='Pamięć dla VM (RAM) w MB')
    parser.add_argument('-cpu', type=int, required=True, help='Ilość rdzeni procesora')
    parser.add_argument('-mode', type=str, choices=['true', 'false'], required=True, help='Tryb odpalenia (false = instalacja, true = odpalenie VM)')
    parser.add_argument('-iso', type=str, help='Podaj ścieżkę do iso')
    parser.add_argument('-file', type=str, help='Określa, czy plik VM ma być stworzony (2) czy już istnieje (1), następnie podaj ścieżkę')
    parser.add_argument('-size_f', type=int, help='Jeśli tworzysz plik VM, podaj ilość GB (np. 50, a nie 50GB)')
    

    # Parsowanie argumentów
    args = parser.parse_args()

    # Przypisanie wartości argumentów
    memory = args.memory
    cpu = args.cpu
    type_p = args.mode == "true"
    edd = False
   

    # Sprawdzanie ścieżki do ISO (wymagana, jeśli `mode` to instalacja)
    if not args.iso and not type_p:
        logging.error("Brak argumentu -iso w trybie instalacji.")
        exit(1)
    
    path_to_iso = args.iso if args.iso else ''

    # Obsługa argumentu -file
    if args.file:
        if len(args.file) < 2:
            logging.error("Argument -file musi zawierać co najmniej dwa znaki (np. '1/path/do/plik').")
            exit(1)
        
        mode_indicator = args.file[0]  # Pierwszy znak określa tryb
        file = args.file[1:]  # Reszta to ścieżka

        if mode_indicator == '1':  # Plik już istnieje
            mode_f = True
        elif mode_indicator == '2':  # Tworzenie nowego pliku
            if not args.size_f:
                logging.error("Brak argumentu -size_f dla nowego pliku VM.")
                exit(1)
            size = args.size_f
        else:
            logging.error("Niepoprawna wartość argumentu -file. Użyj '1/ścieżka' lub '2/ścieżka'.")
            exit(1)
    else:
        logging.error("Brak argumentu -file.")
        exit(1)

    # Uruchomienie VM
    program = VM(
        rdzenie=cpu, 
        memory=memory, 
        type=type_p, 
        patch_iso=path_to_iso, 
        mode=0, 
        bild_file=mode_f, 
        file=file, 
        size_file=size,
        
    )

if __name__ == "__main__":
    main()
