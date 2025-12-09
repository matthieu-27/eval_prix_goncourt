CREATE TABLE Book(
   isbn BIGINT,
   title VARCHAR(50)  NOT NULL,
   summary TEXT NOT NULL,
   main_characters VARCHAR(200)  NOT NULL,
   release_date DATE NOT NULL,
   page_number INT NOT NULL,
   author_name VARCHAR(50)  NOT NULL,
   author_biography TEXT,
   PRIMARY KEY(isbn)
);

CREATE TABLE Selection(
   id INT AUTO_INCREMENT,
   selection_number INT,
   selection_date DATE NOT NULL,
   PRIMARY KEY(id)
);

CREATE TABLE Personality(
   id INT AUTO_INCREMENT,
   name VARCHAR(50)  NOT NULL,
   is_president BOOLEAN NOT NULL,
   PRIMARY KEY(id)
);

CREATE TABLE Editor(
   id INT AUTO_INCREMENT,
   editor_name VARCHAR(50)  NOT NULL,
   PRIMARY KEY(id)
);

CREATE TABLE Selection_Books(
   book_isbn BIGINT,
   selection_id INT,
   number_of_votes INT NOT NULL DEFAULT 0,
   PRIMARY KEY(book_isbn, selection_id),
   FOREIGN KEY(book_isbn) REFERENCES Book(isbn),
   FOREIGN KEY(selection_id) REFERENCES Selection(id)
);

CREATE TABLE Editor_Books(
   book_isbn BIGINT,
   editor_id INT,
   editor_price DECIMAL(19,4) NOT NULL,
   PRIMARY KEY(book_isbn, editor_id),
   FOREIGN KEY(book_isbn) REFERENCES Book(isbn),
   FOREIGN KEY(editor_id) REFERENCES Editor(id)
);

CREATE TABLE Jury(
   selection_id INT,
   personality_id INT,
   PRIMARY KEY(selection_id, personality_id),
   FOREIGN KEY(selection_id) REFERENCES Selection(id),
   FOREIGN KEY(personality_id) REFERENCES Personality(id)
);
