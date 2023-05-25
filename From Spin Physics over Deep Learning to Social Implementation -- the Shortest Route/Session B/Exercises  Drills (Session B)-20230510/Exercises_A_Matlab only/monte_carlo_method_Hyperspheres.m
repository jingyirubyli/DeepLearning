clear all
format compact
format short

% set the seed / starting bit patterin for the random
% number generator to 42 
rand('seed',42) 

      
nsample=10^6
ndim=5
% Estimate the volume for the n-dimensional 
% hypersphere  or N-sphere
% https://en.wikipedia.org/wiki/N-sphere
% with unit radius in a similar way as pi was computed
% by comparing with the Volume of hypercube with 
% edge length 1
% 

format long
V_exact=pi^(ndim/2)/gamma(ndim/2+1)
% If you don't know the gamma-function, type
% help gamma
% and compare gamma(1), gamma(2), gamma(3) ...
% with the factorial 

iinside=0;
for isample=1:nsample
  r=rand(ndim,1);
  dist=sqrt(sum(r.^2)); % implicit loop ( r(1)^2+r(2)^2 ....)^1/2
% we wave to discriminte  
  if dist<1
    iinside=iinside+1;
  end
end

V_MonteCarlo=2^ndim*iinside/nsample
disp(['for the ' num2str(ndim) '-dimensional sphere'])
disp(['with'  num2str(nsample) ' MC-samples'])

return








return

