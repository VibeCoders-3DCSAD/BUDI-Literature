---
conversion_metadata:
  converted_at: "2026-10-11T15:12:43Z"
  converter_tool: "markitdown"
  converter_version: "0.1.8"
  source_pdf: "SciPy, n.d..pdf"
  source_pdf_sha256: "1001ba4a8e977d6ffb634a9bdaef4fa05ffc63f48b58587975ca40609e812d91"
  page_count: 6
  markdown_char_count: 9068
---

10/11/26, 12:41 AM

linprog(method=’highs-ds’) — SciPy v1.15.3 Manual

This is documentation for an old version (1.15.3).

Switch to stable version

› SciPy API › Optimization and root finding ( scipy.optimize ) › linprog(meth...

linprog(method=’highs-ds’)

linprog(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=(0, None),

method='highs', callback=None, options=None, x0=None, integrality=None)

Linear programming: minimize a linear objective function subject to linear equality and

inequality constraints using the HiGHS dual simplex solver.

Linear programming solves problems of the following form:

where

 is a vector of decision variables;  ,

,

,  , and

 are vectors; and

 and

are matrices.

Alternatively, that’s:

minimize:

c @ x

such that:

A_ub @ x <= b_ub
A_eq @ x == b_eq
lb <= x <= ub

Note that by default  lb = 0  and  ub = None  unless specified with  bounds .

https://docs.scipy.org/doc/scipy-1.15.3/reference/optimize.linprog-highs-ds.html

1/6

10/11/26, 12:41 AM

linprog(method=’highs-ds’) — SciPy v1.15.3 Manual

Parameters:

c : 1-D array

The coefficients of the linear objective function to be minimized.

A_ub : 2-D array, optional

The inequality constraint matrix. Each row of  A_ub  specifies the coefficients of a

linear inequality constraint on  x .

b_ub : 1-D array, optional

The inequality constraint vector. Each element represents an upper bound on the

corresponding value of  A_ub @ x .

A_eq : 2-D array, optional

The equality constraint matrix. Each row of  A_eq  specifies the coefficients of a linear

equality constraint on  x .

b_eq : 1-D array, optional

The equality constraint vector. Each element of  A_eq @ x  must equal the

corresponding element of  b_eq .

bounds : sequence, optional

A sequence of  (min, max)  pairs for each element in  x , defining the minimum and

maximum values of that decision variable. Use  None  to indicate that there is no

bound. By default, bounds are  (0, None)  (all decision variables are non-negative).

If a single tuple  (min, max)  is provided, then  min  and  max  will serve as bounds

for all decision variables.

method : str

This is the method-specific documentation for ‘highs-ds’. ‘highs’, ‘highs-ipm’, ‘interior-

point’ (default), ‘revised simplex’, and ‘simplex’ (legacy) are also available.

Returns:

res : OptimizeResult

A  scipy.optimize.OptimizeResult  consisting of the fields:

x : 1D array

The values of the decision variables that minimizes the objective function while

satisfying the constraints.

fun : float

The optimal value of the objective function  c @ x .

https://docs.scipy.org/doc/scipy-1.15.3/reference/optimize.linprog-highs-ds.html

2/6

10/11/26, 12:41 AM

linprog(method=’highs-ds’) — SciPy v1.15.3 Manual

slack : 1D array

The (nominally positive) values of the slack,  b_ub - A_ub @ x .

con : 1D array

The (nominally zero) residuals of the equality constraints,  b_eq - A_eq @ x .

success : bool

True  when the algorithm succeeds in finding an optimal solution.

status : int

An integer representing the exit status of the algorithm.

0  : Optimization terminated successfully.

1  : Iteration or time limit reached.

2  : Problem appears to be infeasible.

3  : Problem appears to be unbounded.

4  : The HiGHS solver ran into a problem.

message : str

A string descriptor of the exit status of the algorithm.

nit : int

The total number of iterations performed. This includes iterations in all phases.

crossover_nit : int

This is always  0  for the HiGHS simplex method. For the HiGHS interior-point

method, this is the number of primal/dual pushes performed during the crossover

routine.

ineqlin : OptimizeResult

Solution and sensitivity information corresponding to the inequality constraints,

b_ub. A dictionary consisting of the fields:

residual : np.ndnarray

The (nominally positive) values of the slack variables,  b_ub - A_ub @ x .

This quantity is also commonly referred to as “slack”.

marginals : np.ndarray

The sensitivity (partial derivative) of the objective function with respect to the

right-hand side of the inequality constraints, b_ub.

eqlin : OptimizeResult

https://docs.scipy.org/doc/scipy-1.15.3/reference/optimize.linprog-highs-ds.html

3/6

10/11/26, 12:41 AM

linprog(method=’highs-ds’) — SciPy v1.15.3 Manual

Solution and sensitivity information corresponding to the equality constraints,

b_eq. A dictionary consisting of the fields:

residual : np.ndarray

The (nominally zero) residuals of the equality constraints,  b_eq - A_eq @

x .

marginals : np.ndarray

The sensitivity (partial derivative) of the objective function with respect to the

right-hand side of the equality constraints, b_eq.

lower, upper : OptimizeResult

Solution and sensitivity information corresponding to the lower and upper bounds

on decision variables, bounds.

residual : np.ndarray

The (nominally positive) values of the quantity  x - lb  (lower) or  ub - x

(upper).

marginals : np.ndarray

The sensitivity (partial derivative) of the objective function with respect to the

lower and upper bounds.



See also

For documentation for the rest of the parameters, see  scipy.optimize.linprog

Options:

——-

maxiter : int

The maximum number of iterations to perform in either phase. Default is the largest

possible value for an  int  on the platform.

disp : bool (default:  False )

Set to  True  if indicators of optimization status are to be printed to the console during

optimization.

presolve : bool (default:  True )

Presolve attempts to identify trivial infeasibilities, identify trivial unboundedness, and

simplify the problem before sending it to the main solver. It is generally recommended

https://docs.scipy.org/doc/scipy-1.15.3/reference/optimize.linprog-highs-ds.html

4/6

10/11/26, 12:41 AM

linprog(method=’highs-ds’) — SciPy v1.15.3 Manual

to keep the default setting  True ; set to  False  if presolve is to be disabled.

time_limit : float

The maximum time in seconds allotted to solve the problem; default is the largest

possible value for a  double  on the platform.

dual_feasibility_tolerance : double (default: 1e-07)

Dual feasibility tolerance for ‘highs-ds’.

primal_feasibility_tolerance : double (default: 1e-07)

Primal feasibility tolerance for ‘highs-ds’.

simplex_dual_edge_weight_strategy : str (default: None)

Strategy for simplex dual edge weights. The default,  None , automatically selects one

of the following.

'dantzig'  uses Dantzig’s original strategy of choosing the most negative reduced

cost.

'devex'  uses the strategy described in [15].

steepest  uses the exact steepest edge strategy as described in [16].

'steepest-devex'  begins with the exact steepest edge strategy until the

computation is too costly or inexact and then switches to the devex method.

Currently,  None  always selects  'steepest-devex' , but this may change as new

options become available.

unknown_options : dict

Optional arguments not used by this particular solver. If  unknown_options  is non-

empty, a warning is issued listing all unused options.

Notes

Method ‘highs-ds’ is a wrapper of the C++ high performance dual revised simplex

implementation (HSOL) [13], [14]. Method ‘highs-ipm’ is a wrapper of a C++ implementation of

an interior-point method [13]; it features a crossover routine, so it is as accurate as a simplex

solver. Method ‘highs’ chooses between the two automatically. For new code involving

linprog , we recommend explicitly choosing one of these three method values instead of

‘interior-point’ (default), ‘revised simplex’, and ‘simplex’ (legacy).

The result fields ineqlin, eqlin, lower, and upper all contain marginals, or partial derivatives of

the objective function with respect to the right-hand side of each constraint. These partial

derivatives are also referred to as “Lagrange multipliers”, “dual values”, and “shadow prices”.

https://docs.scipy.org/doc/scipy-1.15.3/reference/optimize.linprog-highs-ds.html

5/6

10/11/26, 12:41 AM

linprog(method=’highs-ds’) — SciPy v1.15.3 Manual

The sign convention of marginals is opposite that of Lagrange multipliers produced by many

nonlinear solvers.

SciPy

References

[13](1,2)

Huangfu, Q., Galabova, I., Feldmeier, M., and Hall, J. A. J. “HiGHS - high

performance software for linear optimization.” https://highs.dev/

[14]

Huangfu, Q. and Hall, J. A. J. “Parallelizing the dual revised simplex method.”

Mathematical Programming Computation, 10 (1), 119-142, 2018. DOI:

10.1007/s12532-017-0130-5

[15]

Harris, Paula MJ. “Pivot selection methods of the Devex LP code.” Mathematical

programming 5.1 (1973): 1-28.

[16]

Goldfarb, Donald, and John Ker Reid. “A practicable steepest-edge simplex algorithm.”

Mathematical Programming 12.1 (1977): 361-371.

Previous
linprog(method=’highs ipm’)

© Copyright 2008-2025, The SciPy community.

Created using Sphinx 7.3.7.

Next
linprog(method=’highs’)

Built with the PyData Sphinx Theme 0.15.2.

https://docs.scipy.org/doc/scipy-1.15.3/reference/optimize.linprog-highs-ds.html

6/6

