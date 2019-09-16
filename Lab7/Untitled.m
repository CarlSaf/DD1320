indata = textread('spridning.txt');
indata=sort(indata);
figure, plot(1:size(indata), indata)