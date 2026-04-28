import numpy as np
from numba import jit
from pint import UnitRegistry

# Initialize the unit registry
ureg = UnitRegistry()

@jit(nopython=True)
def _solve_physics_engine(m, g, k, t_max, dt):
    """
    Core mathematical engine accelerated by Numba.
    Calculates free fall with air resistance: v' = g - (k/m)*v
    """
    steps = int(t_max / dt)
    v = 0.0
    y = 0.0
    for _ in range(steps):
        # Acceleration considering drag
        a = g - (k / m) * v
        v += a * dt
        y += v * dt
    return y, v

def simulate_fall(mass_str: str, time_str: str, drag_coeff: float = 0.2):
    """
    High-level wrapper using Pint for unit conversion.
    
    Args:
        mass_str: Mass with units (e.g., '80 kg')
        time_str: Duration with units (e.g., '10 s')
        drag_coeff: Air resistance coefficient
    """
    # Convert input data to SI units using Pint
    m = ureg(mass_str).to(ureg.kg).magnitude
    t = ureg(time_str).to(ureg.second).magnitude
    g = 9.81  # m/s^2
    
    # Run the accelerated simulation engine
    dist, final_v = _solve_physics_engine(m, g, drag_coeff, t, 0.001)
    
    # Return results as Pint quantity objects
    return {
        "distance": (dist * ureg.meter).to_compact(),
        "final_velocity": (final_v * ureg.meter / ureg.second).to_compact()
    }

if __name__ == "__main__":
    # Example: falling 80 kg object for 10 seconds
    res = simulate_fall("80 kg", "10 s")
    print(f"Distance traveled: {res['distance']}")
    print(f"Final velocity: {res['final_velocity']}")