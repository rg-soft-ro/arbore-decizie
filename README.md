# Sistem de recomandare de filme

Acesta este un program care folosește un model de arbore de decizie pentru a prezice ratingurile filmelor și a recomanda cele mai bine cotate filme dintr-un anumit gen.

## Descriere

Programul funcționează astfel:

1. **Încărcarea Datelor**: Se încarcă date despre filme și ratinguri din setul de date MovieLens 1M.
2. **Prelucrarea Datelor**: Se extrage anul din titlul filmului și se transformă genurile într-un format adecvat pentru analiză. Se calculează și numărul de ratinguri pentru fiecare film.
3. **Crearea Modelului de Învățare Automată**: Se construiește un model de arbore de decizie (`DecisionTreeRegressor`) pentru a învăța să prezică ratingul unui film bazat pe gen, an și numărul de ratinguri.
4. **Evaluarea Modelului**: Se evaluează modelul utilizând eroarea medie pătratică (MSE) pentru a măsura acuratețea predicțiilor.
5. **Recomandarea Filmelor**: Utilizatorii pot specifica un gen și numărul de filme pe care doresc să le vadă în top. Programul va returna o listă cu topul filmelor recomandate din acel gen.
   
Exemplu de utilizare:

```
Introduceti genul filmului: Action
Câte filme sa fie incluse in top? 10

Top 10 filme cu genul Action:
                                                     titlu  rating_estimat
206777                              Godfather, The (1972)        4.531370
551052  Seven Samurai (The Magnificent Seven) (Shichin...        4.519016
301528                     Raiders of the Lost Ark (1981)        4.477595
67447           Star Wars: Episode IV - A New Hope (1977)        4.457983
239262                          African Queen, The (1951)        4.373272
324376                     Godfather: Part II, The (1974)        4.367940
692115                                 Matrix, The (1999)        4.361205
554929                         Saving Private Ryan (1998)        4.328108
296220  Star Wars: Episode V - The Empire Strikes Back...        4.308500
299210                         Princess Bride, The (1987)        4.289621
```
