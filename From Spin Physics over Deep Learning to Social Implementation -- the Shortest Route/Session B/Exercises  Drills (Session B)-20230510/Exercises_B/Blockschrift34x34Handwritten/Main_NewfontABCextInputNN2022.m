clear all 
format compact
format short
rand('seed',2)
% to do: 
% Write Loop over pattern for recognition
% typewriter-update instead of random
% Write handwritten interface
nquad2=34%54%34
nquad1=34%54%34

% Generate all Patterns as cell arrays
patterns=ReadinFontOutputPatternsBlockschrift(nquad1,nquad2);

% spy(cell2mat(patterns(1)),32)
% axis off
% print -depsc patternA.eps
% spy(1-cell2mat(patterns(1)),32)
% axis off
% print -depsc patternAntiA.eps
% spy(abs(cell2mat(patterns(1))+rand(34)))
% spy(abs(cell2mat(patterns(1))+(rand(34)-.5)))
% spy(floor(cell2mat(patterns(1))+(rand(34)-.5)))
% spy(floor(cell2mat(patterns(1))+(rand(34)-.2)))
% spy(floor(cell2mat(patterns(1))+(rand(34)-.1))),32)
% axis off
% print -depsc patternNoisyA.eps
% 
% return


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
subplot(2,1,2)
hist(J(:))
title(['Std=' num2str(std(J(:))) '  mean=' num2str(mean(J(:)))])
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


% input pattern with cursor from graphics window
CursorOnlyInputDoubleline

% error('compare data')
%inputpat=cell2mat(patterns(1))*2-1
subplot(2,2,1)
spy(inputpat+1)

% rand('seed',13)
% rand('seed',11)
% 
%  for ix=1:lx
%    for iy=1:ly
%      if rand<.34
%        inputpat(ix,iy)=-inputpat(ix,iy);
%      end
%    end
%  end
% subplot(2,2,2)
spy(inputpat+1)
subplot(2,2,3)

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
        spy(disppat)
        input('NoW')  
      else
        DeltaE %disp('LARGER!!!!')
      end
    end
  end
  drawnow
end





return

