%% MATLAB 2 Project - Tande Mungwa


% Before you read - I indepedently devised a method of implmenting
% Jacobi-method which happened to be exactly what was suggested. There may
% be a few discrepanices but I ensure the results are identical.


x = []
x(1,1:21) = 1
x(1:11,21) = 1 
xold = x %
tol = 10^(-6)
avgOld = mean(xold(2,:))
k = 0

%%
while 1
    k = k + 1 
    for j = 10:-1:2
        for i = 20:-1:2
            x(j,i) =  1/4*(xold(j+1,i) + xold(j-1,i) + xold(j,i-1) + xold(j,i+1))
        end
    end
    avgNew = mean(x(2,:)) % convergence criterion 
    [C,h]=contourf(x,10)
    xlabel('x-dimension (m)') 
    ylabel('y-dimension (m)') 
    clabel(C,h)
    title(strcat('Iteration number:', num2str(k), ' ....... Convg-Criterion:', num2str(abs(avgNew-avgOld))))
    pause(1/100)
  
    if abs(avgNew - avgOld) > tol
        xold = x 
        avgOld = avgNew
    else
        xlabel('SOLUTION IS CONVERGED','FontSize',15) 
        break
    end
end

%% Post Questions

% I obtained a convergent solution after 273 iterations.


% I'd probably implement Gauss-Seidel instead, as it updates the
% temperatures thereby speeding up the overall process of heat distribtuion