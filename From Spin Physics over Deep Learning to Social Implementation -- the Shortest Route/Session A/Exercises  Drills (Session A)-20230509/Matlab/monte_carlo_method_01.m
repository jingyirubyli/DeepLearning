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

nexpo=7

format long
for iexpo=1:nexpo
  disp('   ') % Empty line
  nsamples=10^nexpo
  x_rand=rand(nsamples,1); % Vector of sample random numbers
  y_rand=rand(nsamples,1); % Vector of sample random numbers
  insidecircle=0;
  for isamples=1:nsamples  
    if (x_rand(isamples).^2+y_rand(isamples).^2)<1
      insidecircle=insidecircle+1;
    end 
  end
  pi % 16 digit exact value from MATLAB builtin funciton
  pi_approx=4*insidecircle/nsamples
end






return