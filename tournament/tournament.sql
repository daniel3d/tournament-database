-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


-- Create the database
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

-- Create the players table
CREATE TABLE players ( id SERIAL PRIMARY KEY, name TEXT NOT NULL );

-- Create the matches table 
-- result field holds player id or 0 for a draw
CREATE TABLE matches (
	id SERIAL PRIMARY KEY, 
	player INT REFERENCES players(id), 
	opponent INT REFERENCES players(id),
	result INT DEFAULT 0 
);

-- Create View standings
CREATE VIEW standings AS
SELECT 
	p.id, 
	p.name,
	COUNT(*) as matches,
	SUM(m.wins) as wins,
	SUM(m.loses) as loses,
	SUM(m.draws) as draws,
	SUM(m.wins - m.loses + m.draws) as score
FROM (SELECT 
		player AS id,
		CASE result WHEN player THEN 1 ELSE 0 END AS wins, 
		CASE result WHEN player OR 0 THEN 0 ELSE 1 END AS loses, 
		CASE result WHEN 0 THEN 1 ELSE 0 END AS draws 
		FROM matches 
	UNION ALL
	SELECT 
		opponent AS id, 
		CASE result WHEN player THEN 1 ELSE 0 END AS wins, 
		CASE result WHEN player OR 0 THEN 0 ELSE 1 END AS loses, 
		CASE result WHEN 0 THEN 1 ELSE 0 END AS draws 
		FROM matches 
) as m LEFT JOIN players AS p ON p.id = m.id
GROUP BY m.id
ORDER BY score DESC