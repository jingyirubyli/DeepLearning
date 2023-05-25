clear all
format compact
format short
% Set up Ising spins randomly or ordered
% Compute the physical observables 
% - Total magnetization 
%   M_total=∑_i si 
% - Average magnetization per spin `m`: [-1, 1]
%    m = M_total / (Lx*Ly) = ∑_i si / (Lx*Ly)
% - Average energy ener per spin 2>=ener>=-1
%    ener = E_total / (L^2) = -J∑_<i,j> si*sj / (L^2), (J = 1).
%    for nearest-neighbor interaction  <i,j>
%    and periodic boundary conditions: 
%    - leftmost spin interacts with rightmost spin in the same row, 
%    - nethermost spin interact with uppermost spin in the same column
%
% All these observable computations have  complexity O(L=Lx*Ly) 



% set the seed / starting bit patterin for the random
% number generator to 42 
rand('seed',42) 
% ^^^^^^ uncomment if you want different random numbers 
% every time

Lx=10
Ly=10
J=1

 ordered=0
%ordered=1

if ordered==1
  ising=ones(Lx,Ly);
elseif ordered==0
  ising=round(rand(Lx,Ly))*2-1;
else
  error('This option does not exist')
end

M_total=0;
E_total=0;
% read the comments at the end of the program
for ix=1:Lx
  for iy=1:Ly
    M_total=M_total+ising(ix,iy);  
    ixm1=ix-1;
    if ixm1<1 % periodic boundaries in x-direction
      ixm1=ixm1+Lx;
    end
    ixp1=ix+1;
    if ixp1>Lx % periodic boundaries in x-direction
      ixp1=ixp1-Lx;
    end
    iym1=iy-1;
    if iym1<1 % periodic boundaries in y-direction
      iym1=iym1+Ly;
    end
    iyp1=iy+1;
    if iyp1>Ly % periodic boundaries in y-direction
      iyp1=iyp1-Ly;
    end
% Energy contribution for spin (ix,iy) from all four
% nearest neighbors
    DeltaE=-J*ising(ix,iy)*ising(ixp1,iy)...  
           -J*ising(ix,iy)*ising(ixm1,iy)...  
           -J*ising(ix,iy)*ising(ix,iyp1)...  
           -J*ising(ix,iy)*ising(ix,iym1); 
    E_total=E_total+J*DeltaE;
  end
end
m=M_total/(Lx*Ly)
ener=E_total/(2*Lx*Ly)

% Comments:
% 1. In principle, it would be sufficient to sum the energy only over
%    every second spin, because the interaction energy is symmetric
%    from one spin i to anothe spin j
%    The double-counding makes a division /(2Lx*Ly) instead of  /(Lx*Ly)
%    necessary.
%    In that case, two different loops for the computation of the
%    magnetization (which has to be computed over all sites) are necessary.
% 2. The Python-programs use a neighborhood-table where for every
%    ix  the right neighbor and for every iy the upper neighbor is computed


return

