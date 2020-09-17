function [trainingVec] = prepareTraining(numTrials,numConditions)
%% return a random vector of 1's and 2's length of numTrials
trainingVec = randi(numConditions,numTrials);
trainingVec = trainingVec(1,:);

end