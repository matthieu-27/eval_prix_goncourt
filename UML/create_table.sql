CREATE TABLE Selection(
   id INT,
   selection_number INT,
   selection_date DATE NOT NULL,
   number_of_books VARCHAR(50) ,
   PRIMARY KEY(id)
);

CREATE TABLE Jury(
   goncourt_year INT,
   PRIMARY KEY(goncourt_year)
);

CREATE TABLE Personality(
   id INT,
   name VARCHAR(50)  NOT NULL,
   is_president BOOLEAN NOT NULL,
   goncourt_year INT NOT NULL,
   PRIMARY KEY(id),
   FOREIGN KEY(goncourt_year) REFERENCES Jury(goncourt_year)
);

CREATE TABLE Editor(
   id INT,
   editor_name VARCHAR(50)  NOT NULL,
   editor_price DECIMAL(19,4) NOT NULL,
   PRIMARY KEY(id)
);

CREATE TABLE Author(
   id INT,
   author_name VARCHAR(50)  NOT NULL,
   author_biography TEXT,
   PRIMARY KEY(id)
);

CREATE TABLE Awardee(
   book_isbn CHAR(13) ,
   number_of_votes INT,
   PRIMARY KEY(book_isbn)
);

CREATE TABLE Book(
   isbn INT,
   title VARCHAR(50)  NOT NULL,
   summary TEXT NOT NULL,
   main_characters VARCHAR(200)  NOT NULL,
   release_date DATE NOT NULL,
   page_number INT NOT NULL,
   author_id INT NOT NULL,
   PRIMARY KEY(isbn),
   FOREIGN KEY(author_id) REFERENCES Author(id)
);

CREATE TABLE Selection_Content(
   book_isbn INT,
   selection_id INT,
   PRIMARY KEY(book_isbn, selection_id),
   FOREIGN KEY(book_isbn) REFERENCES Book(isbn),
   FOREIGN KEY(selection_id) REFERENCES Selection(id)
);

CREATE TABLE Editor_Books(
   book_isbn INT,
   editor_id INT,
   PRIMARY KEY(book_isbn, editor_id),
   FOREIGN KEY(book_isbn) REFERENCES Book(isbn),
   FOREIGN KEY(editor_id) REFERENCES Editor(id)
);

CREATE TABLE Awardee_Selection(
   selection_id INT,
   book_isbn CHAR(13) ,
   vote_round INT,
   PRIMARY KEY(selection_id, book_isbn),
   FOREIGN KEY(selection_id) REFERENCES Selection(id),
   FOREIGN KEY(book_isbn) REFERENCES Awardee(book_isbn)
);

CREATE TABLE Personality_Selection(
   selection_id INT,
   personality_id INT,
   PRIMARY KEY(selection_id, personality_id),
   FOREIGN KEY(selection_id) REFERENCES Selection(id),
   FOREIGN KEY(personality_id) REFERENCES Personality(id)
);