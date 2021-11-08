# Part 3: Joins and Groups
# Directions: Write a sql query or sql queries that can answer the following questions

# What is each pokemon's primary type?
SELECT P.name, T.name, P.primary_type FROM Types T INNER JOIN Pokemons P ON T.id = P.primary_type;

# What is Rufflet's secondary type?
SELECT P.name, T.name, P.secondary_type FROM Types T INNER JOIN Pokemons P ON T.id = P.secondary_type WHERE P.name = 'Rufflet';

# What are the names of the pokemon that belong to the trainer with trainerID 303?
SELECT T.trainerID, T.pokemon_id, P.name FROM pokemon_trainer T INNER JOIN pokemons P ON T.pokemon_id = P.id WHERE T.trainerID = 303;

# How many pokemon have a secondary type Poison
SELECT COUNT(*) as poison_count FROM pokemons p JOIN types t ON p.secondary_type = t.id WHERE t.name = 'Poison';

# What are all the primary types and how many pokemon have that type?
SELECT t.name, COUNT(*) number_of_types FROM types t JOIN pokemons p ON t.id = p.primary_type GROUP BY t.name;

# How many pokemon at level 100 does each trainer with at least one level 100 pokemone have? (Hint: your query should not display a trainer
SELECT t.trainerId, t.trainername, COUNT(*) as lvl_one_hundred_count FROM pokemon_trainer JOIN trainers t on t.trainerID = pokemon_trainer.trainerID WHERE pokelevel = 100 GROUP BY pokemon_trainer.trainerID ORDER BY lvl_one_hundred_count desc;

# How many pokemon only belong to one trainer and no other?
SELECT COUNT(*) as total_pokemon_with_one_trainer FROM (select pt.pokemon_id, COUNT(pt.trainerId) AS trainer_count FROM pokemon_trainer pt JOIN pokemons p ON pt.pokemon_id = p.id GROUP BY pt.pokemon_id having trainer_count = 1) as pokemon_to_trainer_count;