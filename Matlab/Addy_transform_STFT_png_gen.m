function Addy_transform_STFT_png_gen(Signal,time,fs,ylimit,filename)

global z;
% spectral parameters
Nw      = 121;
nfft    = (length(Signal));% number of FT points
win     = hanning(Nw);          % window for spectrogram
ovlap   = length(win)-1;        % overlap between adjacent windows
time_halfbandwidth = 1.5;
num_seq = floor(2*(time_halfbandwidth))-1;
tapers  = [time_halfbandwidth, num_seq];             % tapers for multitaper NW = 3.5; K = 6

optsMulti = struct('psd',1,'pad','zeros','mean','mean','interp',1);
% optsSpec  = struct('psd',1,'pad','zeros','interp',1);

[RSmulti, fRMulti, ~, ~, ~, ~] = reasmultitapers(Signal,Nw,tapers,ovlap,nfft,fs,optsMulti);

%% 

z=RSmulti.^(1/4);
z((fRMulti>ylimit),:)=[];

z=flipud(z);
% fRMulti((fRMulti>ylimit),:)=[];
% fRMulti=flipud(fRMulti);

% figure
% imagesc(time,fRMulti,z)
% set(gca,'YDir','normal')
% axis tight;
% ylim([0 1e6])
% colormap hot

%imwrite(ind2rgb(im2uint8(mat2gray(z)),hot(256)),strcat(filename,'.png'))
imwrite(mat2gray(z),strcat(filename,'.png'))
end