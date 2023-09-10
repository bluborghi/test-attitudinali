import random
import time

DEFAULT_MAX_ITERATIONS = 5
DEFAULT_CHAR_NUM = 3
DEFAULT_VISIBILITY_INTERVAL = 25

def genera_stringa_casuale(char_num):
    caratteri = '01234567890123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' # doppi numeri per pareggiare meglio la presenza di numeri e lettere
    return ''.join(random.choice(caratteri) for _ in range(char_num))

def genera_matrice_casuale(length):
    matrice = [None]*length
    for i in range(length):
        matrice[i] = genera_stringa_casuale(length)
    return matrice

def stampa_matrice(m):
    print("_"*len(m))
    for i in range(len(m)):
        print(m[i])

def input_matrice(length):
    matrice = [None]*length
    print("_"*length)
    for i in range(length):
        matrice[i] = input()
    return matrice

def confronta_stringhe(stringa_casuale, stringa_utente):
    length = len(stringa_casuale)
    num_errori = sum(c1 != c2 for c1, c2 in zip(stringa_utente.upper() + (" "*length), stringa_casuale))
    return num_errori

def confronta_matrici(matrice_corretta, matrice_input):
    length = len(matrice_corretta)
    tot_errori = 0
    for i in range(length):
        errori_riga = confronta_stringhe(matrice_corretta[i], matrice_input[i])
        tot_errori += errori_riga
    return tot_errori


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
    if (chiedi_domanda_con_default(f"Allenamento classico da {DEFAULT_MAX_ITERATIONS} con matrice {DEFAULT_CHAR_NUM}x{DEFAULT_CHAR_NUM} e {DEFAULT_VISIBILITY_INTERVAL} secondi?")):
        max_iterations = DEFAULT_MAX_ITERATIONS
        char_num = DEFAULT_CHAR_NUM
        visibility_interval = DEFAULT_VISIBILITY_INTERVAL
    else:
        max_iterations = int(input("Quante ripetizioni vuoi fare? "))
        char_num = int(input("Che lunghezza deve avere la matrice? "))
        visibility_interval = int(input("Quanti secondi a disposizione per memorizzare la matrice? "))
    tot_errors = 0
    test_iterations = 0
    input("Quando sei pronto premi invio, comparirà una matrice casuale.")
    while test_iterations < max_iterations:
        print("\033[H\033[J")  # Questo comando pulisce il terminale
        test_iterations += 1
        matrice_casuale = genera_matrice_casuale(char_num)
        print(f"Tentativo #{test_iterations}")
        time.sleep(2)
        print("\033[H\033[J")
        stampa_matrice(matrice_casuale)
        time.sleep(visibility_interval)
        # Cancella la stringa precedente stampata per nasconderla
        print("\033[H\033[J")  # Questo comando pulisce il terminale

        print("Inserisci la matrice come la ricordi")
        matrice_utente = input_matrice(len(matrice_casuale))

        num_errori = confronta_matrici(matrice_casuale, matrice_utente)
        tot_errors += num_errori

        print("\033[H\033[J")  # Questo comando pulisce il terminale
        print(f"Tentativo #{test_iterations}")
        stampa_matrice(matrice_utente)
        stampa_matrice(matrice_casuale)
        print(f"\nHai fatto {num_errori} errori.")
        print(f"Hai indovinato {char_num*char_num - num_errori} caratteri.")

        if max_iterations - test_iterations > 0:
            input(f"Te ne mancano solo {max_iterations - test_iterations} - premi invio per proseguire...")
        else:
            input(f"FINE! premi invio per vedere il punteggio...")

    print("\033[H\033[J")

    mean_errors = tot_errors/(test_iterations)
    mean_correct = (char_num*char_num*test_iterations - tot_errors)/(test_iterations)
    mean_score = (char_num*char_num - mean_errors)/(char_num*char_num)
    print(f"Hai provato a ricordare in {visibility_interval} secondi una matrice di {char_num}x{char_num} per {test_iterations} volte.")
    print(f"Hai fatto in media {round(mean_errors, 2)} errori")
    print(f"Hai indovinato in media {round(mean_correct, 2)} caratteri su {char_num*char_num}")
    print(f"Punteggio: {int(round(mean_score*100, 0))}/100")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgramma terminato.")
