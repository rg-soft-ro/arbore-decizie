import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import numpy as np

# Incarcarea setului de date cu filme si ratinguri pentru a fi prelucrate ulterior
filme = pd.read_csv('ml-1m/movies.dat', sep='::', engine='python', names=['idFilm', 'titlu', 'genuri'], encoding='ISO-8859-1')
ratinguri = pd.read_csv('ml-1m/ratings.dat', sep='::', engine='python', names=['idUtilizator', 'idFilm', 'rating', 'timestamp'], encoding='ISO-8859-1')

# Combinam cele doua seturi de date pentru a asocia fiecare film cu ratingurile sale
ratinguri_filme = pd.merge(filme, ratinguri, on='idFilm')

# Extragerea anului din titlul filmului
# Se utilizeaza expresii regulate pentru a gasi anul in paranteze si il convertim in format numeric
ratinguri_filme['an'] = ratinguri_filme['titlu'].str.extract(r'\((\d{4})\)').astype(float)

# Prelucram genurile pentru a crea coloane separate pentru fiecare gen
ratinguri_filme['genuri'] = ratinguri_filme['genuri'].apply(lambda x: x.split('|'))
toate_genurile = set(gen for sublist in ratinguri_filme['genuri'] for gen in sublist)
for gen in toate_genurile:
    ratinguri_filme[gen] = ratinguri_filme['genuri'].apply(lambda x: 1 if gen in x else 0)

# Calculam numarul de ratinguri pentru fiecare film pentru a evalua popularitatea acestuia
numar_ratinguri = ratinguri_filme.groupby('idFilm').size()
ratinguri_filme['numar_ratinguri'] = ratinguri_filme['idFilm'].map(numar_ratinguri)

# Se filtreaza filmele pentru a elimina cele cu un numar mic de ratinguri, pentru a reduce zgomotul din date.
ratinguri_filme = ratinguri_filme[ratinguri_filme['numar_ratinguri'] > 50]

# Se normalizeaza anul si numarul de ratinguri pentru a fi folosite in modelul de invatare automata
scaler = MinMaxScaler()
ratinguri_filme[['an', 'numar_ratinguri']] = scaler.fit_transform(ratinguri_filme[['an', 'numar_ratinguri']])

# Are loc crearea setului de date pentru model, folosind genurile, anul si numarul de ratinguri ca trasaturi
X = ratinguri_filme[list(toate_genurile) + ['an', 'numar_ratinguri']]
y = ratinguri_filme['rating']

# impartim datele in seturi de antrenament si test pentru a evalua performanta modelului
X_antrenament, X_test, y_antrenament, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Se construieste si se antreneaza modelul de arbore de decizie
model = DecisionTreeRegressor(max_depth=10, min_samples_leaf=10)
model.fit(X_antrenament, y_antrenament)

# Evaluarea modelului
# predictii = model.predict(X_test)
# print("Eroarea medie patratica (MSE):", mean_squared_error(y_test, predictii))

# Definim o functie de recomandare care accepta un gen si un numar de filme pentru a crea un top personalizat
def recomanda_filme(gen, top_n=10):
    if gen not in toate_genurile:
        return f"Genul '{gen}' nu a fost gasit"
    
    # Cream un vector de genuri pentru predictie si filtram filmele din acest gen
    date_gen = np.zeros(len(toate_genurile))
    if gen in toate_genurile:
        date_gen[list(toate_genurile).index(gen)] = 1
    date_gen = date_gen.reshape(1, -1)
    filme_gen = ratinguri_filme[ratinguri_filme[gen] == 1]
    filme_gen = filme_gen[['titlu'] + list(toate_genurile) + ['an', 'numar_ratinguri']].drop_duplicates()
    
    # Se estimeaza ratingul folosind modelul si se sorteaza filmele in functie de ratingul estimat
    filme_gen['rating_estimat'] = model.predict(filme_gen[list(toate_genurile) + ['an', 'numar_ratinguri']])
    return filme_gen.nlargest(top_n, 'rating_estimat')[['titlu', 'rating_estimat']]

gen_utilizator = input("\nIntroduceti genul filmului: ")
top_n_utilizator = int(input("Câte filme sa fie incluse in top? "))

print(f"\nTop {top_n_utilizator} filme cu genul {gen_utilizator}:\n", recomanda_filme(gen_utilizator, top_n_utilizator))
