function [weightVec] = SSVEP5_LearnModel_Scaffolding(recordingFolder)
% SSVEP_LearnModel_Scaffolding outputs a weight vector for all the features
% using a simple multi-class LDA approach. 
% Add your own classifier (SVM, CSP, DL, CONV, Riemann...), and make sure
% to add an accuracy test.

SSVEPFeaturesLabel = readtable(strcat(recordingFolder,'SSVEPFeaturesLabel.csv'));
features = table2array(SSVEPFeaturesLabel(:,1:(end-1)));        % only features matrix
labels = table2array(SSVEPFeaturesLabel(:,end));                % only labels vector

weightVec = LDA(features,labels);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%% ADD OTHER LEARNING PARADIGMS HERE %%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

save(strcat(recordingFolder,'weightVec.mat'),'weightVec');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%% Add a learning accuracy test paradigm here %%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

end


