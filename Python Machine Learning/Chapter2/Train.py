import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import Perceptron as Perceptron
import Iris_dataset2 as training_set

ppn = Perceptron.Perceptron(eta=0.1, n_iter=10);
ppn.fit(X=training_set.X, y=training_set.y3);

plt.plot(np.arange(1, len(ppn.errors_) + 1), ppn.errors_, marker='o');
plt.xlabel("Epochs");
plt.ylabel("Number of updates");

plt.savefig('mis-classification_errors_vs_#_of_epochs.jpg');

plt.show();