SET SQL_SAFE_UPDATES = 0;
delete from teams;

insert into teams ( ID,TeamName, City ) values(1, "Broncos", "Dever");
insert into teams (ID,TeamName, City ) values(2, "Patriots", "New England");
insert into teams (ID,TeamName, City ) values(3, "Cowboys", "Dallas");
insert into teams (ID,TeamName, City ) values( 4, "Eagles","Philadelphia");
insert into teams (ID,TeamName, City ) values( 5, "Packers", "Green Bay");
insert into teams (ID,TeamName, City ) values( 6, "Giants", "New York");


select * from teams;