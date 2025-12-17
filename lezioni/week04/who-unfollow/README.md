Voglio creare un programma che sia in grado di accedere alla lista di follower su Github e riesca a tracciarli giorno per giorno.

1. della lista di follower
- dove si trova? nella sezione follower
- problema:
    - la lista non è completa e per vedere tutti i follower devo navigare tra le pagine. Inoltre devo utilizzare il bottone next per navigare tra le pagine

    <a rel="nofollow" href="https://github.com/emanuelegurini?page=2&amp;tab=followers">Next</a>

    https://github.com/emanuelegurini?page=1&tab=followers

2. voglio prendere tutto il contenuto html della pagina per identificare il pattern

<a class="d-inline-block no-underline mb-1" data-hovercard-type="user" data-hovercard-url="/users/Linda2903/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/Linda2903" aria-keyshortcuts="Alt+ArrowUp">
        <span class="f4 Link--primary"></span>
        <span class="Link--secondary">Linda2903</span>
</a>

3. voglio ottenere le statistiche
    -dal file in cui ci sono tutti i follower che ho preso nei giorni precedenti

OPERAZIONI DA COMPIERE
1. start
2. scarichiamo il contenuto di una pagina
3. verifichiamo se c'è il bottone next
    -se c'è: prendiamo l'url e scarichiamo anche quella pagina
            -ripeto step 3
    -se non c'è: verifichiamo se ci sono i follower attraverso lo specifico elemento html
4. salviamo i follower e il numero
    dove?
    - in un file
    - tabella guarda spredsheet già fatto