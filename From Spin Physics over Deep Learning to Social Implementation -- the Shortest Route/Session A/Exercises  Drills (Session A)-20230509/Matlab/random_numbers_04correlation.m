clear all
format compact
format short

% set the seed / starting bit patterin for the random
% number generator to 42 
rand('seed',42) 
% don't expect the same requence of random numbers as 
% for the python programs
 
nnum=10^4
nt=60

randvec=rand(nnum+nt,1);


for it=0:nt
% .*  elementwise multiplication    
  correlation(it+1)=sum(randvec(1:nnum).*randvec(1+it:nnum+it))/nnum;
end
correlation
corr_diff=abs(correlation-1/4)
% The statistical correlation has an errorbar due to the
% number of samples nnum: 
% The correlation will not decrease (except by chace) below
% that threshold


return




