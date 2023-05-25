clear all
format compact
format long
niter=5

rand('seed',5)
A=rand(3);
A=0.5*(A+A')% symmetric

v=rand(3,1)-.5

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