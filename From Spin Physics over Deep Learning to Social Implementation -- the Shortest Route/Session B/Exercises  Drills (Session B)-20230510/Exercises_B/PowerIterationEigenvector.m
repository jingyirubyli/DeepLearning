clear all
format compact
format long
niter=15

rand('seed',5)
A=rand(3);
A=0.5*(A+A')% symmetric

v=[0.287573463099443   
  -0.922246481669719   
   0.258385236360010] 

diary on
for i=1:niter
  v=A*v;
  normv=norm(v)
  v=v/normv;
  v'
end

[V,D]=eig(A)
diary off

return