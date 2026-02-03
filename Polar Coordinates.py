import cmath

# Read input and convert to complex number
z = complex(input().strip())

# Calculate modulus and phase
r = abs(z)
theta = cmath.phase(z)

# Print results (up to 3 decimal places)
print(f"{r:.3f}")
print(f"{theta:.3f}")
