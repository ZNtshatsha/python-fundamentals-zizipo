CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(100) NOT NULL,
    age INT
);

INSERT INTO users (username, email, age) VALUES
('zamatlwane', 'zamatlwane@gmail.com', 25),
('sinovuyo', 'sinovuyo@gmail.com', 27),
('amahle', 'amahle@gmail.com',29),
('ogiyonke', 'ogiyonke@gmail.com', 23);