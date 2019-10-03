create table teams(
	ID			int not null,
    TeamName	varchar(32),
    City		varchar(32),
	Primary Key(ID)
);

create table players(
	ID			int not null,
    FirstName	varchar(32),
    LastName	varchar(32),
    TeamID		int,
    Position	varchar(2) CHECK (Position = "QB" or "RB" or "WR"),
    Touchdowns	int,
    TotalYards	int,
    Salary		int,
    Primary Key(ID),
    foreign key (TeamID) references teams(ID)
    on delete set null 
);

create table games(
	ID				int not null,
    GameDate		date,
    Stadium			varchar(32),
    Result			varchar(1) check (Result = "W" or "L" or "T"),
    Attendance		int,
    TicketRevenue	int,
    Primary Key(ID)
);

create table plays(
	PlayerID	int,
    GameID		int,
    Primary key (PlayerID, GameID),
    foreign key (PlayerId) references players(ID),
    foreign key (GameID) references games(ID)     
);




    