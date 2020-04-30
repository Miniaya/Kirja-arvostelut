# Tietokantakaavio

![alt text](https://github.com/Miniaya/Kirja-arvostelut/blob/master/documentation/kuvat/tietokantakaavio.png)

## CREATE TABLE -lauseet

        CREATE TABLE account (

        id INTEGER NOT NULL, 
        
        date_created DATETIME, 
        
        date_modified DATETIME, 
        
        name VARCHAR(100) NOT NULL, 
        
        username VARCHAR(24) NOT NULL, 
        
        password VARCHAR(16) NOT NULL, 
        
        PRIMARY KEY (id)
        
        )

        CREATE TABLE author (
        
        id INTEGER NOT NULL, 
        
        name VARCHAR(144) NOT NULL, 
        
        PRIMARY KEY (id)
        )

        CREATE TABLE book (
        
        id INTEGER NOT NULL, 
        
        author_id INTEGER NOT NULL, 
        
        book_name VARCHAR(144) NOT NULL, 
        
        PRIMARY KEY (id), 
        
        FOREIGN KEY(author_id) REFERENCES author (id)
        
        )

        CREATE TABLE review (
        
        id INTEGER NOT NULL, 
        
        date_created DATETIME, 
        
        date_modified DATETIME, 
        
        account_id INTEGER NOT NULL, 
        
        book_id INTEGER NOT NULL, 
        
        review VARCHAR(400) NOT NULL, 
        
        stars INTEGER NOT NULL, 
        
        PRIMARY KEY (id), 
        
        FOREIGN KEY(account_id) REFERENCES account (id), 
        
        FOREIGN KEY(book_id) REFERENCES book (id)
        
        )

        CREATE TABLE mustreads (
        
        id INTEGER NOT NULL, 
        
        date_created DATETIME, 
        
        date_modified DATETIME, 
        
        book_id INTEGER NOT NULL, 
        
        account_id INTEGER NOT NULL, 
        
        read BOOLEAN NOT NULL, 
        
        PRIMARY KEY (id), 
        
        FOREIGN KEY(book_id) REFERENCES book (id), 
        
        FOREIGN KEY(account_id) REFERENCES account (id), 
        
        CHECK (read IN (0, 1))

        )
