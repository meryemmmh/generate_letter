# app.py

import tkinter as tk
from tkinter import ttk, messagebox
import os
from generate_letter import generer_lettre

# Liste des champs à remplir
CHAMPS = ["nom", "date", "objet", "corps"]

def lancer_generation():
    nom_modele = modele_var.get()
    if not nom_modele:
        messagebox.showerror("Erreur", "Veuillez sélectionner un modèle.")
        return

    champs = {champ: entrees[champ].get() for champ in CHAMPS}

    if not all(champs.values()):
        messagebox.showwarning("Champs manquants", "Veuillez remplir tous les champs.")
        return

    try:
        nom_sortie = f"{champs['nom'].replace(' ', '_')}_lettre.docx"
        chemin = generer_lettre(nom_modele, champs, nom_sortie)
        messagebox.showinfo("Succès", f"Lettre générée :\n{chemin}")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Générateur de lettres")

# Chargement des modèles disponibles
liste_modeles = [f for f in os.listdir("modeles") if f.endswith(".docx")]

# Sélecteur de modèle
tk.Label(fenetre, text="Choisissez un modèle de lettre :").pack()
modele_var = tk.StringVar()
menu_modele = ttk.Combobox(fenetre, textvariable=modele_var, values=liste_modeles, state="readonly")
menu_modele.pack()

# Champs de saisie
entrees = {}
for champ in CHAMPS:
    tk.Label(fenetre, text=f"{champ.capitalize()} :").pack()
    entrees[champ] = tk.Entry(fenetre, width=40)
    entrees[champ].pack()

# Bouton pour générer
tk.Button(fenetre, text="Générer la lettre", command=lancer_generation).pack(pady=10)

# Lancer la fenêtre
fenetre.mainloop()
