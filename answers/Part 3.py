# Part 3: Joins and Groups
# Directions: Write a sql query or sql queries that can answer the following questions

# What is each pokemon's primary type?
SELECT P.name, T.name, P.primary_type FROM Types T INNER JOIN Pokemons P ON T.id = P.primary_type;
SELECT p.name, t.name as `primary` FROM pokemons p JOIN types t ON t.id = p.primary_type;

# What is Rufflet's secondary type?
SELECT P.name, T.name, P.secondary_type FROM Types T INNER JOIN Pokemons P ON T.id = P.secondary_type WHERE P.name = 'Rufflet';
SELECT p.name, t.name as secondary FROM pokemons p JOIN types t ON t.id = p.secondary_Type WHERE p.name = 'Rufflet';


# What are the names of the pokemon that belong to the trainer with trainerID 303?
SELECT T.trainerID, T.pokemon_id, P.name FROM pokemon_trainer T INNER JOIN pokemons P ON T.pokemon_id = P.id WHERE T.trainerID = 303;

SELECT pokemon_id FROM pokemon_trainer where trainerID = 303
SELECT p.name FROM pokemons p JOIN pokemon_Trainer pt ON pt.pokemon_id = p.id WHERE trainerID = 303


# How many pokemon have a secondary type Poison
SELECT COUNT(*) as poison_count FROM pokemons p JOIN types t ON p.secondary_type = t.id WHERE t.name = 'Poison';

# What are all the primary types and how many pokemon have that type?
SELECT t.name, COUNT(*) number_of_types FROM types t JOIN pokemons p ON t.id = p.primary_type GROUP BY t.name;

# How many pokemon at level 100 does each trainer with at least one level 100 pokemone have? (Hint: your query should not display a trainer
SELECT trainerID, COUNT(pokemon_id) num_pokemon from pokemon_trainer WHERE pokelevel = 100 GROUP BY trainerID

# How many pokemon only belong to one trainer and no other?
SELECT p.name from pokemon_trainer pt JOIN pokemons p ON p.id = pt.pokemon_id GROUP BY pokemon_id HAVING COUNT(trainerID) = 1;
