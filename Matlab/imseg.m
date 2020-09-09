clear all; close all; clc;

RGB = imread('Cr_0%_1.png');
L = imsegkmeans(RGB,4);
B = labeloverlay(RGB,L);
imshow(B)
title('Labeled Image')