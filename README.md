# Chebyshev Multiplier Sequences
### By Andrzej Piotrowski and Joshua Shterenberg

## Overview and How To Build

Abstract: We demonstrate that a multiplier sequence for the Chebyshev basis cannot be interpolated by a polynomial of odd degree. We exhibit this by direct algebraic proof and by utilizing various computational methods for both preliminary proofs and for the symbolic interpretation of required sequences. Additionally, we provide a basis for continued research for extensions of this basis set into the Gegenbauer and Jacobi basis sets, as well as a preliminary analysis of the even degree multiplier sequences as linear operators of these sets.

To build this file, please ensure you have all the required libraries installed locally on your machine by either installing them individually, or through the requirements.txt file included.
 * pip==20.0.2
 * numpy==1.17.4
 * scipy==1.7.3
 * matplotlib==3.1.2

Then, simply download the file(s) you with to run and execute using Python3. 

## File Descriptions

The following is a brief description of each file used in preliminary examinations of sequences:
 * chebyshev_coeff_gen.py: A general function that, given a test function of x, a given number of Chebyshev coefficients to generate, and a potential multiplier sequence to investigate, applies the methodology in Section 4. It takes the inputted test function and modifies it in terms of the Chebyshev basis set via application of the inner product, and the coefficients are printed. Then, the test function in the new basis is applied the potential multiplier sequence term-wise, and the new polynomial is formed. Finally, the roots of the polynomial are found via numpy, and printed.
 * chebyshev_k_class.py: A nearly identical algorithm to chebyshev_coeff_gen.py, following the algorithm of the Figures and Tables section directly. 
 * cubic_sweep.py: A more basic-level test function that applies the beginning steps of Section 5 on particular cases of a cubic potential multiplier sequence. This function sweeps three-dimensional space and halts when it finds a non-alternating sign change.
 * q2k_gen.py: This function generates terms of a specific Q2K sequence from a user-given test function.
 * quintic_interp.py: Performs quintic interpolation on a specifc test function, as in Section 4. The plot of this interpolation is shown in the paper and below:

![alt text](https://github.com/joshshterenberg/Chebyshev_MS/blob/main/quintic_roots_gen.pdf?raw=true)
