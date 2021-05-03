import numpy as np
import matplotlib.pyplot as plt
import Compare_an_idealistic_ensemble_classifier_to_a_base_classifier as ensembler

# Visualize the error rates in the range from 0.0 to 1.0
error_range = np.arange(0.0, 1.01, 0.01)

ens_errors = [ensembler.ensemble_error(n_classifier=11, error=error) for error in error_range]

plt.plot(error_range, ens_errors, label="Ensemble error", linewidth=2)
plt.plot(error_range, error_range, linestyle='--', label='Base error', linewidth=2)

plt.xlabel('Base error')
plt.ylabel('Base/Ensemble')
plt.legend(loc='upper left')
plt.grid(alpha=0.5)

plt.savefig("Ensemble_versus_base.jpg")

plt.show()
