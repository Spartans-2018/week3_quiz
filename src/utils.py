def findHabitatById(habitats, id):
    for habitat in habitats:
        if habitat.habitat_id == id:
            return habitat

    return None
