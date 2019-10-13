/*	Jeff Lansford, Brandon Ihlein, Kitt Phi
	Table: players
	Assumptions: Player name cannot be NULL.
				 TeamID CAN be NULL (for free-agents).
                 Touchdowns, TotalYards, and Salary each must be no less than 0.
*/

  create table teams(
	TeamID		integer NOT NULL,
    TeamName	varchar(32),
    City		varchar(32),
	Primary Key(TeamID)
);

create table players
   (PlayerID		integer,
    FirsName		varchar(32) NOT NULL,
    LastName		varchar(32) NOT NULL,	
	TeamID			integer,
    Position		varchar(2) check (Position in ('QB', 'RB', 'WR')),
    Touchdowns		integer check (Touchdowns >= 0),
    TotalYards		integer check (TotalYards >= 0),
    Salary			integer check (Salary >= 0),
    primary key 	(PlayerID),
    foreign key (TeamID) references teams(TeamID)
    on delete set null
   );
   
 /*
	Table: games
    Assumptions:	All games in the table have been played already (no future games).
					Neither game date, game stadium, nor game result can be NULL. 
                    Both attendance and TicketRevenue must be no less than 0.
 */

create table games
   (GameID			integer,
	Date			date NOT NULL,
	Stadium			varchar(64) NOT NULL,
	Result			varchar(1) NOT NULL	check (Result in ('W', 'L', 'T')),
	Attendance		integer check (Attendance >= 0),
	TicketRevenue	integer check (TicketRevenue >= 0),
	primary key 	(GameID)
   );


   /*
	Table: play
    Assumptions:	(Only those from previous tabless)
 */
  
create table play
   (PlayerID		integer,
	GameID			integer,
	primary key 	(PlayerID, GameID),
	foreign key 	(PlayerID) references players(PlayerID) on delete cascade,
	foreign key 	(GameID) references games(GameID) on delete cascade
   );
