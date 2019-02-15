# Implémentation et exploitation de la fonction backtrace() en C
par Martial Bornet [Consultant système, auteur du livre "Expressions Régulières, syntaxe et mise en oeuvre" chez ENI, créateur de la commande de colorisation "hl"]

---

Vous avez créé un binaire (issu d'un source C) que vous avez livré à un client, et, de temps en temps, le programme se plante suite à une violation mémoire. Vous n'avez pas la possibilité de lancer votre programme avec un debugger, ni d'examiner un fichier core pour connaître l'origine du plantage ... La fonction backtrace(), associée à quelques outils, va vous sortir de cette situation embarrassante.
