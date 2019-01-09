## SQL and MVC quiz
There are "habitats." Each habitat has a name.

There are "pokemon." Each pokemon has a name and is associated
with a habitat. A pokemon only has one habitat, but a habitat
can have many pokemon.

* *Create a database to represent this relationship*

Create an application with a model, a controller, and views that
provides the following workflow:

```
Welcome to the Pokedex

1. Create Habitat
4. Quit

Your choice: 1
```

```
Create a Habitat

Enter habitat name or enter 'cancel' to cancel.

Habitat Name: Forest
```

```
Welcome to the Pokedex

1. Create Habitat
2. List Pokemon for Habitat
3. Create Pokemon
4. Quit

Your choice: 1
```

```
Create a Habitat

Enter habitat name or enter 'cancel' to cancel.

Habitat Name: Cave
```

```
Welcome to the Pokedex

1. Create Habitat
2. List Pokemon for Habitat
3. Create Pokemon
4. Quit

Your choice: 3
```

```
Create a Pokemon

Enter the Pokemon's name or enter 'cancel' to cancel.

Pokemon Name: Bulbasaur

Which habitat does the Pokemon live in?

1. Cave
2. Forest

Your choice: 1
```

```
Welcome to the Pokedex

1. Create Habitat
2. List Pokemon for Habitat
3. Create Pokemon
4. Quit

Your choice: 2
```

```
List Pokemon for Habitat

Which habitat?

1. Cave
2. Forest

Your choice: 2

Forest Pokemon:
Bulbasaur
```

```
Welcome to the Pokedex

1. Create Habitat
2. List Pokemon for Habitat
3. Create Pokemon
4. Quit

Your choice: 4
```
