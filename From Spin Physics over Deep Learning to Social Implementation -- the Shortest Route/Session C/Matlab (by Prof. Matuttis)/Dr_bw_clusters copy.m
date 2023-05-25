clear all
format compact
format short
% PURPOSE: Read in the portrait of the hatted lady
% and covert it into grayscale and run a Laplace filter 
% USAGE: Standalone Example Program


       

Asmildata=imread('SmileyBW.jpeg');
% imshow(Asmildata)
mesh(Asmildata)
%shading interp
grid
return
subplot(1,2,1)
imshow(Asmildata)

subplot(1,2,2)
hold on
  [B,L,N,A] = bwboundaries(Asmildata);
        for k = 1:N
           % Boundary k is the parent of a hole if the k-th column
           % of the adjacency matrix A contains a non-zero element
           if nnz(A(:,k)) > 0
               boundary = B{k};
               plot(boundary(:,2), boundary(:,1), 'r', 'LineWidth', 2);
               % Loop through the children of boundary k
               for l = find(A(:,k))'
                   boundary = B{l};
                   plot(boundary(:,2), boundary(:,1), 'g', 'LineWidth', 2);
               end
           end
       end
whos

return


      BW = imread('blobs.png');
       [B,L,N,A] = bwboundaries(BW);
       figure; imshow(BW); hold on;
       % Loop through object boundaries
       for k = 1:N
           % Boundary k is the parent of a hole if the k-th column
           % of the adjacency matrix A contains a non-zero element
           if nnz(A(:,k)) > 0
               boundary = B{k};
               plot(boundary(:,2), boundary(:,1), 'r', 'LineWidth', 2);
               % Loop through the children of boundary k
               for l = find(A(:,k))'
                   boundary = B{l};
                   plot(boundary(:,2), boundary(:,1), 'g', 'LineWidth', 2);
               end
           end
       end
       
       return