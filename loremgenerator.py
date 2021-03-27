from pip._vendor.certifi.__main__ import args


class Generator:

    def pgenerator(args):
        # Carico la prima frase iconica standard di lorem ipsum, ad ogni avvio infatti, il mio lorem ipsum dovrà iniziare con questa frase.
        first_phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "

        # Carico il dizionario di parole che serviranno per generare i paragrafi successivi di lorem ipsum
        dictionary = open("resources/dictionary.txt", "r")

        # Uso read() per leggere il documento ed effettuare lo split delle parole sulla base del trailing char \n
        lines = dictionary.read()

        # Creo una lista splittando le linee
        words = lines.split('\n')

        # Chiudo il file
        dictionary.close()

        # Uso una lista vuota per caricarci dentro la frase completa, ripetendo il ciclo N volte effettuando lo shuffling delle parole (???) posso creare dei paragrafi
        single_phrase = []

        # Utilizzo un contatore aggiuntivo per contare le parole del lorem ipsum. Al momento è hardcoded ma sarà uno degli argv
        j = 0
        for i, word in enumerate(words):
        # Aggiungo la parola alla lista creata fuori dal ciclo
            single_phrase.append(word)
        # Aumento il contatore delle parole di 1
            j = j+1
        # Inizio un controllo per verificare che le parole create non siano più di 8. (9 con index 0)
            if j > 9:
                # se j > 8 ferma il ciclo
                break
        # trasformo la lista in una concatenazione di stringhe (stile explode - php), utilizzando lo spazio come delimitatore.
        str1 = " ".join(single_phrase)
        # verifico che siano presenti gli argv
        if (args):
            # concateno la string iniziale con quella ottenuta e aggiungo il punto alla fine.
            generated = first_phrase + str1 + "."
        #ritorno la stringa finale al main
        return generated