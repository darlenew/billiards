from ortools.constraint_solver import pywrapcp

solver = pywrapcp.Solver('Billiards')

# range of possible values
a = solver.IntVar(1, 15, 'a')
b = solver.IntVar(1, 15, 'b')
c = solver.IntVar(1, 15, 'c')

# odd
solver.Add(a % 2 == 1)
solver.Add(b % 2 == 1)
solver.Add(c % 2 == 1)

# unique
solver.Add(a != b !=c )

# sum
solver.Add(a + b + c == 30)

phase = solver.Phase(
    [a, b, c],
    solver.CHOOSE_FIRST_UNBOUND,
    solver.ASSIGN_MIN_VALUE
)

solver.Solve(phase)

solver.NextSolution()

print(a.Value(), b.Value(), c.Value())
