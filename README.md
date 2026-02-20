# PW 15. Sviluppo di un codice python per simulare un processo produttivo nel settore primario. Tesi di Laurea Informatica per le aziende digitali L31 per Università Pegaso, Autore: Matteo Marraffa  Mat. 0312400879




# 🌾 AgriTwin - Digital Twin Stocastico per l'Agricoltura 4.0
**Python

**Project Work:** Sviluppo di un codice Python per simulare un processo produttivo nel settore primario.

##  Obiettivo del Progetto
In questo progetto ho voluto realizzare una modellazione software di un'azienda agricola in ottica di **Agricoltura 4.0**. Invece di limitarmi a un semplice calcolatore di tempi, ho progettato un Simulatore Stocastico (Digital Twin) con lo scopo di:

* **Gestire 3 output produttivi differenziati:** Grano Duro (coltura estensiva meccanizzata), Olive EVO e Uva Riserva (colture con raccolta agevolata/manuale).
* **Simulare l'imprevedibilità del clima:** Ho inserito un motore stocastico che genera eventi meteo casuali (es. ondate di calore, piogge intense), i quali impattano dinamicamente sia sulla resa del campo che sulla velocità dei lavoratori.
* **Integrare metriche ESG (Economia e Sostenibilità):** Il simulatore non calcola solo i giorni di lavoro necessari, ma stima i costi operativi e calcola la *Carbon Footprint* (emissioni di CO2) dei macchinari utilizzati.

Questo Project Work rappresenta il punto di incontro tra le mie competenze informatiche e le logiche manageriali affrontate durante il mio percorso di studi. Ho cercato di applicare i principi di "Operations Management" unendoli a un'architettura software robusta, dimostrando che l'efficienza aziendale oggi non può essere slegata dalla sostenibilità ambientale.

##  Il Cuore del sistema: `simulatore_agricolo.py`
Questo modulo è il nucleo centrale del progetto. Si tratta di uno script in python che modella la logica decisionale e produttiva dell'azienda agricola.

**Caratteristiche Tecniche:**
* **Modellazione OOP (Object-Oriented):** Ho utilizzato la classe `DigitalTwinAgricolo` per incapsulare i dati e i metodi, rendendo il codice scalabile. Se in futuro l'azienda volesse aggiungere un nuovo raccolto (es. Mais), basterebbe aggiungere un record al dizionario senza toccare la logica algoritmica.
* **Motore Stocastico:** La funzione `genera_scenario_climatico()` simula l'interferenza dell'ambiente esterno, restituendo moltiplicatori matematici che alterano le variabili di produzione (Simulazione Monte Carlo-like).
* **Elaborazione sicura dei dati:** Ho evitato l'uso di liste mutabili per i parametri operativi, preferendo le *Tuple* e i metodi `.get()`, per prevenire bug e conflitti durante l'iterazione dei calcoli sui lead-time.

##  CLI Dashboard & Output Direzionale
Al posto di una tradizionale interfaccia web, ho optato per lo sviluppo di una **Dashboard Direzionale a riga di comando (CLI)**, molto usata in ambito Data Science per la sua velocità di esecuzione.

Quando si lancia lo script, l'algoritmo calcola l'intera stagione di raccolta in frazioni di secondo e stampa a video un report formattato e pulito. 
Il sistema comunica al management:
1. Quale evento climatico ha colpito la stagione corrente.
2. Le tonnellate nette realmente raccolte.
3. Il gap analysis sui tempi (Ore di lavoro necessarie e Giornate lavorative totali, tenendo conto dei colli di bottiglia e della capacità massima giornaliera).
4. Un check immediato sui costi in Euro e sui chilogrammi di CO2 emessi per ogni specifico lotto.
   
🚀 Come avviare la simulazione
Il progetto è stato scritto utilizzando esclusivamente le librerie standard di Python (math, random), pertanto non richiede l'installazione di librerie esterne (nessun file requirements.txt necessario).
Per eseguire la simulazione in locale:
Assicurati di avere Python 3 installato sul tuo computer.

Clona questa repository o scarica il file .py

Apri il terminale o il prompt dei comandi nella cartella del progetto.
Esegui il comando:

python simulatore_agricolo.py

Osserva i risultati generati casualmente per la stagione in corso direttamente a schermo. Ripetendo il comando, il motore stocastico genererà scenari operativi e climatici sempre diversi!

## 📂 Struttura della Repository
La struttura del progetto è mantenuta volutamente pulita ed essenziale per facilitarne la riproducibilità in qualsiasi ambiente locale:

```text
/
├── 📄 simulatore_agricolo.py   # Logica Core del Digital Twin (Il Project Work)
└── 📄 README.md                # Documentazione del progetto


