import tensorflow

class PSOptimizer(tensorflow.keras.optimizers.Optimizer):
    def __init__(self, learning_rate=0.01, name="PSOptimizer", **kwargs):
        """Call super().__init__() and use _set_hyper() to store hyperparameters"""
        super().__init__(name, **kwargs)
        self._set_hyper("learning_rate", kwargs.get("lr", learning_rate)) # handle lr=learning_rate
        self._is_first = True

    def _create_slots(self, var_list):
        """For each model variable, create the optimizer variable associated with it.
        TensorFlow calls these optimizer variables "slots".
        For momentum optimization, we need one momentum slot per model variable.
        """
        for var in var_list:
            self.add_slot(var, "previous_weight") #previous variable i.e. weight or bias
        for var in var_list:
            self.add_slot(var, "previous_gradient") #previous gradient
