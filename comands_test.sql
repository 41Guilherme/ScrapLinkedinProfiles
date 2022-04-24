CREATE TABLE `scrap`.`interprize` 
            (`ID` INT NOT NULL,
            `Profiles` VARCHAR(300) NOT NULL,
            `Urls` VARCHAR(150) NOT NULL,
            PRIMARY KEY (`ID`));

INSERT INTO interprize(ID, Profiles, Urls) VALUES (1, "Teste", "Teste.com")

SELECT * FROM interprize

DROP TABLE interprize