clear all 
format compact
format short
rand('seed',2)
% to do: 
% Write Loop over pattern for recognition
% typewriter-update instead of random
% Write handwritten interface
nquad2=34
nquad1=34

% Generate all Patterns as cell arrays
patterns=ReadinBerkeliumFontOutputPatterns(nquad1,nquad2);
% patterns=patterns(1:2:8)
npatterns=length(patterns) 

[lx,ly]=size(cell2mat(patterns(1)));
lxy=lx*ly
% Compute interaction
Amat=[];
for ipattern1=1:npatterns
   pat1=cell2mat(patterns(ipattern1))*2-1;
   pat1vec=pat1(:);
   Amat=[Amat pat1vec];
end
J=Amat*Amat';    
% As many non-zero eigenvalues abs >1e-5 
J=J-diag(diag(J)); % This shifts the eigenvalues
% spy(J) verified
J=J/npatterns; % normalization to variance 1 ?
npatterns
figure(3)
subplot(2,1,1)
semilogy(abs(eig(J)),'*')
title('Eigenvalues with Hopfield rule before Equalization')
subplot(2,1,2)
hist(J(:))
title('Histogram of the interaction Jij')

xlabel(['Std=' num2str(std(J(:))) '  mean=' num2str(mean(J(:)))])
sum(abs(eig(J)+1)>1e-4)
sum(eig(J)>-1+1e-3)

% Rescaling of Eigenvalues to make sure that
% each pattern is properly represented
[V,D] = eig(J);
for i=1:npatterns-1
  D(end-i,end-i)=D(end,end);  
end
J=V*D*inv(V);

figure(4)
% input pattern with random noise
% number in patterns is number of letter in the alphabet,
% A is 1, B is 2 ...
inputpat=cell2mat(patterns(1))*2-1
subplot(2,2,1)
spy(inputpat+1)
title('Selected Pattern')

rand('seed',13)
rand('seed',11)

 for ix=1:lx
   for iy=1:ly
     if rand<.34
       inputpat(ix,iy)=-inputpat(ix,iy);
     end
   end
 end
subplot(2,2,2)
spy(inputpat+1)
title('Pattern with noise')


isvec=inputpat(:)
for iiter=1:1000
  for ixrep=1:lx
    for iyrep=1:ly
      ix=round(rand*lx+.5);
      iy=round(rand*ly+.5);
%       ix=ixrep;
%       iy=iyrep;
      ixy=ix+(iy-1)*lx
      Eold=-isvec(ixy)*J(ixy,:)*isvec;
      Enew=isvec(ixy)*J(ixy,:)*isvec;
      DeltaE=Enew-Eold;
      if DeltaE<0
        isvec(ixy)=-isvec(ixy);
        disppat=(reshape(isvec,lx,ly)+1);
        subplot(2,2,3)
        spy(disppat)
        title('Recovered pattern')
        input('Continue?')  
      else
        DeltaE %disp('LARGER!!!!')
      end
    end
  end
end

return

