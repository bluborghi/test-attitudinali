import random
import time

DEFAULT_MAX_ITERATIONS = 10
DEFAULT_CHAR_NUM = 8
DEFAULT_VISIBILITY_INTERVAL = 4

def genera_stringa_casuale(char_num):
    lettere = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeri = '0123456789'
    return ''.join(random.choice(lettere if random.choice([True, False]) else numeri) for _ in range(char_num))

def confronta_stringhe(stringa_casuale, stringa_utente, char_num):
    num_errori = sum(c1 != c2 for c1, c2 in zip(stringa_utente.upper() + (" "*char_num), stringa_casuale))
    return num_errori

def chiedi_domanda_con_default(domanda, valore_default = True):
    while True:
        risposta = input(domanda + " (" + ("Y/n" if valore_default else "y/N") + "): ").strip().lower()
        if risposta == "":
            return valore_default
        elif risposta == "y":
            return True
        elif risposta == "n":
            return False
        else:
            print("Risposta non valida. Si prega di rispondere con 'Y' o 'N'")

def main():
    if (chiedi_domanda_con_default(f"Allenamento classico da {DEFAULT_MAX_ITERATIONS} con {DEFAULT_CHAR_NUM} caratteri e {DEFAULT_VISIBILITY_INTERVAL} secondi?")):
        max_iterations = DEFAULT_MAX_ITERATIONS
        char_num = DEFAULT_CHAR_NUM
        visibility_interval = DEFAULT_VISIBILITY_INTERVAL
    else:
        max_iterations = int(input("Quante ripetizioni vuoi fare? "))
        char_num = int(input("Con quanti caratteri vuoi esercitarti? "))
        visibility_interval = int(input("Quanti secondi a disposizione per memorizzare la stringa? "))
    tot_errors = 0
    test_iterations = 0
    input("Quando sei pronto premi invio, comparirà una stringa casuale.")
    while test_iterations < max_iterations:
        print("\033[H\033[J")  # Questo comando pulisce il terminale
        test_iterations += 1
        stringa_casuale = genera_stringa_casuale(char_num)
        print(f"Tentativo #{test_iterations}")
        time.sleep(2)
        print("\033[H\033[J")
        print("\n" + stringa_casuale)
        time.sleep(visibility_interval)
        # Cancella la stringa precedente stampata per nasconderla
        print("\033[H\033[J")  # Questo comando pulisce il terminale

        print("Inserisci la stinga come la ricordi")
        print("_"*char_num)
        stringa_utente = input()
        num_errori = confronta_stringhe(stringa_casuale, stringa_utente, char_num)
        tot_errors += num_errori

        print("\033[H\033[J")  # Questo comando pulisce il terminale
        print(f"Tentativo #{test_iterations}")
        print("_"*char_num)
        print("\n" + stringa_utente)
        print(stringa_casuale)
        print(f"\nHai fatto {num_errori} errori.")
        print(f"Hai indovinato {char_num - num_errori} caratteri.")

        if max_iterations - test_iterations > 0:
            input(f"Te ne mancano solo {max_iterations - test_iterations} - premi invio per proseguire...")
        else:
            input(f"FINE! premi invio per vedere il punteggio...")

    print("\033[H\033[J")

    mean_errors = tot_errors/(test_iterations)
    mean_correct = (char_num*test_iterations - tot_errors)/(test_iterations)
    mean_score = (char_num - mean_errors)/char_num
    print(f"Hai provato a ricordare in {visibility_interval} secondi una stringa di {char_num} caratteri per {test_iterations} volte.")
    print(f"Hai fatto in media {round(mean_errors, 2)} errori")
    print(f"Hai indovinato in media {round(mean_correct, 2)} caratteri")
    print(f"Punteggio: {int(round(mean_score*100, 0))}/100")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgramma terminato.")
