from physcalc.core import simulate_fall

def test_simulation_run():
    """Check if the simulation returns expected keys and types."""
    result = simulate_fall("10 kg", "1 s")
    assert "distance" in result
    assert "final_velocity" in result
    # Check if results are Pint objects
    assert hasattr(result["distance"], "units")

def test_physics_logic():
    """Basic sanity check: distance should be positive."""
    result = simulate_fall("1 kg", "2 s")
    assert result["distance"].magnitude > 0