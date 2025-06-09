import pytest
from src.api_client import get_pokemon_list, get_pokemon_details


def test_get_pokemon_list():
      pokemons = get_pokemon_list(limit=5)
      assert isinstance(pokemons,list)
      assert len(pokemons) == 5
      for p in pokemons:
            assert "name" in p
            assert "url" in p

def test_get_pokemon_details():
      pokemons = get_pokemon_list(limit=1)
      assert len(pokemons) == 1
      details = get_pokemon_details(pokemons[0]['url'])
      assert isinstance(details, dict)
      assert "id" in details
      assert "name" in details
      assert "base_experience" in details
      assert "stats" in details
      assert "types" in details
def test_get_pokemon_details_with_invalid_url():
      with pytest.raises(Exception):
            get_pokemon_details("https://pokeapi.co/api/v2/pokemon/invalid-url")
