import pandas as pd
from pathlib import Path

output = Path("outputs")
output.mkdir(exist_ok=True)

df= pd.read_excel("data/ventes.xlsx")
print(df.head())

df["Montant"]= df["Quantite"] * df["Prix_Unitaire"]

CA_total= df["Montant"].sum()
print( "CA :" ,CA_total)

produit_plus_vendu = df.loc[
    df["Quantite"].idxmax(),
    "Produit"
]
print("produit_plus_vendu : ", produit_plus_vendu)

Nbr_total_produits= len(df)
print (" Nombre de produit:", Nbr_total_produits)
resume= pd.DataFrame({
    "Indicateur " : [
        "CA_total",
        "Produit le plus vendu",
        "Nombre total de produits"
    ],
    "Valeur" : [
        CA_total,
        produit_plus_vendu,
        Nbr_total_produits
    
    ] ,
    
})

with pd.ExcelWriter(
    "outputs/rapport.xlsx"
) as writer :
    df.to_excel(
        writer,
        sheet_name= "Ventes",
        index = False
    )
    resume.to_excel(
        writer,
        sheet_name= "Résumé",
        index = False
    )