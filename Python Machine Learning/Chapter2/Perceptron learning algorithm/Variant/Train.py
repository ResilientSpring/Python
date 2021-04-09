import numpy as np
import matplotlib.pyplot as plt
import Perceptron as Perceptron
import Iris_dataset as training_set

ppn = Perceptron.Perceptron(eta=0.1, n_iter=10);
ppn.fit(X=training_set.X1, y=training_set.y5);

plt.plot(np.arange(1, len(ppn.errors_) + 1), ppn.errors_, marker='o');
plt.xlabel("Epochs");
plt.ylabel("Number of updates");

plt.savefig('mis-classification_errors_vs_#_of_epochs.jpg');

plt.show();