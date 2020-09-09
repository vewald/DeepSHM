clear all;close all;clc
load All_crack_signals.mat

class = 4; sensor1 = 1; sensor2 = 3;
sig = signal{class,2};
sound_left = sig(:,sensor1); sound_right = sig(:,sensor2);
Fs = 4096;
nBits = 16;
stereo = [sound_left sound_right];
soundsc(stereo,Fs,nBits)