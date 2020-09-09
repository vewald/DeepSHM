close all; clear all; clc

load scene1.mat; load data_50us.mat;
signal_ = signal{1,2};
C_sim = mat2gray(signal_(40:4101,1));

% 4888 = 500 µs, Time step = 0.1024 µs, Sampling rate = 9765625 Hz
C = resample(C_sim,1024,1000);
start = 256; finish = length(C)-689;
C_exp = mat2gray(smoothdata(C(start:finish)));

figure
plot(C_sim)
hold on
plot(C_exp)

%[c,lags] = xcorr(C_sim, C_exp);
%stem(lags,c)

for k = 1:4062-1
    CC_mat = corrcoef(C_sim(1:k+1),C_exp(1:k+1));
    CC(k) = CC_mat(2,1);
end

CC = mat2gray(CC);

figure
subplot(3,1,1)
plot(C_exp)
subplot(3,1,2)
plot(C_sim)
subplot(3,1,3)
plot(CC)