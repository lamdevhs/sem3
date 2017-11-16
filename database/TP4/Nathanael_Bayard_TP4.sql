/*
Nathanael Bayard - L2Info - Bases de Données - TP4

1)

2) Les commandes \? et \h servent à afficher les commandes que reconnaît le prompt de psql.

3) En utilisant la commande \l, on liste toutes les bases de données avec un certain nombre d'informations. Il y en a 4:
                            Liste des bases de données
       Nom       | Propriétaire | Encodage | Collationnement | Type caract. |    Droits d'accès     
-----------------+--------------+----------+-----------------+--------------+-----------------------
 db_userpostgres | userpostgres | UTF8     | fr_FR.UTF-8     | fr_FR.UTF-8  | 
 postgres        | postgres     | UTF8     | fr_FR.UTF-8     | fr_FR.UTF-8  | 
 template0       | postgres     | UTF8     | fr_FR.UTF-8     | fr_FR.UTF-8  | =c/postgres          +
                 |              |          |                 |              | postgres=CTc/postgres
 template1       | postgres     | UTF8     | fr_FR.UTF-8     | fr_FR.UTF-8  | =c/postgres          +
                 |              |          |                 |              | postgres=CTc/postgres
(4 lignes)


4)
postgres=> select 10*3 + 5;
 ?column? 
----------
       35
(1 ligne)



5)
postgres=> SELECT 10*3 + 5 AS "dix fois 3 font 5";
 dix fois 3 font 5 
-------------------
                35
(1 ligne)

6) afficher la mémoire tampon:
postgres=> \p
SELECT 10*3 + 5 AS "dix fois 3 font 5";


7) la commande `\w TP4SGBD/requete1.sql` n'affiche rien dans le terminal, mais crée tout de même un fichier dont le chemin et le nom valent la valeur précisée, et dont le contenu est égal à la dernière requête SQL passée, càd au contenu de la mémoire tampon, ici:
SELECT 10*3 + 5 AS "dix fois 3 font 5";

8) la commande `\g TP4SGBD/requete1.sql` n'affiche rien dans le terminal, mais crée tout de même un fichier dont le chemin et le nom valent la valeur précisée, et dont le contenu est égal au résultat de la dernière requête SQL passée, ici:
 dix fois 3 font 5 
-------------------
                35
(1 ligne)

9) la commande `\i TP4SGBD/requete1.sql` équivaut à copier le contenu du fichier requete1.sql et à le copier dans psql: càd, elle permet d'exécuter les requêtes écrites dans un fichier, et d'afficher le résultat directement dans le terminal.
Si par exemple requete1.sql contient:
SELECT 10*3 + 5 AS "dix fois 3 font 5";

Alors cette commande affichera dans le terminal:
postgres=> \i TP4SGBD/requete1.sql
 dix fois 3 font 5 
-------------------
                35
(1 ligne)

*/



\echo Question 1: Liste de tous les clients.
-- -------------
SELECT * FROM Client;

\echo Question 2: Liste de tous les clients par ordre alphabétique inverse de noms.
-- -------------
SELECT * FROM Client ORDER BY nom DESC;

\echo Question 3: Désignation et prix en Euro des produits (prendre 1 Euro = 6 FF).
SELECT desi, prixuni/6 FROM produit;

\echo Question 4: Nom et prénom des clients.
SELECT nom, prenom FROM Client;

\echo Question 5: Nom et prénom des clients qui habitent à Lyon.
SELECT nom, prenom FROM Client WHERE Lower(ville) = 'lyon';

\echo Question 6: Commandes en quantité au moins égale à 3.
SELECT * FROM commande WHERE quantite >= 3
ORDER BY numcli ASC, numprod DESC;

\echo Question 7: Désignation des produits dont le prix est compris entre 50 et 100 F.
SELECT desi FROM produit WHERE prixuni BETWEEN 50 AND 100;

\echo Question 8: Commandes en quantité indéterminée.
SELECT * FROM commande WHERE quantite IS NULL;

\echo Question 9: Nom et ville des clients dont la ville contient la chaîne "ll".
SELECT nom, ville FROM Client WHERE ville LIKE '%ll%';

\echo Question 10: Prénom des clients dont le nom est Dupont, Durand, ou Martin
SELECT prenom FROM Client WHERE nom IN ('Dupont', 'Durand', 'Martin');

\echo Question 11: Moyenne des prix des produits.
SELECT AVG (ALL prixuni) FROM Produit;

\echo Question 12: Nombre total de commandes.
SELECT COUNT (*) FROM Commande;

\echo Question 13: Liste des commandes avec le nom des clients.
SELECT nom, datec, quantite FROM Commande LEFT OUTER JOIN Client ON Client.numcli = Commande.numcli;

\echo Question 14: Liste des commandes avec le numéro et le nom des clients.
SELECT Client.numcli, nom, datec, quantite FROM Commande LEFT OUTER JOIN Client ON Client.numcli = Commande.numcli;

\echo Question 15: Nombre des clients qui ont commandé une quantité de 1.
SELECT DISTINCT nom
FROM Client INNER JOIN Commande ON Client.numcli = Commande.numcli
WHERE quantite = 1
ORDER BY nom ASC;

\echo Question 16: Quantité totale commandée par chaque client (donner le numéro de client).
SELECT numcli, SUM (quantite)
FROM Commande
GROUP BY numcli
ORDER BY numcli ASC;

\echo Question 17: Quantité moyenne commandée pour les produits faisant l'objet de plus d'une commande.
SELECT numprod, AVG (quantite)
FROM Commande
GROUP BY numprod
HAVING COUNT (*) > 1
ORDER BY numprod ASC;
