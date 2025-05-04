"""

Training a Machine Learning Model (Metaflow Workflow):

    By using Metaflow to train a machine learning model, we’ll learn how to:

        - Define a workflow that loads data
        - Train a machine learning model
        - Track the results

    By the end, we'll better understand how to use Metaflow to structure and run machine learning workflows efficiently.

    To begin, we will create a basic flow that loads a dataset, performs training, and outputs the model’s results.

"""


from metaflow import FlowSpec, step, NBRunner


class TrainingFlow(FlowSpec):

    @step
    def start(self):
        """
        start(): Loads and splits the dataset.
        In a real-world scenario, you would load data from an actual source (e.g., a file or database).
        """
        # Load and split the dataset
        print("Loading data...")
        self.data = [1, 2, 3, 4, 5]  # Replace with actual data loading logic
        self.label = [0, 1, 0, 1, 0]  # Replace with labels
        self.next(self.train_model)

    @step
    def train_model(self):
        """
        train_model(): Simulates the training of a model.
        A simple average calculation is performed instead of an actual machine learning algorithm,
        but you can replace this with any training code you need.
        """
        # Training a simple model (e.g., linear regression)
        print("Training the model...")
        self.model = sum(self.data) / len(self.data)  # Replace with actual model training
        print(f'Model output: {self.model}')
        self.next(self.end)

    @step
    def end(self):
        """end(): Marks the end of the flow and signifies that the model is ready for deployment."""
        # Final step
        print("Training complete. Model ready for deployment!")


if __name__ == '__main__':
    # Note that this code only works in notebooks (all code must be in one cell)
    # run = NBRunner(TrainingFlow).nbrun()

    # If you want to run this code as a script, remove the NBRunner command.
    TrainingFlow()