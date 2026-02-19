import random
import math

class DigitalTwinAgricolo:
    """
    Simulatore olistico per processi agricoli.
    Implementa variabili stocastiche (clima) e metriche ESG.
    """
    
    def __init__(self):
        # parametri operativi di base dell'organizzazione
        self.ore_lavoro_giornaliere = 8
        self.risultati_simulazione = dict()
        
        # configurazione olistica dei processi: Tempi, Capacità, Costi ed Emissioni
        self.modello_produttivo = dict({
            "Grano_Duro_IoT": dict({
                "sequenza": "Mietitrebbiatura Automatica (1 Fase)",
                "tempi_fasi_ore": tuple((0.3, 0.0)),  
                "cap_max_giornaliera_ton": 80,
                "costo_orario_euro": 160.0,
                "emissioni_co2_kg_ora": 55.0
            }),
            "Olive_EVO": dict({
                "sequenza": "Agevolata + Selezione Ottica (2 Fasi)",
                "tempi_fasi_ore": tuple((2.5, 1.0)),  
                "cap_max_giornaliera_ton": 12,
                "costo_orario_euro": 65.0,
                "emissioni_co2_kg_ora": 15.0
            }),
            "Uva_Riserva": dict({
                "sequenza": "Manuale Selettiva + Ispezione (2 Fasi)",
                "tempi_fasi_ore": tuple((4.0, 1.5)),  
                "cap_max_giornaliera_ton": 6,
                "costo_orario_euro": 85.0,
                "emissioni_co2_kg_ora": 2.5
            })
        })

    def genera_scenario_climatico(self):
        """
        Motore stocastico: seleziona un evento climatico che impatta la produzione.
        Restituisce una tupla: (Nome Evento, Moltiplicatore Resa, Moltiplicatore Tempo)
        """
        scenari = tuple((
            tuple(("Clima Ideale", 1.0, 1.0)),
            tuple(("Ondata di Calore Anomala", 0.85, 1.15)),
            tuple(("Piogge Autunnali Intense", 0.95, 1.35))
        ))
        return random.choice(scenari)

    def simula_raccolto(self):
        """
        Metodo principale che esegue il calcolo algoritmico del processo,
        intersecando quantità base, impatto climatico e metriche strategiche.
        """
        # generazione quantità nominali teoriche
        quantita_teoriche = dict({
            "Grano_Duro_IoT": random.randint(200, 500),
            "Olive_EVO": random.randint(20, 70),
            "Uva_Riserva": random.randint(30, 90)
        })
        
        # estrazione scenario climatico per la stagione corrente
        clima_nome, molt_resa, molt_tempo = self.genera_scenario_climatico()
        
        # registrazione globale dello scenario
        self.risultati_simulazione.update({"SCENARIO_CLIMATICO": clima_nome})
        
        # analisi iterativa per ogni lotto di produzione
        for prodotto, qta_nominale in quantita_teoriche.items():
            parametri = self.modello_produttivo.get(prodotto)
            
            # applicazione impatto climatico
            qta_effettiva = qta_nominale * molt_resa
            
            # calcolo dei tempi con penalità meteorologica
            tempi = parametri.get("tempi_fasi_ore")
            tempo_base_per_tonnellata = sum(tempi)
            tempo_effettivo_per_ton = tempo_base_per_tonnellata * molt_tempo
            
            # operazioni matematiche fondamentali
            ore_totali = qta_effettiva * tempo_effettivo_per_ton
            cap_max = parametri.get("cap_max_giornaliera_ton")
            giorni_necessari = math.ceil(qta_effettiva / cap_max)
            
            # calcolo indicatori strategici 
            costo_totale = ore_totali * parametri.get("costo_orario_euro")
            co2_totale = ore_totali * parametri.get("emissioni_co2_kg_ora")
            
            # compilazione del report per il prodotto
            dati_output = dict({
                "Tonnellate_Raccolte": round(qta_effettiva, 2),
                "Ore_Lavoro": round(ore_totali, 1),
                "Giornate_Lavorative": giorni_necessari,
                "Costo_Operativo_Euro": round(costo_totale, 2),
                "Impatto_Ambientale_CO2_kg": round(co2_totale, 2),
                "Metodologia": parametri.get("sequenza")
            })
            
            self.risultati_simulazione.update({prodotto: dati_output})

    def stampa_report_direzionale(self):
        """
        Genera l'output di presentazione per il management.
        """
        print("=" * 70)
        print("  DIGITAL TWIN AGRICOLO - REPORT DI SIMULAZIONE DIREZIONALE")
        print("=" * 70)
        
        scenario = self.risultati_simulazione.get("SCENARIO_CLIMATICO")
        print(f"> VARIABILE STOCASTICA RILEVATA: Condizione di '{scenario}'\n")
        
        # iterazione per stampare solo i dati dei prodotti (escludendo lo scenario)
        for chiave, dati in self.risultati_simulazione.items():
            if chiave == "SCENARIO_CLIMATICO":
                continue
                
            print(f"--- LOTTO: {chiave} ---")
            print(f"  Metodologia Processo : {dati.get('Metodologia')}")
            print(f"  Resa Effettiva       : {dati.get('Tonnellate_Raccolte')} Ton")
            print(f"  Pianificazione Tempi : {dati.get('Giornate_Lavorative')} Giorni ({dati.get('Ore_Lavoro')} ore tot.)")
            print(f"  Costo Stimato (EUR)  : € {dati.get('Costo_Operativo_Euro')}")
            print(f"  Carbon Footprint     : {dati.get('Impatto_Ambientale_CO2_kg')} kg CO2")
            print("-" * 70)

# ==========================================
# ESECUZIONE PRINCIPALE
# ==========================================
if __name__ == "__main__":
    # istanziazione dell'oggetto (gemello digitale)
    simulatore = DigitalTwinAgricolo()
    
    # esecuzione dei processi
    simulatore.simula_raccolto()
    
    # output dei risultati
    simulatore.stampa_report_direzionale()

