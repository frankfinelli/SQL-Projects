SELECTALL= 'SELECT character_id, name FROM charactercreator_character;'
JOINMAGE = '''SELECT has_pet, name FROM charactercreator_character
JOIN charactercreator_mage
ON charactercreator_character.character_id=charactercreator_mage.character_ptr_id'''