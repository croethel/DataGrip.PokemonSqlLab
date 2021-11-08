# Directions: Write a query that returns the following collumns:

# Pokemon Name	    Trainer Name	Level	        Primary Type	    Secondary Type
# Pokemon's name	Trainer's name	Current Level	Primary Type Name	Secondary Type Name

# Sort the data by finding out which trainer has the strongest pokemon so that this will act
# as a ranking of strongest to weakest trainer. You may interpret strongest in whatever way you want,
# but you will have to explain your decision.


SELECT pokemons_name, trainers_name, current_level, primary_type_name, types.name AS secondary_type_name
FROM (select pokemons.name as pokemons_name, trainers.trainername as trainers_name, pokemon_trainer.pokelevel as current_level, types.name as primary_type_name, pokemons.secondary_type as secondary_type_id
FROM pokemons
JOIN pokemon_trainer ON pokemon_trainer.pokemon_id = pokemons.id
JOIN trainers on trainers.trainerid = pokemon_trainer.trainerid
JOIN types on types.id = pokemons.primary_type) table_1
JOIN types on types.id = secondary_type_id
ORDER BY current_level desc


# Ordered by level