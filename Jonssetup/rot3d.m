function J = rot3d(I, alpha, beta, gamma, xMax, yMax, zMax)
%alpha = 0; % Rotation around x axis
%beta = 0; % rotation around y axis
%gamma = 0; % rotation around z axis

Rz = [cos(gamma) -sin(gamma) 0 0
     sin(gamma) cos(gamma) 0 0
     0 0 1 0
     0 0 0 1];
Ry = [cos(beta) 0 sin(beta) 0
     0 1 0 0
     -sin(beta) 0 cos(beta) 0
     0 0 0 1];
Rx = [1 0 0 0
     0 cos(alpha) -sin(alpha) 0
     0 sin(alpha) cos(alpha) 0
     0 0 0 1];
tform = affine3d(Rz*Ry*Rx); % Extrinsic (Euler) rotation
[xLimitO,yLimitO,zLimitO] = outputLimits(tform,[1 xMax],[1 yMax],[1 zMax]);
x = [0 xMax-1]+1+sum(xLimitO)/2-xMax/2;
y = [0 yMax-1]+1+sum(yLimitO)/2-yMax/2;
z = [0 zMax-1]+1+sum(zLimitO)/2-zMax/2;
J = imwarp(I,tform,'OutputView',imref3d(size(I),x,y,z));
