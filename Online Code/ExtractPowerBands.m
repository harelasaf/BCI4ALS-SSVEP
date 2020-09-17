function [EEG_Features] = ExtractPowerBands(EEG,powerbandFreqs,Fs)
% ExtractPowerBands Extracts the amplitude of the different powerbands
% between the frequencies specified in powerbandFreqs.

% alpha = powerbandFreqs(1,:);
% beta  = powerbandFreqs(2,:);
% theta = powerbandFreqs(3,:);
% delta = powerbandFreqs(4,:);
% gamma = powerbandFreqs(5,:);
chans = size(EEG,1);
feats = size(powerbandFreqs,1);
for chan = 1:chans
    for feat = 1:feats
        EEG_Features(chan,feat) = bandpower(EEG(chan,:)',Fs,powerbandFreqs(feat,:));
    end
end
EEG_Features = reshape(EEG_Features,[1,chans*feats]);
% EEG_Features(2) = bandpower(EEG',Fs,powerbandFreqs(2,:));
% EEG_Features(3) = bandpower(EEG',Fs,powerbandFreqs(3,:));
% EEG_Features(4) = bandpower(EEG',Fs,powerbandFreqs(4,:));
% EEG_Features(5) = bandpower(EEG',Fs,powerbandFreqs(5,:));

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%% Add further features here %%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

end

