N = 64;
r = 4;
n=0;
[sx,sy,sz] = meshgrid(1:N);
I = zeros(size(sx));
I(N/2:N, N/2+[-r:r], N/2+[-r:r])=1;
I(N/2+[-r:r], N/2:round(N*7/8), N/2+[-r:r])=1;
I(N/2+[-r:r], N/2+[-r:r], N/2:round(N*4/5))=1;
n=n+1; figure(n); clf;
isosurface(I,0.5);
axis([1,N,1,N,1,N]); xlabel('2'); ylabel('1'); zlabel('3')

angles = rand(5,3)*2*pi;

P = zeros(N,N,size(angles,1));
K = zeros(N,N,N);
for i = 1:size(angles,1)
  J = rot3d(I,angles(i,1),angles(i,2),angles(i,3),N,N,N);
  P(:,:,i) = sum(J,3) > 0.1;
  n=n+1; figure(n); clf;
  imagesc(P(:,:,i)); colormap(gray); axis tight equal; xlabel('2'); ylabel('1');
  title(sprintf('alpha=%.2f, beta=%.2f, gamma=%.2f',angles(i,1),angles(i,2),angles(i,3)))

  BP = repmat(P(:,:,i),[1,1,N]);
%  T = rot3d(K,angles(i,1),angles(i,2),angles(i,3),N,N,N);
%  T = T + BP;
%  K = invrot3d(T,angles(i,1),angles(i,2),angles(i,3),N,N,N);
  T = invrot3d(BP,angles(i,1),angles(i,2),angles(i,3),N,N,N);
  K = K + T;
end

n=n+1; figure(n); clf;
isosurface(K,size(angles,1)-0.5);
axis([1,N,1,N,1,N]); xlabel('2'); ylabel('1'); zlabel('3')
