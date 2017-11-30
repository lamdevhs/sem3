/*
Nathanael Bayard – L2 Info – TP5 Bases de données – 2017/2018

2) a. Non : chaque discipline sera associé à un seul code_discipline, qui est aussi la clé primaire de DISCIPLINE. Donc pour chaque discipline, il n'y aura qu'une seule ligne dans DISCIPLINE associée, et donc une seule valeur possible pour le champ #code_sport de celle-ci.
b. Chaque sportif est associé à une valeur différente de nom_licence. Dans APPARTENIR_EQUIPE, on voit que ce champ fait partie de la clé primaire avec le champ #num_equipe. On en déduit qu'il pourrait y avoir plusieurs lignes dans APPARTENIR_EQUIPE contenant le même #num_licence, mais un #num_equipe différent.Cela respectera bien le principe d'unicité associé avec la clé primaire de cette table.

*/

-- 8)
\echo a. Nom des sportifs présents dans la base
SELECT DISTINCT nom
FROM sportif;

\echo b. Code et intitulé du sport 19
SELECT *
FROM sport
WHERE code_sport = 19;

\echo c. Liste des pays d origine des sportifs; remarque?
SELECT DISTINCT pays
FROM sportif;
\echo Ils sont tous français.

\echo d. Intitulé des sports dont l intitulé comporte la chaîne "te"
SELECT intitule
FROM sport
WHERE intitule LIKE '%te%';

\echo e. Nom des sportifs dont on ne connait pas la date de naissance
SELECT nom
FROM sportif
WHERE date_naiss IS NULL;

\echo f. Liste des sportifs (nom, prenom, date naissance) par ordre alphabétique
SELECT nom, prenom, date_naiss
FROM sportif
ORDER BY nom ASC, prenom ASC;

\echo g. Liste des sportifs (nom, prenom, date naissance) par âge (décroissant)
SELECT nom, prenom, date_naiss
FROM sportif
ORDER BY date_naiss ASC;

\echo h. Liste des disciplines dont le code sport est compris entre 5 et 10
SELECT *
FROM discipline
WHERE code_sport BETWEEN 5 AND 10;

\echo i. Liste des sportifs (nom, prenom, date naissance) qui avaient moins de 30 ans aux JO de Sydney (les JO de Sydney ont eu lieu du 15 septembre au 1er Octobre 2000)
SELECT nom, prenom, date_naiss
FROM sportif
WHERE '15-09-2000' - date_naiss < 30;

\echo j. Corriger l intitulé de la discipline "-100 kg" en "- 100 kg"
UPDATE discipline
SET intitule = ' - 100 kg'
WHERE intitule = ' -100 kg';

\echo k. Tony Estanguet est né le 06/05/1678; rajouter cette info dans la base.
UPDATE sportif
SET date_naiss = '06/05/1978'
WHERE Lower(nom) = 'estanguet' AND Lower(prenom) = 'tony';

\echo l. Nom des sportifs qui pratiquent l escrime.
SELECT nom
FROM sportif, sport
WHERE Lower(sport.intitule) = 'escrime'
AND sportif.code_sport = sport.code_sport;

\echo m. Intitulé des diverses disciplines de l escrime
SELECT discipline.intitule
FROM discipline INNER JOIN sport
ON sport.code_sport = discipline.code_sport
WHERE Lower(sport.intitule) = 'escrime';

\echo n. Nom des sportifs qui ont gagné une médaille d or en individuel
SELECT nom
FROM sportif INNER JOIN gagner_individuel USING (num_licence)
WHERE Lower(medaille) = 'or';

\echo o. Intitulé de la discipline et nom du sportif pour les médailles d argent individuelle
SELECT intitule, nom
FROM sportif S, discipline D, gagner_individuel GI
WHERE Lower(medaille) = 'argent'
AND S.num_licence = GI.num_licence
AND D.code_discipline = GI.code_discipline;

\echo p. Nom et date de naissance des sportifs plus jeune que Jean-Noel Ferrari.
SELECT S.nom, S.date_naiss
FROM sportif S, sportif Ferrari
WHERE S.date_naiss > Ferrari.date_naiss
AND Lower(Ferrari.nom) = 'ferrari'
AND Lower(Ferrari.prenom) = 'jean-noel';

\echo q. Nom et médaille obtenue en individuel pour tous les escrimeurs
SELECT nom, medaille
FROM sportif SP, sport S, gagner_individuel GI
WHERE Lower(S.intitule) = 'escrime'
AND S.code_sport = SP.code_sport
AND GI.num_licence = SP.num_licence;

\echo r. Composition de l-equipe du <Quatre sans barreur>
SELECT SP.*
FROM sportif SP, appartenir_equipe AE, equipe E
WHERE Lower(E.denomination) = 'quatre sans barreur'
AND   AE.num_equipe = E.num_equipe
AND   SP.num_licence = AE.num_licence;

\echo s. Nom des sportifs qui ont eu une médaille d-or collective
SELECT SP.nom, AE.num_equipe
FROM sportif SP, appartenir_equipe AE, gagner_collectif GC
WHERE Lower(GC.medaille) = 'or'
AND   GC.num_equipe = AE.num_equipe
AND   SP.num_licence = AE.num_licence;

\echo t. Denomination des equipes pour lesquelles on ne connait pas la composition.
(SELECT DISTINCT E.num_equipe
FROM equipe E)
EXCEPT
(SELECT DISTINCT AE.num_equipe
FROM appartenir_equipe AE);

\echo u. Donner le nombre de sports aux JO de Sydney.
SELECT COUNT (S.code_sport) AS "nb sports aux JO de sydney"
FROM sport S;

\echo v. Obtenir le nombre de médailles individuelles par type.
SELECT GI.medaille, COUNT (GI.medaille) AS "medailles individuelles"
FROM gagner_individuel GI
GROUP BY GI.medaille;

\echo w. Liste de tous les sportifs (nom) avec pour chacun le nombre de médailles individuelles.
SELECT SP.nom, GI.medaille,
       COUNT (GI.medaille) AS "medailles individuelles"
FROM sportif SP, gagner_individuel GI
WHERE GI.num_licence = SP.num_licence
GROUP BY SP.nom, GI.medaille;

\echo x. Nom des sportifs qui ont gagné deux médailles en individuel.
SELECT SP.nom
FROM gagner_individuel GI, sportif SP
WHERE GI.num_licence = SP.num_licence
GROUP BY SP.num_licence
HAVING COUNT (SP.num_licence) = 2;

\echo y. Nom des sportifs ayant gagné autant de médailles collectives que David Douillet en individuel.
SELECT SP.nom
FROM gagner_collectif GC, sportif SP, appartenir_equipe AE
WHERE GC.num_equipe = AE.num_equipe
AND   AE.num_licence = SP.num_licence
GROUP BY SP.num_licence
HAVING  COUNT (SP.num_licence) IN
    (SELECT COUNT (*) AS DDnbMedailles
     FROM   gagner_individuel GI, sportif SP
     WHERE  SP.nom = 'Douillet'
     AND    SP.prenom = 'David'
     AND    GI.num_licence = SP.num_licence);

\echo z. Pour chaque sport, le nombre de médailles collectives.
SELECT S.code_sport, S.intitule,
       COUNT (S.code_sport) AS "medailles collectives"
FROM sport S, appartenir_equipe AE, gagner_collectif GC,
     sportif SP
WHERE GC.num_equipe = AE.num_equipe
AND   SP.num_licence = AE.num_licence
AND   SP.code_sport = S.code_sport
GROUP BY S.code_sport;

\echo aa. Nombre total de médailles.
SELECT COUNT (*) AS "nb medailles"
FROM   ((SELECT code_discipline, num_licence AS gagnant, medaille FROM gagner_individuel GI)
       UNION
       (SELECT code_discipline, num_equipe AS gagnant, medaille FROM gagner_collectif GC))
       all_medailles;

