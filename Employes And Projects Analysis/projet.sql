DROP TABLE IF EXISTS employe;
DROP TABLE IF EXISTS projet;

CREATE TABLE projet(
    code INT PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    budget BIGINT NOT NULL,
    dateDebut DATE,
    region VARCHAR(50)
);

CREATE TABLE employe(
    numero INT PRIMARY KEY NOT NULL,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    adresse VARCHAR(50),
    age INT,
    dateEmbauche DATE,
    tel VARCHAR(50),
    profession VARCHAR(50),
    salaire INT NOT NULL,
    projet INT,
    FOREIGN KEY (projet) REFERENCES projet(code)
);