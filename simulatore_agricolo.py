import random
import math

# generiamo le parentesi per i colori dinamicamente
def csi(codice):
    # chr(27) è ESC, chr(91) è la parentesi quadra aperta
    return chr(27) + chr(91) + str(codice) + "m"

# ==========================================
# PALETTE COLORI PER L'INTERFACCIA GRAFICA
# ==========================================
RESET = csi(0)
BOLD = csi(1)
T_BIANCO = csi(97)
T_VERDE = csi(92)
T_GIALLO = csi(93)
T_ROSSO = csi(91)
T_CIANO = csi(96)
T_VIOLA = csi(95)
T_NERO = csi(30)
BG_BLU = csi(44)
BG_VERDE = csi(42)
BG_GIALLO = csi(43)
BG_ROSSO = csi(41)

class DigitalTwinAgricolo:
    """
    Simulatore olistico per processi agricoli con UI colorata .
    """
    
    def __init__(self):
        self.ore_giornaliere = 8
        self.risultati = dict()
        
        # configurazione: tempi, capacita, costi e emissioni
        self.modello = dict({
            "Grano": dict({
                "label": "Grano Duro IoT",
                "colore": T_GIALLO,
                "metodo": "Mietitrebbiatura (1 Fase)",
                "tempi": tuple((0.3, 0.0)),
                "cap_max": 80,
                "costo_h": 160.0,
                "co2_h": 55.0
            }),
            "Olive": dict({
                "label": "Olive EVO",
                "colore": T_VERDE,
                "metodo": "Agevolata + Selezione (2 Fasi)",
                "tempi": tuple((2.5, 1.0)),
                "cap_max": 12,
                "costo_h": 65.0,
                "co2_h": 15.0
            }),
            "Uva": dict({
                "label": "Uva Riserva",
                "colore": T_VIOLA,
                "metodo": "Manuale + Ispezione (2 Fasi)",
                "tempi": tuple((4.0, 1.5)),
                "cap_max": 6,
                "costo_h": 85.0,
                "co2_h": 2.5
            })
        })

    def genera_meteo(self):
        """Motore stocastico che associa anche il colore di sfondo al clima"""
        scenari = tuple((
            tuple(("* Clima Ideale", 1.0, 1.0, BG_VERDE + T_BIANCO)),
            tuple(("! Ondata di Calore Anomala", 0.85, 1.15, BG_ROSSO + T_BIANCO)),
            tuple(("~ Piogge Autunnali Intense", 0.95, 1.35, BG_GIALLO + T_NERO))
        ))
        return random.choice(scenari)

    def simula(self):
        # quantita base
        qta_teoriche = dict({
            "Grano": random.randint(200, 500),
            "Olive": random.randint(20, 70),
            "Uva": random.randint(30, 90)
        })
        
        # generiamo il clima e lo salviamo
        nome_meteo, molt_resa, molt_tempo, bg_colore = self.genera_meteo()
        
        # memorizziamo il meteo in un dizionario
        meteo_dict = dict({"nome": nome_meteo, "colore_sfondo": bg_colore})
        self.risultati.update({"METEO": meteo_dict})
        
        # ciclo sui prodotti
        for prod, q_nom in qta_teoriche.items():
            param = self.modello.get(prod)
            
            # formule con i moltiplicatori climatici
            q_eff = q_nom * molt_resa
            
            tempi = param.get("tempi")
            t_base = sum(tempi)
            t_eff = t_base * molt_tempo
            
            ore_tot = q_eff * t_eff
            cap = param.get("cap_max")
            gg = math.ceil(q_eff / cap)
            
            costo = ore_tot * param.get("costo_h")
            co2 = ore_tot * param.get("co2_h")
            
            # salvataggio nel record
            self.risultati.update({
                prod: dict({
                    "label": param.get("label"),
                    "colore": param.get("colore"),
                    "metodo": param.get("metodo"),
                    "tonnellate": round(q_eff, 2),
                    "ore": round(ore_tot, 1),
                    "giorni": gg,
                    "costo": costo,
                    "co2": co2
                })
            })

    def stampa_dashboard(self):
        # intestazione blu
        print("\n" + BG_BLU + BOLD + T_BIANCO + " " * 76 + RESET)
        titolo = "*** DIGITAL TWIN AGRICOLO - DASHBOARD DIREZIONALE ***"
        spazi_t = " " * int((76 - len(titolo)) / 2)
        riga_titolo = spazi_t + titolo + spazi_t
        if len(riga_titolo) < 76: riga_titolo += " "
        print(BG_BLU + BOLD + T_BIANCO + riga_titolo + RESET)
        print(BG_BLU + BOLD + T_BIANCO + " " * 76 + RESET + "\n")
        
        # stampa del Banner Meteo Colorato
        meteo_dati = self.risultati.get("METEO")
        nome_meteo = meteo_dati.get("nome")
        sfondo = meteo_dati.get("colore_sfondo")
        
        testo_meteo = " IMPATTO CLIMATICO: " + nome_meteo + " "
        spazi_m = " " * int((76 - len(testo_meteo)) / 2)
        riga_meteo = spazi_m + testo_meteo + spazi_m
        if len(riga_meteo) < 76: riga_meteo += " "
        
        print(sfondo + BOLD + riga_meteo + RESET + "\n")
        
        # stampa iterativa dei lotti agricoli
        for chiave, dati in self.risultati.items():
            if chiave == "METEO": 
                continue
            
            colore_titolo = dati.get("colore")
            titolo = dati.get("label")
            
            print(colore_titolo + BOLD + "  " + titolo + RESET)
            print("  |- Metodologia : " + dati.get("metodo"))
            print("  |- Resa Netta  : " + BOLD + str(dati.get("tonnellate")) + " Ton" + RESET)
            print("  |- Tempi       : " + T_CIANO + str(dati.get("giorni")) + " Giorni" + RESET + " (Totale: " + str(dati.get("ore")) + " ore)")
            
            # formattazione numeri europea (punto per migliaia e la virgola per decimali)
            str_costo = "{:,.2f}".format(dati.get("costo")).replace(",", "X").replace(".", ",").replace("X", ".")
            str_co2 = "{:,.1f}".format(dati.get("co2")).replace(",", "X").replace(".", ",").replace("X", ".")
            
            print("  |- Costi       : " + T_VERDE + "EUR " + str_costo + RESET)
            print("  |- Emissioni   : " + T_ROSSO + str_co2 + " kg CO2" + RESET + "\n")
            
        print(BG_BLU + T_BIANCO + "=" * 76 + RESET + "\n")

# ==========================================
# AVVIO DEL PROGRAMMA
# ==========================================
if __name__ == "__main__":
    twin = DigitalTwinAgricolo()
    twin.simula()
    twin.stampa_dashboard()