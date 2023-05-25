clear all
format compact
format short
% Program to verify different probabilistic properties
% of the generated random numbers
% There are more sophisticated tests in 
% D. Knuth, The Art of Computer Programming: Random Numbers
% Volume 2: Seminumerical Algorithms, various editions (all good!)

% set the seed / starting bit patterin for the random
% number generator to 42 
rand('seed',42) 
% ^^^^^^ uncomment if you want different random numbers 
% every time

nexpo=4

for iexpo=1:nexpo
  disp('   ') % Empty line
  nsamples=10^nexpo
  r_rand=rand(nsamples,1); % Vector of sample random numbers
  mean_rand=mean(r_rand);
  variance=var(r_rand);
  mean_diff=mean_rand-0.5
  var_diff=mean_rand-1/12
  
end






return