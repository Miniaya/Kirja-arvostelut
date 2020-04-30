# Käyttöohje

## Asennusohje

### Paikallisesti

Sovelluksessa on käytössä funkioita, jotka toimivat vain postgresql-tietokantajärjestelmässä (ei siis sqlitessä). Mikäli sovelluksen haluaa saada toimimaan paikallisesti, täytyy `application/__init__.py` vaihtaa paikallisesti käytettävä tietokantajärjestelmä tai poistaa tietokantakyselyistä funktiot, jotka toimivat vain postgresqlssä. Näitä funktioita ovat `application/models.py` sarakkeiden luonnissa käytetyt *db.func.current_timestamp(0)* ja `application/reviews/model.py` metodin *get_review_by_book_id(id)* sisältämät *TRUNC()*. Sovellus toimii sqlitessä, mikäli ensimmäisistä funktioista poistaa nollat, ja jälkimmäisen funktion poistaa kyselyistä kokonaan.

### Pilvessä / Herokussa

Herokussa on käytössä postgresql, ja sovellus tietää, koska olemme Herokun ympäristössä. Se siis ei tarvitse mitään sen kummallisempia kikkailuja toimiakseen.

## Sovelluksen toiminnallisuudet

### Rekisteröityminen

Rekisteröityminen sovellukseen tapahtuu sivun oikeasta laidasta painamalla navigointipalkin *Sign in* -painiketta.

### Kirjautuminen sisään ja ulos

Rekisteröitymisen jälkeen sovellus kirjaa käyttäjän automaattisesti sisään. Mikäli käyttäjä on jo aiemmin rekisteröitynyt sovellukseen, *Login* -painike löytyy navigointipalkin oikeasta laidasta *Sign in* -painikkeen vasemmalta puolelta. Kun käyttäjä on kirjautunut sisään, uloskirjautuminen tapahtuu samasta paikasta, painikkeesta *Hello [käyttäjän koko nimi] -- Logout*.

## Sovelluksen perustoiminnallisuudet

### Kaikkien arvostelujen listaaminen

Kaikkien käyttäjien arvostelut saa näkyviin, kun painaa navigointipalkin vasemassa reunassa olevaa *Book Reviews* -painiketta. Näkymässä vasemmalla on listattu viisi käyttäjää, joilla on sovelluksessa eniten arvosteluja ja oikealla viisi kirjaa, jotka ovat saaneet parhaat arvostelut.

### Omien arvostelujen listaaminen

Omat arvostelut löytyvät *List...* -pudotusvalikosta painamalla *own reviews* -painiketta. Tässä näkymässä on myös mahdollista muokata ja poistaa arvosteluja. Arvostelun poistaminen ei poista kirjaa *books I've read* -näkymästä.

### Luettujen kirjojen listaaminen

Luetut kirjat löytyvät samasta pudostuvalikosta painamalla *books I've read* -painiketta. Tästa näkymästä on mahdollista siirtyä luomaan uutta arvostelua kirjoille, joille niitä ei vielä ole, sekä näkymään, josta pystyy lisäämään luettujen / luettavien kirjojen listalle uuden kirjan. Myös luettujen kirjojen poisto on mahdollista. Toiminnallisuus ei poista kirjasta tehtyä arvostelua.

### Luettavien kirjojen listaaminen

Luettavat kirjat löytyvät niin ikään *List...* -pudotusvalikosta painamalla *must-read books* -painiketta. Näkymässä on lista kirjoista, jotka käyttäjä on 

### Uuden arvostelun lisääminen

Uuden arvostelun lisääminen onnistuu painamalla navigointipalkin *add a new review* -nappia. Arvosteluun ei ole pakko kirjoittaa mitään, voi vain antaa arvostelun tähtinä.

### Hakutoiminnallisuus

Kirjojen arvosteluja on mahdollista hakea, kun painaa navigointipalkin *Discover* -painiketta. Haku onnistuu kirjailijan nimellä tai sen osalla.
