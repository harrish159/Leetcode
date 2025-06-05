SELECT name as Customers from Customers c
where id not in (Select customerId from Orders where customerId is not null)