create table orders 
(
  order_id INT,
  order_date DATE,
  customer_id INT,
  order_status STRING
);

INSERT INTO orders 
VALUES
(1, '2020-01-01', 1, 'COMPLETE'),
(2, '2020-01-02', 2, 'PENDING'),
(3, '2020-01-03', 3, 'COMPLETE'),
(4, '2020-01-04', 4, 'CANCELLED'),
(5, '2020-01-05', 5, 'COMPLETE');


SELECT * FROM orders;

-- Insering more data
INSERT INTO orders 
VALUES
(6, '2020-01-06', 6, 'PENDING'),
(7, '2020-01-07', 7, 'COMPLETE');


SELECT * FROM orders;