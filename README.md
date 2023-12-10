# Sistem de recomandare de filme

Acesta este un program care folosește un model de arbore de decizie pentru a prezice ratingurile filmelor și a recomanda cele mai bine cotate filme dintr-un anumit gen.

## Descriere

Programul funcționează astfel:

1. **Încărcarea Datelor**: Se încarcă date despre filme și ratinguri din setul de date MovieLens 1M.
2. **Prelucrarea Datelor**: Se extrage anul din titlul filmului și se transformă genurile într-un format adecvat pentru analiză. Se calculează și numărul de ratinguri pentru fiecare film.
3. **Crearea Modelului de Învățare Automată**: Se construiește un model de arbore de decizie (`DecisionTreeRegressor`) pentru a învăța să prezică ratingul unui film bazat pe gen, an și numărul de ratinguri.
4. **Evaluarea Modelului**: Se evaluează modelul utilizând eroarea medie pătratică (MSE) pentru a măsura acuratețea predicțiilor.
5. **Recomandarea Filmelor**: Utilizatorii pot specifica un gen și numărul de filme pe care doresc să le vadă în top. Programul va returna o listă cu topul filmelor recomandate din acel gen.
