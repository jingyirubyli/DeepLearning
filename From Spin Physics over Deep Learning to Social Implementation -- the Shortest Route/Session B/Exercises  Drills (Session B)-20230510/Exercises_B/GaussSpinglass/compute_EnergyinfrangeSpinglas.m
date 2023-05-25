function Ene_sum = compute_EnergyinfrangeSpinglas(isvec,J)
% COMPUTE_ENERGY of a spinglas with infinite Interactions
%   for a system lxy ising spins and Hamiltonian
%   -J sum si_sj
lxy=length(isvec);
Ene_sum=isvec'*J*isvec/(2*lxy);

return
