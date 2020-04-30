# User Storyt

Tavallisena käyttäjänä pystyn...  

- **...listaamaan kirjat, jotka haluaisin lukea.**

    - SELECT Mustreads.id, Author.name, Book.book_name, Review.id, Mustreads.book_id 
      
      FROM Mustreads 
      
      LEFT JOIN Book ON Mustreads.book_id = Book.id 
      
      LEFT JOIN Author ON Book.author_id = Author.id 
      
      LEFT JOIN Review ON Mustreads.book_id = Review.book_id
      
      WHERE Mustreads.read = False AND Mustreads.account_id = ? 
      
      GROUP BY Mustreads.id, Author.name, Book.book_name, Review.id;

- **...listaamaan lukemiani kirjoja, jotta muistan, mitä kirjoja olen lukenut.**

    - SELECT Mustreads.id, Author.name, Book.book_name, Review.id, Mustreads.book_id
      
      FROM Mustreads 
      
      LEFT JOIN Book ON Mustreads.book_id = Book.id 
      
      LEFT JOIN Author ON Book.author_id = Author.id 
      
      LEFT JOIN Review ON Mustreads.book_id = Review.book_id
      
      WHERE Mustreads.read = True AND Mustreads.account_id = ? 
      
      GROUP BY Mustreads.id, Author.name, Book.book_name, Review.id;
      
- **...lisäämään kirjoja molemmille aiemmin mainituille listoille.**

    - SELECT * FROM Author WHERE name = ?;
    
      - Mikäli kirjailijaa ei ole tietokannassa:
        - INSERT INTO Author (name) VALUES (?);
        
    - SELECT * FROM Book WHERE book_name = ?;
    
      - Mikäli kirjaa ei ole tietokannassa:
        -INSERT INTO Book (author_id, book_name) VALUES (?, ?)

    - INSERT INTO Mustreads (book_id, account_id, read) VALUES (?, ?, ?);

- **...luomaan uuden kirja-arvostelun, jonka muutkin käyttäjät nääkevät.**

    - SELECT * FROM Author WHERE name = ?;
    
      - Mikäli kirjailijaa ei ole tietokannassa:
        - INSERT INTO Author (name) VALUES (?);
        
    - SELECT * FROM Book WHERE book_name = ?;
    
      - Mikäli kirjaa ei ole tietokannassa:
        -INSERT INTO Book (author_id, book_name) VALUES (?, ?)
    
    - INSERT INTO reviews (account_id, book_id, review, stars) VALUES (?, ?, ?, ?);
    
    - SELECT * FROM MustReads WHERE book_id = ?;
      
      - Mikäli kirja ei ole käyttäjän luettujen kirjojen listalla:
        - INSERT INTO MustReads (book_id, account_id, read) VALUES (?, ?, True);

- **...tarkastelemaan aiemmin kirjoittamiani arvosteluja.**

    - SELECT Author.name, Book.book_name, Review.review, Review.stars, Account.username, Review.date_modified, Review.id
      
      FROM Review 
      
      LEFT JOIN Book ON Review.book_id = Book.id
      
      LEFT JOIN Author ON Book.author_id = Author.id
      
      LEFT JOIN Account ON Review.account_id = Account.id
      
      WHERE Review.account_id = ?
      
      GROUP BY Review.id, Author.name, Book.book_name, Account.username
      
      ORDER BY Review.date_modified DESC;

- **...muokkaamaan kirja-arvostelua sanallisesti ja sille antamiani tähtiä, mikäli mieleni kirjasta joskus muuttuu.** 

  - UPDATE Review SET review = ? AND stars = ? WHERE id = ?;

- **...tarkastelemaan muiden kirjoittamia arvosteluja sovelluksen etusivulta.** 

  - SELECT Author.name, Book.book_name, Review.review, Review.stars, Account.username, Review.date_modified, Review.id
    
    FROM Review 
    
    LEFT JOIN Book ON Review.book_id = Book.id 
    
    LEFT JOIN Author ON Book.author_id = Author.id 
    
    LEFT JOIN Account ON Review.account_id = Account.id 
    
    GROUP BY Review.id, Author.name, Book.book_name, Account.username 
    
    ORDER BY Review.date_modified DESC;

- **...löytämään arvosteluja kirjailijan nimen (tai nimen osan) perusteella.**

  - SELECT Author.name, Book.book_name, Review.review, Review.stars, Account.username, Review.date_modified, Review.id
    
    FROM Review 
    
    LEFT JOIN Book ON Review.book_id = Book.id
    
    LEFT JOIN Author ON Book.author_id = Author.id
    
    LEFT JOIN Account ON Review.account_id = Account.id
    
    WHERE LOWER(Author.name) LIKE LOWER(?)
    
    GROUP BY Review.id, Author.name, Book.book_name, Account.username
    
    ORDER BY Review.date_modified DESC;

- **...näkemään, millä viidellä kirjalla on sovelluksessa parhaimmat arvostelut.**

  - SELECT DISTINCT Author.name, Book.book_name, (
  
       SELECT TRUNC(AVG(R.stars), 1) 
        
       FROM Review R WHERE R.book_id = Review.book_id
        
       )
        
      FROM Review 
      
      LEFT JOIN Book ON Review.book_id = Book.id
      
      LEFT JOIN Author ON Book.author_id = Author.id
      
      GROUP BY Review.id, Author.name, Book.book_name
      
      ORDER BY (
      
       SELECT TRUNC(AVG(R.stars), 1) 
       
       FROM Review R WHERE R.book_id = Review.book_id
       
       ) 
       
       DESC, Book.book_name LIMIT 5;

- **...näkemään, ketkä viisi käyttäjää ovat kirjoittaneet eniten arvosteluja.**

  - SELECT DISTINCT Account.username, (
  
       SELECT COUNT(id) 
       
       FROM Review 
       
       WHERE account_id = Account.id
       
       )
                    
     FROM Account 
     
     LEFT JOIN Review ON Review.account_id = Account.id 
                    
     GROUP BY Account.id, Review.id 
     
     ORDER BY (
     
       SELECT COUNT(id) 
       
       FROM Review 
       
       WHERE account_id = Account.id
       
       ) 
       
       DESC LIMIT 5;
