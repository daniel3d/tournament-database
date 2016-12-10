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
\c tournament;

-- Create the players table
DROP  TABLE IF EXISTS players CASCADE;
CREATE TABLE players ( id SERIAL PRIMARY KEY, name TEXT NOT NULL );

-- Create the matches table 
-- result field holds player id or 0 for a draw
DROP TABLE IF EXISTS matches CASCADE;
CREATE TABLE matches (
	id SERIAL PRIMARY KEY, 
	player INT REFERENCES players(id), 
	opponent INT REFERENCES players(id),
	result INT DEFAULT 0 
);

-- Create View standings
DROP VIEW IF EXISTS standings;
CREATE VIEW standings AS
SELECT 
	p.id, 
	p.name,
	COUNT(m.id) as matches,
	SUM(coalesce(m.wins, 0)) as wins,
	SUM(coalesce(m.loses, 0)) as loses,
	SUM(coalesce(m.draws, 0)) as draws,
    SUM(coalesce(m.score, 0)) as score
FROM players AS p LEFT JOIN (SELECT 
		player AS id,
		CASE WHEN result = player THEN 1 ELSE 0 END AS wins, 
		CASE WHEN result = player OR result = 0 THEN 0 ELSE 1 END AS loses,
		CASE WHEN result = 0 THEN 1 ELSE 0 END AS draws,
        CASE WHEN result = 0 THEN 0.5 WHEN result = player THEN 1.0 ELSE 0.0 END AS score
		FROM matches
	UNION ALL
	SELECT 
		opponent AS id, 
		CASE WHEN result = opponent THEN 1 ELSE 0 END AS wins, 
		CASE WHEN result = opponent OR result = 0 THEN 0 ELSE 1 END AS loses,
		CASE WHEN result = 0 THEN 1 ELSE 0 END AS draws,
		CASE WHEN result = 0 THEN 0.5 WHEN result = opponent THEN 1.0 ELSE 0.0 END AS score
		FROM matches
) as m ON p.id = m.id
GROUP BY p.id;