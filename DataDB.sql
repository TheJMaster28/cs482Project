set sql_safe_updates = 0;

insert into teams values ('110011', 'San Francisco', '49ers');
insert into teams values ('220022', 'Detroit','Lions');
insert into teams values ('330033', 'San Francisco','49ers');
insert into teams values ('440044', 'Miami','Dolphins');
insert into teams values ('550055', 'Minnesota','Vikings');

insert into players values ('11111', 'Jerry', 'Rice', '110011', 'WR', '200', '20000', '1000000');
insert into players values ('22222', 'Barry', 'Sanders', '220022', 'RB', '110', '15000', '5000000');
insert into players values ('33333', 'Joe', 'Montana', '330033', 'QB', '500', '40000', '2500000');
insert into players values ('44444', 'Dan', 'Marino', '440044', 'QB', '700', '55000', '3000000');
insert into players values ('55555', 'Cris', 'Carter', '550055', 'WR', '160', '18000', '1500000');

insert into games values ('10001', '19901111', 'The Minneapolis MetroDome', 'L', '55000', '1200000');
insert into games values ('20002', '19881217', 'Arrowhead Stadium', 'T', '67000', '1600000');
insert into games values ('30003', '19850105', 'Soldier Field', 'L', '59000', '1300000');
insert into games values ('40004', '19980929', 'The RCA Dome', 'W', '70000', '2100000');
insert into games values ('50005', '19941021', 'Lambeau Field', 'W', '55000', '1200000');

insert into play values ('44444', '10001');
insert into play values ('55555', '10001');
insert into play values ('33333', '20002');
insert into play values ('22222', '30003');
insert into play values ('11111', '50005');